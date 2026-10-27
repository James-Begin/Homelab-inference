#!/usr/bin/env python3
"""
Targeted 16K Token Runway Probe on Recursive Flint 40B MoE.
Tests 5 candidate 'near-miss' questions that hit the 8,192-token ceiling in Exp 94
to empirically determine if expanding the runway to 16,384 tokens unlocks correct answers.
"""

import json
import os
import signal
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "benchmarks"))

from grading import grade_response, RowStatus

OUTPUT_DIR = ROOT / "logs" / "runs" / "probe_16k_flint"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
ROWS_FILE = OUTPUT_DIR / "rows.jsonl"
SUMMARY_FILE = OUTPUT_DIR / "summary.json"
REPORT_FILE = OUTPUT_DIR / "report.md"
SERVER_LOG = OUTPUT_DIR / "server.log"

TARGET_IDS = ["gpqa_42", "gpqa_128", "gpqa_160", "gpqa_10", "gpqa_144"]
GPQA_FILE = ROOT / "logs" / "raw_checkpoints" / "gpqa_subset_50.json"


def free_port(port: int = 8087):
    try:
        out = subprocess.check_output(["lsof", "-t", f"-i:{port}"], text=True)
        for pid in out.strip().split():
            os.kill(int(pid), signal.SIGKILL)
        time.sleep(1)
    except Exception:
        pass


def build_user_text(item: dict) -> str:
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


def wait_for_server(url: str, timeout: int = 180) -> bool:
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


