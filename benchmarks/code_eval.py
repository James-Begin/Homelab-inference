#!/usr/bin/env python3
"""Generate HumanEval+ completions and optionally evaluate a saved sample file."""

from __future__ import annotations

import argparse
import ast
import importlib.metadata
import json
from pathlib import Path
import re
import shlex
import subprocess
import sys
import time
import urllib.request

from catalog import get_experiment, load_catalog
from manifest import create_manifest, get_file_sha256, verify_resume
from paths import ROOT, bin_dir, expand, ik_home, models_dir
from runtime import decode_rate, require_free_port, stopping_metadata, stop_process_group, wait_for_server
from summarize_runs import summarize_coding

RUNS_DIR = ROOT / "logs/runs"
SYSTEM_PROMPT = "You are an expert Python software engineer. Complete the given Python function according to the docstring specifications. Provide clean, correct, executable Python code."


def build_user_prompt(problem):
    return ("Please complete the following Python function according to its docstring.\n\n"
            f"```python\n{problem['prompt']}\n```\n\n"
            "Provide your reasoning, followed by the complete, executable implementation enclosed in a single ```python code block.")


def query_chat_completion(url, user_text, max_tokens=4096, temperature=0.0, top_p=1.0, system_prompt=None):
    messages = ([{"role": "system", "content": system_prompt}] if system_prompt else [])
    messages.append({"role": "user", "content": user_text})
    payload = {"messages": messages, "max_tokens": max_tokens, "temperature": temperature, "top_p": top_p, "stream": False, "seed": 0}
    request = urllib.request.Request(f"{url}/v1/chat/completions", data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=max(1800, int(max_tokens/10) + 300)) as response:
                raw = json.loads(response.read())
            choice = raw["choices"][0]
            message = choice["message"]
            usage = raw.get("usage", {})
            tokens = usage.get("completion_tokens", 0)
            return {"content": message.get("content") or "", "reasoning_content": message.get("reasoning_content") or "",
                    "tokens_predicted": tokens, "tokens_evaluated": usage.get("prompt_tokens", 0),
                    "timings": raw.get("timings", {}), "raw_response": raw,
                    **stopping_metadata(raw, tokens, max_tokens, choice.get("finish_reason"))}
        except (OSError, ValueError, KeyError, IndexError) as exc:
            print(f"Chat request failed ({attempt + 1}/3): {exc}", file=sys.stderr)
            time.sleep(2)
    return None


def extract_python_solution(raw_text, entry_point):
    if not raw_text:
        return ""
    if "</think>" in raw_text:
        raw_text = raw_text.rsplit("</think>", 1)[1]
    if "<think>" in raw_text:
        return ""
    blocks = re.findall(r"```(?:python|py)?[ \t]*\n(.*?)\n```", raw_text, re.DOTALL | re.IGNORECASE)
    candidates = list(reversed(blocks)) if blocks else [raw_text.strip()]
    for candidate in candidates:
        try:
            tree = ast.parse(candidate.strip())
        except SyntaxError:
            continue
        if any(isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == entry_point for node in tree.body):
            return candidate.strip()
    return ""


def evaluate_saved_run(run_dir, allow_host_execution=False):
    if not allow_host_execution:
        raise ValueError("Evaluation runs model-generated Python on this host. Use a disposable environment and explicitly pass --allow-host-execution.")
    from evalplus.evaluate import evaluate

    run_dir = Path(run_dir)
    samples = run_dir / "samples.jsonl"
    results = run_dir / "samples_eval_results.json"
    if results.exists():
        history = run_dir / "evaluation-history"
        history.mkdir(exist_ok=True)
        results.rename(history / f"{time.time_ns()}_samples_eval_results.json")
    identity = {"samples_sha256": get_file_sha256(samples), "evalplus_version": importlib.metadata.version("evalplus"),
                "execution": "host; no isolation provided by this harness"}
    evaluate(dataset="humaneval", samples=str(samples), parallel=14)
    if not results.exists():
        raise RuntimeError("EvalPlus did not write a result file")
    (run_dir / "evaluation_identity.json").write_text(json.dumps(identity, indent=2) + "\n")
    return summarize_coding(run_dir, write=True)


