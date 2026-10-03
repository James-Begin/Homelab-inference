**Homelab inference: reproducible artifact audit**

Read 49 standardized report files, 45 checkpoint files, and 50 catalog entries. Earlier sweeps and technical postmortems are separate.

Throughput below is reconstructed from saved token counts and rates; it is not a new benchmark. Weighted decode = sum(tokens) / sum(tokens / reported_rate). Wall rate includes the saved request wall time. Neither includes server startup. Positive-speed rows with positive token counts are used for rates; invalid rows remain in score and cap counts.

| Run | Saved rows | Valid timing rows | Recorded correct | Mean t/s | Median t/s | Weighted decode t/s | Request wall t/s | At token ceiling |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 12 | 36 | 36 | 13 | 18.88 | 18.80 | 18.76 | 18.14 | 32 |
| 15 | 50 | 50 | 17 | 19.01 | 18.94 | 19.01 | 18.39 | 45 |
| 16 | 50 | 50 | 16 | 19.17 | 19.08 | 19.13 | 18.54 | 48 |
| 17 | 50 | 50 | 18 | 18.41 | 18.45 | 18.39 | 17.82 | 46 |
| 18 | 50 | 50 | 19 | 19.11 | 18.92 | 19.06 | 18.48 | 46 |
| 19 | 50 | 50 | 14 | 20.87 | 20.74 | 20.83 | 20.16 | 47 |
| 20 | 50 | 50 | 16 | 18.74 | 18.38 | 18.52 | 18.04 | 47 |
| 22 | 50 | 50 | 16 | 18.92 | 18.21 | 18.65 | 18.16 | 43 |
| 23 | 50 | 50 | 15 | 15.38 | 15.08 | 15.31 | 14.94 | 47 |
| 24 | 50 | 50 | 16 | 20.00 | 19.87 | 19.93 | 19.31 | 47 |
| 25 | 50 | 50 | 14 | 19.13 | 18.17 | 18.93 | 18.45 | 46 |
| 26 | 50 | 50 | 15 | 19.65 | 18.70 | 18.94 | 18.37 | 46 |
| 27 | 50 | 50 | 16 | 19.57 | 18.91 | 19.29 | 18.77 | 43 |
| 28 | 50 | 50 | 16 | 17.98 | 17.95 | 18.03 | 17.51 | 47 |
| 29 | 50 | 50 | 14 | 19.64 | 18.62 | 19.44 | 18.92 | 46 |
| 30 | 50 | 50 | 16 | 20.02 | 19.89 | 19.98 | 19.36 | 47 |
| 31 | 50 | 50 | 14 | 19.92 | 18.86 | 19.71 | 19.18 | 46 |
| 32 | 50 | 50 | 17 | 19.43 | 19.58 | 19.60 | 18.99 | 47 |
| 33 | 50 | 50 | 16 | 18.60 | 18.47 | 18.62 | 18.07 | 47 |
| 34 | 50 | 50 | 16 | 19.90 | 19.15 | 19.60 | 19.07 | 43 |
| 35 | 50 | 49 | 16 | 20.81 | 20.75 | 20.77 | 20.13 | 46 |
| 36 | 50 | 50 | 17 | 20.41 | 20.47 | 20.61 | 19.97 | 47 |
| 37 | 50 | 50 | 16 | 20.11 | 19.51 | 19.80 | 19.26 | 43 |
| 38 | 50 | 50 | 16 | 20.75 | 18.48 | 19.27 | 18.39 | 47 |
| 39 | 50 | 50 | 16 | 20.45 | 20.39 | 20.48 | 19.85 | 45 |
| 40 | 50 | 50 | 12 | 20.97 | 18.58 | 19.17 | 18.61 | 46 |
| 41 | 50 | 50 | 14 | 20.38 | 17.77 | 18.50 | 17.98 | 47 |
| 42 | 50 | 50 | 14 | 18.84 | 17.12 | 17.56 | 17.10 | 48 |
| 43 | 50 | 50 | 17 | 20.04 | 19.14 | 19.22 | 17.55 | 46 |
| 44 | 50 | 50 | 16 | 20.78 | 18.49 | 19.29 | 18.41 | 47 |
| 45 | 50 | 50 | 14 | 21.98 | 19.36 | 20.20 | 19.16 | 46 |
| 46 | 50 | 50 | 16 | 22.50 | 22.50 | 22.46 | 21.75 | 48 |
| 47 | 50 | 50 | 18 | 21.30 | 20.99 | 21.07 | 20.44 | 49 |
| 48 | 50 | 50 | 18 | 21.30 | 20.78 | 21.08 | 20.44 | 49 |
| 49 | 50 | 50 | 17 | 20.91 | 20.45 | 20.71 | 20.04 | 50 |
| 50 | 50 | 50 | 18 | 21.33 | 20.98 | 21.10 | 20.46 | 49 |
| 51 | 50 | 50 | 15 | 21.19 | 20.75 | 20.96 | 20.32 | 46 |
| 52 | 50 | 50 | 13 | 22.06 | 21.19 | 21.57 | 20.47 | 48 |
| 53 | 50 | 50 | 15 | 21.42 | 21.26 | 21.35 | 20.71 | 49 |
| 54 | 50 | 50 | 14 | 21.51 | 21.27 | 21.43 | 20.35 | 48 |
| 55 | 50 | 50 | 13 | 20.28 | 19.95 | 20.26 | 19.30 | 47 |
| 57 | 50 | 50 | 18 | 21.10 | 20.60 | 20.87 | 20.24 | 49 |
| 58 | 50 | 50 | 18 | 21.09 | 20.80 | 20.87 | 20.25 | 49 |
| 59 | 50 | 50 | 13 | 20.43 | 20.25 | 20.40 | 19.43 | 47 |
| 60 | 50 | 50 | 18 | 20.97 | 20.67 | 20.74 | 20.13 | 49 |

