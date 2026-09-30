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

SCRATCH_DIR = "/home/james/.gemini/antigravity-cli/brain/816c1d65-6e4b-4024-8ad0-2ebd54f80461/scratch"
BRAIN_DIR = "/home/james/.gemini/antigravity-cli/brain/816c1d65-6e4b-4024-8ad0-2ebd54f80461"
OPTIMIZATION_LOG = f"{BRAIN_DIR}/optimization_log_50tps.md"
BENCHMARK_EXTREME_SCRIPT = f"{SCRATCH_DIR}/benchmark_extreme_context.py"

PHYS_CORES = "0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27"

QUEUE_FILE = f"{SCRATCH_DIR}/pipeline_queue.json"

def get_pipeline_experiments():
    if os.path.exists(QUEUE_FILE):
        try:
            with open(QUEUE_FILE, "r") as f:
                return json.load(f)
        except Exception as e:
            log(f"Warning: Failed to load {QUEUE_FILE}: {e}")
    return []

def log(msg):
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [WATCHDOG] {msg}", flush=True)

def check_server_health(port=8087):
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/health", timeout=3) as resp:
            return resp.status == 200
    except Exception:
        return False

def run_cmd(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True)

def supervise_experiment_gpqa(exp):
    exp_id = exp["id"]
    exp_name = exp["name"]
    unit_name = exp["unit"]
    script_path = exp["script"]
    cp_file = exp["checkpoint"]
    port = exp.get("port", 8087)
    consecutive_stalls = 0

    log("=======================================================")
    log(f"STAGE: SUPERVISING GPQA DIAMOND 50Q FOR {exp_name}")
    log("=======================================================")

    while True:
        count = 0
        if os.path.exists(cp_file):
            try:
                with open(cp_file, "r") as f:
                    data = json.load(f)
                    count = len(data)
            except Exception:
                pass

        if count >= 50:
            log(f"SUCCESS: {exp_id} has completed 50/50 questions!")
            time.sleep(3)
            run_cmd(f"systemctl --user stop {unit_name} 2>/dev/null || true")
            run_cmd(f"fuser -k {port}/tcp 2>/dev/null || true")
            time.sleep(2)
            return True

        res = run_cmd(f"systemctl --user is-active {unit_name}")
        status = res.stdout.strip()

        if status not in ["active", "activating"]:
            log(f"ALERT: {unit_name} is '{status}' but only {count}/50 questions completed! Starting service...")
            run_cmd(f"fuser -k {port}/tcp 2>/dev/null || true")
            time.sleep(2)
            run_cmd(f"systemctl --user reset-failed {unit_name} 2>/dev/null || true")
            run_cmd(f"systemd-run --user --unit={unit_name} /usr/bin/python3 -u {script_path}")
            consecutive_stalls = 0
            time.sleep(10)
            continue

        if not check_server_health(port):
            consecutive_stalls += 1
            if consecutive_stalls > 10:
                log(f"ALERT: {exp_id} server port {port} unresponsive for >150s. Restarting service to self-heal...")
                run_cmd(f"systemctl --user stop {unit_name}")
                run_cmd(f"fuser -k {port}/tcp 2>/dev/null || true")
                time.sleep(3)
                run_cmd(f"systemd-run --user --unit={unit_name} /usr/bin/python3 -u {script_path}")
                consecutive_stalls = 0
                time.sleep(10)
                continue
        else:
            consecutive_stalls = 0

        log(f"{exp_id} healthy | Progress: {count}/50 questions | Service: {status}")
        time.sleep(20)

def run_extreme_context_ladder(exp):
    slug = re.sub(r'[^a-zA-Z0-9_]+', '_', exp["extreme_name"].lower())
    report_file = f"{BRAIN_DIR}/extreme_context_{slug}_report.md"

    if os.path.exists(report_file):
        log(f"Extreme context certification already exists at {report_file}! Skipping ladder.")
        return

    log("=======================================================")
    log(f"STAGE: LAUNCHING EXTENDED NEEDLE RETRIEVAL LADDER FOR {exp['name']} (16K -> 128K)")
    log("=======================================================")

    model_arg = f"--model \"{exp['model']}\" " if "model" in exp else ""
    cmd = (
        f"/usr/bin/python3 -u {BENCHMARK_EXTREME_SCRIPT} "
        f"--name \"{exp['extreme_name']}\" "
        f"--targets 16k,32k,64k,128k "
        f"{model_arg}"
        f"--numactl \"{exp['extreme_numactl']}\" "
        f"--threads {exp['threads']} --threads-batch {exp['threads_batch']} "
        f"--extra-flags \"{exp['extreme_flags']}\""
    )
    log(f"Executing: {cmd}")
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for line in proc.stdout:
        print(line, end="", flush=True)
    proc.wait()

    log(f"{exp['id']} extreme context certification exited with code {proc.returncode}")
    if os.path.exists(report_file):
        try:
            with open(report_file, "r") as f:
                rep_content = f.read()
            with open(OPTIMIZATION_LOG, "a") as f:
                f.write(f"\n\n## Extended Needle Retrieval Certification ({exp['name']})\n\n{rep_content}\n")
            log(f"Appended extreme context report to {OPTIMIZATION_LOG}")
        except Exception as e:
            log(f"Error appending report: {e}")

def main():
    log("=======================================================")
    log("MASTER SELF-HEALING MULTI-EXPERIMENT PIPELINE SUPERVISOR ACTIVE")
    log("Continuous 24/7 Zero-Downtime Autonomous Evaluation Queue")
    log("=======================================================")

    while True:
        experiments = get_pipeline_experiments()
        all_completed = True
        for exp in experiments:
            slug = re.sub(r'[^a-zA-Z0-9_]+', '_', exp["extreme_name"].lower())
            needle_report = f"{BRAIN_DIR}/extreme_context_{slug}_report.md"
            gpqa_cp = exp["checkpoint"]

            is_gpqa_done = False
            if os.path.exists(gpqa_cp):
                try:
                    with open(gpqa_cp) as f:
                        is_gpqa_done = (len(json.load(f)) >= 50)
                except Exception:
                    pass

            is_needle_done = os.path.exists(needle_report)

            if is_gpqa_done and is_needle_done:
                continue

            all_completed = False
            log(f"\n>>> PROCESSING PIPELINE EXPERIMENT: {exp['name']} ({exp['id']})")
            
            # 1. Supervise 50Q GPQA Diamond Reasoning Evaluation
            if not is_gpqa_done:
                supervise_experiment_gpqa(exp)

            # 2. Supervise Extended Needle Retrieval Ladder (16K -> 128K)
            if not is_needle_done:
                run_extreme_context_ladder(exp)

            log(f">>> COMPLETED EXPERIMENT: {exp['name']}!\n")

        if all_completed:
            log(f"All {len(experiments)} queued experiments fully verified! Checking for queue updates in 30s...")
            time.sleep(30)

if __name__ == "__main__":
    main()
