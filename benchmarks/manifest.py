"""Record run inputs and refuse resumes when their identity changes."""

import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess


def get_file_sha256(file_path, max_bytes=None):
    digest = hashlib.sha256()
    with Path(file_path).open("rb") as handle:
        if max_bytes is not None:
            digest.update(handle.read(max_bytes))
        else:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
    return digest.hexdigest()


def get_git_info(repo_path):
    def git(*args):
        return subprocess.check_output(["git", "-C", str(repo_path), *args], stderr=subprocess.DEVNULL)
    try:
        sha = git("rev-parse", "HEAD").decode().strip()
        diff = git("diff", "--binary", "HEAD")
        status = git("status", "--porcelain", "--untracked-files=all")
        untracked = git("ls-files", "--others", "--exclude-standard", "-z").split(b"\0")
        extra = {name.decode(): get_file_sha256(Path(repo_path) / name.decode()) for name in untracked if name and (Path(repo_path) / name.decode()).is_file()}
        return {"sha": sha, "diff_hash": hashlib.sha256(diff).hexdigest(), "dirty": bool(status), "untracked": extra}
    except (OSError, subprocess.CalledProcessError) as exc:
        raise RuntimeError(f"Cannot identify engine checkout: {repo_path}") from exc


def get_system_topology():
    topology = {"platform": platform.platform(), "processor": platform.processor()}
    if hasattr(os, "sched_getaffinity"):
        topology["affinity"] = sorted(os.sched_getaffinity(0))
    for name, command in (("lscpu", ["lscpu", "--json"]), ("numa", ["numactl", "--hardware"])):
        try:
            output = subprocess.check_output(command, text=True, stderr=subprocess.DEVNULL).strip()
            if name == "lscpu":
                output = {row["field"]: row["data"] for row in json.loads(output)["lscpu"] if not any(word in row["field"].lower() for word in ("mhz", "bogomips", "vulnerability"))}
            else:
                output = "\n".join(line for line in output.splitlines() if " free:" not in line)
            topology[name] = output
        except (OSError, subprocess.CalledProcessError):
            topology[name] = None
    thp = Path("/sys/kernel/mm/transparent_hugepage/enabled")
    topology["thp"] = thp.read_text().strip() if thp.exists() else None
    return topology


def get_build_artifacts(engine_dir, server_binary):
    """Hash shared libraries and CMake caches within bounded project build roots."""
    engine_dir = Path(engine_dir).resolve()
    roots = set()
    default_build = engine_dir / "build"
    if default_build.is_dir():
        roots.add(default_build)
    if server_binary:
        binary_dir = Path(server_binary).resolve().parent
        roots.add(binary_dir)
        ancestor = binary_dir
        for _ in range(4):
            if (ancestor / "CMakeCache.txt").is_file():
                roots.add(ancestor)
                break
            if ancestor.parent == ancestor:
                break
            ancestor = ancestor.parent
    roots = sorted(root for root in roots if not any(root != other and other in root.parents for other in roots))
    artifacts = {}
    directory_count = file_count = 0
    for root in roots:
        for directory, subdirs, filenames in os.walk(root, followlinks=False):
            directory = Path(directory)
            directory_count += 1
            if directory_count > 512:
                raise RuntimeError("Build artifact discovery exceeded 512 directories")
            depth = len(directory.relative_to(root).parts)
            subdirs[:] = sorted(name for name in subdirs if name not in ("CMakeFiles", "_deps", ".git", "Testing")) if depth < 5 else []
            for name in sorted(filenames):
                file_count += 1
                if file_count > 8192:
                    raise RuntimeError("Build artifact discovery exceeded 8192 files")
                if name != "CMakeCache.txt" and not (".so" in name or name.endswith((".dylib", ".dll"))):
                    continue
                path = directory / name
                if not path.is_file():
                    raise RuntimeError(f"Build artifact cannot be read: {path}")
                artifacts[str(path)] = {"resolved_path": str(path.resolve()), "sha256": get_file_sha256(path)}
    return {"roots": [str(root) for root in roots], "files": artifacts,
            "library_path": {name: os.environ.get(name) for name in ("LD_LIBRARY_PATH", "DYLD_LIBRARY_PATH", "LD_PRELOAD", "DYLD_INSERT_LIBRARIES")}}


def create_manifest(exp_entry, engine_dir, model_path, prompt_file=None, request_params=None, server_argv=None, dataset=None, server_binary=None):
    request = dict(request_params or {})
    model_path = Path(model_path).resolve()
    binary = Path(server_binary).resolve() if server_binary else None
    harness = Path(__file__).resolve().parent
    manifest = {
        "schema_version": 2,
        "experiment_id": exp_entry.get("id"),
        "experiment_number": exp_entry.get("number"),
        "protocol": request.get("benchmark", exp_entry.get("protocol", "C-gpqa-v2")),
        "model": {"path": str(model_path), "size_bytes": model_path.stat().st_size, "sha256": get_file_sha256(model_path)},
        "engine": {"path": str(Path(engine_dir).resolve()), **get_git_info(engine_dir)},
        "binary": {"path": str(binary), "sha256": get_file_sha256(binary)} if binary else None,
        "build_artifacts": get_build_artifacts(engine_dir, binary),
        "harness": {p.name: get_file_sha256(p) for p in sorted(harness.glob("*.py"))},
        "request": request,
        "catalog_request": exp_entry.get("request", {}),
        "numactl": exp_entry.get("numactl", ""),
        "server_flags": exp_entry.get("server_flags", ""),
        "server_argv": server_argv,
        "system": get_system_topology(),
    }
    if dataset is not None:
        serialized = json.dumps(dataset, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
        manifest["dataset_sha256"] = hashlib.sha256(serialized).hexdigest()
        if isinstance(dataset, dict):
            manifest["dataset_ids"] = sorted(dataset)
        elif isinstance(dataset, list):
            manifest["dataset_ids"] = [str(item["id"]) for item in dataset]
    if prompt_file:
        manifest["prompt_file"] = {"path": str(prompt_file), "sha256": get_file_sha256(prompt_file)}
    return manifest


def verify_resume(existing_manifest, current_manifest):
    if existing_manifest.get("schema_version") != 2:
        return False, "Legacy manifest lacks full input hashes; choose a new run suffix."
    for key in sorted(set(existing_manifest) | set(current_manifest)):
        if existing_manifest.get(key) != current_manifest.get(key):
            return False, f"Run input changed: {key}. Choose a new run suffix."
    return True, None
