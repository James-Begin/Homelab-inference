#!/usr/bin/env python3
"""
Protocol A: Controlled Throughput Benchmark (A-tput-v1)
Implements Phase 3 (Protocol A) of improvement-plan.md.
Measures decode, prefill, TTFT, and speculation metrics on fixed-length outputs.
"""

import argparse
import json
import os
from pathlib import Path
import random
import re
import statistics
import subprocess
import sys
import time
import urllib.request
from typing import Any, Dict, List, Optional


def load_prompts(prompts_dir: Path) -> Dict[str, Dict[str, str]]:
    """Loads standardized prompts grouped by workload class."""
    classes = {"code_edit": {}, "code_gen": {}, "prose": {}}
    for pfile in sorted(prompts_dir.glob("*.txt")):
        name = pfile.stem
        text = pfile.read_text(encoding="utf-8").strip()
        if name.startswith("code_edit"):
            classes["code_edit"][name] = text
        elif name.startswith("code_gen"):
            classes["code_gen"][name] = text
        elif name.startswith("prose"):
            classes["prose"][name] = text
    return classes


def check_degenerate_output(content: str) -> bool:
    """Detects repetitive loops or degenerate punctuation outputs."""
    if not content or len(content) < 50:
        return False
    # Check 8-gram repetition
    words = content.split()
    if len(words) >= 16:
        grams = {}
        for i in range(len(words) - 7):
            g = " ".join(words[i:i+8])
            grams[g] = grams.get(g, 0) + 1
            if grams[g] > 15:
                return True
    # Check punctuation ratio
    punct_count = sum(1 for c in content if c in ".,!?;:-_")
    if len(content) > 200 and (punct_count / len(content)) > 0.45:
        return True
    return False


def query_server(
    url: str,
    prompt: str,
    n_predict: int = 512,
    temperature: float = 0.0,
    ignore_eos: bool = True
) -> Optional[Dict[str, Any]]:
    """Sends a completion request to the server and captures timing statistics."""
    payload = {
        "prompt": f"<|user|>\n{prompt}\n<|assistant|>\n",
        "n_predict": n_predict,
        "temperature": temperature,
        "ignore_eos": ignore_eos,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{url}/completion",
        data=data,
        headers={"Content-Type": "application/json"}
    )
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            t1 = time.time()
            res = json.loads(resp.read().decode("utf-8"))
            res["client_wall_sec"] = t1 - t0
            return res
    except Exception as e:
        print(f"Request error: {e}", file=sys.stderr)
        return None


