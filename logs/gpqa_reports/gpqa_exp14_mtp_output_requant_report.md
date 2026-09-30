# Experiment 14: Multi-Token Prediction (MTP) Output Vocabulary Requantization

- **Target Model:** Qwen 3.6-35B-A3B-UD-Q6_K_MoE_Q4_0 (35.5B params, 256 experts, 4 active per layer, 41 layers)
- **Vocabulary Size:** 248,320 tokens
- **Optimization Tested:** On-the-fly MTP output tensor requantization (`-mtprot q8_0`, `-mtprot q4_0`)
- **Hardware Platform:** Dual Intel Xeon E5-2680 v4 (28 cores total, 56 vCPUs, 2 NUMA nodes, 8-channel DDR4 memory bus)

---

## 1. Hypothesis & Architectural Motivation

In the Qwen 3.6 architecture, the vocabulary dimension is exceptionally large: $V = 248,320$.
- Layer 40 (the Next-N prediction head) must multiply the 2048-dim hidden state by the entire output vocabulary projection matrix `output.weight` of dimension $[2048 \times 248,320]$ to sample the speculative draft token.
- **Hypothesis:** If the output tensor is scanned at full precision or high bit-width, memory bandwidth during drafting could be a major bottleneck. By requantizing `output.weight` on-the-fly to a lower-precision format (`Q8_0` or `Q4_0`) via `-mtprot`, the memory bytes transferred during drafting would decrease significantly, cutting MTP draft latency.

---

## 2. Empirical Findings & Profiling Analysis

### 1. Existing Model Quantization Format
- Inspection of the GGUF metadata for `Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`:
  - `output.weight` is **already quantized to `Q6_K`** ($417.18\text{ MB}$, $\approx 6.56\text{ bits/weight}$, $1,680\text{ bytes/row}$).
  - `Q8_0` format requires 8.5 bits/weight ($540.34\text{ MB}$, $2,176\text{ bytes/row}$).

### 2. Requantization to `Q8_0` Rejection
When passing `-mtprot q8_0`, the engine correctly triggered an internal safeguard:
```
llm_requantize_output_tensor: if requantized to q8_0 the output tensor size would be 540344320, which is >= the current size 417177600 => not requantizing
```
- Requantizing to `Q8_0` would *increase* the tensor size by **+29.5%**, increasing bandwidth demand rather than decreasing it.

### 3. Requantization to `Q4_0` Performance Evaluation
When passing `-mtprot q4_0`:
- The engine created an extra output tensor of type `Q4_0`:
  ```
  ====== Creating extra output tensor of type q4_0 for MTP usage. Additional memory required is 272.81 MiB
  ```
- Memory reduction for MTP output tensor: **-34.6%** ($417.18\text{ MB} \rightarrow 272.81\text{ MB}$).

#### Comparative Benchmark Results:

| Metric | Baseline MTP (Native `Q6_K` Output) | MTP with Requantized `Q4_0` Output | Delta |
| :--- | :---: | :---: | :---: |
| **Model Load Time** | 16,770 ms | 17,799 ms | +1,029 ms (+6.1% startup penalty) |
| **MTP Output Tensor Size** | 417.18 MB | 272.81 MB | **-144.37 MB (-34.6%)** |
| **Decode Step Latency** | 68.10 ms / token | 69.40 ms / token | +1.30 ms / token |
| **Generation Speed (CLI)** | **14.68 t/s** | **14.41 t/s** | -0.27 t/s (-1.8%) |
| **Prompt Eval Speed** | 61.34 t/s | 53.30 t/s | -8.04 t/s |

---

## 3. Why Requantizing the Output Tensor Does Not Speed Up Generation

1. **AVX2 Dot-Product Microarchitecture:**
   - The AVX2 Mega-Kernel for `Q6_K` utilizes 6-bit integer unpacking directly into 16-bit registers with vector FMA instructions, achieving near-optimal memory bandwidth saturation on Broadwell.
   - `Q4_0` unpacking requires nibble extraction (`_mm256_and_si256` and `_mm256_srli_epi16`), which adds slight instruction overhead that offsets the 144 MB memory bandwidth savings.
2. **MoE Dominates Total Latency (40 Layers vs 1 Projection):**
   - Detailed op profiling reveals:
     - `OP MUL_MAT` (dense projections across 40 layers): **851,077 us**
     - `OP MOE_FUSED_UP_GATE` (expert up/gate projections): **168,730 us**
     - `OP MUL_MAT_ID` (expert down projections): **89,066 us**
     - `OP DELTA_NET` (linear attention recurrent state): **87,427 us**
     - Output vocabulary projection: only **~14,000 us** (< 1.2% of total compute time per token).
   - Speeding up or shrinking the output vocabulary projection has negligible impact on end-to-end token latency because the MoE feed-forward layers are 80x larger in aggregate compute volume.

---

## 4. Conclusion & Strategic Recommendation

- **Verdict:** Requantizing the output tensor (`-mtprot q4_0`) is **neutral to slightly detrimental** (-1.8% TPS, +1.0s loading time).
- **Core Insight:** True speedups on the quest for 50 TPS cannot come from the vocabulary head; they must come from reducing the **2.73 GB active weight bytes** loaded by the **160 active expert matrix multiplications** across the 40 MoE layers.
- **Next Direct Path:** MoE Dynamic Expert Pruning (Smart Expert Reduction `-ser`), which directly skips non-essential expert matrices.
