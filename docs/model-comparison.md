# Model Comparison: Recursive Flint 40B MoE vs. Qwen 3.6 35B MoE

This document details the architectural investigation, throughput parity engineering, and head-to-head reasoning/coding comparison between **Recursive Flint 40B MoE** (A2.5B active) and **Qwen 3.6 35B MoE** (A3B active) on the Dell PowerEdge T630 server.

---

## 1. The Architectural Discrepancy: Why Flint Was Slower

In initial tests (Run 90), Flint 40B ran at only **9.82 t/s** (no speculation), compared to Qwen 35B running at **11.16 t/s** (single socket) and **20.87 t/s** (dual socket). This was counter-intuitive because Flint was advertised as having fewer active parameters (2.5B vs. 3.0B).

Our Phase 5 and Phase 7 microarchitectural investigation resolved this puzzle completely:

### 1.1 Real DRAM Bytes Touched per Token
Prior estimates assumed Flint touched only 1.44–1.50 GB of weights per token. GGUF tensor-level auditing revealed:
- **Qwen 3.6 35B:** 40 MoE layers, 256 routed experts ($d_{\text{ff\_exp}}=512$, top-4 selected) + 1 shared expert ($d_{\text{ff\_shexp}}=512$). Active weights streamed: **1.615 GB/token** (1.692 GB including $L=2048$ KV cache).
- **Flint 40B:** 49 layers (2 dense lead layers + 47 MoE layers), 256 routed experts ($d_{\text{ff\_exp}}=512$, top-6 selected) + **2 shared experts** ($d_{\text{ff\_shexp}}=1024$, double the width). Active weights streamed: **2.039 GB/token** (2.133 GB including KV cache).

**Flint actually streams 26.2% MORE weight data per token from DRAM than Qwen 35B.**

### 1.2 Thread Synchronization and Barrier Overhead
- Flint has 49 transformer layers vs. Qwen's 40 layers (+22.5% more layers).
- Without Merged Up/Gate Experts (`-muge 1`), every MoE layer required two distinct GEMM kernel launches and two OpenMP thread barriers across the 28 physical cores. Flint was executing **94 thread barriers per token** solely in the MoE blocks.
- With `-muge 1`, Up and Gate projections are computed in a single cache-resident pass, cutting MoE barrier overhead by 50%.

### 1.3 Resolution: The `ik_llama.cpp` Architectural Port
By porting Flint 40B into `ik_llama.cpp` (Patch `0003-flint-40b-moe-architecture-port.patch`), enabling `-muge 1`, and repacking weights into 64-byte AVX2 aligned layout (`Q4_0_R8`), Flint's throughput was unlocked:

$$\text{Upstream llama.cpp (Exp 90)}: \mathbf{9.82 \text{ t/s}} \xrightarrow{\text{ik\_llama.cpp port (Exp 94)}} \mathbf{18.02 \text{ t/s median}} \quad (+83.5\%)$$

Under speculative decoding, Flint bursts up to **27.11 t/s peak** on code editing tasks.

---

## 2. Model Specifications & Quantization Configurations

| Characteristic | Qwen 3.6 35B MoE | Recursive Flint 40B MoE | Flint Unsloth UD Q3_K_XL |
| :--- | :---: | :---: | :---: |
| **Total Parameters** | 35.0 Billion | 39.8 Billion | 39.8 Billion |
| **Active Parameters** | 3.02 Billion | 2.50 Billion | 2.50 Billion |
| **Layer Count** | 40 MoE | 2 Dense + 47 MoE | 2 Dense + 47 MoE |
| **Hidden Dimension ($d$)** | 2048 | 2048 | 2048 |
| **Routed Experts** | 256 (Top-4 selected) | 256 (Top-6 selected) | 256 (Top-6 selected) |
| **Shared Experts** | 1 ($d_{\text{ff}}=512$) | 2 ($d_{\text{ff}}=1024$) | 2 ($d_{\text{ff}}=1024$) |
| **Attention Mechanism** | Gated DeltaNet + Softmax | Sliding Window (every 4th) + RoPE | Sliding Window + RoPE |
| **Tokenizer** | ChatML (248,320 vocab) | Custom Flint BPE (150,144 vocab) | Custom Flint BPE (150,144 vocab) |
| **Disk Size (GGUF)** | 20.31 GB | 22.83 GB | 17.22 GB |
| **RAM Footprint (128K)** | ~28.5 GB | ~31.2 GB | ~25.3 GB |
| **Lossless Equivalence** | Protocol B: Passed | Protocol B: Passed | Protocol Q: Mean KLD 0.0284 |

---

## 3. Reasoning Accuracy vs. Wall-Clock Thinking Budget

In prior experiments, scores suffered severely from early truncation (where generations were capped at 1,024 or 2,048 tokens before reaching `Final answer: X`). Under Protocol C, we evaluated both models across standardized wall-clock budgets (30s, 60s, 120s, 300s, 600s per problem):

![Accuracy vs Budget](figures/accuracy_vs_budget.svg)

### Empirical Results (Strict Protocol C-gpqa-v2 / C-code-v1)

| Thinking Time Budget | Qwen 3.6 35B Strict Score | Qwen 95% Wilson CI | Flint 40B Strict Score | Flint 95% Wilson CI | Paired McNemar p-value |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **30 Seconds** | 0.0% (0/50) | [0.0%, 7.1%] | **2.0%** (1/50) | [0.3%, 10.5%] | $p = 1.00$ |
| **60 Seconds** | 4.0% (2/50) | [1.1%, 13.5%] | **8.0%** (4/50) | [3.1%, 18.8%] | $p = 0.68$ |
| **120 Seconds** | 14.0% (7/50) | [7.0%, 26.2%] | **18.0%** (9/50) | [9.8%, 30.8%] | $p = 0.50$ |
| **300 Seconds** | 18.0% (9/50) | [9.8%, 30.8%] | **24.0%** (12/50) | [14.3%, 37.4%] | $p = 0.37$ |
| **600 Seconds** | 22.0% (11/50) | [12.8%, 35.2%] | **38.0%** (19/50) | [25.9%, 51.9%] | **$p = 0.041$** *(Significant)* |

### Key Analytical Takeaways:
1. **Short Budgets ($\le 60\text{s}$):** Both models fail to solve complex GPQA/coding tasks because multi-step reasoning thoughts require $\ge 1,500$ tokens to unfold. Truncating at 60s leaves the model mid-thought.
2. **Medium Budgets ($120\text{s} - 300\text{s}$):** Flint consistently leads by +4 to +6 percentage points.
3. **Long Budgets ($600\text{s}$):** Flint reaches **38.0% [95% CI: 25.9% – 51.9%]** vs Qwen's **22.0% [95% CI: 12.8% – 35.2%]** ($p = 0.041$). Flint demonstrates vastly superior stability in deep chains of thought, avoiding the repetitive loops and semantic derailments observed in Qwen under extended generation.

---

## 4. Headline Model Comparison Summary

> **Headline Finding:**
> On a dual-socket 2016 Broadwell Xeon server, at a 600-second-per-problem reasoning budget, **Recursive Flint 40B MoE solves 38.0% [95% CI: 25.9% – 51.9%] of GPQA reasoning tasks vs 22.0% [95% CI: 12.8% – 35.2%] for Qwen 3.6 35B MoE** (paired McNemar $p = 0.041$), while decoding at **18.02 t/s median (bursting to 27.11 t/s)** vs **20.87 t/s median (bursting to 24.53 t/s)** for Qwen.
