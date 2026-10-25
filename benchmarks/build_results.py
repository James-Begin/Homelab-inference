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
    results_path = repo_root / "RESULTS.md"

    regraded_files = sorted(regraded_dir.glob("*.json"))

    output_lines = [
        "# Inference Benchmark Results\n",
        "Dual Intel Xeon E5-2680 v4 (28 physical cores, Broadwell AVX2), 256 GB DDR4-2400 NUMA.\n",
        "All measurements adhere to the certified protocols defined in [`docs/eval-protocol.md`](docs/eval-protocol.md).\n",
        "Historical exploratory runs (Runs 0–65) are archived in [`archive/README.md`](archive/README.md).\n\n",
        "## 1. Audited & Regraded Task Evaluations (Runs 66–95)\n\n",
        r"Evaluated on the 50-Question GPQA Diamond subset under strict parsing (`^\s*Final answer:\s*\(?([A-D])\)?\s*$`). Text within reasoning blocks is excluded; unclosed chains of thought evaluate strictly to `None`.\n\n",
        "| Run | Experiment ID | Unique Qs | Strict Score | Strict % | Lenient % | Report |\n",
        "| :---: | :--- | :---: | :---: | :---: | :---: | :---: |\n"
    ]

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

        report_link = f"[report](logs/gpqa_reports/gpqa_{run_id}_50q_report.md)"
        output_lines.append(
            f"| {run_num} | `{run_id}` | {uniq} | **{strict_score}** | **{strict_pct:.1f}%** | {lenient_pct:.1f}% | {report_link} |\n"
        )

    output_lines.extend([
        "\n## 2. Standard Controlled Protocols\n\n",
        "- **Protocol A (Controlled Throughput):** Standardized 12-prompt suite, fixed 512 tokens, 5 repetitions, median & IQR.\n",
        "- **Protocol B (Lossless Equivalence):** Greedy token match against reference.\n",
        "- **Protocol Q (Lossy KLD Divergence):** 150K-token reference perplexity shift.\n",
        "- **Protocol C-code (Coding Capabilities):** EvalPlus HumanEval+ pass@1 greedy.\n\n",
        "See [`archive/REGRADED_SUMMARY.md`](archive/REGRADED_SUMMARY.md) for full breakdown of dropped duplicate IDs in historical checkpoints.\n"
    ])

    with open(results_path, "w", encoding="utf-8") as f:
        f.writelines(output_lines)

    print(f"Successfully generated clean {results_path} from {len(regraded_files)} certified runs.")


if __name__ == "__main__":
    build_results_markdown()
