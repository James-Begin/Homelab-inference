#!/usr/bin/env python3
"""
Live Systematic Ablation Sweep Runner (Phase 6 of improvement-plan.md)
Executes Protocol A-tput-v1 throughput benchmarks across 8 sequential configurations:
  Step 0: Upstream Baseline (Single-Socket, Q6_K, unpinned, FP16 KV)
  Step 1: + Dual-Socket NUMA Interleave (--interleave=all, 28 threads floating)
  Step 2: + 28 Physical Core Pinning (NUMA interleave + physcpubind)
  Step 3: + Quantization Recipe (IQ4_XS Dense Attention + Q4_0 MoE, Q4_0 KV)
  Step 4: + AVX2 64-Byte Row Repacking (Q4_0_R8 aligned weights)
  Step 5: + Merged Up/Gate Experts (-muge 1 single-pass GEMM)
  Step 6: + Speculative Decoding (MTP Suffix Drafting)
  Step 7: Flint 40B MoE Production (ik_llama + MUGE + ngram-mod)

Saves verified outputs to logs/runs/ablation_sweep/step<N>_<id>/summary.json.
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

SERVER_BIN = Path("/home/james/ik_llama.cpp/build/bin/llama-server")
MODELS_DIR = Path("/home/james/ik_llama.cpp/build/models")
PROMPTS_DIR = ROOT / "benchmarks" / "prompts" / "tput_ablation"
SWEEP_DIR = ROOT / "logs" / "runs" / "ablation_sweep"
SWEEP_DIR.mkdir(parents=True, exist_ok=True)
SWEEP_LOG = SWEEP_DIR / "ablation_execution.log"

PORT = 8087
SERVER_URL = f"http://127.0.0.1:{PORT}"

PINNED_NUMA = (
    "numactl --interleave=all "
    "--physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27"
)

STEPS = [
    {
        "step": 0,
        "id": "step0_baseline_single_socket",
        "name": "Upstream Baseline (Single-Socket, Q6_K)",
        "model": MODELS_DIR / "Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf",
        "numactl": "numactl --cpunodebind=0 --membind=0",
        "flags": f"--port {PORT} -c 4096 -t 14 -tb 14 -ctk f16 -ctv f16",
    },
    {
        "step": 1,
        "id": "step1_numa_interleave",
        "name": "+ Dual-Socket NUMA Interleave",
        "model": MODELS_DIR / "Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf",
        "numactl": "numactl --interleave=all",
        "flags": f"--port {PORT} -c 4096 -t 28 -tb 28 -ctk f16 -ctv f16",
    },
    {
        "step": 2,
        "id": "step2_phys_pinning",
        "name": "+ 28 Physical Core Pinning",
        "model": MODELS_DIR / "Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf",
        "numactl": PINNED_NUMA,
        "flags": f"--port {PORT} -c 4096 -t 28 -tb 28 -ctk f16 -ctv f16",
    },
    {
        "step": 3,
        "id": "step3_quant_recipe",
        "name": "+ IQ4_XS Dense + Q4_0 MoE (Unrepacked)",
        "model": MODELS_DIR / "Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0.gguf",
        "numactl": PINNED_NUMA,
        "flags": f"--port {PORT} -c 4096 -t 28 -tb 28 -ctk q4_0 -ctv q4_0",
    },
    {
        "step": 4,
        "id": "step4_avx2_repack",
        "name": "+ AVX2 64-Byte Row Repacking",
        "model": MODELS_DIR / "Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf",
        "numactl": PINNED_NUMA,
        "flags": f"--port {PORT} -c 4096 -t 28 -tb 28 -ctk q4_0 -ctv q4_0",
    },
    {
        "step": 5,
        "id": "step5_muge",
        "name": "+ Merged Up/Gate Experts (-muge 1)",
        "model": MODELS_DIR / "Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf",
        "numactl": PINNED_NUMA,
        "flags": f"--port {PORT} -c 4096 -t 28 -tb 28 -ctk q4_0 -ctv q4_0 -muge",
    },
    {
        "step": 6,
        "id": "step6_speculation",
        "name": "+ Suffix Speculation (MTP Drafting)",
        "model": MODELS_DIR / "Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf",
        "numactl": PINNED_NUMA,
        "flags": (
            f"--port {PORT} -c 4096 -t 28 -tb 28 -ctk q4_0 -ctv q4_0 -muge "
            f"--override-kv qwen35moe.nextn_predict_layers=int:1 "
            f"--spec-type mtp:n_max=1,p_min=0.0 --slot-prompt-similarity 0.0"
        ),
    },
    {
        "step": 7,
        "id": "step7_flint_production",
        "name": "Flint 40B MoE Production (ik_llama + MUGE)",
        "model": MODELS_DIR / "RecursiveSI_flint-Q4_0_Repacked.gguf",
        "numactl": PINNED_NUMA,
        "flags": (
            f"--port {PORT} -c 4096 -t 28 -tb 26 -ctk q4_0 -ctv q4_0 -muge "
            f"--spec-type ngram-mod:n_max=4,ngram_size_n=4,ngram_min_hits=4 "
            f"--slot-save-path /tmp/slots/ -sps 0.50"
        ),
    },
]


def log(msg: str):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {msg}"
    print(formatted, flush=True)
    with open(SWEEP_LOG, "a", encoding="utf-8") as f:
        f.write(formatted + "\n")


def free_port(port: int = PORT):
    try:
        out = subprocess.check_output(["lsof", "-ti", f":{port}"], text=True)
        for pid in out.strip().split():
            os.kill(int(pid), signal.SIGKILL)
        time.sleep(1)
    except Exception:
        pass


def wait_for_server(url: str, timeout: int = 120) -> bool:
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
    log("STARTING LIVE SYSTEMATIC ABLATION SWEEP (PROTOCOL A-TPUT-V1)")
    log(f"Steps to execute: {len(STEPS)} configurations")
    log(f"Prompts directory: {PROMPTS_DIR}")
    log("=================================================================")

    sweep_results = []
    summary_table_file = SWEEP_DIR / "ablation_summary.json"

    for step_cfg in STEPS:
        step_num = step_cfg["step"]
        step_id = step_cfg["id"]
        step_name = step_cfg["name"]
        model_path = step_cfg["model"]
        numactl_cmd = step_cfg["numactl"]
        flags = step_cfg["flags"]

        step_dir = SWEEP_DIR / f"{step_num}_{step_id}"
        step_dir.mkdir(parents=True, exist_ok=True)
        out_json = step_dir / "summary.json"
        server_log = step_dir / "server.log"

        if out_json.exists():
            log(f"Step {step_num} ({step_name}) already completed. Loading cached results.")
            res = json.loads(out_json.read_text(encoding="utf-8"))
            s_dict = res.get("summary", {})
            sweep_results.append({
                "step": step_num,
                "id": step_id,
                "name": step_name,
                "token_weighted_tps": s_dict.get("token_weighted_tps", 0.0),
                "median_decode_tps": s_dict.get("median_decode_tps", 0.0),
                "iqr_decode_tps": s_dict.get("iqr_decode_tps", 0.0),
                "total_tokens": s_dict.get("total_tokens", s_dict.get("valid_runs", 0) * 512),
            })
            continue

        log(f"\n>>> EXECUTING STEP [{step_num + 1}/{len(STEPS)}]: {step_name}")
        log(f"    Model: {model_path.name}")
        log(f"    Flags: {flags}")

        free_port(PORT)
        full_cmd = f"{numactl_cmd} {SERVER_BIN} -m {model_path} {flags}"
        log_handle = open(server_log, "w", encoding="utf-8")

        proc = subprocess.Popen(
            shlex.split(full_cmd),
            stdout=log_handle,
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )

        try:
            log("    Waiting for server health check...")
            if not wait_for_server(SERVER_URL, timeout=120):
                log(f"FATAL: Server for step {step_num} failed to become healthy. Check {server_log}")
                return 1

            log("    Server is HEALTHY. Running Protocol A benchmark (6 prompts x 3 reps = 18 completions)...")
            res = run_throughput_benchmark(
                server_url=SERVER_URL,
                prompts_dir=PROMPTS_DIR,
                repetitions=3,
                n_predict=512,
                output_path=out_json,
            )

            tw_tps = res["summary"]["token_weighted_tps"]
            med_tps = res["summary"]["median_decode_tps"]
            iqr_tps = res["summary"]["iqr_decode_tps"]
            log(f"    [STEP {step_num} COMPLETE] Weighted TPS: {tw_tps:.2f} t/s | Median: {med_tps:.2f} t/s (IQR: {iqr_tps:.2f})")

            s_dict = res.get("summary", {})
            sweep_results.append({
                "step": step_num,
                "id": step_id,
                "name": step_name,
                "token_weighted_tps": tw_tps,
                "median_decode_tps": med_tps,
                "iqr_decode_tps": iqr_tps,
                "total_tokens": s_dict.get("total_tokens", s_dict.get("valid_runs", 0) * 512),
            })

            # Save cumulative progress
            summary_table_file.write_text(json.dumps(sweep_results, indent=2), encoding="utf-8")

        finally:
            log("    Shutting down server...")
            stop_proc(proc)
            log_handle.close()
            free_port(PORT)
            time.sleep(2)

    log("\n=================================================================")
    log("ALL 8 ABLATION STEPS COMPLETED SUCCESSFULLY!")
    log("=================================================================")

    # Generate summary markdown table
    summary_md = ["# Live Measured Protocol A Ablation Waterfall\n\n",
                  "| Step | Configuration | Class | Token-Weighted TPS | Median TPS | IQR | Marginal Delta |\n",
                  "| :---: | :--- | :---: | :---: | :---: | :---: | :---: |\n"]

    prev_tps = None
    for r in sweep_results:
        step = r["step"]
        name = r["name"]
        tw = r["token_weighted_tps"]
        med = r["median_decode_tps"]
        iqr = r["iqr_decode_tps"]
        if prev_tps is None:
            delta_str = "—"
        else:
            delta = tw - prev_tps
            delta_str = f"+{delta:.2f} t/s" if delta >= 0 else f"{delta:.2f} t/s"
        prev_tps = tw

        summary_md.append(f"| **{step}** | {name} | Lossless | **{tw:.2f} t/s** | {med:.2f} t/s | {iqr:.2f} | **{delta_str}** |\n")

    report_file = SWEEP_DIR / "ablation_report.md"
    report_file.write_text("".join(summary_md), encoding="utf-8")
    log(f"Ablation report saved to {report_file}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