def run_throughput_benchmark(
    server_url: str = "http://127.0.0.1:8087",
    prompts_dir: Optional[Path] = None,
    repetitions: int = 5,
    n_predict: int = 512,
    output_path: Optional[Path] = None,
) -> Dict[str, Any]:
    if prompts_dir is None:
        prompts_dir = Path(__file__).resolve().parent / "prompts" / "tput"

    prompts_by_class = load_prompts(prompts_dir)
    all_prompts = []
    for cls_name, pdict in prompts_by_class.items():
        for pname, ptext in pdict.items():
            all_prompts.append((cls_name, pname, ptext))

    print(f"Loaded {len(all_prompts)} prompts across {len(prompts_by_class)} workload classes.")
    print(f"Running {repetitions} repetitions per prompt with n_predict={n_predict} (Protocol A-tput-v1)...")

    # Warm-up request (discarded)
    print("Performing initial warm-up request...")
    query_server(server_url, "Warm-up query: Write 16 tokens.", n_predict=16)

    measurements = []
    task_queue = []
    for rep in range(repetitions):
        for cls_name, pname, ptext in all_prompts:
            task_queue.append((rep, cls_name, pname, ptext))

    random.shuffle(task_queue)

    for idx, (rep, cls_name, pname, ptext) in enumerate(task_queue):
        res = query_server(server_url, ptext, n_predict=n_predict, ignore_eos=True)
        if res is None:
            continue

        timings = res.get("timings", {})
        content = res.get("content", "")
        predicted_n = timings.get("predicted_n", n_predict)
        predicted_ms = timings.get("predicted_ms", 0.0)
        prompt_n = timings.get("prompt_n", 0)
        prompt_ms = timings.get("prompt_ms", 0.0)

        decode_tps = (predicted_n / (predicted_ms / 1000.0)) if predicted_ms > 0 else 0.0
        prefill_tps = (prompt_n / (prompt_ms / 1000.0)) if prompt_ms > 0 else 0.0

        is_degenerate = check_degenerate_output(content)

        entry = {
            "repetition": rep,
            "workload_class": cls_name,
            "prompt_name": pname,
            "predicted_tokens": predicted_n,
            "decode_ms": predicted_ms,
            "decode_tps": decode_tps,
            "prompt_tokens": prompt_n,
            "prefill_ms": prompt_ms,
            "prefill_tps": prefill_tps,
            "is_degenerate": is_degenerate,
            "wall_sec": res.get("client_wall_sec", 0.0)
        }
        measurements.append(entry)
        deg_flag = " [DEGENERATE]" if is_degenerate else ""
        print(f"[{idx+1}/{len(task_queue)}] Rep {rep+1} | {cls_name:<12} | {pname:<15} | Decode: {decode_tps:5.2f} t/s | Prefill: {prefill_tps:6.2f} t/s{deg_flag}")

    # Compute Statistics
    valid_decode = [m["decode_tps"] for m in measurements if not m["is_degenerate"] and m["decode_tps"] > 0]
    total_tokens = sum(m["predicted_tokens"] for m in measurements if not m["is_degenerate"])
    total_time_sec = sum(m["decode_ms"] / 1000.0 for m in measurements if not m["is_degenerate"])
    token_weighted_tps = (total_tokens / total_time_sec) if total_time_sec > 0 else 0.0

    stats = {
        "protocol": "A-tput-v1",
        "total_runs": len(measurements),
        "valid_runs": len(valid_decode),
        "median_decode_tps": statistics.median(valid_decode) if valid_decode else 0.0,
        "token_weighted_tps": round(token_weighted_tps, 2),
        "iqr_decode_tps": round(statistics.quantiles(valid_decode, n=4)[2] - statistics.quantiles(valid_decode, n=4)[0], 2) if len(valid_decode) >= 4 else 0.0,
        "per_class": {}
    }

    for c in ["code_edit", "code_gen", "prose"]:
        c_speeds = [m["decode_tps"] for m in measurements if m["workload_class"] == c and not m["is_degenerate"]]
        if c_speeds:
            stats["per_class"][c] = {
                "median_decode_tps": round(statistics.median(c_speeds), 2),
                "mean_decode_tps": round(statistics.mean(c_speeds), 2)
            }

    summary_out = {
        "summary": stats,
        "measurements": measurements
    }

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(summary_out, f, indent=2)
        print(f"\nSaved throughput benchmark results to {output_path}")

    print("\n=======================================================")
    print("PROTOCOL A THROUGHPUT RESULTS:")
    print(f"Token-Weighted Throughput: {stats['token_weighted_tps']} t/s")
    print(f"Median Decode: {stats['median_decode_tps']:.2f} t/s (IQR: {stats['iqr_decode_tps']:.2f} t/s)")
    for c, cstats in stats["per_class"].items():
        print(f" - {c:<12}: Median {cstats['median_decode_tps']:.2f} t/s")
    print("=======================================================")

    return summary_out


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, default="http://127.0.0.1:8087")
    parser.add_argument("--reps", type=int, default=5)
    parser.add_argument("--n-predict", type=int, default=512)
    parser.add_argument("--out", type=str, default="summary.json")
    args = parser.parse_args()

    run_throughput_benchmark(
        server_url=args.url,
        repetitions=args.reps,
        n_predict=args.n_predict,
        output_path=Path(args.out)
    )
