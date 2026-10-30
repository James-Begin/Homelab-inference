#!/usr/bin/env python3
"""Run EvalPlus HumanEval+ coding evaluation from benchmarks/experiments.json under Protocol C-code-v1.

Implements Protocol C-code-v1 of improvement-plan.md:
- Full EvalPlus HumanEval+ (164 coding tasks, pass@1 greedy)
- Physical core pinning and NUMA interleaving per catalog entry
- Full thinking runway with sanitize-based extraction
- Structured output under logs/runs/code_<id>/
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import signal
import subprocess
import sys
import time
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional

from evalplus.data import get_human_eval_plus
from evalplus.evaluate import evaluate as run_evalplus_evaluation
from evalplus.sanitize import sanitize

from paths import ROOT, bin_dir, expand, models_dir
from catalog import load_catalog, get_experiment
from manifest import create_manifest, verify_resume

CATALOG_PATH = Path(__file__).resolve().parent / "experiments.json"
RUNS_DIR = ROOT / "logs" / "runs"

sys.stdout.reconfigure(line_buffering=True)
sys.stderr.reconfigure(line_buffering=True)


def build_user_prompt(problem: Dict[str, Any]) -> str:
    """Builds the standardized coding prompt requesting function completion."""
    prompt_text = problem["prompt"]
    return (
        "Please complete the following Python function according to its docstring.\n\n"
        f"```python\n{prompt_text}\n```\n\n"
        "Provide your reasoning, followed by the complete, executable implementation enclosed in a single ```python code block."
    )


def wait_for_server(url: str, timeout: int = 120) -> bool:
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=2) as resp:
                if resp.status == 200:
                    return True
        except Exception:
            pass
        time.sleep(1)
    return False


def free_port(port: int) -> None:
    try:
        out = subprocess.check_output(["lsof", "-ti", f":{port}"], text=True)
        pids = [int(p) for p in out.strip().split() if p.strip()]
        for pid in pids:
            try:
                os.kill(pid, signal.SIGTERM)
            except ProcessLookupError:
                pass
        for _ in range(20):
            time.sleep(0.5)
            check = subprocess.run(["lsof", "-ti", f":{port}"], capture_output=True, text=True)
            if not check.stdout.strip():
                return
        check = subprocess.run(["lsof", "-ti", f":{port}"], capture_output=True, text=True)
        for pid in [int(p) for p in check.stdout.strip().split() if p.strip()]:
            try:
                os.kill(pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
        time.sleep(1)
    except Exception:
        pass


def stop_process_group(proc: subprocess.Popen) -> None:
    try:
        os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
        proc.wait(timeout=5)
    except Exception:
        try:
            os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
        except Exception:
            pass


def query_chat_completion(
    url: str,
    user_text: str,
    max_tokens: int = 4096,
    temperature: float = 0.0,
    top_p: float = 1.0,
    system_prompt: Optional[str] = None
) -> Optional[Dict[str, Any]]:
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": user_text})

    payload = {
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": top_p,
        "stream": False,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{url}/v1/chat/completions",
        data=data,
        headers={"Content-Type": "application/json"}
    )
    req_timeout = max(1800, int(max_tokens / 10.0) + 300)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=req_timeout) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                choice = res.get("choices", [{}])[0]
                msg = choice.get("message", {})
                usage = res.get("usage", {})
                timings = res.get("timings", {})

                completion_tokens = usage.get("completion_tokens", 0)
                prompt_tokens = usage.get("prompt_tokens", 0)

                return {
                    "content": msg.get("content", ""),
                    "reasoning_content": msg.get("reasoning_content", ""),
                    "finish_reason": choice.get("finish_reason", "unknown"),
                    "tokens_predicted": completion_tokens,
                    "tokens_evaluated": prompt_tokens,
                    "timings": timings,
                    "raw_response": res
                }
        except urllib.error.HTTPError as exc:
            err_body = exc.read().decode("utf-8", errors="replace")
            print(f"Chat completion HTTP error {exc.code} (attempt {attempt + 1}/3): {err_body}")
            time.sleep(2)
        except Exception as exc:
            print(f"Chat completion query error (attempt {attempt + 1}/3): {exc}")
            time.sleep(2)
    return None


def extract_python_solution(raw_text: str, entry_point: str) -> str:
    """Robustly extracts the Python code solution for entry_point from model output.

    Handles reasoning monologues, <think> tags, and markdown fences, avoiding the
    O(N^3) line-slice AST parsing explosion in evalplus.sanitize.code_extract on large outputs.
    """
    if not raw_text:
        return ""

    # 1. Search for markdown code blocks (```python ... ``` or ``` ... ```)
    blocks = re.findall(r"```(?:python)?\s*\n(.*?)\n```", raw_text, re.DOTALL)
    if blocks:
        # Search backwards from the last block for the entry_point definition
        for block in reversed(blocks):
            if f"def {entry_point}" in block:
                try:
                    san = sanitize(block, entrypoint=entry_point)
                    if san.strip():
                        return san
                except Exception:
                    pass
                return block.strip()
        # Fallback to the last code block
        last_block = blocks[-1].strip()
        try:
            san = sanitize(last_block, entrypoint=entry_point)
            if san.strip():
                return san
        except Exception:
            pass
        return last_block

    # 2. If no markdown fence, strip <think>...</think> if present
    no_think = re.sub(r"<think>.*?</think>", "", raw_text, flags=re.DOTALL).strip()
    candidate = no_think if no_think else raw_text

    # 3. If entry_point exists in candidate, find def {entry_point}
    if f"def {entry_point}" in candidate:
        start_idx = candidate.rfind(f"def {entry_point}")
        tail = candidate[start_idx:]
        try:
            san = sanitize(tail, entrypoint=entry_point)
            if san.strip():
                return san
        except Exception:
            pass
        return tail

    # 4. Fallback: sanitize candidate directly
    try:
        san = sanitize(candidate, entrypoint=entry_point)
        if san.strip():
            return san
    except Exception:
        pass

    return candidate


def run_code_eval(
    exp_key: str,
    port: int = 8087,
    max_tokens: int = 4096,
    dry_run: bool = False,
    force_new_run: bool = False
) -> int:
    catalog = load_catalog()
    exp = get_experiment(catalog, exp_key)

    dataset = get_human_eval_plus()
    problems = list(dataset.values())

    model_raw = exp["model"]
    model_expanded = expand(model_raw)
    model_path = Path(model_expanded)
    if not model_path.is_absolute() or not model_path.exists():
        cand = models_dir() / model_raw
        if cand.exists():
            model_path = cand
    if not model_path.exists():
        raise SystemExit(f"Model path does not exist: {model_path}")

    engine_home = Path(os.environ.get("IK_LLAMA_HOME", "/home/james/ik_llama.cpp")).resolve()
    server_bin = engine_home / "build" / "bin" / "llama-server"
    if not server_bin.exists():
        server_bin = engine_home / "build" / "bin" / "Release" / "llama-server"
    if not server_bin.exists():
        raise SystemExit(f"llama-server not found in {engine_home}")

    server_flags = exp["server_flags"].format(port=port)
    needed_ctx = max(32768, max_tokens + 4096) if max_tokens >= 8192 else max(16384, max_tokens + 4096)
    if "-c " in server_flags:
        server_flags = re.sub(
            r"-c\s+(\d+)",
            lambda m: f"-c {max(needed_ctx, int(m.group(1)))}" if int(m.group(1)) < needed_ctx else m.group(0),
            server_flags
        )
    else:
        server_flags += f" -c {needed_ctx}"

    numactl_cmd = exp.get("numactl", "")
    full_cmd = f"{numactl_cmd} {server_bin} -m {model_path} {server_flags}".strip()
    argv = shlex.split(full_cmd)

    run_id = f"code_{exp['id']}"
    run_dir = RUNS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    manifest_file = run_dir / "manifest.json"
    rows_file = run_dir / "rows.jsonl"
    samples_file = run_dir / "samples.jsonl"
    server_log_file = run_dir / "server.log"
    summary_file = run_dir / "summary.json"
    report_file = run_dir / "report.md"

    system_prompt = (
        "You are an expert Python software engineer. Complete the given Python function according to the docstring specifications. "
        "Provide clean, correct, executable Python code."
    )

    current_manifest = create_manifest(
        exp_entry=exp,
        engine_dir=engine_home,
        model_path=model_path,
        prompt_file=None,
        request_params={"max_tokens": max_tokens, "endpoint": "chat", "benchmark": "HumanEvalPlus-164", "system_prompt": system_prompt}
    )

    if dry_run:
        print("=== DRY RUN MANIFEST & RESOLVED COMMAND ===")
        print(f"Command:\n  {full_cmd}\n")
        print("Manifest:")
        print(json.dumps(current_manifest, indent=2))
        print("===========================================")
        return 0

    if manifest_file.exists() and not force_new_run:
        prior_manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
        ok, reason = verify_resume(prior_manifest, current_manifest)
        if not ok:
            print("ERROR: Resume guard rejected continuation due to manifest mismatch:")
            print(f"  - {reason}")
            print("Use --force-new-run to start fresh.")
            return 1
    else:
        manifest_file.write_text(json.dumps(current_manifest, indent=2), encoding="utf-8")
        if force_new_run:
            if rows_file.exists():
                rows_file.unlink()
            if samples_file.exists():
                samples_file.unlink()

    existing_rows: Dict[str, Dict[str, Any]] = {}
    if rows_file.exists():
        for line in rows_file.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                existing_rows[r["task_id"]] = r
        print(f"Resuming run: loaded {len(existing_rows)} completed coding problems.")

    if len(existing_rows) >= len(problems) and summary_file.exists():
        print(f"All {len(problems)} coding problems already completed and evaluated for {exp_key}. Skipping generation.")
        return 0

    free_port(port)
    time.sleep(1)
    log_handle = server_log_file.open("a", encoding="utf-8")
    proc = subprocess.Popen(
        argv,
        stdout=log_handle,
        stderr=subprocess.STDOUT,
        start_new_session=True,
    )

    url_base = f"http://127.0.0.1:{port}"
    url_health = f"{url_base}/health"

    system_prompt = (
        "You are an expert Python software engineer. Complete the given Python function according to the docstring specifications. "
        "Provide clean, correct, executable Python code."
    )

    try:
        print(f"Launching server on port {port} (log: {server_log_file})...")
        if not wait_for_server(url_health, timeout=120):
            print("Server failed to respond to /health. Check server.log.")
            return 1
        print("Server is ready. Beginning code generation...")

        completed_count = len(existing_rows)

        for idx, prob in enumerate(problems):
            task_id = prob["task_id"]
            if task_id in existing_rows:
                continue

            entry_point = prob["entry_point"]
            user_text = build_user_prompt(prob)

            t0 = time.time()
            res = query_chat_completion(
                url=url_base,
                user_text=user_text,
                max_tokens=max_tokens,
                temperature=0.0,
                top_p=1.0,
                system_prompt=system_prompt
            )
            wall_sec = time.time() - t0

            if res is None:
                print(f"Error querying task {task_id}. Halting pipeline for resume.")
                return 1

            content = res.get("content", "")
            reasoning = res.get("reasoning_content", "")
            full_text = f"{reasoning}\n\n{content}" if reasoning and content else (content or reasoning or "")
            finish_reason = res.get("finish_reason", "unknown")
            tokens_pred = res.get("tokens_predicted", 0)

            # Sanitize and extract the Python function cleanly using pre-extraction
            sanitized_solution = extract_python_solution(full_text, entry_point=entry_point)

            timings = res.get("timings", {})
            pred_ms = timings.get("predicted_ms", 0.0)
            speed_tps = (tokens_pred / (pred_ms / 1000.0)) if pred_ms > 0 else (tokens_pred / wall_sec if wall_sec > 0 else 0.0)

            row_entry = {
                "idx": completed_count + 1,
                "task_id": task_id,
                "entry_point": entry_point,
                "tokens": tokens_pred,
                "speed_tps": round(speed_tps, 2),
                "wall_time": round(wall_sec, 2),
                "finish_reason": finish_reason,
                "solution": sanitized_solution,
            }

            with open(rows_file, "a", encoding="utf-8") as rf:
                rf.write(json.dumps(row_entry) + "\n")

            with open(samples_file, "a", encoding="utf-8") as sf:
                sf.write(json.dumps({"task_id": task_id, "solution": sanitized_solution}) + "\n")

            existing_rows[task_id] = row_entry
            completed_count += 1

            print(
                f"[{completed_count:03d}/{len(problems)}] Task: {task_id:<14} | "
                f"{speed_tps:5.2f} t/s | {tokens_pred:4d} tok | {wall_sec:5.1f}s"
            )

        print("\nAll 164 problems generated. Initiating EvalPlus unit-test sandbox evaluation...")
        eval_result = run_evalplus_evaluation(
            dataset="humaneval",
            samples=str(samples_file),
            parallel=14
        )

        # Extract base and plus scores from EvalPlus evaluation result file
        eval_result_path = samples_file.parent / f"{samples_file.stem}_eval_results.json"
        base_pass = 0.0
        plus_pass = 0.0
        if eval_result_path.exists():
            try:
                eval_data = json.loads(eval_result_path.read_text(encoding="utf-8"))
                eval_dict = eval_data.get("eval", {})
                if eval_dict:
                    n_eval = len(eval_dict)
                    b_pass = sum(1 for v in eval_dict.values() if v and v[0].get("base_status") == "pass")
                    p_pass = sum(1 for v in eval_dict.values() if v and v[0].get("plus_status") == "pass")
                    base_pass = b_pass / n_eval
                    plus_pass = p_pass / n_eval
            except Exception as e:
                print(f"Warning: could not parse eval results file: {e}")

        all_rows = list(existing_rows.values())
        avg_speed = sum(r.get("speed_tps", 0.0) for r in all_rows) / len(all_rows) if all_rows else 0.0
        total_wall = sum(r.get("wall_time", 0.0) for r in all_rows)
        avg_wall = total_wall / len(all_rows) if all_rows else 0.0

        summary_data = {
            "run_id": run_id,
            "experiment_id": exp["id"],
            "model": exp["model"],
            "total_problems": len(all_rows),
            "max_tokens_ceiling": max_tokens,
            "base_pass_pct": round(base_pass * 100.0, 2),
            "plus_pass_pct": round(plus_pass * 100.0, 2),
            "average_decode_tps": round(avg_speed, 2),
            "total_wall_time_sec": round(total_wall, 1),
            "avg_wall_time_per_task_sec": round(avg_wall, 2),
        }
        summary_file.write_text(json.dumps(summary_data, indent=2), encoding="utf-8")

        report_md = f"""# Coding Benchmark Report: {exp['name']}