def run_code_eval(exp_key, port=8087, max_tokens=4096, dry_run=False, force_new_run=False, run_suffix="", allow_host_execution=False):
    from evalplus.data import get_human_eval_plus

    if max_tokens <= 0:
        raise ValueError("Token ceiling must be positive")
    if not re.fullmatch(r"[A-Za-z0-9_.-]*", run_suffix):
        raise ValueError("Run suffix may contain letters, digits, underscores, dots and hyphens")
    exp = get_experiment(load_catalog(), exp_key)
    dataset = get_human_eval_plus()
    problems = list(dataset.values())
    model_path = Path(expand(exp["model"]))
    if not model_path.exists():
        model_path = models_dir() / exp["model"]
    if not model_path.exists():
        raise FileNotFoundError(model_path)
    engine_home = ik_home().resolve()
    server_bin = bin_dir() / "llama-server"
    if not server_bin.exists():
        server_bin = bin_dir() / "Release/llama-server"
    if not server_bin.exists():
        raise FileNotFoundError(server_bin)
    flags = expand(exp["server_flags"], port=port)
    needed = max(32768 if max_tokens >= 8192 else 16384, max_tokens + 4096)
    flags = re.sub(r"-c\s+(\d+)", lambda match: f"-c {max(needed, int(match.group(1)))}", flags) if re.search(r"-c\s+\d+", flags) else flags + f" -c {needed}"
    argv = shlex.split(exp.get("numactl", "")) + [str(server_bin), "-m", str(model_path)] + shlex.split(flags)
    if force_new_run:
        run_suffix += f"_{time.time_ns()}"
    run_id = f"code_{exp['id']}{run_suffix}"
    run_dir = RUNS_DIR / run_id
    rows_file = run_dir / "rows.jsonl"
    samples_file = run_dir / "samples.jsonl"
    manifest_file = run_dir / "manifest.json"
    request_params = {"benchmark": "HumanEvalPlus-164", "endpoint": "chat", "max_tokens": max_tokens, "temperature": 0.0, "top_p": 1.0,
                      "stream": False, "seed": 0, "system_prompt": SYSTEM_PROMPT, "prompts": {p["task_id"]: build_user_prompt(p) for p in problems},
                      "extractor": "final-content-python-ast-v2", "evalplus_version": importlib.metadata.version("evalplus")}
    manifest = create_manifest(exp, engine_home, model_path, request_params=request_params, server_argv=argv, dataset=dataset, server_binary=server_bin)
    if dry_run:
        print(shlex.join(argv))
        print(json.dumps(manifest, indent=2))
        return 0
    run_dir.mkdir(parents=True, exist_ok=True)
    if manifest_file.exists():
        ok, reason = verify_resume(json.loads(manifest_file.read_text()), manifest)
        if not ok:
            raise ValueError(reason)
    elif rows_file.exists() or samples_file.exists():
        raise ValueError("Existing samples lack a manifest; choose a new run suffix")
    else:
        manifest_file.write_text(json.dumps(manifest, indent=2) + "\n")
    existing = {}
    if rows_file.exists():
        for line in rows_file.read_text().splitlines():
            row = json.loads(line)
            if row["task_id"] in existing or row["task_id"] not in dataset:
                raise ValueError("Duplicate or unknown task in saved rows")
            existing[row["task_id"]] = row
    if samples_file.exists():
        samples = [json.loads(line) for line in samples_file.read_text().splitlines() if line.strip()]
        if len(samples) != len(existing) or {r["task_id"]: r["solution"] for r in samples} != {key: row["solution"] for key, row in existing.items()}:
            raise ValueError("Saved samples differ from rows; repair the interrupted append before resuming")
    elif existing:
        raise ValueError("Saved rows lack samples; repair the interrupted append before resuming")
    proc = log_handle = None
    try:
        if len(existing) < len(problems):
            require_free_port(port)
            log_handle = (run_dir / "server.log").open("a")
            proc = subprocess.Popen(argv, stdout=log_handle, stderr=subprocess.STDOUT, start_new_session=True)
            url = f"http://127.0.0.1:{port}"
            if not wait_for_server(f"{url}/health", proc):
                raise RuntimeError("Server failed to become healthy; see server.log")
            for problem in problems:
                task_id = problem["task_id"]
                if task_id in existing:
                    continue
                start = time.monotonic()
                response = query_chat_completion(url, build_user_prompt(problem), max_tokens, system_prompt=SYSTEM_PROMPT)
                elapsed = time.monotonic() - start
                if response is None:
                    return 1
                solution = extract_python_solution(response["content"], problem["entry_point"])
                speed = decode_rate(response["tokens_predicted"], response["timings"].get("predicted_ms"))
                row = {"idx": len(existing) + 1, "task_id": task_id, "entry_point": problem["entry_point"], "tokens": response["tokens_predicted"],
                       "speed_tps": round(speed, 2) if speed is not None else None, "wall_time": round(elapsed, 2), "solution": solution,
                       "content": response["content"], "reasoning_content": response["reasoning_content"], "timings": response["timings"],
                       "finish_reason": response["finish_reason"], "max_tokens_hit": response["max_tokens_hit"], "raw_stopping": response["raw_stopping"]}
                with rows_file.open("a") as handle:
                    handle.write(json.dumps(row) + "\n")
                with samples_file.open("a") as handle:
                    handle.write(json.dumps({"task_id": task_id, "solution": solution}) + "\n")
                existing[task_id] = row
                print(f"{len(existing)}/{len(problems)} {task_id}: {row['tokens']} tokens, {elapsed:.1f} s, decode {row['speed_tps']}")
    finally:
        if proc is not None:
            stop_process_group(proc)
        if log_handle is not None:
            log_handle.close()
    summary = {"run_id": run_id, "experiment_id": exp["id"], "model": exp["model"], "total_problems": len(existing), "max_tokens_ceiling": max_tokens,
               "evaluation_status": "not executed", "extraction": "final-content-python-ast-v2"}
    if not (run_dir / "samples_eval_results.json").exists():
        (run_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    if allow_host_execution:
        evaluate_saved_run(run_dir, allow_host_execution=True)
    else:
        print(f"Saved completions to {run_dir}. Evaluation was not run; use a disposable environment and --evaluate-run PATH --allow-host-execution.")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--exp")
    parser.add_argument("--port", type=int, default=8087)
    parser.add_argument("--max-tokens", type=int, default=4096)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force-new-run", action="store_true", help="Create a timestamped run directory; retain existing artifacts")
    parser.add_argument("--run-suffix", default="")
    parser.add_argument("--evaluate-run", type=Path, help="Evaluate existing samples without starting inference")
    parser.add_argument("--allow-host-execution", action="store_true", help="Explicitly permit model-generated Python to run on this host; use a disposable environment")
    args = parser.parse_args()
    if args.evaluate_run:
        evaluate_saved_run(args.evaluate_run, args.allow_host_execution)
    elif args.exp:
        sys.exit(run_code_eval(args.exp, args.port, args.max_tokens, args.dry_run, args.force_new_run, args.run_suffix, args.allow_host_execution))
    else:
        parser.error("Provide --exp or --evaluate-run")


if __name__ == "__main__":
    main()
