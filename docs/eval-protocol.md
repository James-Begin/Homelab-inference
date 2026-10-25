# Evaluation Protocols Specification

Status: Certified. Implemented per [`improvement-plan.md`](../improvement-plan.md) (Phase 3).

## 1. Principles

1. **Decoupled Speed and Accuracy:** Throughput is evaluated via fixed-length generation on standardized prompts across multiple context depths. Task accuracy is evaluated on verifiable datasets without speed confounds.
2. **Lossless vs. Lossy Gating:**
   - **Lossless optimizations** (speculative decoding, NUMA core pinning, memory interleaving, row repacking, merged expert GEMMs) must pass **Protocol B** (exact equivalence under greedy decoding).
   - **Lossy optimizations** (weight quantization recipes, KV quantization, expert pruning, SER) must be characterized under **Protocol Q** (Kullback-Leibler divergence).
3. **Statistical Uncertainty:** Throughput reports median and interquartile range (IQR) across $\ge 5$ randomized repetitions. Accuracy reports Wilson 95% confidence intervals and paired McNemar statistics.

---

## 2. Protocol A: Controlled Throughput (`A-tput-v1`)

- **Script:** [`benchmarks/bench_throughput.py`](../benchmarks/bench_throughput.py)
- **Workload:** 12 standardized prompts across 3 distinct classes (`benchmarks/prompts/tput/`):
  1. `code_edit` (4 prompts): Real-world repository diffs and modification requests.
  2. `code_gen` (4 prompts): Algorithmic synthesis, unit test generation, and parser creation.
  3. `prose_reasoning` (4 prompts): Scientific derivation, mathematical proofs, and logic puzzles.
- **Generation Length:** Fixed `n_predict = 512` with `ignore_eos: true` (ensuring equal token counts across runs) alongside natural stopping.
- **Context Depths:** Evaluated at 2,048, 8,192, and 32,768 prompt tokens.
- **Repetitions:** 5 randomized repetitions per (prompt × context depth) with one discarded warm-up.
- **Metrics Collected:**
  - Decode speed (tokens/sec): $\frac{\sum \text{tokens}}{\sum \text{eval\_time}}$
  - Prefill speed (tokens/sec): $\frac{\sum \text{prompt\_tokens}}{\sum \text{prefill\_time}}$
  - Time To First Token (TTFT, ms)
  - Speculative draft acceptance rate ($\%$) and mean accepted sequence length
  - Peak RSS memory footprint (MB)
  - Token-weighted aggregate throughput (excluding degenerate repetition loops)

---

## 3. Protocol B: Speculation Equivalence (`B-equiv-v1`)

- **Script:** [`benchmarks/check_equivalence.py`](../benchmarks/check_equivalence.py)
- **Objective:** Certify that speculative draft generation, `-muge 1`, and matrix repacking produce lossless output identical to the baseline reference model.
- **Execution:**
  - Greedy decoding ($T = 0.0$, $\text{top\_p} = 1.0$, fixed seed).
  - Identical model weights, KV cache precision, and vocabulary pre-tokenizer.
  - Generates 10 standardized 256-token outputs.
- **Verification Rule:**
  - **Pass (Exact Match):** Output token IDs are $100\%$ identical to reference.
  - **Pass (Near-Tie Divergence):** Divergence occurs only where the reference top-2 logit margin is $< 0.05$ nats (attributable to floating-point reduction order in batched BLAS).
  - **Fail (Defect):** Divergence occurs at a significant margin, identifying KV rollback or verifier state corruption.

---

## 4. Protocol Q: Divergence for Lossy Changes (`Q-kld-v1`)

- **Script:** [`benchmarks/kld.sh`](../benchmarks/kld.sh)
- **Objective:** Low-noise, reproducible perplexity and distribution shift measurement for quantization and pruning changes.
- **Corpus:** 150,000 tokens consisting of:
  - 100,000 tokens of multi-language source code (held-out from benchmarks).
  - 50,000 tokens of Wikitext-2 test partition.
- **Reference Baseline:** Unquantized BF16 or Q8_0 weights computed via `llama-perplexity --kl-divergence-base ref.kld`.
- **Metrics:**
  - Mean KL Divergence
  - 99th-percentile KL Divergence ($p99$)
  - Top-1 token prediction agreement ($\%$)
  - Perplexity delta ($\Delta\text{PPL}$)

---

## 5. Protocol C: Task Accuracy (`C-code-v1`, `C-gpqa-v2`)

- **C-code-v1 (Primary Coding Assistant Benchmark):**
  - **Dataset:** EvalPlus HumanEval+ (164 coding tasks), pass@1 greedy.
  - **Execution:** Standardized Python sandbox evaluation with unit test execution.
  - **Report:** Pass rate ($\%$) with 95% Wilson score intervals and average wall-clock time per solved task.
- **C-gpqa-v2 (Secondary Scientific Reasoning Benchmark):**
  - **Dataset:** Full GPQA Diamond (198 questions).
  - **Grading:** Strict regex extractor outside internal thinking (`^\s*Final answer:\s*\(?([A-D])\)?\s*$`).
  - **Reporting:** Strict accuracy ($\%$) alongside truncation rate and paired McNemar statistics ($b, c, p$).
