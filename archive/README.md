# Archive: Historical Notebook (Runs 0–95)

This directory quarantines artifacts, checkpoints, and runners from the exploratory phase of the project (tag `notebook-v1`, commits up to `1d0cd38`).

## 1. Overview and Validity Classification

| Run Series | Status | Scoring Method | Can Regrade? | Throughput Validity |
| :--- | :--- | :--- | :---: | :--- |
| **Runs 0–65** | Quarantined | Lenient regex parser on live stream; full completion text was **not recorded** in checkpoints. | **No** | Mean of variable-length decode rates; not a controlled throughput benchmark. |
| **Runs 66–91** | Audited Historical | Full `content` saved in checkpoints. Strict and lenient parsers evaluated offline. | **Yes** | Variable-length generation speed under 4,096 token ceiling. |
| **Runs 92–95** | Flint Series | Evaluated on Recursive Flint 40B MoE. Runs 94 & 95 port Flint to `ik_llama.cpp` (-muge 1 + repacking). | **Yes** | Controlled comparison against baseline upstream Flint. |

## 2. Key Findings & Known Anomalies

1. **Defect H1 / H2 (Harness Divergence):**
   The runner committed in `benchmarks/gpqa_eval.py` at earlier commits lacked `correct` assignment and hard-coded a 1,536-token ceiling. The actual runners that produced Runs 66–91 and Runs 92–95 have been recovered from the test host and archived in `archive/harness/`.
2. **Defect H5 / Finding 0.3 (Exp 93 Tokenizer Incompatibility):**
   Exp 93 attempted to use `Qwen3.5-0.8B` as an auxiliary speculative draft model for `RecursiveSI_flint-Q4_0.gguf`. Tokenizer inspection confirms Flint uses a 150,144-vocabulary BPE with custom regex (type 52), whereas Qwen uses a 248,320-vocabulary BPE (type 35). Because token representations and IDs are entirely disjoint, draft acceptance was zero, yielding 10.04 t/s (identical to non-speculative baseline).
3. **Anomaly R4 (Run 40/42 Peak Speeds):**
   The peak speeds of 66.30 t/s reported in Runs 40 and 42 were produced by degenerate repetition loops (`<think> The. . . .`) hitting the token ceiling. Under the new protocol, all degenerate outputs are excluded from useful throughput metrics.
4. **Offline Regrading of Runs 66–95:**
   Regraded outputs using the strict regex extractor (`^\s*Final answer:\s*\(?([A-D])\)?\s*$`) and deduplicated question IDs are located in `archive/regraded/`.
