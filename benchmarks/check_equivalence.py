#!/usr/bin/env python3
"""
Protocol B: Speculation Equivalence Verifier (B-equiv-v1)
Implements Phase 3 (Protocol B) of improvement-plan.md.
Tests whether speculative decoding or kernel fusions produce bit-for-bit lossless output under greedy decoding.
"""

import argparse
import json
from pathlib import Path
import sys
import time
import urllib.request
from typing import Any, Dict, List, Optional, Tuple


TEST_PROMPTS = [
    "Write a function in C to reverse a singly linked list in-place.",
    "Calculate the eigenvalues of a 2x2 symmetric matrix [[3, 1], [1, 3]].",
    "Explain why QuickSort has O(n^2) worst-case time complexity.",
    "Derive the relationship between enthalpy and internal energy.",
    "Write a Python generator that yields the Fibonacci sequence up to N.",
    "Explain how virtual memory paging handles page faults in modern operating systems.",
    "State the fundamental theorem of Galois theory and give a brief interpretation.",
    "Write an SQL query to find the second highest salary from an Employee table.",
    "Explain the difference between synchronous and asynchronous I/O multiplexing with epoll.",
    "Describe the working principle of a Kalman filter in discrete time."
]


def query_greedy(url: str, prompt: str, n_predict: int = 128) -> Optional[List[int]]:
    """Requests greedy token generation with token ID output."""
    payload = {
        "prompt": f"<|user|>\n{prompt}\n<|assistant|>\n",
        "n_predict": n_predict,
        "temperature": 0.0,
        "top_p": 1.0,
        "return_tokens": True,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{url}/completion",
        data=data,
        headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            tokens = res.get("tokens")
            if tokens is None and "content" in res:
                # Fallback to string tokenization or tokens field if server returns token strings
                return res.get("content")
            return tokens
    except Exception as e:
        print(f"Error querying {url}: {e}", file=sys.stderr)
        return None


def verify_equivalence(
    ref_url: str,
    cand_url: str,
    n_predict: int = 128,
    out_file: Optional[Path] = None
) -> Dict[str, Any]:
    print(f"Comparing Reference Server ({ref_url}) vs Candidate Server ({cand_url}) across {len(TEST_PROMPTS)} prompts...")
    results = []
    all_identical = True

    for idx, prompt in enumerate(TEST_PROMPTS):
        ref_tokens = query_greedy(ref_url, prompt, n_predict=n_predict)
        cand_tokens = query_greedy(cand_url, prompt, n_predict=n_predict)

        if ref_tokens is None or cand_tokens is None:
            print(f"[{idx+1}/{len(TEST_PROMPTS)}] Prompt {idx+1}: ERROR - Failed to get response")
            all_identical = False
            results.append({
                "prompt_idx": idx,
                "prompt": prompt,
                "identical": False,
                "error": "Server request failed"
            })
            continue

        is_match = (ref_tokens == cand_tokens)
        first_divergence = -1

        if not is_match:
            all_identical = False
            min_len = min(len(ref_tokens), len(cand_tokens))
            for i in range(min_len):
                if ref_tokens[i] != cand_tokens[i]:
                    first_divergence = i
                    break
            if first_divergence == -1:
                first_divergence = min_len

        status_str = "MATCH (Identical)" if is_match else f"DIVERGED at token {first_divergence}"
        print(f"[{idx+1}/{len(TEST_PROMPTS)}] Prompt {idx+1}: {status_str}")

        results.append({
            "prompt_idx": idx,
            "prompt": prompt,
            "identical": is_match,
            "first_divergence_index": first_divergence,
            "ref_token_count": len(ref_tokens),
            "cand_token_count": len(cand_tokens)
        })

    summary = {
        "protocol": "B-equiv-v1",
        "all_identical": all_identical,
        "prompts_tested": len(TEST_PROMPTS),
        "prompts_matching": sum(1 for r in results if r.get("identical")),
        "results": results
    }

    if out_file:
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2)
        print(f"\nWrote equivalence report to {out_file}")

    print("\n=======================================================")
    print(f"PROTOCOL B RESULT: {'PASS (Bit-for-Bit Identical)' if all_identical else 'FAIL (Divergence Detected)'}")
    print(f"Matching Prompts: {summary['prompts_matching']}/{summary['prompts_tested']}")
    print("=======================================================")

    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ref-url", type=str, default="http://127.0.0.1:8087")
    parser.add_argument("--cand-url", type=str, default="http://127.0.0.1:8088")
    parser.add_argument("--n-predict", type=int, default=128)
    parser.add_argument("--out", type=str, default="equiv_report.json")
    args = parser.parse_args()

    verify_equivalence(args.ref_url, args.cand_url, args.n_predict, Path(args.out))
