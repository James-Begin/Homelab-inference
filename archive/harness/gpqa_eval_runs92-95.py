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

MODEL_PATH = "/home/james/ik_llama.cpp/build/models/flint-UD-Q3_K_XL_Repacked.gguf"
SERVER_BIN = "/home/james/ik_llama.cpp/build/bin/llama-server"
PASSKEY_BIN = "/home/james/ik_llama.cpp/build/bin/llama-passkey"
GPQA_FILE = "/home/james/.gemini/antigravity-cli/brain/816c1d65-6e4b-4024-8ad0-2ebd54f80461/scratch/gpqa_subset_50.json"
PORT = 8087
URL_HEALTH = f"http://127.0.0.1:{PORT}/health"
URL_COMPLETION = f"http://127.0.0.1:{PORT}/completion"
SERVER_LOG = "/tmp/flint_exp95_server.log"
OPTIMIZATION_LOG = "/home/james/.gemini/antigravity-cli/brain/816c1d65-6e4b-4024-8ad0-2ebd54f80461/optimization_log_50tps.md"

EXP = {
    "id": "exp95_flint_unsloth_ud_q3kxl_repacked_muge_ngram_mod_slot050_decoupled26_ceiling4096_q4kv",
    "number": 95,
    "name": "Exp 95: Recursive Flint 40B MoE Unsloth UD Q3_K_XL on ik_llama.cpp (Merged Up/Gate -muge + Repacked AVX2 Q3_K_R4/Q4_0_R8 + N-Gram Mod Speculation n_max=4, match=4 + Slot Cache 0.50 + Decoupled Prefill -tb 26 + 4K Ceiling)",
    "unit": "flint_exp95_eval",
    "model": MODEL_PATH,
    "extreme_name": "Exp95_Flint_Unsloth_UD_Q3KXL_Repacked_MUGE_Ngram_Mod_Slot050_Decoupled26_Ceiling4096_Q4KV",
    "numactl": "numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27",
    "server_flags": "--port {port} -c 8192 -t 28 -tb 26 --spec-type ngram-mod:n_max=4,ngram_size_n=4,ngram_min_hits=4 --slot-save-path /tmp/slots/ -sps 0.50 -ctk q4_0 -ctv q4_0 --numa numactl -muge",
    "threads": 28,
    "threads_batch": 26,
    "port": PORT,
    "max_tokens": 4096,
    "temperature": 0.0,
    "top_p": 1.0,
    "system_prompt": "You are an expert scientific researcher. Provide concise, rigorous reasoning within 600 words, then state your final answer choice clearly.",
    "change": "Evaluating Unsloth flint-UD-Q3_K_XL repacked to AVX2 row-aligned formats (Q3_K_R4 / IQ4_XS_R8 / Q8_0_R8, 17.22 GB) with Merged Up/Gate (-muge) + N-Gram Mod Speculation (n_max=4, match=4) + Slot Cache 0.50 + Decoupled Prefill (-tb 26) targeting 35-45+ tokens/sec throughput."
}

MAX_TOKENS = 4096
SYSTEM_PROMPT = "You are an expert scientific researcher. Provide concise, rigorous reasoning within 600 words, then state your final answer choice clearly."
TEMPERATURE = 0.0
TOP_P = 1.0

def wait_for_server(timeout=240):
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

def query_completion(prompt_text):
    payload = {
        "prompt": f"<|system|>\n{SYSTEM_PROMPT}<|end_of_text|>\n<|user|>\n{prompt_text}<|end_of_text|>\n<|assistant|>\n",
        "n_predict": MAX_TOKENS,
        "temperature": TEMPERATURE,
        "top_p": TOP_P,
        "stop": ["<|end_of_text|>", "<|user|>", "<|system|>"]
    }
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        URL_COMPLETION,
        data=data,
        headers={'Content-Type': 'application/json'}
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=600) as resp:
                return json.loads(resp.read().decode('utf-8'))
        except Exception as e:
            print(f"Query error (attempt {attempt+1}/3): {e}", flush=True)
            time.sleep(2)
    return None

def extract_answer_letter(completion_text: str):
    clean_text = completion_text
    if "</think>" in clean_text:
        clean_text = clean_text.split("</think>", 1)[1]
    elif "<think>" in clean_text:
        return None

    match = re.search(
        r"(?:final answer is|the correct answer is|correct answer is|answer is|choice|option)[:\*\s]*\s*(?:\(?([A-D])\)?)",
        clean_text,
        re.IGNORECASE,
    )
    if match:
        return match.group(1).upper()

    match = re.search(r"\\boxed\{\s*\(?([A-D])\)?\s*\}", clean_text)
    if match:
        return match.group(1).upper()

    lines = [line.strip() for line in clean_text.splitlines() if line.strip()]
    if lines:
        match = re.search(r"\b([A-D])\b", lines[-1])
        if match:
            return match.group(1).upper()

    return None

def update_optimization_log(exp_id, exp_name, change_desc, n_correct, total_q, score_20q, total_20q, avg_speed, peak_speed, report_file):
    pct = (n_correct / total_q) * 100.0 if total_q > 0 else 0.0
    pct_20q = (score_20q / total_20q) * 100.0 if total_20q > 0 else 0.0

    entry = f"""
### Run {exp_id}: {exp_name}
- **Single Change Tested:** {change_desc}
- **50Q GPQA Diamond Score:** **`{n_correct}/{total_q} ({pct:.1f}%)`** (Standard 20Q: **`{score_20q}/{total_20q} ({pct_20q:.1f}%)`**)
- **Generation Speed:** Avg **`{avg_speed:.2f} t/s`** | Peak **`{peak_speed:.2f} t/s`**
- **Token Ceiling:** {MAX_TOKENS} tokens (Unconstrained 4K Chain-of-Thought)
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

    if not os.path.exists(MODEL_PATH):
        raise RuntimeError(f"Model {MODEL_PATH} does not exist!")

    subprocess.run(f"fuser -k {PORT}/tcp", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2)

    os.makedirs("/tmp/slots", exist_ok=True)

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
        if not wait_for_server(timeout=240):
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
            resp = query_completion(question_text)
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
            reasoning_done = ("</think>" in content) or ("<think>" not in content)

            res_entry = {
                "idx": idx,
                "id": qid,
                "gold": gold,
                "pred": pred_letter,
                "correct": is_correct,
                "tokens": n_tokens,
                "speed_tps": tps,
                "wall_time": wall_time,
                "reasoning_completed": reasoning_done,
                "content": content
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
        print(f"=======================================================", flush=True)

        report_md = f"""# 50-Question GPQA Diamond Report: {exp_name}

- **Experiment ID:** `{exp_id}`
- **Total Score (50Q):** **{n_correct} / {total_q} ({score_pct:.1f}%)**
- **Standard 20Q Subset:** **{sum(1 for r in results[:20] if r['correct'])} / {min(20, total_q)} ({(sum(1 for r in results[:20] if r['correct']) / min(20, total_q) * 100.0) if total_q > 0 else 0.0:.1f}%)**
- **Average Generation Speed:** **`{avg_speed:.2f} tokens/second`**
- **Peak Generation Speed:** **`{peak_speed:.2f} tokens/second`**
- **Token Ceiling:** {MAX_TOKENS} tokens (Unconstrained 4K Chain-of-Thought)

## Question-by-Question Breakdown

| # | ID | Gold | Pred | Result | Tokens | Speed (t/s) | Wall Time (s) |
| :-: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
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
            exp["change"],
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
