#!/usr/bin/env python3
"""Build RESULTS.md from saved task artifacts and historical regrades."""

import json
from pathlib import Path

from summarize_runs import summarize_coding, summarize_gpqa
from runtime import positive_number

ROOT = Path(__file__).resolve().parent.parent


def format_rate(value):
    return f"{value:.2f}" if positive_number(value) else "unavailable"


def build_results_markdown():
    runs = ROOT / "logs/runs"
    lines = ["# Saved benchmark results\n\n",
             "These are recorded configurations on a Dell PowerEdge T630 with two Xeon E5-2680 v4 CPUs (28 physical cores total) and 256 GB RAM. The current DIMM inventory runs at 1866 MT/s; historical manifests do not establish the DIMM rate for every run.\n\n",
             "No inference or generated code is executed by this report generator. Regenerate derived run reports with `python3 benchmarks/summarize_runs.py --write`, then run `python3 benchmarks/build_results.py`.\n\n",
             "## Coding\n\n",
             "Each run contains one completion per HumanEval task. HumanEval+ success requires **both base and extra tests**. Earlier reports counted extra tests alone (107 Qwen, 149 Flint); the corrected counts are 106 and 148. Raw samples and EvalPlus result files are unchanged.\n\n",
             "| Run | Model | Base passed | Base + extra passed | Mean decode tokens/s | Mean request s | Sum request min | Report |\n",
             "| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |\n"]
    for directory in sorted(runs.glob("code_exp*")):
        if not (directory / "samples_eval_results.json").exists():
            continue
        summary = summarize_coding(directory)
        n = summary["total_problems"]
        link = directory.relative_to(ROOT).as_posix()
        lines.append(f"| {summary['experiment_id']} | `{summary['model']}` | {summary['base_pass_count']}/{n} | {summary['plus_pass_count']}/{n} | {format_rate(summary['average_decode_tps'])} | {summary['avg_wall_time_per_task_sec']:.2f} | {summary['total_wall_time_sec']/60:.1f} | [report]({link}/report.md) |\n")
    lines.extend(["\nMean request times include failed tasks. Decode rate is an arithmetic mean of finite positive saved rates for completions longer than one token. Qwen uses 163 timing rows: `HumanEval/111` generated one token with a saved rate of 1,000,000 tokens/s and is excluded from the rate mean. All 164 tasks remain in pass counts and elapsed times. Flint uses all 164 timing rows. Elapsed time and test success measure different things. The models use different quantization, prompts, extraction and serving settings. These runs compare the local pipelines; they do not isolate model architecture or individual patch gains.\n\n",
                  "## GPQA Diamond subset\n\n",
                  "The saved subset has 50 questions. Strict grading accepts an explicit final-answer line or boxed letter outside reasoning tags; a lenient parser is retained for comparison. Scores below retain the recorded grading flags.\n\n",
                  "| Run | Output ceiling | Mean decode tokens/s | Strict score | Lenient score | Token-limit rows | No final answer at truncation | Report |\n",
                  "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |\n"])
    for directory in sorted(runs.glob("run_exp*")):
        if not directory.is_dir() or not (directory / "rows.jsonl").exists():
            continue
        summary = summarize_gpqa(directory)
        link = directory.relative_to(ROOT).as_posix()
        lines.append(f"| {directory.name.removeprefix('run_')} | {summary['max_tokens_ceiling']:,} | {format_rate(summary['average_decode_tps'])} | {summary['strict_score']} | {summary['lenient_score']} | {summary['token_limit_count']}/{summary['total_questions']} | {summary['truncated_count']}/{summary['total_questions']} | [report]({link}/report.md) |\n")
    lines.extend(["\nToken-limit rows reached the recorded output ceiling or report `finish_reason=length`. A final answer can still appear in such a row, so this count differs from no-answer truncations. Older rows lack raw stopping flags; responses below the ceiling are not established natural completions.\n\n",
                  "## Historical regrades\n\n",
                  "These regrades audit saved answers from the earlier exploratory runs. They do not establish controlled throughput, output equivalence, or an isolated optimization effect. [Archived notebook](archive/README.md) retains the original observations and their limits.\n\n",
                  "| Run | Unique questions | Strict score | Lenient score | Source regrade |\n",
                  "| --- | ---: | ---: | ---: | --- |\n"])
    for path in sorted((ROOT / "archive/regraded").glob("*.json")):
        data = json.loads(path.read_text())
        run_id = data.get("run_id", path.stem)
        lines.append(f"| `{run_id}` | {data.get('unique_questions', '?')} | {data.get('strict_score', '?')} | {data.get('lenient_score', '?')} | [JSON]({path.relative_to(ROOT).as_posix()}) |\n")
    lines.append("\nSee [evaluation methods](docs/eval-protocol.md) and [historical deduplication](archive/REGRADED_SUMMARY.md). Throughput, token-equivalence and KL-divergence tools are available, but the presence of a tool is not a completed validation result.\n")
    (ROOT / "RESULTS.md").write_text("".join(lines))
    print("Wrote RESULTS.md from saved artifacts.")


if __name__ == "__main__":
    build_results_markdown()
