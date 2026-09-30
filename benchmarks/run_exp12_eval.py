#!/usr/bin/env python3
import json
import os
import re
import subprocess
import sys
import time
import urllib.request

sys.stdout.reconfigure(line_buffering=True)
sys.stderr.reconfigure(line_buffering=True)

MODEL_PATH = "/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf"
SERVER_BIN = "/home/james/ik_llama.cpp/build/bin/llama-server"
GPQA_FILE = "/home/james/.gemini/antigravity-cli/brain/816c1d65-6e4b-4024-8ad0-2ebd54f80461/scratch/gpqa_subset_50.json"
PORT = 8085
URL_HEALTH = f"http://127.0.0.1:{PORT}/health"
URL_COMPLETION = f"http://127.0.0.1:{PORT}/completion"
SERVER_LOG = "/tmp/exp12_server.log"
OPTIMIZATION_LOG = "/home/james/.gemini/antigravity-cli/brain/816c1d65-6e4b-4024-8ad0-2ebd54f80461/optimization_log_50tps.md"

EXP = {
    "id": "exp12_precision_spec",
    "name": "Exp 12: Dual NUMA + MegaKernel + Precision Chained Speculation (ngram_min_hits=2 + MTP)",
    "numactl": "numactl --interleave=all",
    "server_flags": "--port {port} -c 8192 -t 14 -tb 28 -ctk q8_0 -ctv q8_0 --defer-experts --run-time-repack --numa distribute -fa 1 --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type ngram-map-k:n_max=16,ngram_min_hits=2,ngram_size_n=8 --spec-type mtp:n_max=1,p_min=0.0"
}

def wait_for_server(timeout=180):
    start = time.time()
    while time.time() - start < timeout:
        try:
            with urllib.request.urlopen(URL_HEALTH, timeout=2) as resp:
                if resp.status == 200:
                    return True
        except Exception:
            pass
        time.sleep(1)
    return False

def query_completion(prompt_text, max_tokens=1536):
    payload = {
        "prompt": f"<|im_start|>system\nYou are an expert scientific researcher. Always provide your final answer choice first.<|im_end|>\n<|im_start|>user\n{prompt_text}<|im_end|>\n<|im_start|>assistant\n",
        "n_predict": max_tokens,
        "temperature": 0.0,
        "top_p": 1.0,
        "stop": ["<|im_end|>"]
    }
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        URL_COMPLETION,
        data=data,
        headers={'Content-Type': 'application/json'}
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except Exception as e:
        print(f"Query error: {e}", flush=True)
        return None

def extract_answer_letter(completion_text):
    m = re.search(r"(?:answer is|answer|choice|option)[:\*\s]*\s*(?:\(?([A-D])\)?)", completion_text, re.IGNORECASE)
    if m:
        return m.group(1).upper()
    m = re.search(r"\b([A-D])\b", completion_text)
    if m:
        return m.group(1).upper()
    return None

