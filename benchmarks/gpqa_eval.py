#!/usr/bin/env python3
"""Generate and grade GPQA responses from the experiment catalog."""

from __future__ import annotations

import argparse
import json
import re
import shlex
import subprocess
import sys
import time
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional

from paths import ROOT, bin_dir, expand, ik_home, models_dir
from grading import grade_response, RowStatus
from catalog import load_catalog, get_experiment
from manifest import create_manifest, verify_resume
from runtime import decode_rate, require_free_port, stopping_metadata, stop_process_group, wait_for_server
from summarize_runs import summarize_gpqa

GPQA_FILE = ROOT / "benchmarks" / "data" / "gpqa_subset_50.json"
SYSTEM_PROMPT = "You are an expert scientific researcher. Reason step by step, then conclude with Final answer: X."
RUNS_DIR = ROOT / "logs" / "runs"



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


def build_raw_prompt(user_text, flint=False):
    if flint:
        return f"<|system|>\n{SYSTEM_PROMPT}<|end_of_text|>\n<|user|>\n{user_text}<|end_of_text|>\n<|assistant|>\n"
    return f"<|im_start|>system\n{SYSTEM_PROMPT}<|im_end|>\n<|im_start|>user\n{user_text}<|im_end|>\n<|im_start|>assistant\n"


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
        "seed": 0,
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
                    "content": msg.get("content") or "",
                    "reasoning_content": msg.get("reasoning_content", ""),
                    **stopping_metadata(res, completion_tokens, max_tokens, choice.get("finish_reason")),
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