- **Run ID:** `{run_id}`
- **Protocol:** Protocol C-code-v1 (EvalPlus HumanEval+)
- **Model:** `{exp['model']}`
- **Total Problems:** {len(all_rows)}
- **Base Pass@1:** **{summary_data['base_pass_pct']}%**
- **Plus Pass@1:** **{summary_data['plus_pass_pct']}%**
- **Average Decode Speed:** {summary_data['average_decode_tps']} tokens/sec
- **Total Wall Time:** {summary_data['total_wall_time_sec']}s ({summary_data['total_wall_time_sec']/60:.1f} min)
- **Average Time Per Task:** {summary_data['avg_wall_time_per_task_sec']}s
"""
        report_file.write_text(report_md, encoding="utf-8")
        print(f"\n=======================================================")
        print(f"EVALPLUS EVALUATION COMPLETE: {exp['id']}")
        print(f"Base Pass@1: {summary_data['base_pass_pct']}%")
        print(f"Plus Pass@1: {summary_data['plus_pass_pct']}%")
        print(f"Average Decode Speed: {summary_data['average_decode_tps']} t/s")
        print(f"Average Wall Time per Task: {summary_data['avg_wall_time_per_task_sec']}s")
        print(f"Saved run artifacts to {run_dir}/")
        print(f"=======================================================\n")
        return 0

    finally:
        stop_process_group(proc)
        log_handle.close()
        free_port(port)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run EvalPlus HumanEval+ under Protocol C-code-v1.")
    parser.add_argument("--exp", required=True, help="Experiment number or id (e.g. 50, 94)")
    parser.add_argument("--port", type=int, default=8087)
    parser.add_argument("--max-tokens", type=int, default=4096, help="Token ceiling (default: 4096)")
    parser.add_argument("--dry-run", action="store_true", help="Print resolved command and manifest, then exit")
    parser.add_argument("--force-new-run", action="store_true", help="Overwrite existing manifest and start fresh")
    args = parser.parse_args()

    sys.exit(run_code_eval(
        exp_key=args.exp,
        port=args.port,
        max_tokens=args.max_tokens,
        dry_run=args.dry_run,
        force_new_run=args.force_new_run
    ))


if __name__ == "__main__":
    main()
