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
SERVER_LOG = "/tmp/exp17_server.log"
OPTIMIZATION_LOG = "/home/james/.gemini/antigravity-cli/brain/816c1d65-6e4b-4024-8ad0-2ebd54f80461/optimization_log_50tps.md"

EXP = {
    "id": "exp17_combined_champion",
    "name": "Exp 17: Combined Champion (Dual NUMA + MegaKernel + Precision Chained Spec + SER + Fused Barrier Isolation)",
    "numactl": "numactl --interleave=all",
    "server_flags": "--port {port} -c 8192 -t 14 -tb 28 -ctk q8_0 -ctv q8_0 --defer-experts --run-time-repack --numa distribute -fa 1 --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type ngram-map-k:n_max=16,ngram_min_hits=2,ngram_size_n=8 --spec-type mtp:n_max=1,p_min=0.0 -ser 2,0.05"
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

        CHECKPOINT_FILE = f"/home/james/.gemini/antigravity-cli/brain/816c1d65-6e4b-4024-8ad0-2ebd54f80461/scratch/{exp_id}_checkpoint.json"
        results = []
        completed_ids = set()
        if os.path.exists(CHECKPOINT_FILE):
            try:
                with open(CHECKPOINT_FILE, "r") as f:
                    results = json.load(f)
                completed_ids = {r["id"] for r in results}
                print(f"Loaded {len(results)} previously completed questions from checkpoint! Resuming...", flush=True)
            except Exception as e:
                print(f"Error loading checkpoint: {e}", flush=True)

        for i, q in enumerate(questions):
            q_id = q["id"]
            if q_id in completed_ids:
                continue

            print(f"[{exp_id}] Processing Q{i+1}/50 (ID: {q_id})...", flush=True)
            t0 = time.time()
            resp = query_completion(q["prompt"], max_tokens=1536)
            t1 = time.time()

            if resp is None:
                print(f"  FAILED to get response for Q{i+1}", flush=True)
                continue

            content = resp.get("content", "")
            timings = resp.get("timings", {})
            pred_letter = extract_answer_letter(content)
            gold_choice = q.get("correct_letter") or q.get("gold_choice")
            correct = (pred_letter == gold_choice)

            gen_speed = timings.get("predicted_per_second", 0.0)
            pred_n = timings.get("predicted_n", 0)
            pred_ms = timings.get("predicted_ms", 0.0)
            prompt_speed = timings.get("prompt_per_second", 0.0)

            res_item = {
                "id": q_id,
                "index": i + 1,
                "gold_choice": gold_choice,
                "pred_choice": pred_letter,
                "correct": correct,
                "pred_n": pred_n,
                "pred_ms": pred_ms,
                "gen_speed": gen_speed,
                "prompt_speed": prompt_speed,
                "wall_time": t1 - t0,
                "completion_preview": content[:150].replace("\n", " ")
            }
            results.append(res_item)
            completed_ids.add(q_id)

            curr_correct = sum(1 for r in results if r["correct"])
            curr_speeds = [r["gen_speed"] for r in results if r["gen_speed"] > 0]
            curr_avg_spd = sum(curr_speeds)/len(curr_speeds) if curr_speeds else 0.0

            print(f"  Q{i+1}: Gold={gold_choice} Got={pred_letter} {'[CORRECT]' if correct else '[WRONG]'} "
                  f"| Tokens={pred_n} | Speed={gen_speed:.2f} t/s | Cumulative={curr_correct}/{len(results)} ({curr_correct/len(results)*100:.1f}%) | AvgSpeed={curr_avg_spd:.2f} t/s", flush=True)

            with open(CHECKPOINT_FILE, "w") as f:
                json.dump(results, f, indent=2)

        # Finished all questions
        total_q = len(results)
        total_correct = sum(1 for r in results if r["correct"])
        speeds = [r["gen_speed"] for r in results if r["gen_speed"] > 0]
        avg_gen_speed = sum(speeds) / len(speeds) if speeds else 0.0
        peak_gen_speed = max(speeds) if speeds else 0.0
        sub_20_correct = sum(1 for r in results[:20] if r["correct"])

        report = {
            "id": exp_id,
            "name": exp_name,
            "total_questions": total_q,
            "total_correct": total_correct,
            "score_pct": (total_correct / total_q) * 100.0 if total_q > 0 else 0.0,
            "sub_20_correct": sub_20_correct,
            "sub_20_pct": (sub_20_correct / 20.0) * 100.0,
            "avg_gen_speed": avg_gen_speed,
            "peak_gen_speed": peak_gen_speed,
            "results": results
        }

        # Write Report Markdown
        report_file = f"/home/james/.gemini/antigravity-cli/brain/816c1d65-6e4b-4024-8ad0-2ebd54f80461/gpqa_{exp_id}_50q_report.md"
        with open(report_file, "w") as f:
            f.write(f"# 50-Question GPQA Diamond Report: {exp_name}\n\n")
            f.write(f"- **Experiment ID:** `{exp_id}`\n")
            f.write(f"- **Total Score (50Q):** **{total_correct} / {total_q} ({report['score_pct']:.1f}%)**\n")
            f.write(f"- **Standard 20Q Subset:** **{sub_20_correct} / 20 ({report['sub_20_pct']:.1f}%)**\n")
            f.write(f"- **Average Generation Speed:** **`{avg_gen_speed:.2f} tokens/second`**\n")
            f.write(f"- **Peak Generation Speed:** **`{peak_gen_speed:.2f} tokens/second`**\n")
            f.write(f"- **Token Ceiling:** 1,536 tokens (unconstrained Chain-of-Thought)\n\n")
            f.write("## Question-by-Question Breakdown\n\n")
            f.write("| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |\n")
            f.write("| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n")
            for r in results:
                f.write(f"| {r['index']} | `{r['id'][:8]}` | {r['gold_choice']} | {r['pred_choice']} | {'CORRECT' if r['correct'] else 'WRONG'} | {r['pred_n']} | {r['gen_speed']:.2f} | {r['wall_time']:.2f} |\n")

        print(f"\n=======================================================", flush=True)
        print(f"COMPLETED {exp_id}!", flush=True)
        print(f"Score: {total_correct}/{total_q} ({report['score_pct']:.1f}%) | Avg Speed: {avg_gen_speed:.2f} t/s", flush=True)
        print(f"Report written to: {report_file}", flush=True)
        print(f"=======================================================\n", flush=True)

        return report

    finally:
        print("Stopping server...", flush=True)
        proc.terminate()
        try:
            proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            proc.kill()
        print("Server stopped.", flush=True)

if __name__ == "__main__":
    rep = run_experiment(EXP)
    print("Done!")
