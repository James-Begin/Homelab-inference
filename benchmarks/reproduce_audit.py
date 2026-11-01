#!/usr/bin/env python3
"""Check saved artifacts without starting inference or executing generated code."""

import argparse
import json
from pathlib import Path
import sys

from catalog import load_catalog
from summarize_runs import summarize_coding, summarize_gpqa


def audit(repo):
    catalog = load_catalog(repo / "benchmarks/experiments.json")
    print(f"Catalog: {len(catalog)} unique experiment entries")
    failures = []
    checked = 0
    for run_dir in sorted((repo / "logs/runs").iterdir()):
        if not run_dir.is_dir() or not (run_dir / "rows.jsonl").exists() or not (run_dir / "summary.json").exists():
            continue
        if run_dir.name.startswith("code_"):
            derived = summarize_coding(run_dir)
            keys = ("total_problems", "base_pass_count", "plus_pass_count", "extra_only_pass_count", "base_pass_pct", "plus_pass_pct", "average_decode_tps", "total_wall_time_sec", "avg_wall_time_per_task_sec", "valid_timing_rows", "invalid_timing_rows", "aggregation", "derived_from")
            print(f"{run_dir.name}: base {derived['base_pass_count']}/{derived['total_problems']}, base+extra {derived['plus_pass_count']}/{derived['total_problems']}")
        elif run_dir.name.startswith("run_exp"):
            derived = summarize_gpqa(run_dir)
            keys = ("total_questions", "strict_score", "lenient_score", "truncated_count", "token_limit_count", "at_or_above_ceiling_count", "strict_pct", "lenient_pct", "average_decode_tps", "valid_timing_rows", "invalid_timing_rows", "derived_from")
            print(f"{run_dir.name}: strict {derived['strict_score']}, token-limit rows {derived['token_limit_count']}")
        else:
            continue
        saved = json.loads((run_dir / "summary.json").read_text())
        for key in keys:
            if saved.get(key) != derived[key]:
                failures.append(f"{run_dir.name}/{key}: saved {saved.get(key)!r}, reconstructed {derived[key]!r}")
        if not (run_dir / "manifest.json").exists():
            failures.append(f"{run_dir.name}: missing original manifest")
        checked += 1
    if checked == 0:
        failures.append("No supported saved runs found")
    if failures:
        print("\nArtifact mismatches:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print(f"Verified {checked} derived task summaries. Raw artifacts were read only.")
    print("This checks saved records and aggregation; it does not reproduce inference or certify model outputs.")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", type=Path, nargs="?", default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    try:
        return audit(args.repo.resolve())
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"Artifact audit failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
