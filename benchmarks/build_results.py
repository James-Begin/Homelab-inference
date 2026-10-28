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
        "## 1. Certified Protocol C-gpqa-v2 Production Runs (8,192-Token Runway)\n\n",
        "Evaluated on the standardized 50-Question GPQA Diamond subset under strict parsing (`Final answer: X` outside reasoning blocks). Server context size expanded to `-c 16384` with unconstrained `--max-tokens 8192`.\n\n",
        "| Exp | Model | Architecture | Decode t/s | Strict Score | Strict % | Natural Accuracy | Truncated % | Report |\n",
        "| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |\n"
    ]

    # Process certified runs in logs/runs
    certified_dirs = [
        runs_dir / "run_exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv",
        runs_dir / "run_exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv",
    ]

    for cdir in certified_dirs:
        sum_file = cdir / "summary.json"
        if not sum_file.exists():
            continue
        try:
            data = json.loads(sum_file.read_text(encoding="utf-8"))
            exp_id = data.get("experiment_id", cdir.name)
            m = re.search(r"exp(\d+)", exp_id)
            exp_num = m.group(1) if m else "?"

            # Compute natural completion stats if rows exist
            rows_file = cdir / "rows.jsonl"
            nat_acc_str = "-"
            if rows_file.exists():
                rows = [json.loads(line) for line in rows_file.read_text(encoding="utf-8").splitlines() if line.strip()]
                natural = [r for r in rows if r.get("tokens", 0) < data.get("max_tokens_ceiling", 8192)]
                if natural:
                    nat_corr = sum(1 for r in natural if r.get("regraded_strict_correct"))
                    nat_acc_str = f"**{nat_corr}/{len(natural)}** ({nat_corr/len(natural)*100:.1f}%)"
                else:
                    nat_acc_str = "0/0"

            trunc_cnt = data.get("truncated_count", 0)
            total_q = data.get("total_questions", 50)
            trunc_pct = (trunc_cnt / total_q * 100.0) if total_q > 0 else 0.0

            arch = "Qwen 3.6 35B MoE" if "exp50" in exp_id else "Recursive Flint 40B MoE"
            model_name = data.get("model", "")
            tps = data.get("average_decode_tps", 0.0)
            strict_score = data.get("strict_score", "?")
            strict_pct = data.get("strict_pct", 0.0)
            report_link = f"[report]({cdir.relative_to(repo_root)}/report.md)"

            output_lines.append(
                f"| {exp_num} | `{model_name}` | {arch} | {tps:.2f} | **{strict_score}** | **{strict_pct:.1f}%** | {nat_acc_str} | {trunc_pct:.1f}% | {report_link} |\n"
            )
        except Exception as e:
            print(f"Warning: could not process {sum_file}: {e}")

    output_lines.extend([
        "\n## 2. Audited & Regraded Historical Task Evaluations (Runs 66–95)\n\n",
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
        "\n## 3. Standard Controlled Protocols\n\n",
        "- **Protocol A (Controlled Throughput):** Standardized 12-prompt suite, fixed 512 tokens, 5 repetitions, median & IQR.\n",
        "- **Protocol B (Lossless Equivalence):** Greedy token match against reference.\n",
        "- **Protocol Q (Lossy KLD Divergence):** 150K-token reference perplexity shift.\n",
        "- **Protocol C-code (Coding Capabilities):** EvalPlus HumanEval+ pass@1 greedy.\n\n",
        "See [`archive/REGRADED_SUMMARY.md`](archive/REGRADED_SUMMARY.md) for full breakdown of dropped duplicate IDs in historical checkpoints.\n"
    ])

    with open(results_path, "w", encoding="utf-8") as f:
        f.writelines(output_lines)

    print(f"Successfully generated clean {results_path} from certified production runs and {len(regraded_files)} historical regraded runs.")


if __name__ == "__main__":
    build_results_markdown()