Run 12's committed checkpoint contains only 36 rows despite a 50-question report. Run 35 has one row with zero tokens and zero speed; excluding that row changes how its mean is calculated. Do not silently compare these recomputations to a different denominator.

**All standardized reported results**

These retain the published score and arithmetic mean, including runs without complete raw checkpoints. They are historical observations, not quality certifications.

| Run | Configuration | Avg t/s | Peak t/s | Recorded score |
| ---: | --- | ---: | ---: | --- |
| 0 | Baseline (Single NUMA Pure Decode) | 11.16 | 11.27 | 16 / 50 (32.0%) |
| 4 | Dual NUMA Interleaved Pure Decode (Mega-Kernel) | 15.72 | 15.89 | 18 / 50 (36.0%) |
| 5 | Dual NUMA + Native MTP (Mega-Kernel) | 19.26 | 21.10 | 22 / 50 (44.0%) |
| 6 | Dual NUMA + Chained Speculation (Unfiltered N-Gram + MTP) | 14.60 | 22.47 | 20 / 50 (40.0%) |
| 12 | Dual NUMA + MegaKernel + Precision Chained Speculation (ngram_min_hits=2 + MTP) | 18.74 | 26.35 | 17 / 50 (34.0%) |
| 15 | Dual NUMA + Native MTP + MegaKernel + Dynamic Expert Pruning (-ser 2,0.05) | 19.01 | 20.82 | 17 / 50 (34.0%) |
| 16 | Dual NUMA + Native MTP + Fused Operator Graph Compilation & Barrier NUMA Isolation | 19.17 | 21.01 | 16 / 50 (32.0%) |
| 17 | Combined Champion (Dual NUMA + MegaKernel + Precision Chained Spec + SER + Fused Barrier Isolation) | 18.41 | 20.89 | 18 / 50 (36.0%) |
| 18 | Calibrated SER (Dual NUMA + Native MTP + -ser 2,0.5 + Fused Barrier Isolation) | 19.11 | 21.07 | 19 / 50 (38.0%) |
| 19 | Pure Uniform Q4_0 + Native MTP (Dual NUMA + MegaKernel + Barrier Isolation) | 20.87 | 22.86 | 14 / 50 (28.0%) |
| 20 | DFlash Speculative Diffusion Drafting (Dual NUMA + n_max=3 + SER 2,0.5) | 18.74 | 23.11 | 16 / 50 (32.0%) |
| 22 | KV Cache Quantization Ladder (-ctk q4_0 -ctv q4_0 + DFlash Spec + SER 2,0.5) | 18.92 | 23.76 | 16 / 50 (32.0%) |
| 23 | Grand Unified Champion (Chained Precision Spec + Q4_0 KV Cache + SER 2,0.5) | 15.38 | 28.19 | 15 / 50 (30.0%) |
| 24 | Calibrated Native MTP + Q4_0 KV Cache + SER 2,0.5 (Dual NUMA) | 20.00 | 22.87 | 16 / 50 (32.0%) |
| 25 | Multi-Token Batch Verification Scaling (DFlash n_max=4 + Q4_0 KV Cache + SER 2,0.5) | 19.13 | 28.74 | 14 / 50 (28.0%) |
| 26 | Precision Chained Speculation (N=8, Hits=3) + Native MTP + Q4_0 KV Cache + SER 2,0.5 | 19.65 | 65.27 | 15 / 50 (30.0%) |
| 27 | Confidence-Filtered Speculative Diffusion (DFlash n_max=3, p_min=0.4 + Q4_0 KV Cache + SER 2,0.5) | 19.57 | 24.57 | 16 / 50 (32.0%) |
| 28 | Window-Bounded Precision Chained Speculation (N=8, M=8, Hits=3) + Native MTP + Q4_0 KV Cache + SER 2,0.5 | 17.98 | 21.15 | 16 / 50 (32.0%) |
| 29 | Confidence-Gated Speculative Diffusion Scaling (DFlash n_max=4, p_min=0.45 + Q4_0 KV Cache + SER 2,0.5) | 19.64 | 29.72 | 14 / 50 (28.0%) |
| 30 | Native MTP + Q4_0 KV Cache + SER 2,0.5 | 20.02 | 23.02 | 16 / 50 (32.0%) |
| 31 | Confidence-Gated Speculative Diffusion (DFlash n_max=4, p_min=0.45 + Q4_0 KV + SER 2,0.5) | 19.92 | 29.91 | 14 / 50 (28.0%) |
| 32 | Precision Chained Spec (N=8, M=12, hits=2) + Native MTP + Q4_0 KV + SER 2,0.5 | 19.43 | 23.03 | 17 / 50 (34.0%) |
| 33 | Burst-16 Chained Spec (n_max=16, N=8, M=24, hits=2) + Native MTP + Q4_0 KV + SER 2,0.5 | 18.60 | 22.09 | 16 / 50 (32.0%) |
| 34 | Calibrated Speculative Diffusion (DFlash n_max=3, p_min=0.40 + Q4_0 KV + SER 2,0.5) | 19.90 | 25.18 | 16 / 50 (32.0%) |
| 35 | 28 threads, Native MTP + Q4_0 KV + SER 2,0.5 | 20.81 | 23.02 | 16 / 50 (32.0%) |
| 36 | 28 threads, Window Chained Spec (N=8, M=12, hits=2) + Native MTP + Q4_0 KV + SER 2,0.5 | 20.41 | 23.81 | 17 / 50 (34.0%) |
| 37 | 28 threads, Calibrated Speculative Diffusion (DFlash n_max=3, p_min=0.40 + Q4_0 KV + SER 2,0.5) | 20.11 | 25.27 | 16 / 50 (32.0%) |
| 38 | 28 threads, Dynamic Suffix-Tree Speculation (n_max=8, match=4, depth=32) + Native MTP + Q4_0 KV + SER 2,0.5 | 20.75 | 48.88 | 16 / 50 (32.0%) |
| 39 | 28 threads, Tuned Window Chained Spec (n_max=10, N=8, M=16, hits=2) + Native MTP + Q4_0 KV + SER 2,0.5 | 20.45 | 26.09 | 16 / 50 (32.0%) |
| 40 | 28 threads, Burst-16 Suffix Speculation (n_max=16, match=5, depth=64) + Native MTP + Q4_0 KV + SER 2,0.5 | 20.97 | 66.25 | 12 / 50 (24.0%) |
| 41 | 28 threads, Balanced Suffix Speculation (n_max=12, match=4, depth=48) + Native MTP + Q4_0 KV + SER 2,0.5 | 20.38 | 63.69 | 14 / 50 (28.0%) |
| 42 | 28 threads, Confidence-Gated Suffix Speculation (n_max=16, p_min=0.15, match=4, depth=64) + Native MTP + Q4_0 KV + SER 2,0.5 | 18.84 | 66.30 | 14 / 50 (28.0%) |
| 43 | 28 threads, Calibrated Precision Suffix Speculation (n_max=8, match=5, depth=48) + Native MTP + Q4_0 KV + SER 2,0.5 | 20.04 | 36.62 | 17 / 50 (34.0%) |
| 44 | 28 threads, Merged Up/Gate Experts (-muge) + Dynamic Suffix Speculation (n_max=8, match=4) + Native MTP + Q4_0 KV + SER 2,0.5 | 20.78 | 48.86 | 16 / 50 (32.0%) |
| 45 | 28 threads, Merged Up/Gate Experts (-muge) + Precision Suffix Spec (n_max=9, match=5) + Native MTP + Q4_0 KV + SER 2,0.5 | 21.98 | 57.55 | 14 / 50 (28.0%) |
| 46 | 28 threads, Custom Non-Linear Dense Quantization (IQ4_XS Attention + Q4_0 MoE) + Native MTP + Q4_0 KV + SER 2,0.5 | 22.50 | 23.88 | 16 / 50 (32.0%) |
| 47 | 28 threads, Custom Non-Linear Dense Quantization (IQ4_XS Attention + Q4_0 MoE) + Precision Suffix Speculation (n_max=8, match=5, depth=48) + Native MTP + Q4_0 KV + SER 2,0.5 | 21.30 | 38.35 | 18 / 50 (36.0%) |
| 48 | 28 threads, Custom IQ4_XS Attention + Merged Up/Gate Experts (-muge) + Precision Suffix Speculation (n_max=8, match=5, depth=48) + Native MTP + Q4_0 KV + SER 2,0.5 | 21.30 | 38.22 | 18 / 50 (36.0%) |
| 49 | 28 threads, Custom Non-Linear Dense Quantization (IQ4_NL Attention + Q4_0 MoE) + Merged Up/Gate Experts (-muge) + Precision Suffix Speculation (n_max=8, match=5) + Native MTP + Q4_0 KV + SER 2,0.5 | 20.91 | 38.31 | 17 / 50 (34.0%) |
| 50 | 28 threads, Repacked GGUF + Merged Up/Gate Experts (-muge) + Precision Suffix Speculation (n_max=8, match=5) + Native MTP + Q4_0 KV + SER 2,0.5 | 21.33 | 38.23 | 18 / 50 (36.0%) |
| 51 | Repacked GGUF + Merged Experts (-muge) + Calibrated Horizon Expansion (n_max=10, match=6, depth=48) + Native MTP + Q4_0 KV + SER 2,0.5 | 21.19 | 39.09 | 15 / 50 (30.0%) |
| 52 | Repacked GGUF + Merged Experts (-muge) + Deep Precision Suffix (n_max=12, match=7, depth=64) + Native MTP + Q4_0 KV + SER 2,0.5 | 22.06 | 48.74 | 13 / 50 (26.0%) |
| 53 | Repacked GGUF + Merged Experts (-muge) + High-Throughput Precision Suffix (n_max=14, match=8, depth=64) + Native MTP + Q4_0 KV + SER 2,0.5 | 21.42 | 27.45 | 15 / 50 (30.0%) |
| 54 | Repacked GGUF + Merged Experts (-muge) + Confidence-Gated Burst Suffix (n_max=16, match=8, p_min=0.10, depth=64) + Native MTP + Q4_0 KV + SER 2,0.5 | 21.51 | 28.26 | 14 / 50 (28.0%) |
| 55 | Repacked GGUF + Merged Experts (-muge) + Calibrated Speculative Diffusion (DFlash n_max=3, p_min=0.45, cross_ctx=512) + Q4_0 KV + SER 2,0.5 | 20.28 | 26.32 | 13 / 50 (26.0%) |
| 57 | Repacked + Suffix (n_max=8, match=5) + Confidence-Gated MTP (p_min=0.15) + Q4_0 KV + SER 2,0.5 | 21.10 | 37.99 | 18 / 50 (36.0%) |
| 58 | Repacked + Suffix (n_max=8, match=5) + Speculative Autotuning (--spec-autotune) + Native MTP + Q4_0 KV + SER 2,0.5 | 21.09 | 37.67 | 18 / 50 (36.0%) |
| 59 | Repacked + High-Confidence Speculative Diffusion (DFlash n_max=3, p_min=0.60) + Q4_0 KV + SER 2,0.5 | 20.43 | 26.43 | 13 / 50 (26.0%) |
| 60 | Repacked + Suffix (n_max=8, match=5) + Prefix Cache Sharing (similarity=0.20) + Native MTP + Q4_0 KV + SER 2,0.5 | 20.97 | 37.60 | 18 / 50 (36.0%) |

