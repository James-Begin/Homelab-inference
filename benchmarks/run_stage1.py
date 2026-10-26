#!/usr/bin/env python3
"""
Stage 1 Execution Runner: Protocol A Throughput Benchmark & Smoke Verification
Orchestrates:
  1. Boot Qwen 35B (Exp 50 config) on dual-socket Broadwell with physical pinning
  2. Health check & verification
  3. Protocol A throughput benchmark (12 prompts x 5 reps, 512 tokens)
  4. Tear down Qwen server
  5. Boot Flint 40B (Exp 94 config) on dual-socket Broadwell with physical pinning
  6. Health check & verification
  7. Protocol A throughput benchmark (12 prompts x 5 reps, 512 tokens)
  8. Tear down Flint server
  9. Report verified results
"""

import json
import os
import shlex
import signal
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "benchmarks"))

from bench_throughput import run_throughput_benchmark

RUNS_DIR = ROOT / "logs" / "runs"
RUNS_DIR.mkdir(parents=True, exist_ok=True)
STAGE1_LOG = RUNS_DIR / "stage1_execution.log"


def log(msg: str):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {msg}"
    print(formatted, flush=True)
    with open(STAGE1_LOG, "a", encoding="utf-8") as f:
        f.write(formatted + "\n")


def free_port(port: int = 8087):
    try:
        out = subprocess.check_output(["lsof", "-ti", f":{port}"], text=True)
        for pid in out.strip().split():
            os.kill(int(pid), signal.SIGTERM)
        time.sleep(1)
    except Exception:
        pass


def wait_for_server(url: str, timeout: int = 150) -> bool:
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with urllib.request.urlopen(f"{url}/health", timeout=2) as resp:
                if resp.status == 200:
                    return True
        except Exception:
            pass
        time.sleep(2)
    return False


def stop_proc(proc: subprocess.Popen):
    try:
        os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
        proc.wait(timeout=8)
    except Exception:
        try:
            os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
        except Exception:
            pass


def main():
    log("=================================================================")
    log("STARTING STAGE 1: PROTOCOL A THROUGHPUT VERIFICATION")
    log("=================================================================")

    # -------------------------------------------------------------
    # 1. QWEN 3.6 35B MOE (EXP 50 CONFIGURATION)
    # -------------------------------------------------------------
    qwen_model = Path("/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf")
    server_bin = Path("/home/james/ik_llama.cpp/build/bin/llama-server")
    numactl = "numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27"
    
    qwen_flags = (
        "-c 8192 -t 28 -tb 28 -ctk q4_0 -ctv q4_0 --defer-experts "
        "--numa distribute -fa 1 -ser 2,0.5 -muge "
        "--override-kv qwen35moe.nextn_predict_layers=int:1 "
        "--spec-type mtp:n_max=1,p_min=0.0 --slot-prompt-similarity 0.0"
    )
    port = 8087
    server_url = f"http://127.0.0.1:{port}"

    free_port(port)
    qwen_cmd = f"{numactl} {server_bin} -m {qwen_model} --port {port} {qwen_flags}"
    log(f"Launching Qwen 35B server:\n  {qwen_cmd}")

    qwen_log_file = RUNS_DIR / "qwen_stage1_server.log"
    qwen_log_handle = open(qwen_log_file, "w", encoding="utf-8")

    qwen_proc = subprocess.Popen(
        shlex.split(qwen_cmd),
        stdout=qwen_log_handle,
        stderr=subprocess.STDOUT,
        start_new_session=True
    )

    try:
        log("Waiting for Qwen server health check...")
        if not wait_for_server(server_url, timeout=120):
            log("FATAL: Qwen server failed to become healthy. Check server log.")
            sys.exit(1)
        log("Qwen server is HEALTHY. Beginning Protocol A benchmark (60 requests)...")

        qwen_out = RUNS_DIR / "run_exp50_qwen_tput.json"
        res_qwen = run_throughput_benchmark(
            server_url=server_url,
            repetitions=5,
            n_predict=512,
            output_path=qwen_out
        )
        log(f"Qwen Benchmark complete. Token-weighted throughput: {res_qwen['summary']['token_weighted_tps']} t/s")
    finally:
        log("Stopping Qwen server...")
        stop_proc(qwen_proc)
        qwen_log_handle.close()
        free_port(port)

    time.sleep(3)

    # -------------------------------------------------------------
    # 2. RECURSIVE FLINT 40B MOE (EXP 94 CONFIGURATION)
    # -------------------------------------------------------------
    flint_model = Path("/home/james/ik_llama.cpp/build/models/RecursiveSI_flint-Q4_0_Repacked.gguf")
    flint_flags = (
        "-c 8192 -t 28 -tb 26 "
        "--spec-type ngram-mod:n_max=4,ngram_size_n=4,ngram_min_hits=4 "
        "--slot-save-path /tmp/slots/ -sps 0.50 -ctk q4_0 -ctv q4_0 --numa numactl -muge"
    )
    flint_cmd = f"{numactl} {server_bin} -m {flint_model} --port {port} {flint_flags}"
    log(f"Launching Flint 40B server:\n  {flint_cmd}")

    flint_log_file = RUNS_DIR / "flint_stage1_server.log"
    flint_log_handle = open(flint_log_file, "w", encoding="utf-8")

    flint_proc = subprocess.Popen(
        shlex.split(flint_cmd),
        stdout=flint_log_handle,
        stderr=subprocess.STDOUT,
        start_new_session=True
    )

    try:
        log("Waiting for Flint server health check...")
        if not wait_for_server(server_url, timeout=120):
            log("FATAL: Flint server failed to become healthy. Check server log.")
            sys.exit(1)
        log("Flint server is HEALTHY. Beginning Protocol A benchmark (60 requests)...")

        flint_out = RUNS_DIR / "run_exp94_flint_tput.json"
        res_flint = run_throughput_benchmark(
            server_url=server_url,
            repetitions=5,
            n_predict=512,
            output_path=flint_out
        )
        log(f"Flint Benchmark complete. Token-weighted throughput: {res_flint['summary']['token_weighted_tps']} t/s")
    finally:
        log("Stopping Flint server...")
        stop_proc(flint_proc)
        flint_log_handle.close()
        free_port(port)

    log("=================================================================")
    log("STAGE 1 COMPLETED SUCCESSFULLY")
    log(f"Qwen 35B Throughput:  {res_qwen['summary']['token_weighted_tps']} t/s (Median: {res_qwen['summary']['median_decode_tps']} t/s)")
    log(f"Flint 40B Throughput: {res_flint['summary']['token_weighted_tps']} t/s (Median: {res_flint['summary']['median_decode_tps']} t/s)")
    log("=================================================================")


if __name__ == "__main__":
    main()
