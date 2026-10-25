#!/usr/bin/env python3
"""Run one GPQA Diamond eval from benchmarks/experiments.json under Protocol C-gpqa-v2.

Implements Phase 1 (Harness Repair) and Phase 3 (Protocol C-gpqa-v2) of improvement-plan.md:
- Supports /v1/chat/completions and raw endpoint
- Configurable --max-tokens (default: 8192, allowing thoughts to unfold to full context)
- Strict regex extraction outside reasoning blocks via benchmarks/grading.py
- Manifest collection and resume guard via benchmarks/manifest.py
- Structured output under logs/runs/<id>/
"""

from __future__ import annotations

import argparse
import hashlib
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

from paths import ROOT, bin_dir, expand, models_dir
from grading import grade_response, RowStatus
from catalog import load_catalog, get_experiment
from manifest import create_manifest, verify_resume

CATALOG_PATH = Path(__file__).resolve().parent / "experiments.json"
GPQA_FILE = ROOT / "logs" / "raw_checkpoints" / "gpqa_subset_50.json"
RUNS_DIR = ROOT / "logs" / "runs"
REPORT_DIR = ROOT / "logs" / "gpqa_reports"
CHECKPOINT_DIR = ROOT / "logs" / "raw_checkpoints"

sys.stdout.reconfigure(line_buffering=True)
sys.stderr.reconfigure(line_buffering=True)


def build_user_text(item: dict) -> str:
    """Builds the standardized user prompt requesting free reasoning ending in Final answer: X."""
    options = item["options"]
    return (
        f"{item['question']}\n\n"
        "Options:\n"
        f"A) {options['A']}\n"
        f"B) {options['B']}\n"
        f"C) {options['C']}\n"
        f"D) {options['D']}\n\n"
        "Think step by step and reason carefully. When you are finished, end your response on its own line with exactly:\n"
        "Final answer: X\n"
        "where X is the single letter (A, B, C, or D) of the correct option."
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
        for pid in out.strip().split():
            os.kill(int(pid), signal.SIGTERM)
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
    max_tokens: int = 8192,
    temperature: float = 0.0,
    top_p: float = 1.0,
    system_prompt: Optional[str] = None
) -> Optional[Dict[str, Any]]:
    """Queries the server's OpenAI-compatible /v1/chat/completions endpoint."""
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
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=600) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                choice = res.get("choices", [{}])[0]
                msg = choice.get("message", {})
                usage = res.get("usage", {})
                timings = res.get("timings", {})

                # If server doesn't provide timings in chat format, approximate from usage
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
        except Exception as exc:
            print(f"Chat completion query error (attempt {attempt + 1}/3): {exc}")
            time.sleep(2)
    return None


def query_raw_completion(
    url: str,
    prompt_text: str,
    max_tokens: int = 8192,
    temperature: float = 0.0,
    top_p: float = 1.0,
    stop: Optional[List[str]] = None
) -> Optional[Dict[str, Any]]:
    """Fallback to /completion endpoint."""
    payload = {
        "prompt": prompt_text,
        "n_predict": max_tokens,
        "temperature": temperature,
        "top_p": top_p,
        "stop": stop or ["<|im_end|>", "<|end_of_text|>"],
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{url}/completion",
        data=data,
        headers={"Content-Type": "application/json"}
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=600) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                timings = res.get("timings", {})
                return {
                    "content": res.get("content", ""),
                    "reasoning_content": "",
                    "finish_reason": "stop" if not res.get("truncated") else "length",
                    "tokens_predicted": timings.get("predicted_n", 0),
                    "tokens_evaluated": timings.get("prompt_n", 0),
                    "timings": timings,
                    "raw_response": res
                }
        except Exception as exc:
            print(f"Raw completion query error (attempt {attempt + 1}/3): {exc}")
            time.sleep(2)
    return None


