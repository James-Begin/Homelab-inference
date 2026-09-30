#!/usr/bin/env python3
"""Run one GPQA Diamond eval from benchmarks/experiments.json.

The per-experiment scripts that used to live next to this file differed only
in the model, the server flags, and an optional quantize or repack step.
Those settings are the catalog. This runner launches llama-server, resumes
from logs/raw_checkpoints/<id>_checkpoint.json, and writes a report under
logs/gpqa_reports/.

    export IK_LLAMA_HOME=~/ik_llama.cpp
    python benchmarks/gpqa_eval.py --list
    python benchmarks/gpqa_eval.py --exp 47 --dry-run
    python benchmarks/gpqa_eval.py --exp 47
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

from paths import ROOT, bin_dir, expand, models_dir

CATALOG_PATH = Path(__file__).resolve().parent / "experiments.json"
GPQA_FILE = ROOT / "logs" / "raw_checkpoints" / "gpqa_subset_50.json"
REPORT_DIR = ROOT / "logs" / "gpqa_reports"
CHECKPOINT_DIR = ROOT / "logs" / "raw_checkpoints"
OPTIMIZATION_LOG = ROOT / "logs" / "optimization_tracker" / "optimization_log_50tps.md"

sys.stdout.reconfigure(line_buffering=True)
sys.stderr.reconfigure(line_buffering=True)


def load_catalog() -> list[dict]:
    return json.loads(CATALOG_PATH.read_text())


def find_experiment(catalog: list[dict], key: str) -> dict:
    hits = [
        exp for exp in catalog
        if str(exp["number"]) == key or exp["id"] == key
    ]
    if len(hits) == 1:
        return hits[0]
    prefix = [exp for exp in catalog if exp["id"].startswith(key)]
    if len(prefix) == 1:
        return prefix[0]
    known = ", ".join(str(exp["number"]) for exp in catalog)
    raise SystemExit(f"No single experiment matches {key!r}. Numbers in the catalog: {known}")


def checkpoint_path(exp: dict) -> Path:
    return CHECKPOINT_DIR / f"{exp['id']}_checkpoint.json"


def short_name(exp: dict) -> str:
    return re.sub(r"^Exp\s+\d+:\s*", "", exp["name"])


def print_catalog(catalog: list[dict]) -> None:
    for exp in catalog:
        prep = exp.get("prep") or {}
        kind = prep.get("kind", "")
        suffix = f"  [{kind}]" if kind else ""
        print(f"{exp['number']:>3}  {exp['model']}")
        print(f"     {short_name(exp)}{suffix}")


def build_user_text(item: dict, style: str) -> str:
    if style == "stored" and item.get("prompt"):
        return item["prompt"]
    options = item["options"]
    return (
        f"{item['question']}\n\n"
        "Options:\n"
        f"A) {options['A']}\n"
        f"B) {options['B']}\n"
        f"C) {options['C']}\n"
        f"D) {options['D']}\n\n"
        "Please state your final answer choice first (e.g. 'Answer: A'), then provide your brief reasoning."
    )


def chat_prompt(user_text: str) -> str:
    return (
        "<|im_start|>system\n"
        "You are an expert scientific researcher. Always provide your final answer choice first."
        "<|im_end|>\n"
        f"<|im_start|>user\n{user_text}<|im_end|>\n"
        "<|im_start|>assistant\n"
    )


def extract_answer_letter(completion_text: str):
    match = re.search(
        r"(?:answer is|answer|choice|option)[:\*\s]*\s*(?:\(?([A-D])\)?)",
        completion_text,
        re.IGNORECASE,
    )
    if match:
        return match.group(1).upper()
    match = re.search(r"\b([A-D])\b", completion_text)
    if match:
        return match.group(1).upper()
    return None


def question_id(row: dict):
    return row.get("id")


def row_correct(row: dict) -> bool:
    if "correct" in row:
        return bool(row["correct"])
    if "passed" in row:
        return bool(row["passed"])
    return False


def row_speed(row: dict) -> float:
    for key in ("speed_tps", "gen_speed"):
        value = row.get(key)
        if isinstance(value, (int, float)) and value > 0:
            return float(value)
    return 0.0


def server_argv(exp: dict, port: int) -> list[str]:
    # Keep the models directory out of the shell split so a path with spaces survives.
    token = "@@MODELS@@"
    flags = exp["server_flags"].replace("{models}", token).replace("{port}", str(port))
    parts = shlex.split(expand(exp["numactl"]))
    parts += [str(bin_dir() / "llama-server"), "-m", str(models_dir() / exp["model"])]
    parts += [part.replace(token, str(models_dir())) for part in shlex.split(flags)]
    return parts


def prepare_model(exp: dict, dry_run: bool) -> None:
    prep = exp.get("prep")
    if not prep:
        return
    dest = models_dir() / exp["model"]
    source = models_dir() / prep["source"]
    quantize = bin_dir() / "llama-quantize"
    if prep["kind"] == "repack":
        cmd = [str(quantize), "--repack", str(source), str(dest), "COPY", "28"]
    elif prep["kind"] == "quantize":
        cmd = [
            str(quantize),
            "--allow-requantize",
            "--custom-q",
            prep["custom_q"],
            str(source),
            str(dest),
            prep.get("out_type", "Q6_K"),
            "28",
        ]
    else:
        raise SystemExit(f"Unknown prep kind {prep['kind']!r} on exp {exp['number']}")
    if dest.exists():
        print(f"Model already present: {dest}")
        return
    print("Preparing model:", " ".join(cmd))
    if dry_run:
        return
    if not source.exists():
        raise SystemExit(f"Source model not found: {source}")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        raise SystemExit(f"Model prep failed with exit code {result.returncode}")


def wait_for_server(url: str, timeout: int = 180) -> bool:
    start = time.time()
    while time.time() - start < timeout:
        try:
            with urllib.request.urlopen(url, timeout=2) as resp:
                if resp.status == 200:
                    return True
        except Exception:
            pass
        time.sleep(1)
    return False


def query_completion(url: str, prompt_text: str, max_tokens: int = 1536):
    payload = {
        "prompt": chat_prompt(prompt_text),
        "n_predict": max_tokens,
        "temperature": 0.0,
        "top_p": 1.0,
        "stop": ["<|im_end|>"],
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=300) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as exc:
            print(f"Query error (attempt {attempt + 1}/3): {exc}")
            time.sleep(2)
    return None


def load_checkpoint(path: Path) -> list[dict]:
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        print(f"Checkpoint {path} is not valid JSON ({exc}). Starting over.")
        return []
    if not isinstance(data, list):
        print(f"Checkpoint {path} is not a list. Starting over.")
        return []
    return data


def append_optimization_log(exp: dict, report_name: str, n_correct: int, total_q: int, n_20: int, total_20: int, avg_speed: float, peak_speed: float) -> None:
    pct = (n_correct / total_q * 100.0) if total_q else 0.0
    pct_20 = (n_20 / total_20 * 100.0) if total_20 else 0.0
    change = exp.get("change") or short_name(exp)
    entry = f"""
