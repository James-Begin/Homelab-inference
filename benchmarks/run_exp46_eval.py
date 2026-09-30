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

MODEL_BASE = "/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf"
MODEL_PATH = "/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0.gguf"
QUANTIZE_BIN = "/home/james/ik_llama.cpp/build/bin/llama-quantize"
SERVER_BIN = "/home/james/ik_llama.cpp/build/bin/llama-server"
GPQA_FILE = "/home/james/.gemini/antigravity-cli/brain/816c1d65-6e4b-4024-8ad0-2ebd54f80461/scratch/gpqa_subset_50.json"
PORT = 8087
URL_HEALTH = f"http://127.0.0.1:{PORT}/health"
URL_COMPLETION = f"http://127.0.0.1:{PORT}/completion"
SERVER_LOG = "/tmp/exp46_server.log"
OPTIMIZATION_LOG = "/home/james/.gemini/antigravity-cli/brain/816c1d65-6e4b-4024-8ad0-2ebd54f80461/optimization_log_50tps.md"

PHYS_CORES = "0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27"

EXP = {
    "id": "exp46_phys_pinning_28threads_iq4xs_dense_mtp_q4kv",
    "name": "Exp 46: Physical Core Pinning (Anti-SMT) + Full 28-Core Scaling (-t 28 -tb 28) + Custom Non-Linear Dense Quantization (IQ4_XS Attention + Q4_0 MoE) + Native MTP + Q4_0 KV + SER 2,0.5",
    "numactl": f"numactl --interleave=all --physcpubind={PHYS_CORES}",
    "server_flags": "--override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.0 --port {port} -c 8192 -t 28 -tb 28 -ctk q4_0 -ctv q4_0 --defer-experts --run-time-repack --numa distribute -fa 1 -ser 2,0.5 --slot-prompt-similarity 0.0"
}

def ensure_quantized_model():
    if not os.path.exists(MODEL_PATH):
        print(f"Generating custom quantized model: {MODEL_PATH}...", flush=True)
        cmd = [
            QUANTIZE_BIN,
            "--allow-requantize",
            "--custom-q", ".*attn_.*=iq4_xs,.*ssm_out.*=iq4_xs,.*ffn_.*_exps.*=q4_0",
            MODEL_BASE,
            MODEL_PATH,
            "Q6_K",
            "28"
        ]
        print(f"Executing: {' '.join(cmd)}", flush=True)
        t0 = time.time()
        res = subprocess.run(cmd, capture_output=True, text=True)
        dt = time.time() - t0
        if res.returncode != 0:
            print(f"Quantization failed with code {res.returncode}:\n{res.stderr}", flush=True)
            raise RuntimeError(f"llama-quantize failed: {res.stderr}")
        size_mb = os.path.getsize(MODEL_PATH) / (1024 * 1024)
        print(f"Quantization complete in {dt:.1f}s! Generated {MODEL_PATH} ({size_mb:.2f} MB)", flush=True)
    else:
        print(f"Model {MODEL_PATH} already exists ({os.path.getsize(MODEL_PATH) / (1024*1024):.2f} MB).", flush=True)

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

def update_optimization_log(exp_id, exp_name, change_desc, n_correct, total_q, score_20q, total_20q, avg_speed, peak_speed, report_file):
    pct = (n_correct / total_q) * 100.0 if total_q > 0 else 0.0
    pct_20q = (score_20q / total_20q) * 100.0 if total_20q > 0 else 0.0

    entry = f"""
### Run {exp_id}: {exp_name}
- **Single Change Tested:** {change_desc}
- **50Q GPQA Diamond Score:** **`{n_correct}/{total_q} ({pct:.1f}%)`** (Standard 20Q: **`{score_20q}/{total_20q} ({pct_20q:.1f}%)`**)
- **Generation Speed:** Avg **`{avg_speed:.2f} t/s`** | Peak **`{peak_speed:.2f} t/s`**
- **Detailed Report:** [`{os.path.basename(report_file)}`]({report_file})
"""
    try:
        with open(OPTIMIZATION_LOG, "a") as f:
            f.write(entry)
        print(f"Appended results to {OPTIMIZATION_LOG}", flush=True)
    except Exception as e:
        print(f"Error updating optimization log: {e}", flush=True)