def run_eval(
    exp_key: str,
    port: int = 8087,
    max_tokens: int = 8192,
    dry_run: bool = False,
    endpoint: str = "chat",
    gpqa_path: Optional[Path] = None,
    force_new_run: bool = False
) -> int:
    catalog = load_catalog()
    exp = get_experiment(catalog, exp_key)

    if gpqa_path is None:
        gpqa_path = GPQA_FILE
    questions = json.loads(gpqa_path.read_text())

    # Build server command line
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
    # Ensure server context -c has sufficient headroom for max_tokens generation + prompt
    needed_ctx = max(16384, max_tokens + 4096)
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

    # Manifest and Run Directory Setup
    run_id = f"run_{exp['id']}"
    run_dir = RUNS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    manifest_file = run_dir / "manifest.json"
    rows_file = run_dir / "rows.jsonl"
    server_log_file = run_dir / "server.log"
    summary_file = run_dir / "summary.json"
    report_file = run_dir / "report.md"

    current_manifest = create_manifest(
        exp_entry=exp,
        engine_dir=engine_home,
        model_path=model_path,
        prompt_file=None,
        request_params={"max_tokens": max_tokens, "endpoint": endpoint}
    )

    if dry_run:
        print("=== DRY RUN MANIFEST & RESOLVED COMMAND ===")
        print(f"Command:\n  {full_cmd}\n")
        print("Manifest:")
        print(json.dumps(current_manifest, indent=2))
        print("===========================================")
        return 0

    # Resume guard: verify manifest if previous run exists
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

    # Load existing rows to resume
    existing_rows: Dict[str, Dict[str, Any]] = {}
    if rows_file.exists():
        for line in rows_file.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                existing_rows[r["id"]] = r
        print(f"Resuming run: loaded {len(existing_rows)} completed questions.")

    # Launch server
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

    try:
        print(f"Launching server on port {port} (log: {server_log_file})...")
        if not wait_for_server(url_health, timeout=120):
            print("Server failed to respond to /health. Check server.log.")
            return 1
        print("Server is ready. Beginning evaluation...")

        completed_count = len(existing_rows)
        correct_strict_count = sum(1 for r in existing_rows.values() if r.get("regraded_strict_correct"))

        for idx, item in enumerate(questions):
            qid = item["id"]
            if qid in existing_rows:
                continue

            gold = item.get("correct_letter") or item.get("gold")
            user_text = build_user_text(item)

            t0 = time.time()
            if endpoint == "chat":
                res = query_chat_completion(
                    url=url_base,
                    user_text=user_text,
                    max_tokens=max_tokens,
                    temperature=0.0,
                    top_p=1.0,
                    system_prompt="You are an expert scientific researcher. Reason step by step, then conclude with Final answer: X."
                )
                if res is None:
                    print("Notice: Chat endpoint failed, falling back to /completion...")
                    if "flint" in exp["model"].lower():
                        prompt_text = f"<|system|>\nYou are an expert scientific researcher. Reason step by step, then conclude with Final answer: X.<|end_of_text|>\n<|user|>\n{user_text}<|end_of_text|>\n<|assistant|>\n"
                    else:
                        prompt_text = f"<|im_start|>system\nYou are an expert scientific researcher. Reason step by step, then conclude with Final answer: X.<|im_end|>\n<|im_start|>user\n{user_text}<|im_end|>\n<|im_start|>assistant\n"
                    res = query_raw_completion(
                        url=url_base,
                        prompt_text=prompt_text,
                        max_tokens=max_tokens,
                        temperature=0.0,
                        top_p=1.0
                    )
            else:
                prompt_text = f"<|user|>\n{user_text}\n<|assistant|>\n"
                res = query_raw_completion(
                    url=url_base,
                    prompt_text=prompt_text,
                    max_tokens=max_tokens,
                    temperature=0.0,
                    top_p=1.0
                )
            wall_sec = time.time() - t0

            if res is None:
                print(f"Error querying question {qid}. Halting pipeline for resume.")
                return 1

            content = res.get("content", "")
            finish_reason = res.get("finish_reason", "unknown")
            tokens_pred = res.get("tokens_predicted", 0)

            # Grade response strictly using grading.py
            is_length_truncated = (finish_reason == "length")
            row_grade = grade_response(content, gold, is_length_truncated=is_length_truncated)

            status_str = "CORRECT" if row_grade.is_strict_correct else f"WRONG (pred={row_grade.strict_answer})"
            if row_grade.status == RowStatus.NO_ANSWER_TRUNCATED:
                status_str = "TRUNCATED (hit token ceiling mid-thought)"

            timings = res.get("timings", {})
            pred_ms = timings.get("predicted_ms", 0.0)
            speed_tps = (tokens_pred / (pred_ms / 1000.0)) if pred_ms > 0 else (tokens_pred / wall_sec if wall_sec > 0 else 0.0)

            row_entry = {
                "idx": completed_count + 1,
                "id": qid,
                "gold": gold,
                "pred": row_grade.strict_answer,
                "lenient_pred": row_grade.lenient_answer,
                "regraded_strict_correct": row_grade.is_strict_correct,
                "regraded_lenient_correct": row_grade.is_lenient_correct,
                "status": row_grade.status.value,
                "tokens": tokens_pred,
                "speed_tps": round(speed_tps, 2),
                "wall_time": round(wall_sec, 2),
                "finish_reason": finish_reason,
                "content": content,
            }

            # Append row to rows.jsonl
            with open(rows_file, "a", encoding="utf-8") as rf:
                rf.write(json.dumps(row_entry) + "\n")

            existing_rows[qid] = row_entry
            completed_count += 1
            if row_grade.is_strict_correct:
                correct_strict_count += 1

            print(
                f"[{completed_count:02d}/{len(questions)}] ID: {qid} | "
                f"Gold: {gold} | Strict: {status_str} | "
                f"{speed_tps:5.2f} t/s | {tokens_pred} tok | {wall_sec:5.1f}s"
            )

        # Build summary and report
        all_rows = list(existing_rows.values())
        strict_corr = sum(1 for r in all_rows if r.get("regraded_strict_correct"))
        lenient_corr = sum(1 for r in all_rows if r.get("regraded_lenient_correct"))
        trunc_count = sum(1 for r in all_rows if r.get("status") == RowStatus.NO_ANSWER_TRUNCATED.value)
        avg_speed = sum(r.get("speed_tps", 0.0) for r in all_rows) / len(all_rows) if all_rows else 0.0

        summary_data = {
            "run_id": run_id,
            "experiment_id": exp["id"],
            "model": exp["model"],
            "total_questions": len(all_rows),
            "max_tokens_ceiling": max_tokens,
            "strict_score": f"{strict_corr}/{len(all_rows)}",
            "strict_pct": round((strict_corr / len(all_rows)) * 100.0, 2) if all_rows else 0.0,
            "lenient_score": f"{lenient_corr}/{len(all_rows)}",
            "lenient_pct": round((lenient_corr / len(all_rows)) * 100.0, 2) if all_rows else 0.0,
            "truncated_count": trunc_count,
            "average_decode_tps": round(avg_speed, 2),
        }
        summary_file.write_text(json.dumps(summary_data, indent=2), encoding="utf-8")

        # Generate markdown report
        report_md = f"""# Benchmark Report: {exp['name']}
- **Run ID:** `{run_id}`
- **Protocol:** Protocol C-gpqa-v2
- **Model:** `{exp['model']}`
- **Token Ceiling (max_tokens):** {max_tokens} tokens
- **Strict Score:** **{strict_corr}/{len(all_rows)}** ({summary_data['strict_pct']}%)
- **Lenient Score:** {lenient_corr}/{len(all_rows)} ({summary_data['lenient_pct']}%)
- **Mid-Thought Truncations:** {trunc_count} ({round(trunc_count/len(all_rows)*100, 1)}%)
- **Average Decode Speed:** {summary_data['average_decode_tps']} tokens/sec

## Detailed Question Rows
| ID | Gold | Pred | Strict Status | Tokens | Decode Speed | Wall Time |
| :--- | :---: | :---: | :--- | :---: | :---: | :---: |
"""
        for r in all_rows:
            report_md += f"| `{r['id']}` | {r['gold']} | {r['pred'] or '-'} | `{r['status']}` | {r['tokens']} | {r.get('speed_tps', 0.0)} t/s | {r.get('wall_time', 0.0)}s |\n"

        report_file.write_text(report_md, encoding="utf-8")
        print(f"\n=======================================================")
        print(f"EVALUATION COMPLETE: {exp['id']}")
        print(f"Strict Score: {strict_corr}/{len(all_rows)} ({summary_data['strict_pct']}%)")
        print(f"Lenient Score: {lenient_corr}/{len(all_rows)} ({summary_data['lenient_pct']}%)")
        print(f"Truncated Mid-Thought: {trunc_count}/{len(all_rows)}")
        print(f"Average Decode Speed: {summary_data['average_decode_tps']} t/s")
        print(f"Saved run artifacts to {run_dir}/")
        print(f"=======================================================\n")
        return 0

    finally:
        stop_process_group(proc)
        log_handle.close()
        free_port(port)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a catalogued GPQA Diamond eval under Protocol C-gpqa-v2.")
    parser.add_argument("--exp", required=False, help="Experiment number or id (e.g. 50, 94)")
    parser.add_argument("--list", action="store_true", help="Print experiment catalog")
    parser.add_argument("--dry-run", action="store_true", help="Print resolved command and manifest, then exit")
    parser.add_argument("--port", type=int, default=8087)
    parser.add_argument("--max-tokens", type=int, default=8192, help="Token ceiling for thinking (default: 8192)")
    parser.add_argument("--endpoint", choices=["chat", "raw"], default="chat", help="API endpoint")
    parser.add_argument("--force-new-run", action="store_true", help="Overwrite existing manifest and start fresh")
    args = parser.parse_args()

    if args.list:
        catalog = load_catalog()
        for e in catalog:
            print(f"{e.get('number', 0):>3}  {e.get('id')}")
        return

    if not args.exp:
        parser.print_help()
        sys.exit(1)

    sys.exit(run_eval(
        exp_key=args.exp,
        port=args.port,
        max_tokens=args.max_tokens,
        dry_run=args.dry_run,
        endpoint=args.endpoint,
        force_new_run=args.force_new_run
    ))


if __name__ == "__main__":
    main()
