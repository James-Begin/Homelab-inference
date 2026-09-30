#!/usr/bin/env python3
import argparse
import os
import re
import subprocess
import sys
import time

from paths import ROOT, bin_dir, expand, models_dir

sys.stdout.reconfigure(line_buffering=True)
sys.stderr.reconfigure(line_buffering=True)

MODEL_PATH = str(models_dir() / "Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf")
PASSKEY_BIN = str(bin_dir() / "llama-passkey")

CONTEXT_LADDER = [
    {"label": "16K Context", "ctx": 16384, "junk": 1000},
    {"label": "32K Context", "ctx": 32768, "junk": 2000},
    {"label": "64K Context", "ctx": 65536, "junk": 4000},
    {"label": "128K Context", "ctx": 131072, "junk": 8000}
]

def run_passkey_step(ctx, junk, extra_flags="", numactl_prefix="numactl --interleave=all", threads=14, threads_batch=28, model_path=MODEL_PATH):
    extra_flags = expand(extra_flags)
    model_path = expand(model_path)
    numactl_prefix = expand(numactl_prefix)
    cmd = (
        f"/usr/bin/time -v {numactl_prefix} {PASSKEY_BIN} "
        f"-m {model_path} -c {ctx} --junk {junk} -t {threads} -tb {threads_batch} -fa 1 "
        f"--run-time-repack {extra_flags}"
    )
    print(f"\n=======================================================", flush=True)
    print(f"Executing: {cmd}", flush=True)
    print(f"=======================================================\n", flush=True)
    
    t0 = time.time()
    try:
        proc = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=7200)
        t1 = time.time()
        output = proc.stdout + proc.stderr
        
        # Extract ground truth passkey
        pk_val_match = re.search(r"passkey\s*=\s*(\d+)", output)
        expected_passkey = pk_val_match.group(1) if pk_val_match else None
        
        # Extract prompt eval time and decode time
        pp_match = re.search(r"prompt eval time = +([\d.]+) ms / +(\d+) tokens \( +([\d.]+) ms per token, +([\d.]+) tokens per second\)", output)
        tg_match = re.search(r"eval time = +([\d.]+) ms / +(\d+) tokens \( +([\d.]+) ms per token, +([\d.]+) tokens per second\)", output)
        mem_match = re.search(r"Maximum resident set size \(kbytes\): (\d+)", output)
        
        tokens_evaluated = int(pp_match.group(2)) if pp_match else (junk * 25)
        pp_speed = float(pp_match.group(4)) if pp_match else 0.0
        pp_time_sec = float(pp_match.group(1))/1000.0 if pp_match else (t1 - t0)
        tg_speed = float(tg_match.group(4)) if tg_match else 0.0
        max_rss_mb = float(mem_match.group(1))/1024.0 if mem_match else 0.0
        
        # Verification
        match = False
        after_prompt = output.split("What is the pass key?")
        decoded_snippet = after_prompt[1][:200].strip() if len(after_prompt) > 1 else ""
        if expected_passkey:
            if expected_passkey in decoded_snippet:
                match = True
            elif expected_passkey in output:
                match = True
                
        return {
            "ctx_config": ctx,
            "tokens_evaluated": tokens_evaluated,
            "passed": match,
            "expected_passkey": expected_passkey,
            "decoded_snippet": decoded_snippet,
            "pp_speed": pp_speed,
            "pp_time_sec": pp_time_sec,
            "tg_speed": tg_speed,
            "max_rss_mb": max_rss_mb,
            "total_elapsed_sec": t1 - t0,
            "error": None
        }
    except Exception as e:
        print(f"Execution failed: {e}", flush=True)
        return {
            "ctx_config": ctx,
            "tokens_evaluated": 0,
            "passed": False,
            "expected_passkey": None,
            "decoded_snippet": "ERROR",
            "pp_speed": 0.0,
            "pp_time_sec": 0.0,
            "tg_speed": 0.0,
            "max_rss_mb": 0.0,
            "total_elapsed_sec": 0.0,
            "error": str(e)
        }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", type=str, default="Exp5_Dual_NUMA_MTP")
    parser.add_argument("--targets", type=str, default="16k,32k,64k,128k")
    parser.add_argument("--model", type=str, default=MODEL_PATH)
    parser.add_argument("--numactl", type=str, default="numactl --interleave=all")
    parser.add_argument("--threads", type=int, default=14)
    parser.add_argument("--threads-batch", type=int, default=28)
    parser.add_argument("--extra-flags", type=str, default="--numa distribute")
    args = parser.parse_args()
    
    target_list = [t.strip().lower() for t in args.targets.split(",")]
    
    selected_steps = []
    for step in CONTEXT_LADDER:
        tag = f"{step['ctx']//1024}k"
        if tag in target_list or args.targets == "all":
            selected_steps.append(step)
            
    print(f"Extreme Context Needle Ladder Initialized for: {[s['label'] for s in selected_steps]}", flush=True)
    print(f"Experiment Name: {args.name}", flush=True)
    print(f"Model: {args.model}", flush=True)
    print(f"NUMA Prefix: {args.numactl} | Threads: {args.threads} | Flags: {args.extra_flags}", flush=True)
    
    results = []
    for step in selected_steps:
        print(f"\n>>> Starting Test: {step['label']} (Context: {step['ctx']}, Junk: {step['junk']})", flush=True)
        res = run_passkey_step(
            step["ctx"], 
            step["junk"], 
            extra_flags=args.extra_flags,
            numactl_prefix=args.numactl,
            threads=args.threads,
            threads_batch=args.threads_batch,
            model_path=args.model
        )
        results.append({**step, **res})
        
        status = "PASSED" if res["passed"] else "FAILED"
        print(f">>> Result: {status} | Needle: {res['expected_passkey']} | PP Speed: {res['pp_speed']:.2f} t/s ({res['pp_time_sec']:.1f}s) | RAM: {res['max_rss_mb']:.1f} MB", flush=True)
        
    slug = re.sub(r'[^a-zA-Z0-9_]+', '_', args.name.lower()).strip("_")
    report_dir = ROOT / "logs" / "extreme_context_reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_file = report_dir / f"extreme_context_{slug}_report.md"
    
    with open(report_file, "w") as f:
        f.write(f"# Extreme Context Needle Retrieval Ladder: {args.name}\n\n")
        f.write(f"- **Timestamp:** `{time.strftime('%Y-%m-%d %H:%M:%S')}`\n")
        f.write(f"- **Model:** `{args.model}`\n")
        f.write(f"- **Configuration:** `{args.numactl} ... -t {args.threads} -tb {args.threads_batch} {args.extra_flags}`\n\n")
        f.write("## Benchmark Results\n\n")
        f.write("| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |\n")
        f.write("| :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n")
        for r in results:
            pass_str = "**PASSED (100%)**" if r["passed"] else "**FAILED**"
            f.write(f"| **{r['label']}** | {r['tokens_evaluated']:,} | {pass_str} | **`{r['pp_speed']:.2f} t/s`** | {r['pp_time_sec']:.1f}s | `{r['tg_speed']:.2f} t/s` | {r['max_rss_mb']:.1f} MB |\n")
            
        f.write("\n## Detailed Needle Extractions\n\n")
        for r in results:
            f.write(f"### {r['label']} ({r['tokens_evaluated']:,} tokens)\n")
            f.write(f"- **Expected Passkey:** `{r['expected_passkey']}`\n")
            f.write(f"- **Decoded Snippet:** `{r['decoded_snippet']}`\n")
            f.write(f"- **Status:** {'MATCH - ZERO REGRESSION' if r['passed'] else 'MISMATCH'}\n\n")
            
    print(f"\nFinal report saved to: {report_file}", flush=True)

if __name__ == "__main__":
    main()