**Executable parser demonstrations**

1. An unfinished thinking block with no final answer is scored as `B`: `<think>I should test option B before calculating the final answer.`. This demonstrates a failure mode; historical full completions were not saved, so their answers cannot all be regraded.

2. A fake process that returns exit code 1, prints a diagnostic passkey, and generates `The answer is unknown` is marked PASSED with no error.

3. With prompt speed 100 t/s and decode speed 10 t/s, the same function reports decode speed 100 t/s because the unanchored regex matches the prompt timing line.

4. Run 40 peak: 66.25 t/s, 1536 tokens, recorded correct=False, answer=None. Saved preview: `<think> The.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .`

4. Run 42 peak: 66.30 t/s, 1536 tokens, recorded correct=False, answer=None. Saved preview: `<think> The.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .`

**Queued experiments**

- 61: Exp 61: Pre-Repacked Offline GGUF + Merged Experts (-muge) + Grand Composite Champion (Suffix n_max=8, match=5 + Confidence MTP p_min=0.15 + Spec Autotune + Slot Similarity 0.20 + Q4_0 KV + SER 2,0.5)
- 62: Exp 62: Pre-Repacked Offline GGUF + Merged Experts (-muge) + Direct NUMA Map Pinning (--numa numactl) + Precision Suffix (n_max=8, match=5) + Confidence MTP (p_min=0.15) + Q4_0 KV + SER 2,0.5
- 63: Exp 63: Pre-Repacked Offline GGUF + Merged Experts (-muge) + Dynamic 3-Expert Pruning (expert_used_count=int:3) + Precision Suffix (n_max=8, match=5) + Confidence MTP (p_min=0.15) + Q4_0 KV + SER 2,0.5
- 64: Exp 64: Pre-Repacked Offline GGUF + Merged Experts (-muge) + N-Gram Mod Hash Spec (n_max=10, N=8, M=16, hits=2) + Confidence MTP (p_min=0.15) + Spec Autotune + Q4_0 KV + SER 2,0.5
- 65: Exp 65: Pre-Repacked Offline GGUF + Merged Experts (-muge) + Grouped Expert Routing (-ger) + Precision Suffix (n_max=8, match=5) + Confidence MTP (p_min=0.15) + Q4_0 KV + SER 2,0.5
