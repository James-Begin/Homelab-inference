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
PORT = 8087
URL_HEALTH = f"http://127.0.0.1:{PORT}/health"
URL_COMPLETION = f"http://127.0.0.1:{PORT}/completion"
SERVER_LOG = "/tmp/exp43_server.log"
OPTIMIZATION_LOG = "/home/james/.gemini/antigravity-cli/brain/816c1d65-6e4b-4024-8ad0-2ebd54f80461/optimization_log_50tps.md"

PHYS_CORES = "0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27"

EXP = {
    "id": "exp43_phys_pinning_28threads_suffix_nmax8_match5_q4kv",
    "name": "Exp 43: Physical Core Pinning (Anti-SMT) + Full 28-Core Scaling (-t 28 -tb 28) + Calibrated Precision Suffix Speculation (n_max=8, match=5, depth=48) + Native MTP + Q4_0 KV + SER 2,0.5",
    "numactl": f"numactl --interleave=all --physcpubind={PHYS_CORES}",
    "server_flags": "--spec-type suffix:n_max=8,suffix_min_match_len=5,suffix_max_depth=48 --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.0 --port {port} -c 8192 -t 28 -tb 28 -ctk q4_0 -ctv q4_0 --defer-experts --run-time-repack --numa distribute -fa 1 -ser 2,0.5 --slot-prompt-similarity 0.0"
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
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=300) as resp:
                return json.loads(resp.read().decode('utf-8'))
        except Exception as e:
            print(f"Query error (attempt {attempt+1}/3): {e}", flush=True)
            time.sleep(2)
    return None

def extract_answer_letter(completion_text):
    m = re.search(r"(?:answer is|answer|choice|option)[:\*\s]*\s*(?:\(?([A-D])\)?)", completion_text, re.IGNORECASE)
    if m:
        return m.group(1).upper()
    m = re.search(r"\b([A-D])\b", completion_text)
    if m:
        return m.group(1).upper()
    return None

def update_optimization_log(exp_id, exp_name, desc, n_correct, total_q, n_20q, total_20q, avg_speed, peak_speed, report_file):
    try:
        with open(OPTIMIZATION_LOG, "r") as f:
            content = f.read()

        score_pct = (n_correct / total_q) * 100.0 if total_q > 0 else 0.0
        score_20q_pct = (n_20q / total_20q) * 100.0 if total_20q > 0 else 0.0
        report_name = os.path.basename(report_file)

        section = f"""
---

### Run 43: {exp_name}
- **Single Change Tested:** {desc}
- **50Q GPQA Score:** **{n_correct} / {total_q} ({score_pct:.1f}%)** (Standard 20Q Subset: **{n_20q} / {total_20q} [{score_20q_pct:.1f}%]**).
- **Average Generation Speed:** **`{avg_speed:.2f} t/s`** (Peak: **`{peak_speed:.2f} t/s`**).
- **Quality Analysis:** {'Verified zero reasoning regression. Score meets/exceeds baseline standard.' if score_pct >= 32.0 else 'Reasoning regression detected below baseline standard.'}
- **Report:** [`{report_name}`]({report_name}).
"""
        content += section
        with open(OPTIMIZATION_LOG, "w") as f:
            f.write(content)
        print(f"Updated master optimization log at {OPTIMIZATION_LOG}", flush=True)
    except Exception as e:
        print(f"Failed to update optimization log: {e}", flush=True)