def query_chat_completion(url: str, user_text: str, max_tokens: int = 16384) -> dict:
    payload = {
        "messages": [
            {
                "role": "system",
                "content": "You are an expert scientific researcher. Reason step by step, then conclude with Final answer: X."
            },
            {"role": "user", "content": user_text}
        ],
        "max_tokens": max_tokens,
        "temperature": 0.0,
        "top_p": 1.0,
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
            # 16K generation at 12-17 t/s takes up to ~1400s (~23 min). Allow 3600s timeout.
            with urllib.request.urlopen(req, timeout=3600) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                choice = res.get("choices", [{}])[0]
                msg = choice.get("message", {})
                usage = res.get("usage", {})
                timings = res.get("timings", {})
                return {
                    "content": msg.get("content", ""),
                    "finish_reason": choice.get("finish_reason", "unknown"),
                    "tokens_predicted": usage.get("completion_tokens", 0),
                    "tokens_evaluated": usage.get("prompt_tokens", 0),
                    "timings": timings
                }
        except Exception as exc:
            print(f"Query attempt {attempt + 1}/3 failed: {exc}", flush=True)
            time.sleep(3)
    return None


def main():
    print("=================================================================", flush=True)
    print("STARTING TARGETED 16K RUNWAY PROBE (FLINT 40B MOE)", flush=True)
    print(f"Testing {len(TARGET_IDS)} candidate questions with max_tokens=16384, -c 24576", flush=True)
    print("=================================================================", flush=True)

    all_questions = json.loads(GPQA_FILE.read_text())
    targets = [q for q in all_questions if q["id"] in TARGET_IDS]
    # Sort in specified candidate order
    targets.sort(key=lambda q: TARGET_IDS.index(q["id"]))

    free_port(8087)

    server_cmd = [
        "numactl", "--interleave=all",
        "--physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27",
        "/home/james/ik_llama.cpp/build/bin/llama-server",
        "-m", "/home/james/ik_llama.cpp/build/models/RecursiveSI_flint-Q4_0_Repacked.gguf",
        "--port", "8087",
        "-c", "24576",
        "-t", "28",
        "-tb", "26",
        "--spec-type", "ngram-mod:n_max=4,ngram_size_n=4,ngram_min_hits=4",
        "--slot-save-path", "/tmp/slots/",
        "-sps", "0.50",
        "-ctk", "q4_0",
        "-ctv", "q4_0",
        "--numa", "numactl",
        "-muge"
    ]

    log_file = open(SERVER_LOG, "w", encoding="utf-8")
    proc = subprocess.Popen(server_cmd, stdout=log_file, stderr=subprocess.STDOUT, start_new_session=True)

    try:
        print("Launching llama-server (-c 24576, -muge)...", flush=True)
        if not wait_for_server("http://127.0.0.1:8087/health", timeout=180):
            print("FATAL: Server failed to become healthy. Check server.log", flush=True)
            return 1
        print("Server is healthy. Beginning 16K evaluations...\n", flush=True)

        results = []
        # Clear or resume rows
        completed_ids = set()
        if ROWS_FILE.exists():
            for line in ROWS_FILE.read_text().splitlines():
                if line.strip():
                    r = json.loads(line)
                    results.append(r)
                    completed_ids.add(r["id"])

        for idx, item in enumerate(targets):
            qid = item["id"]
            if qid in completed_ids:
                print(f"Skipping already completed question {qid}", flush=True)
                continue

            gold = item.get("correct_letter") or item.get("gold")
            user_text = build_user_text(item)
            print(f">>> Evaluating [{idx + 1}/{len(targets)}] ID: {qid} (Gold: {gold}) with 16K runway...", flush=True)

            t0 = time.time()
            res = query_chat_completion("http://127.0.0.1:8087", user_text, max_tokens=16384)
            wall_sec = time.time() - t0

            if res is None:
                print(f"ERROR: Failed to query {qid}. Halting probe.", flush=True)
                return 1

            content = res.get("content", "")
            finish_reason = res.get("finish_reason", "unknown")
            tokens_pred = res.get("tokens_predicted", 0)

            # Grade strictly
            is_length_truncated = (finish_reason == "length")
            status, strict_ans, lenient_ans = grade_response(
                content=content,
                gold=gold,
                finish_reason=finish_reason,
                max_tokens_hit=is_length_truncated
            )

            is_strict_correct = (status == RowStatus.CORRECT)
            speed_tps = (tokens_pred / wall_sec) if wall_sec > 0 else 0.0

            row_data = {
                "idx": idx + 1,
                "id": qid,
                "gold": gold,
                "pred": strict_ans,
                "lenient_pred": lenient_ans,
                "regraded_strict_correct": is_strict_correct,
                "status": status.value,
                "tokens": tokens_pred,
                "speed_tps": round(speed_tps, 2),
                "wall_time": round(wall_sec, 2),
                "finish_reason": finish_reason,
                "content": content
            }

            with open(ROWS_FILE, "a", encoding="utf-8") as rf:
                rf.write(json.dumps(row_data) + "\n")

            results.append(row_data)

            exceeded_8k = (tokens_pred > 8192)
            status_str = "CORRECT" if is_strict_correct else f"WRONG (pred={strict_ans})"
            print(f"    Result: {status_str} | Tokens: {tokens_pred} (Exceeded 8K: {exceeded_8k}) | {speed_tps:.2f} t/s | {wall_sec:.1f}s\n", flush=True)

        # Build summary and report
        strict_corr = sum(1 for r in results if r["regraded_strict_correct"])
        over_8k_count = sum(1 for r in results if r["tokens"] > 8192)
        over_8k_corr = sum(1 for r in results if r["tokens"] > 8192 and r["regraded_strict_correct"])

        summary = {
            "total_probed": len(results),
            "max_tokens_ceiling": 16384,
            "strict_score": f"{strict_corr}/{len(results)}",
            "strict_pct": round(strict_corr / len(results) * 100.0, 1),
            "questions_exceeding_8k": over_8k_count,
            "rescued_by_16k_runway": over_8k_corr,
        }
        with open(SUMMARY_FILE, "w", encoding="utf-8") as sf:
            json.dump(summary, sf, indent=2)

        # Build report
        report_lines = [
            "# Targeted 16K Runway Probe Report: Recursive Flint 40B MoE",
            f"- **Target Questions:** {len(results)} candidate questions that timed out at the 8K ceiling in Exp 94",
            f"- **Token Runway Ceiling:** 16,384 tokens (`-c 24576`)",
            f"- **Strict Score Achieved:** **{strict_corr}/{len(results)}** ({summary['strict_pct']}%)",
            f"- **Questions Exceeding 8,192 Tokens:** {over_8k_count}/{len(results)}",
            f"- **Correct Answers Enabled by >8K Runway:** **{over_8k_corr} questions**",
            "",
            "## Question-by-Question Results",
            "| ID | Gold | Pred (16K) | Strict Status | Tokens Used | Wall Time | Exceeded 8K? | Rescued? |",
            "| :--- | :---: | :---: | :--- | :---: | :---: | :---: | :---: |"
        ]
        for r in results:
            exceeded = "Yes" if r["tokens"] > 8192 else "No"
            rescued = "RESCUED" if (r["tokens"] > 8192 and r["regraded_strict_correct"]) else ("Solved <8K" if r["regraded_strict_correct"] else "Failed")
            report_lines.append(f"| `{r['id']}` | {r['gold']} | {r['pred'] or '-'} | `{r['status']}` | {r['tokens']} | {r['wall_time']}s | {exceeded} | **{rescued}** |")

        report_lines.append("")
        with open(REPORT_FILE, "w", encoding="utf-8") as rf:
            rf.write("\n".join(report_lines) + "\n")

        print("=================================================================", flush=True)
        print(f"PROBE COMPLETE: {strict_corr}/{len(results)} strict correct | Rescued by >8K Runway: {over_8k_corr}", flush=True)
        print("=================================================================", flush=True)

    finally:
        print("Shutting down llama-server...", flush=True)
        try:
            os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
            proc.wait(timeout=10)
        except Exception:
            try:
                proc.kill()
            except Exception:
                pass
        free_port(8087)
        log_file.close()


if __name__ == "__main__":
    main()