def run_experiment(exp):
    exp_id = exp["id"]
    exp_name = exp["name"]
    numactl_cmd = exp["numactl"]
    server_flags = exp["server_flags"].format(port=PORT)

    checkpoint_file = f"/home/james/.gemini/antigravity-cli/brain/816c1d65-6e4b-4024-8ad0-2ebd54f80461/scratch/{exp_id}_checkpoint.json"

    print("=======================================================", flush=True)
    print(f"STARTING: {exp_name}", flush=True)
    print("=======================================================", flush=True)

    ensure_quantized_model()

    subprocess.run(f"fuser -k {PORT}/tcp", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2)

    cmd = f"{numactl_cmd} {SERVER_BIN} -m {MODEL_PATH} {server_flags}"
    print(f"Launching Server: {cmd}", flush=True)

    server_log_f = open(SERVER_LOG, "w")
    proc = subprocess.Popen(
        cmd,
        shell=True,
        stdout=server_log_f,
        stderr=subprocess.STDOUT,
        preexec_fn=os.setsid
    )

    try:
        print("Waiting for server health check...", flush=True)
        if not wait_for_server(timeout=180):
            print("ERROR: Server failed to reach healthy state!", flush=True)
            return None
        print("Server healthy and listening on port!", flush=True)

        with open(GPQA_FILE, "r") as f:
            questions = json.load(f)

        results = []
        if os.path.exists(checkpoint_file):
            try:
                with open(checkpoint_file, "r") as cf:
                    results = json.load(cf)
                print(f"Resuming from checkpoint with {len(results)} questions completed.", flush=True)
            except Exception as e:
                print(f"Error loading checkpoint: {e}", flush=True)

        for idx in range(len(results) + 1, len(questions) + 1):
            q_data = questions[idx - 1]
            qid = q_data.get("id", f"gpqa_{idx}")
            question_text = q_data.get("prompt") or q_data.get("question")
            gold = q_data.get("correct_letter") or q_data.get("gold") or q_data.get("gold_choice")

            t0 = time.time()
            resp = query_completion(question_text, max_tokens=1536)
            wall_time = time.time() - t0

            if resp is None:
                print(f"[{idx:02d}/50] ID: {qid} | FAILED TO GET RESPONSE", flush=True)
                continue

            content = resp.get("content", "")
            timings = resp.get("timings", {})
            predicted_n = timings.get("predicted_n", 0)
            predicted_ms = timings.get("predicted_ms", 0.0)

            tps = (predicted_n / (predicted_ms / 1000.0)) if predicted_ms > 0 else (predicted_n / wall_time if wall_time > 0 else 0.0)
            n_tokens = predicted_n

            pred_letter = extract_answer_letter(content)
            is_correct = (pred_letter == gold)

            res_entry = {
                "idx": idx,
                "id": qid,
                "gold": gold,
                "pred": pred_letter,
                "correct": is_correct,
                "tokens": n_tokens,
                "speed_tps": tps,
                "wall_time": wall_time
            }
            results.append(res_entry)

            with open(checkpoint_file, "w") as cf:
                json.dump(results, cf, indent=2)

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
            "Anti-SMT physical core pinning (--physcpubind=0-27) scaled to all 28 physical cores (-t 28 -tb 28) combined with Custom Non-Linear Dense Quantization (IQ4_XS dense attention + Q4_0 MoE experts) with hand-tuned AVX2 kernel (mul_mat_iq4_xs_r8_q8_k_avx2), Native MTP (mtp:n_max=1), Q4_0 KV Cache, and calibrated SER 2,0.5.",
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