def query_raw_completion(
    url: str,
    prompt_text: str,
    max_tokens: int = 8192,
    temperature: float = 0.0,
    top_p: float = 1.0,
    stop: Optional[List[str]] = None
) -> Optional[Dict[str, Any]]:
    """Query the explicitly selected raw-completion endpoint."""
    payload = {
        "prompt": prompt_text,
        "n_predict": max_tokens,
        "temperature": temperature,
        "top_p": top_p,
        "stop": stop or ["<|im_end|>", "<|end_of_text|>"],
        "seed": 0,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{url}/completion",
        data=data,
        headers={"Content-Type": "application/json"}
    )
    req_timeout = max(1800, int(max_tokens / 10.0) + 300)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=req_timeout) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                timings = res.get("timings", {})
                return {
                    "content": res.get("content") or "",
                    "reasoning_content": "",
                    **stopping_metadata(res, timings.get("predicted_n", 0), max_tokens),
                    "tokens_predicted": timings.get("predicted_n", 0),
                    "tokens_evaluated": timings.get("prompt_n", 0),
                    "timings": timings,
                    "raw_response": res
                }
        except urllib.error.HTTPError as exc:
            err_body = exc.read().decode("utf-8", errors="replace")
            print(f"Raw completion HTTP error {exc.code} (attempt {attempt + 1}/3): {err_body}")
            time.sleep(2)
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
    force_new_run: bool = False,
    run_suffix: str = ""
) -> int:
    if endpoint not in ("chat", "raw") or max_tokens <= 0:
        raise ValueError("Invalid endpoint or token ceiling")
    if not re.fullmatch(r"[A-Za-z0-9_.-]*", run_suffix):
        raise ValueError("Invalid run suffix")
    if force_new_run:
        run_suffix += f"_{time.time_ns()}"
    catalog = load_catalog()
    exp = get_experiment(catalog, exp_key)

    if gpqa_path is None:
        gpqa_path = GPQA_FILE
    questions = json.loads(gpqa_path.read_text())
    if not questions or len({q["id"] for q in questions}) != len(questions):
        raise ValueError("GPQA dataset is empty or has duplicate question IDs")

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

    engine_home = ik_home().resolve()
    server_bin = bin_dir() / "llama-server"
    if not server_bin.exists():
        server_bin = bin_dir() / "Release/llama-server"
    if not server_bin.exists():
        raise SystemExit(f"llama-server not found in {engine_home}")

    server_flags = expand(exp["server_flags"], port=port)
    # Ensure server context -c has sufficient headroom for max_tokens generation + prompt
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
    argv = shlex.split(numactl_cmd) + [str(server_bin), "-m", str(model_path)] + shlex.split(server_flags)
    full_cmd = shlex.join(argv)

    # Manifest and Run Directory Setup
    run_id = f"run_{exp['id']}{run_suffix}"
    run_dir = RUNS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    manifest_file = run_dir / "manifest.json"
    rows_file = run_dir / "rows.jsonl"
    server_log_file = run_dir / "server.log"
    summary_file = run_dir / "summary.json"

    current_manifest = create_manifest(
        exp_entry=exp,
        engine_dir=engine_home,
        model_path=model_path,
        prompt_file=gpqa_path,
        request_params={"max_tokens": max_tokens, "endpoint": endpoint, "temperature": 0.0, "top_p": 1.0, "stream": False, "seed": 0,
                        "system_prompt": SYSTEM_PROMPT, "prompts": {str(q["id"]): build_user_text(q) for q in questions},
                        "raw_template": "flint" if "flint" in exp["model"].lower() else "qwen", "stops": ["<|im_end|>", "<|end_of_text|>"]},
        dataset=questions, server_argv=argv, server_binary=server_bin
    )

    if dry_run:
        print("=== DRY RUN MANIFEST & RESOLVED COMMAND ===")
        print(f"Command:\n  {full_cmd}\n")
        print("Manifest:")
        print(json.dumps(current_manifest, indent=2))
        return 0

    # Resume guard: verify manifest if previous run exists
    if manifest_file.exists():
        prior_manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
        ok, reason = verify_resume(prior_manifest, current_manifest)
        if not ok:
            print("ERROR: Resume guard rejected continuation due to manifest mismatch:")
            print(f"  - {reason}")
            print("Use --run-suffix or --force-new-run to retain these records and start separately.")
            return 1
    else:
        if rows_file.exists():
            raise ValueError("Existing rows lack a manifest; choose a new run suffix")
        manifest_file.write_text(json.dumps(current_manifest, indent=2), encoding="utf-8")

    # Load existing rows to resume
    existing_rows: Dict[str, Dict[str, Any]] = {}
    if rows_file.exists():
        for line in rows_file.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                if r["id"] in existing_rows or r["id"] not in {q["id"] for q in questions}:
                    raise ValueError("Duplicate or unknown question in saved rows")
                existing_rows[r["id"]] = r
        print(f"Resuming run: loaded {len(existing_rows)} completed questions.")

    if len(existing_rows) == len(questions) and summary_file.exists():
        print(f"All {len(questions)} questions already completed for {exp_key}. Skipping generation.")
        return 0

    # Launch server
    require_free_port(port)
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
        if not wait_for_server(url_health, proc, timeout=120):
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

            t0 = time.monotonic()
            if endpoint == "chat":
                res = query_chat_completion(
                    url=url_base,
                    user_text=user_text,
                    max_tokens=max_tokens,
                    temperature=0.0,
                    top_p=1.0,
                    system_prompt=SYSTEM_PROMPT
                )
            else:
                prompt_text = build_raw_prompt(user_text, "flint" in exp["model"].lower())
                res = query_raw_completion(url=url_base, prompt_text=prompt_text, max_tokens=max_tokens, temperature=0.0, top_p=1.0)
            wall_sec = time.monotonic() - t0

            if res is None:
                print(f"Error querying question {qid}. Halting pipeline for resume.")
                return 1

            content = res.get("content", "")
            finish_reason = res.get("finish_reason", "unknown")
            tokens_pred = res.get("tokens_predicted", 0)

            # Grade response strictly using grading.py
            is_length_truncated = res.get("max_tokens_hit", False)
            status, strict_ans, lenient_ans = grade_response(
                content=content,
                gold=gold,
                finish_reason=finish_reason,
                max_tokens_hit=is_length_truncated
            )

            is_strict_correct = (status == RowStatus.CORRECT)
            is_lenient_correct = (lenient_ans is not None and lenient_ans.upper() == gold.upper())

            status_str = "CORRECT" if is_strict_correct else f"WRONG (pred={strict_ans})"
            if status == RowStatus.NO_ANSWER_TRUNCATED:
                status_str = "NO FINAL ANSWER (length stop or unclosed thinking tag)"

            timings = res.get("timings", {})
            pred_ms = timings.get("predicted_ms", 0.0)
            speed_tps = decode_rate(tokens_pred, pred_ms)

            row_entry = {
                "idx": completed_count + 1,
                "id": qid,
                "gold": gold,
                "pred": strict_ans,
                "lenient_pred": lenient_ans,
                "regraded_strict_correct": is_strict_correct,
                "regraded_lenient_correct": is_lenient_correct,
                "status": status.value,
                "tokens": tokens_pred,
                "speed_tps": round(speed_tps, 2) if speed_tps is not None else None,
                "wall_time": round(wall_sec, 2),
                "finish_reason": finish_reason,
                "max_tokens_hit": is_length_truncated,
                "raw_stopping": res.get("raw_stopping", {}),
                "timings": timings,
                "reasoning_content": res.get("reasoning_content", ""),
                "content": content,
            }

            # Append row to rows.jsonl
            with open(rows_file, "a", encoding="utf-8") as rf:
                rf.write(json.dumps(row_entry) + "\n")

            existing_rows[qid] = row_entry
            completed_count += 1
            if is_strict_correct:
                correct_strict_count += 1

            print(
                f"[{completed_count:02d}/{len(questions)}] ID: {qid} | "
                f"Gold: {gold} | Strict: {status_str} | "
                f"decode {speed_tps} t/s | {tokens_pred} tok | {wall_sec:5.1f}s"
            )

        summary_file.write_text(json.dumps({"run_id": run_id, "experiment_id": exp["id"], "model": exp["model"], "max_tokens_ceiling": max_tokens}, indent=2))
        summary = summarize_gpqa(run_dir, write=True)
        print(f"Strict score: {summary['strict_score']}; token-limit responses: {summary['token_limit_count']}. Saved {run_dir}")
        return 0

    finally:
        stop_process_group(proc)
        log_handle.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a catalogued GPQA Diamond eval under Protocol C-gpqa-v2.")
    parser.add_argument("--exp", required=False, help="Experiment number or id (e.g. 50, 94)")
    parser.add_argument("--list", action="store_true", help="Print experiment catalog")
    parser.add_argument("--dry-run", action="store_true", help="Print resolved command and manifest, then exit")
    parser.add_argument("--port", type=int, default=8087)
    parser.add_argument("--max-tokens", type=int, default=8192, help="Token ceiling for thinking (default: 8192)")
    parser.add_argument("--endpoint", choices=["chat", "raw"], default="chat", help="API endpoint")
    parser.add_argument("--force-new-run", action="store_true", help="Create a separate timestamped run directory")
    parser.add_argument("--run-suffix", default="")
    parser.add_argument("--dataset", type=Path, help="Local GPQA subset JSON")
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
        force_new_run=args.force_new_run, run_suffix=args.run_suffix, gpqa_path=args.dataset
    ))


if __name__ == "__main__":
    main()