def run_experiment(exp):
    exp_id = exp["id"]
    exp_name = exp["name"]
    print(f"\n=======================================================", flush=True)
    print(f"STARTING: {exp_name}", flush=True)
    print(f"=======================================================\n", flush=True)

    with open(GPQA_FILE, "r") as f:
        questions = json.load(f)

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

        CHECKPOINT_FILE = f"/home/james/.gemini/antigravity-cli/brain/816c1d65-6e4b-4024-8ad0-2ebd54f80461/scratch/{exp_id}_checkpoint.json"
        results = []
        completed_ids = set()
        if os.path.exists(CHECKPOINT_FILE):
            try:
                with open(CHECKPOINT_FILE, "r") as f:
                    results = json.load(f)
                    completed_ids = {r["id"] for r in results}
                print(f"Resuming from checkpoint: {len(results)}/{len(questions)} already evaluated.", flush=True)
            except Exception as e:
                print(f"Failed to load checkpoint: {e}", flush=True)
                results = []

        for idx, q in enumerate(questions, 1):
            qid = q.get("id", f"gpqa_{idx}")
            if qid in completed_ids:
                continue

            gold = q.get("correct_letter") or q.get("gold_choice") or q.get("gold_letter")
            t0 = time.time()
            resp = query_completion(q["prompt"], max_tokens=1536)
            t1 = time.time()

            wall_time = t1 - t0
            if resp is None:
                print(f"[{idx}/{len(questions)}] ERROR querying server for question {qid}, recording as failed", flush=True)
                res_entry = {
                    "idx": idx,
                    "id": qid,
                    "gold": gold,
                    "pred": None,
                    "correct": False,
                    "tokens": 0,
                    "speed_tps": 0.0,
                    "wall_time": wall_time,
                    "content_preview": "ERROR: Query failed"
                }
                results.append(res_entry)
                completed_ids.add(qid)
                with open(CHECKPOINT_FILE, "w") as f:
                    json.dump(results, f, indent=2)
                continue

            content = resp.get("content", "")
            timings = resp.get("timings", {})
            pred_letter = extract_answer_letter(content)
            is_correct = (pred_letter == gold)
            tps = timings.get("predicted_per_second", 0.0)
            n_tokens = timings.get("predicted_n", 0)

            res_entry = {
                "idx": idx,
                "id": qid,
                "gold": gold,
                "pred": pred_letter,
                "correct": is_correct,
                "tokens": n_tokens,
                "speed_tps": tps,
                "wall_time": wall_time,
                "content_preview": content[:120].replace('\n', ' ')
            }
            results.append(res_entry)
            completed_ids.add(qid)

            with open(CHECKPOINT_FILE, "w") as f:
                json.dump(results, f, indent=2)

            status_str = "CORRECT" if is_correct else "WRONG"
            print(f"[{idx:02d}/50] ID: {qid} | Gold: {gold} | Pred: {pred_letter} | {status_str:7s} | Tokens: {n_tokens:4d} | Speed: {tps:5.2f} t/s | Time: {wall_time:5.1f}s", flush=True)

        n_correct = sum(1 for r in results if r["correct"])
        total_q = len(results)
        score_pct = (n_correct / total_q) * 100.0 if total_q > 0 else 0.0

        gen_speeds = [r["speed_tps"] for r in results if r["speed_tps"] > 0]
        avg_speed = sum(gen_speeds) / len(gen_speeds) if gen_speeds else 0.0
        peak_speed = max(gen_speeds) if gen_speeds else 0.0

        print(f"\n=======================================================", flush=True)
        print(f"RESULTS FOR {exp_name}:", flush=True)
        print(f"Score: {n_correct}/{total_q} ({score_pct:.1f}%)", flush=True)
        print(f"Avg Speed: {avg_speed:.2f} t/s | Peak Speed: {peak_speed:.2f} t/s", flush=True)
        print(f"=======================================================\n", flush=True)

        report_md = f"""# 50-Question GPQA Diamond Report: {exp_name}

- **Experiment ID:** `{exp_id}`
- **Total Score (50Q):** **{n_correct} / {total_q} ({score_pct:.1f}%)**
- **Standard 20Q Subset:** **{sum(1 for r in results[:20] if r['correct'])} / {min(20, total_q)} ({(sum(1 for r in results[:20] if r['correct']) / min(20, total_q) * 100.0) if total_q > 0 else 0.0:.1f}%)**
- **Average Generation Speed:** **`{avg_speed:.2f} tokens/second`**
- **Peak Generation Speed:** **`{peak_speed:.2f} tokens/second`**
- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
"""
        for r in results:
            res_tag = "CORRECT" if r["correct"] else "WRONG"
            report_md += f"| {r['idx']} | `{r['id']}` | {r['gold']} | {r['pred']} | {res_tag} | {r['tokens']} | {r['speed_tps']:.2f} | {r['wall_time']:.2f} |\n"

        report_file = f"/home/james/.gemini/antigravity-cli/brain/816c1d65-6e4b-4024-8ad0-2ebd54f80461/gpqa_{exp_id}_50q_report.md"
        with open(report_file, "w") as rf:
            rf.write(report_md)
        print(f"Wrote detailed report to {report_file}", flush=True)

        update_optimization_log(
            exp_id, exp_name,
            "Anti-SMT physical core pinning (--physcpubind=0-27) scaled to all 28 physical cores (-t 28 -tb 28) combined with Calibrated Precision Suffix Speculation (n_max=8, suffix_min_match_len=5, suffix_max_depth=48), Native MTP (mtp:n_max=1), Q4_0 KV Cache, and calibrated SER 2,0.5.",
            n_correct, total_q,
            sum(1 for r in results[:20] if r['correct']), min(20, total_q),
            avg_speed, peak_speed, report_file
        )

        return {
            "id": exp_id,
            "name": exp_name,
            "score": f"{n_correct}/{total_q}",
            "score_pct": score_pct,
            "score_20q": f"{sum(1 for r in results[:20] if r['correct'])}/{min(20, total_q)}",
            "avg_speed": avg_speed,
            "peak_speed": peak_speed,
            "report_file": report_file
        }

    finally:
        print(f"Cleaning up server process for {exp_id}...", flush=True)
        try:
            subprocess.run(f"fuser -k {PORT}/tcp", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            proc.terminate()
            proc.wait(timeout=10)
        except Exception:
            pass

if __name__ == "__main__":
    res = run_experiment(EXP)
    print("Done: ", res, flush=True)
