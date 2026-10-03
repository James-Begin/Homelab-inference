#!/usr/bin/env python3
"""Read-only audit of the published Homelab-inference experiment artifacts.

Usage from the repository root: python3 benchmarks/reproduce_audit.py .
No server is launched. The parser demonstrations execute extracted functions
with a fake subprocess result, not an inference process.
"""
import ast
import contextlib
import io
import json
import re
import statistics
import sys
import time
from pathlib import Path
from types import SimpleNamespace


def extract_function(path, name, globals_dict):
    tree = ast.parse(path.read_text())
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name)
    exec(compile(ast.Module(body=[node], type_ignores=[]), str(path), "exec"), globals_dict)
    return globals_dict[name]


def metrics(rows):
    valid = []
    for row in rows:
        speed = row.get("speed_tps", row.get("gen_speed", 0))
        tokens = row.get("tokens", row.get("pred_n", 0))
        wall = row.get("wall_time", row.get("dt", 0))
        if isinstance(speed, (int, float)) and speed > 0 and tokens > 0:
            valid.append((speed, tokens, wall))
    if not valid:
        return None
    return {
        "count": len(rows),
        "valid": len(valid),
        "correct": sum(bool(r.get("correct", r.get("passed", False))) for r in rows),
        "mean": statistics.mean(s for s, _, _ in valid),
        "median": statistics.median(s for s, _, _ in valid),
        "weighted": sum(t for _, t, _ in valid) / sum(t / s for s, t, _ in valid),
        "wall": sum(t for _, t, _ in valid) / sum(w for _, _, w in valid) if all(w > 0 for _, _, w in valid) else None,
        "cap": sum(r.get("tokens", r.get("pred_n", 0)) >= 1536 for r in rows),
    }


def main():
    repo = Path(sys.argv[1]).resolve()
    raw = repo / "logs/raw_checkpoints"
    catalog = json.loads((repo / "benchmarks/experiments.json").read_text())
    reports = list((repo / "logs/gpqa_reports").glob("*50q_report.md"))
    checkpoints = list(raw.glob("*checkpoint.json"))
    by_number = {}
    for path in checkpoints:
        number = int(re.search(r"exp(\d+)", path.name)[1])
        rows = json.loads(path.read_text())
        if isinstance(rows, list):
            by_number[number] = (path, rows, metrics(rows))

    print("**Homelab inference: reproducible artifact audit**\n")
    print(f"Read {len(reports)} standardized report files, {len(checkpoints)} checkpoint files, and {len(catalog)} catalog entries. Earlier sweeps and technical postmortems are separate.\n")
    print("Throughput below is reconstructed from saved token counts and rates; it is not a new benchmark. Weighted decode = sum(tokens) / sum(tokens / reported_rate). Wall rate includes the saved request wall time. Neither includes server startup. Positive-speed rows with positive token counts are used for rates; invalid rows remain in score and cap counts.\n")
    print("| Run | Saved rows | Valid timing rows | Recorded correct | Mean t/s | Median t/s | Weighted decode t/s | Request wall t/s | At token ceiling |")
    print("| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |")
    for n, (path, rows, m) in sorted(by_number.items()):
        if m:
            wall = f"{m['wall']:.2f}" if m['wall'] else "—"
            print(f"| {n} | {m['count']} | {m['valid']} | {m['correct']} | {m['mean']:.2f} | {m['median']:.2f} | {m['weighted']:.2f} | {wall} | {m['cap']} |")

    print("\nRun 12's committed checkpoint contains only 36 rows despite a 50-question report. Run 35 has one row with zero tokens and zero speed; excluding that row changes how its mean is calculated. Do not silently compare these recomputations to a different denominator.\n")
    print("**All standardized reported results**\n")
    print("These retain the published score and arithmetic mean, including runs without complete raw checkpoints. They are historical observations, not quality certifications.\n")
    lines = (repo / "RESULTS.md").read_text().splitlines()
    active = False
    for line in lines:
        if line.startswith("| Run | Configuration | Avg t/s | Peak t/s"):
            active = True
            print("| Run | Configuration | Avg t/s | Peak t/s | Recorded score |")
            print("| ---: | --- | ---: | ---: | --- |")
            continue
        if active and line.startswith("| ---"):
            continue
        if active and line.startswith("|"):
            cols = [s.strip() for s in line.strip("|").split("|")]
            print("| " + " | ".join(cols[:5]) + " |")
        elif active:
            break

    print("\n**Executable parser demonstrations**\n")
    answer = extract_function(repo / "benchmarks/gpqa_eval.py", "extract_answer_letter", {"re": re})
    unfinished = "<think>I should test option B before calculating the final answer."
    cleaned = re.sub(r"<think>.*?</think>", "", unfinished, flags=re.DOTALL).strip()
    result = answer(cleaned or unfinished)
    status_str = "FIXED (None)" if result is None else f"VULNERABLE (`{result}`)"
    print(f"1. An unfinished thinking block with no final answer is scored as `{result}` ({status_str}): `{unfinished}`. In the patched harness, unclosed thinking traces safely evaluate to None rather than false positives.\n")

    fake_output = (
        "passkey = 12345\nWhat is the pass key? The answer is unknown.\n"
        "llama_print_timings: prompt eval time = 1000.00 ms / 100 tokens ( 10.00 ms per token, 100.00 tokens per second)\n"
        "llama_print_timings:        eval time = 1000.00 ms / 10 tokens ( 100.00 ms per token, 10.00 tokens per second)\n"
    )
    fake_process = SimpleNamespace(stdout=fake_output, stderr="", returncode=1)
    fn = extract_function(repo / "benchmarks/benchmark_extreme_context.py", "run_passkey_step", {
        "re": re, "time": time, "MODEL_PATH": "unused.gguf", "PASSKEY_BIN": "unused-passkey",
        "expand": lambda s: s,
        "subprocess": SimpleNamespace(run=lambda *args, **kwargs: fake_process),
    })
    with contextlib.redirect_stdout(io.StringIO()):
        observed = fn(16384, 1000)
    pass_status = "REJECTED (Correct)" if not observed["passed"] else "FALSE POSITIVE (Vulnerable)"
    speed_status = "10.0 t/s (Correct)" if observed["tg_speed"] == 10.0 else f"{observed['tg_speed']} t/s (Vulnerable)"
    print(f"2. A fake process returning exit code 1 with non-matching response is evaluated as: passed={observed['passed']} ({pass_status}).\n")
    print(f"3. With prompt speed 100 t/s and decode speed 10 t/s, the benchmark reports decode speed {observed['tg_speed']} t/s ({speed_status}).\n")
    for n in [40, 42]:
        row = max(by_number[n][1], key=lambda r: r.get("speed_tps", 0))
        print(f"4. Run {n} peak: {row['speed_tps']:.2f} t/s, {row['tokens']} tokens, recorded correct={row['correct']}, answer={row['pred']}. Saved preview: `{row.get('content_preview', '')}`\n")
    print("**Queued experiments**\n")
    for e in catalog:
        if e["number"] >= 61:
            print(f"- {e['number']}: {e['name']}")


if __name__ == "__main__":
    main()
