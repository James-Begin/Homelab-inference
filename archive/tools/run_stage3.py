#!/usr/bin/env python3
"""Stage 3 Execution Runner: Protocol C-code-v1 Coding Suite (EvalPlus HumanEval+ 164 Problems)

Orchestrates:
  1. Exp 50 (Qwen 3.6 35B MoE, Repacked IQ4_XS/Q4_0, Native MTP, 4K runway)
     - Full 164 HumanEval+ coding problems
     - pass@1 greedy evaluation
  2. Exp 94 (Recursive Flint 40B MoE, ik_llama.cpp, -muge 1, Repacked Q4_0_R8, N-gram spec)
     - Full 164 HumanEval+ coding problems
     - pass@1 greedy evaluation
  3. Comparative analysis: Pass rates (Base vs. Plus), solve speed, time-to-solution budget curves.
"""

import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "benchmarks"))

from code_eval import run_code_eval

RUNS_DIR = ROOT / "logs" / "runs"
RUNS_DIR.mkdir(parents=True, exist_ok=True)
STAGE3_LOG = RUNS_DIR / "stage3_execution.log"


def log(msg: str):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {msg}"
    print(formatted, flush=True)
    with open(STAGE3_LOG, "a", encoding="utf-8") as f:
        f.write(formatted + "\n")


def main():
    log("=================================================================")
    log("STARTING STAGE 3: PROTOCOL C-code-v1 CODING SUITE (HUMANEVAL+ 164)")
    log("=================================================================")

    # 1. QWEN 3.6 35B MOE (EXP 50)
    log(">>> LAUNCHING EXP 50: QWEN 3.6 35B CODING BENCHMARK (HUMANEVAL+ 16K RUNWAY)")
    t0_qwen = time.time()
    rc_qwen = run_code_eval(
        exp_key="50",
        port=8087,
        max_tokens=16384,
        force_new_run=False
    )
    t1_qwen = time.time()

    if rc_qwen != 0:
        log(f"FATAL: Exp 50 (Qwen 35B) coding eval exited with return code {rc_qwen}. Halting Stage 3.")
        sys.exit(rc_qwen)

    log(f"Exp 50 (Qwen 35B) coding eval completed successfully in {(t1_qwen - t0_qwen)/60:.1f} minutes.")
    time.sleep(5)

    # 2. RECURSIVE FLINT 40B MOE (EXP 94)
    log(">>> LAUNCHING EXP 94: FLINT 40B MOE CODING BENCHMARK (HUMANEVAL+ 16K RUNWAY)")
    t0_flint = time.time()
    rc_flint = run_code_eval(
        exp_key="94",
        port=8087,
        max_tokens=16384,
        force_new_run=False
    )
    t1_flint = time.time()

    if rc_flint != 0:
        log(f"FATAL: Exp 94 (Flint 40B) coding eval exited with return code {rc_flint}. Halting Stage 3.")
        sys.exit(rc_flint)

    log(f"Exp 94 (Flint 40B) coding eval completed successfully in {(t1_flint - t0_flint)/60:.1f} minutes.")

    log("=================================================================")
    log("STAGE 3 COMPLETED SUCCESSFULLY ACROSS BOTH MODELS")
    log("=================================================================")

    # Seamlessly chain to GPQA 16K Reasoning Expansion
    log(">>> AUTOMATICALLY CHAINING TO GPQA 16K REASONING EXPANSION...")
    time.sleep(5)
    gpqa_16k_script = ROOT / "benchmarks" / "run_gpqa_16k.py"
    res = subprocess.run([sys.executable, "-u", str(gpqa_16k_script)])
    if res.returncode != 0:
        log(f"FATAL: GPQA 16K reasoning run exited with return code {res.returncode}.")
        sys.exit(res.returncode)

    log("=================================================================")
    log("ALL 16K REASONING & CODING CAMPAIGNS COMPLETED SUCCESSFULLY")
    log("=================================================================")


if __name__ == "__main__":
    main()
