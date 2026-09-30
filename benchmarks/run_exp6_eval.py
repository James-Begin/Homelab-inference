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
PASSKEY_BIN = "/home/james/ik_llama.cpp/build/bin/llama-passkey"
GPQA_FILE = "/home/james/.gemini/antigravity-cli/brain/816c1d65-6e4b-4024-8ad0-2ebd54f80461/scratch/gpqa_subset_20.json"
PORT = 8085
URL_HEALTH = f"http://127.0.0.1:{PORT}/health"
URL_COMPLETION = f"http://127.0.0.1:{PORT}/completion"
REPORT_FILE = "/home/james/.gemini/antigravity-cli/brain/816c1d65-6e4b-4024-8ad0-2ebd54f80461/gpqa_exp6_numa_chained_spec_report.md"

def query_completion(prompt_text, max_tokens=384):
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
        with urllib.request.urlopen(req, timeout=120) as resp:
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

def run_passkey_test():
    cmd = f"numactl --interleave=all {PASSKEY_BIN} -m {MODEL_PATH} -c 8192 --junk 250 -t 10 -tb 28 -fa 1 --run-time-repack --numa distribute --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type ngram-mod:n_max=16,n_min=3,ngram_size_n=4 --spec-type mtp:n_max=1,p_min=0.0"
    print(f"Running Passkey Long-Context test: {cmd}", flush=True)
    try:
        proc = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=180)
        output = proc.stdout + proc.stderr
        pk_val_match = re.search(r"passkey\s*=\s*(\d+)", output)
        expected_passkey = pk_val_match.group(1) if pk_val_match else None
        
        match = False
        if expected_passkey:
            after_prompt = output.split("What is the pass key?")
            if len(after_prompt) > 1 and expected_passkey in after_prompt[1]:
                match = True
            elif expected_passkey in output:
                match = True

        pp_match = re.search(r"prompt eval time = .* \( +([\d.]+) ms per token, +([\d.]+) tokens per second\)", output)
        tg_match = re.search(r"eval time = .* \( +([\d.]+) ms per token, +([\d.]+) tokens per second\)", output)
        pp_speed = float(pp_match.group(2)) if pp_match else 0.0
        tg_speed = float(tg_match.group(2)) if tg_match else 0.0
        return {
            "passed": match,
            "pp_speed": pp_speed,
            "tg_speed": tg_speed,
            "expected": expected_passkey
        }
    except Exception as e:
        print(f"Passkey error: {e}", flush=True)
        return {"passed": False, "pp_speed": 0.0, "tg_speed": 0.0, "error": str(e)}

def main():
    print(f"=======================================================", flush=True)
    print(f"RESUMING EXPERIMENT 6: Dual-Socket NUMA + Chained Speculation", flush=True)
    print(f"Server is currently running on port {PORT}", flush=True)
    print(f"=======================================================\n", flush=True)
    
    with open(GPQA_FILE, "r") as f:
        questions = json.load(f)
        
    results = []
    for i, item in enumerate(questions, 1):
        qid = item["id"]
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
        resp = query_completion(prompt, max_tokens=384)
        t1 = time.time()
        
        if not resp:
            print(f"  [{i:02d}/20] FAILED to get response for {qid}", flush=True)
            results.append({
                "id": qid,
                "passed": False,
                "predicted": None,
                "expected": correct_letter,
                "gen_speed": 0.0,
                "pp_speed": 0.0,
                "tokens": 0
            })
            continue
            
        content = resp.get("content", "")
        non_think = re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL).strip()
        text_to_search = non_think if non_think else content
        predicted_letter = extract_answer_letter(text_to_search)
        passed = (predicted_letter == correct_letter)
        
        timings = resp.get("timings", {})
        gen_speed = timings.get("predicted_per_second", 0.0)
        pp_speed = timings.get("prompt_per_second", 0.0)
        tokens = timings.get("predicted_n", 0)
        
        status_str = "PASSED" if passed else "FAILED"
        print(f"  [{i:02d}/20] {qid}: {status_str} | Pred: {predicted_letter} (Exp: {correct_letter}) | Speed: {gen_speed:.2f} t/s | Tokens: {tokens} | Time: {t1-t0:.1f}s", flush=True)
        
        results.append({
            "id": qid,
            "passed": passed,
            "predicted": predicted_letter,
            "expected": correct_letter,
            "gen_speed": gen_speed,
            "pp_speed": pp_speed,
            "tokens": tokens
        })
        
    print("\nAll 20 questions finished! Stopping llama-server for Exp 6...", flush=True)
    subprocess.run("killall -9 llama-server 2>/dev/null || true", shell=True)
    time.sleep(2)
    
    print("\n--- Running Long Context (4K Needle) Passkey Test ---", flush=True)
    pk_res = run_passkey_test()
    print(f"Passkey Result: {'PASSED' if pk_res.get('passed') else 'FAILED'} | TG: {pk_res.get('tg_speed', 0.0):.2f} t/s | PP: {pk_res.get('pp_speed', 0.0):.2f} t/s\n", flush=True)
    
    num_passed = sum(1 for r in results if r["passed"])
    total_q = len(results)
    avg_gen_speed = sum(r["gen_speed"] for r in results if r["gen_speed"] > 0) / max(1, sum(1 for r in results if r["gen_speed"] > 0))
    avg_pp_speed = sum(r["pp_speed"] for r in results if r["pp_speed"] > 0) / max(1, sum(1 for r in results if r["pp_speed"] > 0))
    
    with open(REPORT_FILE, "w") as f:
        f.write("# GPQA (20 Questions) & Long-Context Report: Exp 6: Dual-Socket NUMA + Chained Speculation\n\n")
        f.write(f"- **Timestamp:** `{time.strftime('%Y-%m-%d %H:%M:%S')}`\n")
        f.write(f"- **GPQA Score:** **{num_passed} / {total_q} ({num_passed/total_q*100:.1f}%)**\n")
        f.write(f"- **Average Generation Speed:** **`{avg_gen_speed:.2f} t/s`**\n")
        f.write(f"- **Average Prompt Speed:** **`{avg_pp_speed:.2f} t/s`**\n")
        f.write(f"- **4K Context Needle Passkey:** **{'PASSED' if pk_res.get('passed') else 'FAILED'}**\n\n")
        f.write("## Question Breakdown\n\n")
        f.write("| # | Question ID | Expected | Predicted | Status | Gen Speed | Tokens |\n")
        f.write("| :---: | :--- | :---: | :---: | :---: | :---: | :---: |\n")
        for i, r in enumerate(results, 1):
            f.write(f"| {i} | `{r['id']}` | **{r['expected']}** | `{r['predicted']}` | {'PASSED' if r['passed'] else 'FAILED'} | `{r['gen_speed']:.2f} t/s` | {r['tokens']} |\n")
        f.write(f"\n| - | `passkey_4k` | **Match** | `{'Match' if pk_res.get('passed') else 'Fail'}` | {'PASSED' if pk_res.get('passed') else 'FAILED'} | `{pk_res.get('tg_speed', 0.0):.2f} t/s` | Needle |\n")
        
    print(f"Report saved to: {REPORT_FILE}", flush=True)

if __name__ == "__main__":
    main()
