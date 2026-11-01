#!/usr/bin/env python3
"""Stage 2 Expansion Runner: Protocol C-gpqa-v2 Certified Reasoning (16,384-Token Runway)

Evaluates:
  1. Exp 50 (Qwen 3.6 35B MoE, Repacked IQ4_XS/Q4_0, Native MTP, 16K runway, -c 32768)
     - Full 50-Question GPQA Diamond
     - --max-tokens 16384
  2. Exp 94 (Recursive Flint 40B MoE, ik_llama.cpp, -muge 1, Repacked Q4_0_R8, N-gram spec, -c 32768)
     - Full 50-Question GPQA Diamond
     - --max-tokens 16384
"""

import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "benchmarks"))

from gpqa_eval import run_eval

RUNS_DIR = ROOT / "logs" / "runs"
RUNS_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = RUNS_DIR / "gpqa_16k_execution.log"


def log(msg: str):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {msg}"
    print(formatted, flush=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(formatted + "\n")


def main():
    log("=================================================================")
    log("STARTING GPQA 16K EXPANSION: PROTOCOL C-gpqa-v2 (16,384-TOKEN RUNWAY)")
    log("=================================================================")

    # 1. QWEN 3.6 35B MOE (EXP 50)
    log(">>> LAUNCHING EXP 50: QWEN 3.6 35B (16,384-TOKEN RUNWAY, -c 32768)")
    t0_qwen = time.time()
    rc_qwen = run_eval(
        exp_key="50",
        port=8087,
        max_tokens=16384,
        endpoint="chat",
        force_new_run=False,
        run_suffix="_16k_runway"
    )
    t1_qwen = time.time()

    if rc_qwen != 0:
        log(f"FATAL: Exp 50 (Qwen 35B) 16K reasoning eval exited with return code {rc_qwen}.")
        sys.exit(rc_qwen)

    log(f"Exp 50 (Qwen 35B) 16K reasoning eval completed in {(t1_qwen - t0_qwen)/60:.1f} minutes.")
    time.sleep(5)

    # 2. RECURSIVE FLINT 40B MOE (EXP 94)
    log(">>> LAUNCHING EXP 94: FLINT 40B MOE (16,384-TOKEN RUNWAY, -c 32768)")
    t0_flint = time.time()
    rc_flint = run_eval(
        exp_key="94",
        port=8087,
        max_tokens=16384,
        endpoint="chat",
        force_new_run=False,
        run_suffix="_16k_runway"
    )
    t1_flint = time.time()

    if rc_flint != 0:
        log(f"FATAL: Exp 94 (Flint 40B) 16K reasoning eval exited with return code {rc_flint}.")
        sys.exit(rc_flint)

    log(f"Exp 94 (Flint 40B) 16K reasoning eval completed in {(t1_flint - t0_flint)/60:.1f} minutes.")

    log("=================================================================")
    log("GPQA 16K EXPANSION COMPLETED SUCCESSFULLY ACROSS BOTH MODELS")
    log("=================================================================")


if __name__ == "__main__":
    main()