def run_experiment(exp):
    exp_id = exp["id"]
    exp_name = exp["name"]
    print(f"\n=======================================================", flush=True)
    print(f"STARTING: {exp_name}", flush=True)
    print(f"=======================================================\n", flush=True)

    with open(GPQA_FILE, "r") as f:
        questions = json.load(f)

    # 1. Start Server
    server_flags = exp["server_flags"].format(port=PORT)
    full_cmd = f"{exp['numactl']} {SERVER_BIN} -m {MODEL_PATH} {server_flags}"
    print(f"Launching Server: {full_cmd}", flush=True)

    with open(SERVER_LOG, "w") as log_file:
        proc = subprocess.Popen(full_cmd, shell=True, stdout=log_file, stderr=subprocess.STDOUT)

    try:
        print("Waiting for server health check...", flush=True)
        if not wait_for_server():
            print("ERROR: Server failed to start within timeout!", flush=True)
            return None

        CHECKPOINT_FILE = "/home/james/.gemini/antigravity-cli/brain/816c1d65-6e4b-4024-8ad0-2ebd54f80461/scratch/exp12_checkpoint.json"
        results = []
        completed_ids = set()
        if os.path.exists(CHECKPOINT_FILE):
            try:
                with open(CHECKPOINT_FILE, "r") as f:
                    results = json.load(f)
                completed_ids = {r["id"] for r in results}
                print(f"Loaded {len(results)} previously completed questions from checkpoint! Resuming...", flush=True)
            except Exception as e:
                print(f"Warning: could not load checkpoint: {e}", flush=True)

        for i, item in enumerate(questions, 1):
            qid = item["id"]
            if qid in completed_ids:
                continue

            correct_letter = item["correct_letter"]
            
            prompt = (
                f"{item['question']}\n\n"
                f"Options:\n"
                f"A) {item['options']['A']}\n"
                f"B) {item['options']['B']}\n"
                f"C) {item['options']['C']}\n"
                f"D) {item['options']['D']}\n\n"
                f"Please state your final answer choice first (e.g. 'Answer: A'), then provide your brief reasoning."
            )
            
            t0 = time.time()
            resp = query_completion(prompt, max_tokens=1536)
            dt = time.time() - t0
            
            if not resp:
                print(f"[{i:02d}/{len(questions)}] FAILED to get response for {qid}", flush=True)
                results.append({
                    "id": qid, "expected": correct_letter, "predicted": "ERR",
                    "passed": False, "gen_speed": 0.0, "pp_speed": 0.0, "tokens": 0, "dt": dt
                })
                with open(CHECKPOINT_FILE, "w") as f:
                    json.dump(results, f, indent=2)
                continue
                
            completion = resp.get("content", "")
            non_think = re.sub(r"<think>.*?</think>", "", completion, flags=re.DOTALL).strip()
            text_to_search = non_think if non_think else completion
            predicted = extract_answer_letter(text_to_search)
            passed = (predicted == correct_letter)
            
            timings = resp.get("timings", {})
            gen_speed = timings.get("predicted_per_second", 0.0)
            pp_speed = timings.get("prompt_per_second", 0.0)
            tokens = timings.get("predicted_n", 0)
            
            status = "CORRECT" if passed else "WRONG"
            print(f"[{i:02d}/{len(questions)}] {qid}: Expected={correct_letter}, Got={predicted} -> {status} | Gen Speed: {gen_speed:.2f} t/s | Tokens: {tokens} ({dt:.1f}s)", flush=True)
            
            results.append({
                "id": qid, "expected": correct_letter, "predicted": predicted,
                "passed": passed, "gen_speed": gen_speed, "pp_speed": pp_speed,
                "tokens": tokens, "dt": dt
            })
            with open(CHECKPOINT_FILE, "w") as f:
                json.dump(results, f, indent=2)

    finally:
        print("Stopping server...", flush=True)
        proc.terminate()
        try:
            proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            proc.kill()
        time.sleep(3)
        subprocess.run("killall -9 llama-server 2>/dev/null || true", shell=True)
        time.sleep(2)

    # Analyze & Output Report
    num_passed = sum(1 for r in results if r["passed"])
    total_q = len(results)
    num_passed_20 = sum(1 for r in results[:20] if r["passed"])
    total_q_20 = min(20, len(results))
    
    gen_speeds = [r["gen_speed"] for r in results if r["gen_speed"] > 0]
    avg_gen_speed = sum(gen_speeds) / len(gen_speeds) if gen_speeds else 0.0
    peak_gen_speed = max(gen_speeds) if gen_speeds else 0.0
    avg_pp_speed = sum(r["pp_speed"] for r in results if r["pp_speed"] > 0) / max(1, sum(1 for r in results if r["pp_speed"] > 0))

    report_file = f"/home/james/.gemini/antigravity-cli/brain/816c1d65-6e4b-4024-8ad0-2ebd54f80461/gpqa_{exp_id}_report.md"
    with open(report_file, "w") as f:
        f.write(f"# GPQA (50 Questions) Report: {exp_name}\n\n")
        f.write(f"- **Timestamp:** `{time.strftime('%Y-%m-%d %H:%M:%S')}`\n")
        f.write(f"- **Model:** `{MODEL_PATH}`\n")
        f.write(f"- **Command:** `{full_cmd}`\n")
        f.write(f"- **GPQA 50Q Score:** **{num_passed} / {total_q} ({num_passed/total_q*100:.1f}%)**\n")
        f.write(f"- **GPQA 20Q Baseline Subset Score:** **{num_passed_20} / {total_q_20} ({num_passed_20/total_q_20*100:.1f}%)**\n")
        f.write(f"- **Average Generation Speed:** **`{avg_gen_speed:.2f} t/s`**\n")
        f.write(f"- **Peak Generation Speed:** **`{peak_gen_speed:.2f} t/s`**\n")
        f.write(f"- **Average Prompt Speed:** **`{avg_pp_speed:.2f} t/s`**\n\n")
        f.write("## Question Breakdown\n\n")
        f.write("| # | Question ID | Expected | Predicted | Status | Gen Speed | Tokens |\n")
        f.write("| :---: | :--- | :---: | :---: | :---: | :---: | :---: |\n")
        for i, r in enumerate(results, 1):
            f.write(f"| {i} | `{r['id']}` | **{r['expected']}** | `{r['predicted']}` | {'PASSED' if r['passed'] else 'FAILED'} | `{r['gen_speed']:.2f} t/s` | {r['tokens']} |\n")

    print(f"Report written to: {report_file}", flush=True)
    if os.path.exists(CHECKPOINT_FILE):
        try:
            os.remove(CHECKPOINT_FILE)
        except Exception:
            pass

    summary = {
        "id": exp_id,
        "name": exp_name,
        "avg_gen_speed": avg_gen_speed,
        "peak_gen_speed": peak_gen_speed,
        "avg_pp_speed": avg_pp_speed,
        "score_50": f"{num_passed} / {total_q} ({num_passed/total_q*100:.1f}%)",
        "score_20": f"{num_passed_20} / {total_q_20} ({num_passed_20/total_q_20*100:.1f}%)",
        "report_file": report_file
    }
    return summary

def main():
    subprocess.run("killall -9 llama-server 2>/dev/null || true", shell=True)
    time.sleep(2)

    res = run_experiment(EXP)
    if res:
        print("\n\n=======================================================", flush=True)
        print(f"EXP 12 COMPLETE: Avg Gen={res['avg_gen_speed']:.2f} t/s | Peak Gen={res['peak_gen_speed']:.2f} t/s | GPQA={res['score']}", flush=True)
        print("=======================================================", flush=True)

if __name__ == "__main__":
    main()
