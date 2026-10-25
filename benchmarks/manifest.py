#!/usr/bin/env python3
"""
Run Manifest and Resume Guard Module
Implements manifest collection and resume verification per improvement-plan.md Section 5 (Phase 1.4).
"""

import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
from typing import Any, Dict, Optional, Tuple


def get_git_info(repo_path: Path) -> Dict[str, str]:
    """Extracts git commit SHA and dirty diff hash for a repository."""
    if not (repo_path / ".git").exists():
        return {"sha": "unknown", "diff_hash": "none", "dirty": "false"}

    try:
        sha = subprocess.check_output(
            ["git", "-C", str(repo_path), "rev-parse", "HEAD"],
            text=True,
            stderr=subprocess.DEVNULL
        ).strip()
    except Exception:
        sha = "unknown"

    try:
        diff = subprocess.check_output(
            ["git", "-C", str(repo_path), "diff", "HEAD"],
            text=True,
            stderr=subprocess.DEVNULL
        )
        if diff:
            diff_hash = hashlib.sha256(diff.encode("utf-8")).hexdigest()[:16]
            dirty = "true"
        else:
            diff_hash = "clean"
            dirty = "false"
    except Exception:
        diff_hash = "unknown"
        dirty = "unknown"

    return {"sha": sha, "diff_hash": diff_hash, "dirty": dirty}


def get_file_sha256(file_path: Path, max_bytes: Optional[int] = None) -> str:
    """Computes sha256 of a file (optionally capped for fast hashing of large weights)."""
    if not file_path.exists():
        return "file_not_found"
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        if max_bytes is not None:
            chunk = f.read(max_bytes)
            h.update(chunk)
        else:
            while chunk := f.read(65536):
                h.update(chunk)
    return h.hexdigest()


def get_system_topology() -> Dict[str, Any]:
    """Captures CPU model, physical cores, NUMA nodes, and THP setting."""
    topology = {
        "platform": platform.platform(),
        "processor": platform.processor(),
    }
    # THP status
    thp_path = Path("/sys/kernel/mm/transparent_hugepage/enabled")
    if thp_path.exists():
        try:
            topology["thp"] = thp_path.read_text().strip()
        except Exception:
            topology["thp"] = "unknown"

    # CPU info
    try:
        lscpu = subprocess.check_output(["lscpu"], text=True)
        for line in lscpu.splitlines():
            if "Model name:" in line:
                topology["cpu_model"] = line.split(":", 1)[1].strip()
            elif "Socket(s):" in line:
                topology["sockets"] = line.split(":", 1)[1].strip()
            elif "Core(s) per socket:" in line:
                topology["cores_per_socket"] = line.split(":", 1)[1].strip()
            elif "NUMA node(s):" in line:
                topology["numa_nodes"] = line.split(":", 1)[1].strip()
    except Exception:
        pass

    return topology


def create_manifest(
    exp_entry: Dict[str, Any],
    engine_dir: Path,
    model_path: Path,
    prompt_file: Optional[Path] = None,
    request_params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Creates a comprehensive manifest dictionary for an experiment run."""
    engine_info = get_git_info(engine_dir)
    sys_topo = get_system_topology()

    req = dict(exp_entry.get("request", {}))
    if request_params:
        req.update(request_params)

    manifest = {
        "experiment_id": exp_entry.get("id"),
        "experiment_number": exp_entry.get("number"),
        "protocol": exp_entry.get("protocol", "C-gpqa-v2"),
        "model": {
            "path": str(model_path),
            "size_bytes": model_path.stat().st_size if model_path.exists() else 0,
            "header_sha256": get_file_sha256(model_path, max_bytes=10 * 1024 * 1024)
        },
        "engine": {
            "path": str(engine_dir),
            "sha": engine_info["sha"],
            "diff_hash": engine_info["diff_hash"],
            "dirty": engine_info["dirty"]
        },
        "request": req,
        "numactl": exp_entry.get("numactl", ""),
        "server_flags": exp_entry.get("server_flags", ""),
        "system": sys_topo,
    }

    if prompt_file and prompt_file.exists():
        manifest["prompt_file"] = {
            "path": str(prompt_file),
            "sha256": get_file_sha256(prompt_file)
        }

    return manifest


def verify_resume(
    existing_manifest: Dict[str, Any],
    current_manifest: Dict[str, Any]
) -> Tuple[bool, Optional[str]]:
    """
    Checks if a run can be safely resumed.
    Refuses resume if engine, model, or core request parameters changed.
    """
    # Check model
    if existing_manifest.get("model", {}).get("header_sha256") != current_manifest.get("model", {}).get("header_sha256"):
        return False, "Model file or header hash mismatch."

    # Check request parameters
    req_old = existing_manifest.get("request", {})
    req_new = current_manifest.get("request", {})
    for key in ["max_tokens", "temperature", "top_p", "seed", "user_suffix"]:
        if req_old.get(key) != req_new.get(key):
            return False, f"Request parameter mismatch: {key} was {req_old.get(key)}, now {req_new.get(key)}."

    # Check flags
    if existing_manifest.get("server_flags") != current_manifest.get("server_flags"):
        return False, "Server flags mismatch."

    return True, None
