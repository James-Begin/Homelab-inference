#!/usr/bin/env python3
"""
Stage 2 Execution Runner: Protocol C-gpqa-v2 Certified Reasoning Rerun (8K Token Runway)
Orchestrates:
  1. Exp 50 (Qwen 3.6 35B MoE, Repacked IQ4_XS/Q4_0, Suffix + MTP spec)
     - Full 50-Question GPQA Diamond
     - --max-tokens 8192
  2. Exp 94 (Recursive Flint 40B MoE, ik_llama.cpp, -muge 1, Repacked Q4_0_R8, N-gram spec)
     - Full 50-Question GPQA Diamond
     - --max-tokens 8192
  3. Strict vs. Lenient regrading, manifest verification, and report generation
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
STAGE2_LOG = RUNS_DIR / "stage2_execution.log"


def log(msg: str):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {msg}"
    print(formatted, flush=True)
    with open(STAGE2_LOG, "a", encoding="utf-8") as f:
        f.write(formatted + "\n")


def main():
    log("=================================================================")
    log("STARTING STAGE 2: PROTOCOL C-gpqa-v2 CERTIFIED REASONING RUNS (8K RUNWAY)")
    log("=================================================================")

    # -------------------------------------------------------------
    # 1. QWEN 3.6 35B MOE (EXP 50)
    # -------------------------------------------------------------
    log(">>> LAUNCHING EXP 50: QWEN 3.6 35B (8,192-TOKEN RUNWAY)")
    t0_qwen = time.time()
    rc_qwen = run_eval(
        exp_key="50",
        port=8087,
        max_tokens=8192,
        endpoint="chat",
        force_new_run=False
    )
    t1_qwen = time.time()

    if rc_qwen != 0:
        log(f"FATAL: Exp 50 (Qwen 35B) exited with return code {rc_qwen}. Halting Stage 2.")
        sys.exit(rc_qwen)

    log(f"Exp 50 (Qwen 35B) completed successfully in {(t1_qwen - t0_qwen)/60:.1f} minutes.")
    time.sleep(5)

    # -------------------------------------------------------------
    # 2. RECURSIVE FLINT 40B MOE (EXP 94)
    # -------------------------------------------------------------
    log(">>> LAUNCHING EXP 94: FLINT 40B MOE ON ik_llama.cpp (8,192-TOKEN RUNWAY)")
    t0_flint = time.time()
    rc_flint = run_eval(
        exp_key="94",
        port=8087,
        max_tokens=8192,
        endpoint="chat",
        force_new_run=False
    )
    t1_flint = time.time()

    if rc_flint != 0:
        log(f"FATAL: Exp 94 (Flint 40B) exited with return code {rc_flint}. Halting Stage 2.")
        sys.exit(rc_flint)

    log(f"Exp 94 (Flint 40B) completed successfully in {(t1_flint - t0_flint)/60:.1f} minutes.")

    log("=================================================================")
    log("STAGE 2 COMPLETED SUCCESSFULLY ACROSS BOTH MODELS")
    log("=================================================================")


if __name__ == "__main__":
    main()
