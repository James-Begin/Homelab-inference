#!/usr/bin/env python3
"""
Offline Regrading of Historical Runs (Runs 66–95)
Implements Phase 2.1 of improvement-plan.md:
Deduplicates by ID, evaluates strict vs lenient extraction, and writes archive/regraded/<run>.json.
"""

import json
from pathlib import Path
import re
import sys

# Ensure benchmarks module can be imported
sys.path.insert(0, str(Path(__file__).resolve().parent))

from grading import (
    RowStatus,
    extract_answer_lenient,
    extract_answer_strict,
    grade_response,
)


def regrade_all_historical_runs():
    repo_root = Path(__file__).resolve().parent.parent
    checkpoints_dir = repo_root / "logs" / "raw_checkpoints"
    out_dir = repo_root / "archive" / "regraded"
    out_dir.mkdir(parents=True, exist_ok=True)

    checkpoint_files = sorted(checkpoints_dir.glob("exp*.json"))

    print("==========================================================================================================")
    print(f"{'Run ID':<45} | {'Rows':<5} | {'Uniq':<5} | {'Dup':<4} | {'Orig Score':<12} | {'Lenient':<10} | {'Strict':<10} | {'Strict %':<8}")
    print("==========================================================================================================")

    summary_records = []

    for cp_path in checkpoint_files:
        # Determine run number from filename
        m = re.search(r"exp(\d+)", cp_path.stem)
        if not m:
            continue
        run_num = int(m.group(1))
        # Filter for runs 66 and above (runs with saved full content)
        if run_num < 66:
            continue

        try:
            with open(cp_path, "r", encoding="utf-8") as f:
                rows = json.load(f)
        except Exception as e:
            print(f"Error loading {cp_path.name}: {e}")
            continue

        if not isinstance(rows, list) or len(rows) == 0:
            continue

        # Check if rows have content
        has_content = any("content" in r and r["content"] for r in rows)
        if not has_content:
            continue

        seen_ids = set()
        dedup_rows = []
        dup_count = 0

        for r in rows:
            qid = r.get("id") or f"idx_{r.get('idx')}"
            if qid in seen_ids:
                dup_count += 1
                continue
            seen_ids.add(qid)
            dedup_rows.append(r)

        regraded_rows = []
        strict_correct = 0
        lenient_correct = 0
        orig_correct = sum(1 for r in dedup_rows if r.get("correct") is True)

        for r in dedup_rows:
            content = r.get("content", "")
            gold = r.get("gold") or r.get("gold_choice") or ""
            tokens = r.get("tokens", 0)
            is_length_truncated = (tokens >= 4096 or tokens == 1536) and ("</think>" not in content)

            status, strict_ans, lenient_ans = grade_response(
                content=content,
                gold=gold,
                max_tokens_hit=is_length_truncated
            )

            is_strict = (status == RowStatus.CORRECT)
            is_lenient = (lenient_ans is not None and lenient_ans.upper() == gold.upper())

            if is_strict:
                strict_correct += 1
            if is_lenient:
                lenient_correct += 1

            regraded_entry = dict(r)
            regraded_entry["regraded_status"] = status.value
            regraded_entry["regraded_strict_answer"] = strict_ans
            regraded_entry["regraded_lenient_answer"] = lenient_ans
            regraded_entry["regraded_strict_correct"] = is_strict
            regraded_entry["regraded_lenient_correct"] = is_lenient
            regraded_rows.append(regraded_entry)

        total_unique = len(dedup_rows)
        strict_pct = (strict_correct / total_unique * 100.0) if total_unique > 0 else 0.0

        # Save to archive/regraded/
        out_file = out_dir / cp_path.name
        with open(out_file, "w", encoding="utf-8") as out_f:
            json.dump({
                "run_id": cp_path.stem,
                "total_rows": len(rows),
                "unique_questions": total_unique,
                "duplicates_dropped": dup_count,
                "strict_score": f"{strict_correct}/{total_unique}",
                "strict_pct": round(strict_pct, 2),
                "lenient_score": f"{lenient_correct}/{total_unique}",
                "original_score": f"{orig_correct}/{total_unique}",
                "rows": regraded_rows
            }, out_f, indent=2)

        short_id = cp_path.stem[:45]
        print(f"{short_id:<45} | {len(rows):<5} | {total_unique:<5} | {dup_count:<4} | {orig_correct}/{total_unique:<8} | {lenient_correct}/{total_unique:<6} | {strict_correct}/{total_unique:<6} | {strict_pct:>6.1f}%")

        summary_records.append({
            "run_id": cp_path.stem,
            "total_rows": len(rows),
            "unique": total_unique,
            "duplicates": dup_count,
            "orig_correct": orig_correct,
            "lenient_correct": lenient_correct,
            "strict_correct": strict_correct,
            "strict_pct": strict_pct
        })

    print("==========================================================================================================")
    print(f"Successfully regraded and archived {len(summary_records)} historical runs into {out_dir}")

    # Write summary table into archive/README.md
    summary_path = repo_root / "archive" / "REGRADED_SUMMARY.md"
    with open(summary_path, "w", encoding="utf-8") as sf:
        sf.write("# Regraded Historical Scores (Runs 66–95)\n\n")
        sf.write("| Run ID | Rows | Unique | Dropped Dups | Orig Score | Lenient Regrade | Strict Regrade | Strict % |\n")
        sf.write("| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n")
        for rec in summary_records:
            sf.write(f"| `{rec['run_id']}` | {rec['total_rows']} | {rec['unique']} | {rec['duplicates']} | {rec['orig_correct']}/{rec['unique']} | {rec['lenient_correct']}/{rec['unique']} | **{rec['strict_correct']}/{rec['unique']}** | **{rec['strict_pct']:.1f}%** |\n")

    print(f"Saved summary markdown to {summary_path}")


if __name__ == "__main__":
    regrade_all_historical_runs()
