#!/usr/bin/env python3
"""Rebuild derived reports from saved rows and EvalPlus results; never run samples."""

import argparse
import json
from pathlib import Path
import statistics

from runtime import positive_number


def load_rows(path, id_key):
    rows = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
    ids = [row[id_key] for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError(f"Duplicate {id_key} in {path}")
    return rows


HUMANEVAL_IDS = frozenset(f"HumanEval/{index}" for index in range(164))
GPQA_SUBSET = Path(__file__).resolve().parent / "data/gpqa_subset_50.json"


def validate_complete_run(actual_ids, expected_ids, label):
    actual = set(actual_ids)
    expected = set(expected_ids)
    if not expected or len(expected_ids) != len(expected) or actual != expected:
        missing = sorted(expected - actual)
        unexpected = sorted(actual - expected)
        raise ValueError(f"Incomplete {label} task set: {len(actual)}/{len(expected)} expected IDs; missing {missing[:5]}, unexpected {unexpected[:5]}")


def gpqa_expected_ids(run_dir):
    manifest = json.loads((run_dir / "manifest.json").read_text())
    if manifest.get("schema_version") == 2:
        expected = manifest.get("dataset_ids")
        prompts = manifest.get("request", {}).get("prompts", {})
        digest = manifest.get("dataset_sha256")
        if not isinstance(expected, list) or not expected or not isinstance(digest, str) or len(digest) != 64:
            raise ValueError("GPQA manifest lacks dataset IDs or full dataset identity")
        validate_complete_run(prompts, expected, "GPQA request")
        return expected
    dataset = json.loads(GPQA_SUBSET.read_text())
    if len(dataset) != 50:
        raise ValueError("Published GPQA subset must contain 50 questions")
    return [question["id"] for question in dataset]


def coding_scores(eval_data, expected_ids):
    evaluations = eval_data.get("eval", {})
    if set(evaluations) != set(expected_ids):
        raise ValueError("EvalPlus task IDs differ from generated task IDs")
    base = combined = extra_only = 0
    for task_id in expected_ids:
        samples = evaluations[task_id]
        if len(samples) != 1:
            raise ValueError(f"Expected one completion for {task_id}")
        result = samples[0]
        if result.get("base_status") not in ("pass", "fail") or result.get("plus_status") not in ("pass", "fail"):
            raise ValueError(f"Missing or unsupported result status for {task_id}")
        base_ok = result["base_status"] == "pass"
        extra_ok = result["plus_status"] == "pass"
        base += base_ok
        extra_only += extra_ok
        combined += base_ok and extra_ok
    total = len(expected_ids)
    if total == 0:
        raise ValueError("No evaluated tasks")
    return {"base_pass_count": base, "plus_pass_count": combined, "extra_only_pass_count": extra_only,
            "base_pass_pct": round(100 * base / total, 2), "plus_pass_pct": round(100 * combined / total, 2)}


def timing_summary(rows):
    # A one-token completion provides no interval between decoded tokens.
    speeds = [row.get("speed_tps") for row in rows if positive_number(row.get("speed_tps")) and positive_number(row.get("tokens")) and row["tokens"] > 1]
    return {"average_decode_tps": round(statistics.mean(speeds), 2) if speeds else None,
            "valid_timing_rows": len(speeds), "invalid_timing_rows": len(rows) - len(speeds),
            "timing_filter": "Finite positive saved rate and more than one generated token"}


def write_coding_report(run_dir, summary):
    n = summary["total_problems"]
    text = f"""# Coding results: {summary['experiment_id']}

Saved run: `{summary['run_id']}`. Model: `{summary['model']}`.

| Metric | Result |
| --- | ---: |
| HumanEval base | {summary['base_pass_count']}/{n} ({summary['base_pass_pct']:.2f}%) |
| HumanEval+ (base and extra) | {summary['plus_pass_count']}/{n} ({summary['plus_pass_pct']:.2f}%) |
| Mean decode rate | {summary['average_decode_tps']} tokens/s |
| Mean request elapsed time | {summary['avg_wall_time_per_task_sec']} s |
| Sum of request elapsed times | {summary['total_wall_time_sec']} s |

Elapsed times include failed tasks. Decode rates use {summary['valid_timing_rows']} saved timing rows and exclude {summary['invalid_timing_rows']} rows. A rate must be finite and positive, with more than one generated token. Startup is excluded.

These are local end-to-end configurations, with different quantization, prompting, extraction and serving settings. They do not isolate model architecture or an individual patch.

Regenerated from `rows.jsonl` and `samples_eval_results.json` with `python3 benchmarks/summarize_runs.py --write`. The earlier report counted extra tests alone ({summary['extra_only_pass_count']}/{n}); HumanEval+ here requires both base and extra tests. Raw rows, samples, results and manifests are unchanged.
"""
    (run_dir / "report.md").write_text(text)


def summarize_coding(run_dir, write=False):
    summary_path = run_dir / "summary.json"
    summary = json.loads(summary_path.read_text()) if summary_path.exists() else {}
    rows = load_rows(run_dir / "rows.jsonl", "task_id")
    validate_complete_run([row["task_id"] for row in rows], HUMANEVAL_IDS, "HumanEval+")
    sample_rows = load_rows(run_dir / "samples.jsonl", "task_id")
    samples = {r["task_id"]: r["solution"] for r in sample_rows}
    if samples != {r["task_id"]: r["solution"] for r in rows}:
        raise ValueError(f"Samples and row solutions differ: {run_dir}")
    eval_data = json.loads((run_dir / "samples_eval_results.json").read_text())
    for task_id, solution in samples.items():
        evaluations = eval_data.get("eval", {}).get(task_id, [])
        if len(evaluations) != 1 or evaluations[0].get("solution") != solution:
            raise ValueError(f"EvalPlus result is stale or incomplete for {task_id}: {run_dir}")
    summary.update(coding_scores(eval_data, [r["task_id"] for r in rows]))
    summary.update(timing_summary(rows))
    total_wall = sum(r["wall_time"] for r in rows)
    summary.update({"total_problems": len(rows), "total_wall_time_sec": round(total_wall, 1),
                    "avg_wall_time_per_task_sec": round(total_wall / len(rows), 2),
                    "aggregation": "base_status == pass AND plus_status == pass",
                    "derived_from": ["rows.jsonl", "samples.jsonl", "samples_eval_results.json"],
                    "regeneration": "benchmarks/summarize_runs.py"})
    if write:
        summary_path.write_text(json.dumps(summary, indent=2) + "\n")
        write_coding_report(run_dir, summary)
    return summary


def summarize_gpqa(run_dir, write=False):
    summary_path = run_dir / "summary.json"
    summary = json.loads(summary_path.read_text())
    rows = load_rows(run_dir / "rows.jsonl", "id")
    validate_complete_run([str(row["id"]) for row in rows], gpqa_expected_ids(run_dir), "GPQA")
    n = len(rows)
    strict = sum(r.get("regraded_strict_correct", r.get("pred") == r.get("gold")) is True for r in rows)
    lenient = sum(r.get("regraded_lenient_correct", r.get("lenient_pred") == r.get("gold")) is True for r in rows)
    ceiling = summary["max_tokens_ceiling"]
    cap = sum(r.get("max_tokens_hit") is True or r.get("finish_reason") == "length" or r.get("tokens", 0) >= ceiling for r in rows)
    no_answer = sum(r.get("status") == "no_answer_truncated" for r in rows)
    summary.update({"total_questions": n, "strict_score": f"{strict}/{n}", "strict_pct": round(100 * strict/n, 2),
                    "lenient_score": f"{lenient}/{n}", "lenient_pct": round(100 * lenient/n, 2),
                    "truncated_count": no_answer, "token_limit_count": cap, "at_or_above_ceiling_count": sum(r.get("tokens", 0) >= ceiling for r in rows),
                    "derived_from": ["rows.jsonl"], "regeneration": "benchmarks/summarize_runs.py"})
    summary.update(timing_summary(rows))
    if write:
        summary_path.write_text(json.dumps(summary, indent=2) + "\n")
        lines = [f"# GPQA results: {summary['experiment_id']}\n\n",
                 f"Saved run: `{summary['run_id']}`. Model: `{summary['model']}`. Ceiling: {ceiling:,} output tokens.\n\n",
                 f"Strict score: **{strict}/{n}** ({summary['strict_pct']:.1f}%). Lenient audit: {lenient}/{n}.\n\n",
                 f"Mean saved decode rate: {summary['average_decode_tps']} tokens/s across {summary['valid_timing_rows']} timing rows; {summary['invalid_timing_rows']} excluded. Rates must be finite and positive, with more than one generated token.\n\n",
                 f"{cap}/{n} rows reached the recorded token ceiling or reported a length stop. {no_answer}/{n} rows were recorded as having no final answer at truncation. These are different counts. Older rows lack raw stopping flags, so a below-ceiling response is not proof of a natural stop.\n\n",
                 "Regenerated from saved rows with `python3 benchmarks/summarize_runs.py --write`; recorded answers and grading flags are retained. Raw rows and manifests are unchanged.\n\n",
                 "| ID | Gold | Pred | Recorded status | Tokens | Decode tokens/s | Request s |\n",
                 "| --- | --- | --- | --- | ---: | ---: | ---: |\n"]
        for row in rows:
            lines.append(f"| `{row['id']}` | {row['gold']} | {row.get('pred') or '-'} | {row.get('status', '-')} | {row.get('tokens', 0)} | {row.get('speed_tps')} | {row.get('wall_time')} |\n")
        (run_dir / "report.md").write_text("".join(lines))
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Replace derived summary.json/report.md only")
    parser.add_argument("--runs-dir", type=Path, default=Path(__file__).resolve().parent.parent / "logs/runs")
    args = parser.parse_args()
    for run_dir in sorted(args.runs_dir.iterdir()):
        if not run_dir.is_dir() or not (run_dir / "rows.jsonl").exists() or not (run_dir / "summary.json").exists():
            continue
        if run_dir.name.startswith("code_"):
            summary = summarize_coding(run_dir, args.write)
            print(f"{run_dir.name}: base {summary['base_pass_count']}/{summary['total_problems']}; base+extra {summary['plus_pass_count']}/{summary['total_problems']}")
        elif run_dir.name.startswith("run_exp"):
            summary = summarize_gpqa(run_dir, args.write)
            print(f"{run_dir.name}: strict {summary['strict_score']}; token limit {summary['token_limit_count']}")


if __name__ == "__main__":
    main()