### Run {exp['id']}: {exp['name']}
- **Single Change Tested:** {change}
- **50Q GPQA Diamond Score:** **`{n_correct}/{total_q} ({pct:.1f}%)`** (Standard 20Q: **`{n_20}/{total_20} ({pct_20:.1f}%)`**)
- **Generation Speed:** Avg **`{avg_speed:.2f} t/s`** | Peak **`{peak_speed:.2f} t/s`**
- **Detailed Report:** [`{report_name}`](../gpqa_reports/{report_name})
"""
    existing = OPTIMIZATION_LOG.read_text() if OPTIMIZATION_LOG.exists() else ""
    if entry.strip() in existing:
        print(f"Optimization log already contains this result for {exp['id']}.")
        return
    with OPTIMIZATION_LOG.open("a") as handle:
        handle.write(entry)
    print(f"Appended results to {OPTIMIZATION_LOG}")


def write_report(exp: dict, results: list[dict], questions: list[dict], command: str) -> Path:
    by_id = {question_id(row): row for row in results if question_id(row)}
    ordered = [by_id[item["id"]] for item in questions if item["id"] in by_id]
    first_ids = [item["id"] for item in questions[:20]]
    n_correct = sum(1 for row in ordered if row_correct(row))
    total_q = len(ordered)
    n_20 = sum(1 for qid in first_ids if qid in by_id and row_correct(by_id[qid]))
    total_20 = sum(1 for qid in first_ids if qid in by_id)
    speeds = [row_speed(row) for row in ordered if row_speed(row) > 0]
    avg_speed = sum(speeds) / len(speeds) if speeds else 0.0
    peak_speed = max(speeds) if speeds else 0.0
    score_pct = (n_correct / total_q * 100.0) if total_q else 0.0
    score_20_pct = (n_20 / total_20 * 100.0) if total_20 else 0.0

    lines = [
        f"# 50-Question GPQA Diamond Report: {exp['name']}",
        "",
        f"- **Experiment ID:** `{exp['id']}`",
        f"- **Model:** `{exp['model']}`",
        f"- **Command:** `{command}`",
        f"- **Total Score (50Q):** **{n_correct} / {total_q} ({score_pct:.1f}%)**",
        f"- **Standard 20Q Subset:** **{n_20} / {total_20} ({score_20_pct:.1f}%)**",
        f"- **Average Generation Speed:** **`{avg_speed:.2f} tokens/second`**",
        f"- **Peak Generation Speed:** **`{peak_speed:.2f} tokens/second`**",
        "- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)",
        "",
        "## Question-by-Question Breakdown",
        "",
        "| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |",
        "| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
    ]
    for index, row in enumerate(ordered, 1):
        gold = row.get("gold", row.get("expected", row.get("gold_choice")))
        pred = row.get("pred", row.get("predicted", row.get("pred_choice")))
        tokens = row.get("tokens", row.get("pred_n", ""))
        wall = row.get("wall_time", row.get("dt", 0.0)) or 0.0
        result = "CORRECT" if row_correct(row) else "WRONG"
        lines.append(
            f"| {index} | `{question_id(row)}` | {gold} | {pred} | {result} | {tokens} | {row_speed(row):.2f} | {float(wall):.2f} |"
        )
    lines.append("")
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORT_DIR / f"gpqa_{exp['id']}_50q_report.md"
    report_path.write_text("\n".join(lines))
    print(f"Wrote {report_path}")
    append_optimization_log(exp, report_path.name, n_correct, total_q, n_20, total_20, avg_speed, peak_speed)
    return report_path


def stop_process_group(proc: subprocess.Popen | None) -> None:
    if proc is None or proc.poll() is not None:
        return
    try:
        os.killpg(proc.pid, signal.SIGTERM)
        proc.wait(timeout=10)
    except Exception:
        try:
            os.killpg(proc.pid, signal.SIGKILL)
        except Exception:
            pass


def free_port(port: int) -> None:
    subprocess.run(
        ["fuser", "-k", f"{port}/tcp"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def run_experiment(exp: dict, port: int, dry_run: bool) -> int:
    argv = server_argv(exp, port)
    command = " ".join(shlex.quote(part) for part in argv)
    print(exp["name"])
    print(f"Command: {command}")
    checkpoint = checkpoint_path(exp)
    done = load_checkpoint(checkpoint)
    print(f"Checkpoint: {checkpoint} ({len(done)} questions on disk)")
    prepare_model(exp, dry_run)
    if dry_run:
        server = bin_dir() / "llama-server"
        if not server.exists():
            print(f"llama-server not found at {server}. Set IK_LLAMA_HOME.")
        return 0

    questions = json.loads(GPQA_FILE.read_text())
    completed = {question_id(row) for row in done if question_id(row)}
    pending = [item for item in questions if item["id"] not in completed]
    if not pending and len(completed) >= len(questions):
        print("Checkpoint already covers the question set. Rewriting the report.")
        write_report(exp, done, questions, command)
        return 0

    url_health = f"http://127.0.0.1:{port}/health"
    url_completion = f"http://127.0.0.1:{port}/completion"
    free_port(port)
    time.sleep(1)
    log_path = Path(f"/tmp/{exp['id']}_server.log")
    log_handle = log_path.open("w")
    proc = subprocess.Popen(
        argv,
        stdout=log_handle,
        stderr=subprocess.STDOUT,
        start_new_session=True,
    )
    try:
        print(f"Waiting for {url_health} (server log {log_path})")
        if not wait_for_server(url_health):
            print("Server did not become healthy. See the server log.")
            return 1
        for item in pending:
            gold = item.get("correct_letter") or item.get("gold")
            user_text = build_user_text(item, exp.get("prompt", "stored"))
            started = time.time()
            response = query_completion(url_completion, user_text)
            wall = time.time() - started
            if response is None:
                print(f"{item['id']}: no response after retries. Checkpoint kept; rerun to resume.")
                return 1
            content = response.get("content", "")
            non_think = re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL).strip()
            predicted = extract_answer_letter(non_think or content)
            timings = response.get("timings", {})
            predicted_n = int(timings.get("predicted_n", 0) or 0)
            predicted_ms = float(timings.get("predicted_ms", 0.0) or 0.0)
            if timings.get("predicted_per_second"):
                speed = float(timings["predicted_per_second"])
            elif predicted_ms > 0:
                speed = predicted_n / (predicted_ms / 1000.0)
            elif wall > 0:
                speed = predicted_n / wall
            else:
                speed = 0.0
            correct = predicted == gold
            done.append({
                "idx": len(done) + 1,
                "id": item["id"],
                "gold": gold,
                "pred": predicted,
                "correct": correct,
                "tokens": predicted_n,
                "speed_tps": speed,
                "wall_time": wall,
            })
            checkpoint.write_text(json.dumps(done, indent=2) + "\n")
            status = "CORRECT" if correct else "WRONG"
            print(
                f"[{len(done):02d}/{len(questions)}] {item['id']}: "
                f"gold {gold} pred {predicted} {status} | {speed:.2f} t/s | {predicted_n} tok | {wall:.1f}s"
            )
        write_report(exp, done, questions, command)
        return 0
    finally:
        stop_process_group(proc)
        log_handle.close()
        free_port(port)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a catalogued GPQA Diamond eval.")
    parser.add_argument("--exp", help="Experiment number or id, for example 47")
    parser.add_argument("--list", action="store_true", help="Print the experiment catalog")
    parser.add_argument("--dry-run", action="store_true", help="Print the command and prep step, then exit")
    parser.add_argument("--port", type=int, default=8087)
    args = parser.parse_args()
    catalog = load_catalog()
    if args.list or not args.exp:
        print_catalog(catalog)
        if not args.exp:
            return
    exp = find_experiment(catalog, args.exp)
    raise SystemExit(run_experiment(exp, args.port, args.dry_run))


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        try:
            sys.stdout.close()
        except Exception:
            pass
        raise SystemExit(0)
