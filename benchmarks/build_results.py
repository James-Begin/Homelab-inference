#!/usr/bin/env python3
"""
Automated Results Generator
Implements Phase 1.5 of improvement-plan.md:
Generates RESULTS.md from certified protocol summary files and regraded archives.
"""

import json
from pathlib import Path
import re
import sys


def build_results_markdown():
    repo_root = Path(__file__).resolve().parent.parent
    regraded_dir = repo_root / "archive" / "regraded"
    runs_dir = repo_root / "logs" / "runs"
    results_path = repo_root / "RESULTS.md"

    regraded_files = sorted(regraded_dir.glob("*.json"))

    output_lines = [
        "# Inference Benchmark Results\n\n",
        "Dual Intel Xeon E5-2680 v4 (28 physical cores, Broadwell AVX2), 256 GB DDR4-2400 NUMA.\n",
        "All measurements adhere to the certified protocols defined in [`docs/eval-protocol.md`](docs/eval-protocol.md).\n",
        "Historical exploratory runs (Runs 0–65) are archived in [`archive/README.md`](archive/README.md).\n\n",
        "## 1. Certified Protocol C-code-v1 Coding Suite (EvalPlus HumanEval+ 164 Problems)\n\n",
        "Evaluated on the full 164 coding tasks using the EvalPlus sandbox verification suite (`evalplus` v0.3.1). Pass@1 greedy decoding with full physical core pinning and NUMA interleaving.\n\n",
        "| Exp | Model | Architecture | Base Pass@1 | Plus Pass@1 | Decode Speed | Avg Time / Task | Total Time | Report |\n",
        "| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |\n"
    ]

    code_runs = [
        ("50", runs_dir / "code_exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv", "Qwen 3.6 35B MoE"),
        ("94", runs_dir / "code_exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv", "Recursive Flint 40B MoE"),
    ]

    for exp_num, cdir, arch in code_runs:
        sum_file = cdir / "summary.json"
        if not sum_file.exists():
            continue
        try:
            d = json.loads(sum_file.read_text(encoding="utf-8"))
            model_name = d.get("model", "")
            base_pass = d.get("base_pass_pct", 0.0)
            plus_pass = d.get("plus_pass_pct", 0.0)
            tps = d.get("average_decode_tps", 0.0)
            avg_time = d.get("avg_wall_time_per_task_sec", 0.0)
            total_sec = d.get("total_wall_time_sec", 0.0)
            total_min = total_sec / 60.0
            report_link = f"[report]({cdir.relative_to(repo_root)}/report.md)"

            output_lines.append(
                f"| {exp_num} | `{model_name}` | {arch} | **{base_pass:.1f}%** | **{plus_pass:.1f}%** | {tps:.2f} t/s | {avg_time:.1f}s | {total_min:.1f} min | {report_link} |\n"
            )
        except Exception as e:
            print(f"Warning: could not process {sum_file}: {e}")

    output_lines.extend([
        "\n## 2. Certified Protocol C-gpqa-v2 Reasoning Suite: 8K vs. 16K Runway Scaling\n\n",
        "Evaluated on the standardized 50-Question GPQA Diamond subset under strict parsing (`Final answer: X` outside reasoning blocks) and audited lenient parsing. Comparing 8,192-token runway (`-c 16384`) vs. 16,384-token runway (`-c 32768`).\n\n",
        "| Exp | Model | Runway | Decode t/s | Strict Score | Strict % | Lenient % | Natural Completions | Truncated % | Report |\n",
        "| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n"
    ])

    gpqa_runs = [
        ("50", runs_dir / "run_exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv", "8K (8,192)", "Qwen 3.6 35B MoE"),
        ("50", runs_dir / "run_exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv_16k_runway", "16K (16,384)", "Qwen 3.6 35B MoE"),
        ("94", runs_dir / "run_exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv", "8K (8,192)", "Recursive Flint 40B MoE"),
        ("94", runs_dir / "run_exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv_16k_runway", "16K (16,384)", "Recursive Flint 40B MoE"),
    ]

    for exp_num, cdir, runway_str, arch in gpqa_runs:
        sum_file = cdir / "summary.json"
        if not sum_file.exists():
            continue
        try:
            d = json.loads(sum_file.read_text(encoding="utf-8"))
            model_name = d.get("model", "")
            tps = d.get("average_decode_tps", 0.0)
            strict_score = d.get("strict_score", "?")
            strict_pct = d.get("strict_pct", 0.0)
            lenient_pct = d.get("lenient_pct", 0.0)
            trunc_cnt = d.get("truncated_count", 0)
            total_q = d.get("total_questions", 50)
            trunc_pct = (trunc_cnt / total_q * 100.0) if total_q > 0 else 0.0

            rows_file = cdir / "rows.jsonl"
            nat_str = "-"
            if rows_file.exists():
                rows = [json.loads(line) for line in rows_file.read_text(encoding="utf-8").splitlines() if line.strip()]
                ceil_tok = d.get("max_tokens_ceiling", 8192)
                natural = [r for r in rows if r.get("tokens", 0) < ceil_tok]
                if natural:
                    nat_corr = sum(1 for r in natural if r.get("regraded_strict_correct") or r.get("pred") == r.get("gold"))
                    nat_str = f"**{nat_corr}/{len(natural)}** ({nat_corr/len(natural)*100:.1f}%)"
                else:
                    nat_str = "0/0"

            report_link = f"[report]({cdir.relative_to(repo_root)}/report.md)"

            output_lines.append(
                f"| {exp_num} | `{model_name}` | {runway_str} | {tps:.2f} | **{strict_score}** | **{strict_pct:.1f}%** | {lenient_pct:.1f}% | {nat_str} | {trunc_pct:.1f}% | {report_link} |\n"
            )
        except Exception as e:
            print(f"Warning: could not process {sum_file}: {e}")

    output_lines.extend([
        "\n## 3. Audited & Regraded Historical Task Evaluations (Runs 66–95)\n\n",
        "Evaluated on the 50-Question GPQA Diamond subset under strict parsing (`^\\s*Final answer:\\s*\\(?([A-D])\\)?\\s*$`). Text within reasoning blocks is excluded; unclosed chains of thought evaluate strictly to `None`.\n\n",
        "| Run | Experiment ID | Unique Qs | Strict Score | Strict % | Lenient % | Report |\n",
        "| :---: | :--- | :---: | :---: | :---: | :---: | :---: |\n"
    ])

    for rf in regraded_files:
        try:
            with open(rf, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            continue

        run_id = data.get("run_id", rf.stem)
        m = re.search(r"exp(\d+)", run_id)
        run_num = m.group(1) if m else "?"

        uniq = data.get("unique_questions", 50)
        strict_score = data.get("strict_score", "?")
        strict_pct = data.get("strict_pct", 0.0)
        lenient_score = data.get("lenient_score", "?")
        try:
            l_num, l_den = map(int, lenient_score.split("/"))
            lenient_pct = (l_num / l_den * 100.0) if l_den > 0 else 0.0
        except Exception:
            lenient_pct = 0.0

        report_link = f"[report](archive/notebook-v1/gpqa_reports/gpqa_{run_id}_50q_report.md)"
        output_lines.append(
            f"| {run_num} | `{run_id}` | {uniq} | **{strict_score}** | **{strict_pct:.1f}%** | {lenient_pct:.1f}% | {report_link} |\n"
        )

    output_lines.extend([
        "\n## 4. Standard Controlled Protocols\n\n",
        "- **Protocol A (Controlled Throughput):** Standardized 12-prompt suite, fixed 512 tokens, 5 repetitions, median & IQR.\n",
        "- **Protocol B (Lossless Equivalence):** Greedy token match against reference.\n",
        "- **Protocol Q (Lossy KLD Divergence):** 150K-token reference perplexity shift.\n",
        "- **Protocol C-code (Coding Capabilities):** EvalPlus HumanEval+ pass@1 greedy.\n",
        "- **Protocol C-gpqa (Scientific Reasoning):** GPQA Diamond 50 questions strict parsing.\n\n",
        "See [`archive/REGRADED_SUMMARY.md`](archive/REGRADED_SUMMARY.md) for full breakdown of dropped duplicate IDs in historical checkpoints.\n"
    ])

    with open(results_path, "w", encoding="utf-8") as f:
        f.writelines(output_lines)

    print(f"Successfully generated clean {results_path} from certified production runs and {len(regraded_files)} historical regraded runs.")


if __name__ == "__main__":
    build_results_markdown()
