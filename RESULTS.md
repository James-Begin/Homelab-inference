# Results

Scores below are read from the report files in [`logs/`](logs/). The standardized runs are GPQA Diamond, 50 questions, with a 1,536 token ceiling. The earlier sweeps are 20 questions at a 384 token ceiling, so those percentages are a different test.

The 128K column is the needle check at 192,065 tokens. **Passed** means the passkey matched. The tokens/second figure next to it is the short generation printed in that report (`speed:` after the needle), not the prompt-processing column. In the raw ladder files that column repeats prompt-processing speed.

## 50-question GPQA

| Run | Configuration | Avg t/s | Peak t/s | 50Q | First 20 | 128K needle | Report |
| ---: | --- | ---: | ---: | ---: | ---: | --- | --- |
| 0 | Baseline (Single NUMA Pure Decode) | 11.16 | 11.27 | 16 / 50 (32.0%) | 7 / 20 (35.0%) | — | [report](logs/gpqa_reports/gpqa_exp0_single_numa_baseline_50q_report.md) |
| 4 | Dual NUMA Interleaved Pure Decode (Mega-Kernel) | 15.72 | 15.89 | 18 / 50 (36.0%) | 7 / 20 (35.0%) | — | [report](logs/gpqa_reports/gpqa_exp4_numa_interleave_pure_decode_50q_report.md) |
| 5 | Dual NUMA + Native MTP (Mega-Kernel) | 19.26 | 21.10 | 22 / 50 (44.0%) | 9 / 20 (45.0%) | Passed, 3.72 t/s | [report](logs/gpqa_reports/gpqa_exp5_numa_native_mtp_50q_report.md) |
| 6 | Dual NUMA + Chained Speculation (Unfiltered N-Gram + MTP) | 14.60 | 22.47 | 20 / 50 (40.0%) | 10 / 20 (50.0%) | — | [report](logs/gpqa_reports/gpqa_exp6_numa_chained_spec_50q_report.md) |
| 12 | Dual NUMA + MegaKernel + Precision Chained Speculation (ngram_min_hits=2 + MTP) | 18.74 | 26.35 | 17 / 50 (34.0%) | 9 / 20 (45.0%) | — | [report](logs/gpqa_reports/gpqa_exp12_precision_spec_50q_report.md) |
| 15 | Dual NUMA + Native MTP + MegaKernel + Dynamic Expert Pruning (-ser 2,0.05) | 19.01 | 20.82 | 17 / 50 (34.0%) | 10 / 20 (50.0%) | — | [report](logs/gpqa_reports/gpqa_exp15_dynamic_expert_pruning_50q_report.md) |
| 16 | Dual NUMA + Native MTP + Fused Operator Graph Compilation & Barrier NUMA Isolation | 19.17 | 21.01 | 16 / 50 (32.0%) | 9 / 20 (45.0%) | — | [report](logs/gpqa_reports/gpqa_exp16_fused_graph_compilation_50q_report.md) |
| 17 | Combined Champion (Dual NUMA + MegaKernel + Precision Chained Spec + SER + Fused Barrier Isolation) | 18.41 | 20.89 | 18 / 50 (36.0%) | 9 / 20 (45.0%) | — | [report](logs/gpqa_reports/gpqa_exp17_combined_champion_50q_report.md) |
| 18 | Calibrated SER (Dual NUMA + Native MTP + -ser 2,0.5 + Fused Barrier Isolation) | 19.11 | 21.07 | 19 / 50 (38.0%) | 8 / 20 (40.0%) | Passed, 4.94 t/s | [report](logs/gpqa_reports/gpqa_exp18_calibrated_ser_50q_report.md) |
| 19 | Pure Uniform Q4_0 + Native MTP (Dual NUMA + MegaKernel + Barrier Isolation) | 20.87 | 22.86 | 14 / 50 (28.0%) | 7 / 20 (35.0%) | — | [report](logs/gpqa_reports/gpqa_exp19_q4_0_uniform_mtp_50q_report.md) |
| 20 | DFlash Speculative Diffusion Drafting (Dual NUMA + n_max=3 + SER 2,0.5) | 18.74 | 23.11 | 16 / 50 (32.0%) | 8 / 20 (40.0%) | — | [report](logs/gpqa_reports/gpqa_exp20_dflash_spec_50q_report.md) |
| 22 | KV Cache Quantization Ladder (-ctk q4_0 -ctv q4_0 + DFlash Spec + SER 2,0.5) | 18.92 | 23.76 | 16 / 50 (32.0%) | 10 / 20 (50.0%) | — | [report](logs/gpqa_reports/gpqa_exp22_kv_quant_50q_report.md) |
| 23 | Grand Unified Champion (Chained Precision Spec + Q4_0 KV Cache + SER 2,0.5) | 15.38 | 28.19 | 15 / 50 (30.0%) | 7 / 20 (35.0%) | Passed, 4.50 t/s | [report](logs/gpqa_reports/gpqa_exp23_grand_champion_50q_report.md) |
| 24 | Calibrated Native MTP + Q4_0 KV Cache + SER 2,0.5 (Dual NUMA) | 20.00 | 22.87 | 16 / 50 (32.0%) | 5 / 20 (25.0%) | Passed, 5.64 t/s | [report](logs/gpqa_reports/gpqa_exp24_native_mtp_q4kv_50q_report.md) |
| 25 | Multi-Token Batch Verification Scaling (DFlash n_max=4 + Q4_0 KV Cache + SER 2,0.5) | 19.13 | 28.74 | 14 / 50 (28.0%) | 7 / 20 (35.0%) | Passed, 5.59 t/s | [report](logs/gpqa_reports/gpqa_exp25_dflash_nmax4_q4kv_50q_report.md) |
| 26 | Precision Chained Speculation (N=8, Hits=3) + Native MTP + Q4_0 KV Cache + SER 2,0.5 | 19.65 | 65.27 | 15 / 50 (30.0%) | 5 / 20 (25.0%) | Passed, 5.44 t/s | [report](logs/gpqa_reports/gpqa_exp26_precision_chained_q4kv_50q_report.md) |
| 27 | Confidence-Filtered Speculative Diffusion (DFlash n_max=3, p_min=0.4 + Q4_0 KV Cache + SER 2,0.5) | 19.57 | 24.57 | 16 / 50 (32.0%) | 10 / 20 (50.0%) | Passed, 5.39 t/s | [report](logs/gpqa_reports/gpqa_exp27_dflash_pmin04_q4kv_50q_report.md) |
| 28 | Window-Bounded Precision Chained Speculation (N=8, M=8, Hits=3) + Native MTP + Q4_0 KV Cache + SER 2,0.5 | 17.98 | 21.15 | 16 / 50 (32.0%) | 6 / 20 (30.0%) | Passed, 5.62 t/s | [report](logs/gpqa_reports/gpqa_exp28_window_chained_q4kv_50q_report.md) |
| 29 | Confidence-Gated Speculative Diffusion Scaling (DFlash n_max=4, p_min=0.45 + Q4_0 KV Cache + SER 2,0.5) | 19.64 | 29.72 | 14 / 50 (28.0%) | 7 / 20 (35.0%) | Passed, 5.40 t/s | [report](logs/gpqa_reports/gpqa_exp29_dflash_nmax4_pmin045_q4kv_50q_report.md) |
| 30 | Native MTP + Q4_0 KV Cache + SER 2,0.5 | 20.02 | 23.02 | 16 / 50 (32.0%) | 5 / 20 (25.0%) | Passed, 5.62 t/s | [report](logs/gpqa_reports/gpqa_exp30_phys_pinning_mtp_q4kv_50q_report.md) |
| 31 | Confidence-Gated Speculative Diffusion (DFlash n_max=4, p_min=0.45 + Q4_0 KV + SER 2,0.5) | 19.92 | 29.91 | 14 / 50 (28.0%) | 7 / 20 (35.0%) | Passed, 5.66 t/s | [report](logs/gpqa_reports/gpqa_exp31_phys_pinning_dflash_nmax4_q4kv_50q_report.md) |
| 32 | Precision Chained Spec (N=8, M=12, hits=2) + Native MTP + Q4_0 KV + SER 2,0.5 | 19.43 | 23.03 | 17 / 50 (34.0%) | 11 / 20 (55.0%) | Passed, 5.49 t/s | [report](logs/gpqa_reports/gpqa_exp32_phys_pinning_chained_spec_q4kv_50q_report.md) |
| 33 | Burst-16 Chained Spec (n_max=16, N=8, M=24, hits=2) + Native MTP + Q4_0 KV + SER 2,0.5 | 18.60 | 22.09 | 16 / 50 (32.0%) | 7 / 20 (35.0%) | Passed, 5.48 t/s | [report](logs/gpqa_reports/gpqa_exp33_phys_pinning_burst16_chained_spec_q4kv_50q_report.md) |
| 34 | Calibrated Speculative Diffusion (DFlash n_max=3, p_min=0.40 + Q4_0 KV + SER 2,0.5) | 19.90 | 25.18 | 16 / 50 (32.0%) | 10 / 20 (50.0%) | Passed, 5.60 t/s | [report](logs/gpqa_reports/gpqa_exp34_phys_pinning_dflash_nmax3_pmin04_q4kv_50q_report.md) |
| 35 | 28 threads, Native MTP + Q4_0 KV + SER 2,0.5 | 20.81 | 23.02 | 16 / 50 (32.0%) | 5 / 20 (25.0%) | Passed, 8.00 t/s | [report](logs/gpqa_reports/gpqa_exp35_phys_pinning_28threads_mtp_q4kv_50q_report.md) |
| 36 | 28 threads, Window Chained Spec (N=8, M=12, hits=2) + Native MTP + Q4_0 KV + SER 2,0.5 | 20.41 | 23.81 | 17 / 50 (34.0%) | 11 / 20 (55.0%) | Passed, 7.81 t/s | [report](logs/gpqa_reports/gpqa_exp36_phys_pinning_28threads_chained_spec_q4kv_50q_report.md) |
| 37 | 28 threads, Calibrated Speculative Diffusion (DFlash n_max=3, p_min=0.40 + Q4_0 KV + SER 2,0.5) | 20.11 | 25.27 | 16 / 50 (32.0%) | 10 / 20 (50.0%) | Passed, 8.09 t/s | [report](logs/gpqa_reports/gpqa_exp37_phys_pinning_28threads_dflash_nmax3_pmin04_q4kv_50q_report.md) |
| 38 | 28 threads, Dynamic Suffix-Tree Speculation (n_max=8, match=4, depth=32) + Native MTP + Q4_0 KV + SER 2,0.5 | 20.75 | 48.88 | 16 / 50 (32.0%) | 10 / 20 (50.0%) | Passed, 7.85 t/s | [report](logs/gpqa_reports/gpqa_exp38_phys_pinning_28threads_suffix_spec_q4kv_50q_report.md) |
| 39 | 28 threads, Tuned Window Chained Spec (n_max=10, N=8, M=16, hits=2) + Native MTP + Q4_0 KV + SER 2,0.5 | 20.45 | 26.09 | 16 / 50 (32.0%) | 7 / 20 (35.0%) | Passed, 7.87 t/s | [report](logs/gpqa_reports/gpqa_exp39_phys_pinning_28threads_tuned_chained_spec_q4kv_50q_report.md) |
| 40 | 28 threads, Burst-16 Suffix Speculation (n_max=16, match=5, depth=64) + Native MTP + Q4_0 KV + SER 2,0.5 | 20.97 | 66.25 | 12 / 50 (24.0%) | 7 / 20 (35.0%) | Passed, 7.85 t/s | [report](logs/gpqa_reports/gpqa_exp40_phys_pinning_28threads_suffix_burst16_q4kv_50q_report.md) |
| 41 | 28 threads, Balanced Suffix Speculation (n_max=12, match=4, depth=48) + Native MTP + Q4_0 KV + SER 2,0.5 | 20.38 | 63.69 | 14 / 50 (28.0%) | 8 / 20 (40.0%) | Passed, 7.85 t/s | [report](logs/gpqa_reports/gpqa_exp41_phys_pinning_28threads_suffix_nmax12_q4kv_50q_report.md) |
| 42 | 28 threads, Confidence-Gated Suffix Speculation (n_max=16, p_min=0.15, match=4, depth=64) + Native MTP + Q4_0 KV + SER 2,0.5 | 18.84 | 66.30 | 14 / 50 (28.0%) | 6 / 20 (30.0%) | Passed, 8.04 t/s | [report](logs/gpqa_reports/gpqa_exp42_phys_pinning_28threads_suffix_pmin015_burst16_q4kv_50q_report.md) |
| 43 | 28 threads, Calibrated Precision Suffix Speculation (n_max=8, match=5, depth=48) + Native MTP + Q4_0 KV + SER 2,0.5 | 20.04 | 36.62 | 17 / 50 (34.0%) | 8 / 20 (40.0%) | Passed, 7.90 t/s | [report](logs/gpqa_reports/gpqa_exp43_phys_pinning_28threads_suffix_nmax8_match5_q4kv_50q_report.md) |
| 44 | 28 threads, Merged Up/Gate Experts (-muge) + Dynamic Suffix Speculation (n_max=8, match=4) + Native MTP + Q4_0 KV + SER 2,0.5 | 20.78 | 48.86 | 16 / 50 (32.0%) | 10 / 20 (50.0%) | Passed, 7.84 t/s | [report](logs/gpqa_reports/gpqa_exp44_phys_pinning_28threads_muge_suffix_q4kv_50q_report.md) |
| 45 | 28 threads, Merged Up/Gate Experts (-muge) + Precision Suffix Spec (n_max=9, match=5) + Native MTP + Q4_0 KV + SER 2,0.5 | 21.98 | 57.55 | 14 / 50 (28.0%) | 6 / 20 (30.0%) | Passed, 7.87 t/s | [report](logs/gpqa_reports/gpqa_exp45_phys_pinning_28threads_muge_suffix_nmax9_match5_q4kv_50q_report.md) |
| 46 | 28 threads, Custom Non-Linear Dense Quantization (IQ4_XS Attention + Q4_0 MoE) + Native MTP + Q4_0 KV + SER 2,0.5 | 22.50 | 23.88 | 16 / 50 (32.0%) | 8 / 20 (40.0%) | Passed, 8.56 t/s | [report](logs/gpqa_reports/gpqa_exp46_phys_pinning_28threads_iq4xs_dense_mtp_q4kv_50q_report.md) |
| 47 | 28 threads, Custom Non-Linear Dense Quantization (IQ4_XS Attention + Q4_0 MoE) + Precision Suffix Speculation (n_max=8, match=5, depth=48) + Native MTP + Q4_0 KV + SER 2,0.5 | 21.30 | 38.35 | 18 / 50 (36.0%) | 8 / 20 (40.0%) | Passed, 8.29 t/s | [report](logs/gpqa_reports/gpqa_exp47_phys_pinning_28threads_iq4xs_suffix_match5_q4kv_50q_report.md) |
| 48 | 28 threads, Custom IQ4_XS Attention + Merged Up/Gate Experts (-muge) + Precision Suffix Speculation (n_max=8, match=5, depth=48) + Native MTP + Q4_0 KV + SER 2,0.5 | 21.30 | 38.22 | 18 / 50 (36.0%) | 8 / 20 (40.0%) | Passed, 8.25 t/s | [report](logs/gpqa_reports/gpqa_exp48_phys_pinning_28threads_iq4xs_muge_suffix_q4kv_50q_report.md) |
| 49 | 28 threads, Custom Non-Linear Dense Quantization (IQ4_NL Attention + Q4_0 MoE) + Merged Up/Gate Experts (-muge) + Precision Suffix Speculation (n_max=8, match=5) + Native MTP + Q4_0 KV + SER 2,0.5 | 20.91 | 38.31 | 17 / 50 (34.0%) | 7 / 20 (35.0%) | Passed, 8.25 t/s | [report](logs/gpqa_reports/gpqa_exp49_phys_pinning_28threads_iq4nl_muge_suffix_q4kv_50q_report.md) |
| 50 | 28 threads, Repacked GGUF + Merged Up/Gate Experts (-muge) + Precision Suffix Speculation (n_max=8, match=5) + Native MTP + Q4_0 KV + SER 2,0.5 | 21.33 | 38.23 | 18 / 50 (36.0%) | 8 / 20 (40.0%) | Passed, 8.23 t/s | [report](logs/gpqa_reports/gpqa_exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv_50q_report.md) |
| 51 | Repacked GGUF + Merged Experts (-muge) + Calibrated Horizon Expansion (n_max=10, match=6, depth=48) + Native MTP + Q4_0 KV + SER 2,0.5 | 21.19 | 39.09 | 15 / 50 (30.0%) | 7 / 20 (35.0%) | Passed, 8.34 t/s | [report](logs/gpqa_reports/gpqa_exp51_phys_pinning_28threads_repacked_iq4xs_muge_suffix_nmax10_match6_q4kv_50q_report.md) |
| 52 | Repacked GGUF + Merged Experts (-muge) + Deep Precision Suffix (n_max=12, match=7, depth=64) + Native MTP + Q4_0 KV + SER 2,0.5 | 22.06 | 48.74 | 13 / 50 (26.0%) | 6 / 20 (30.0%) | Passed, 8.29 t/s | [report](logs/gpqa_reports/gpqa_exp52_phys_pinning_28threads_repacked_iq4xs_muge_suffix_nmax12_match7_q4kv_50q_report.md) |
| 53 | Repacked GGUF + Merged Experts (-muge) + High-Throughput Precision Suffix (n_max=14, match=8, depth=64) + Native MTP + Q4_0 KV + SER 2,0.5 | 21.42 | 27.45 | 15 / 50 (30.0%) | 8 / 20 (40.0%) | Passed, 8.28 t/s | [report](logs/gpqa_reports/gpqa_exp53_phys_pinning_28threads_repacked_iq4xs_muge_suffix_nmax14_match8_q4kv_50q_report.md) |
| 54 | Repacked GGUF + Merged Experts (-muge) + Confidence-Gated Burst Suffix (n_max=16, match=8, p_min=0.10, depth=64) + Native MTP + Q4_0 KV + SER 2,0.5 | 21.51 | 28.26 | 14 / 50 (28.0%) | 6 / 20 (30.0%) | Passed, 8.21 t/s | [report](logs/gpqa_reports/gpqa_exp54_phys_pinning_28threads_repacked_iq4xs_muge_suffix_nmax16_match8_pmin010_q4kv_50q_report.md) |
| 55 | Repacked GGUF + Merged Experts (-muge) + Calibrated Speculative Diffusion (DFlash n_max=3, p_min=0.45, cross_ctx=512) + Q4_0 KV + SER 2,0.5 | 20.28 | 26.32 | 13 / 50 (26.0%) | 7 / 20 (35.0%) | Passed, 8.28 t/s | [report](logs/gpqa_reports/gpqa_exp55_phys_pinning_28threads_repacked_iq4xs_muge_dflash_nmax3_pmin045_q4kv_50q_report.md) |
| 57 | Repacked + Suffix (n_max=8, match=5) + Confidence-Gated MTP (p_min=0.15) + Q4_0 KV + SER 2,0.5 | 21.10 | 37.99 | 18 / 50 (36.0%) | 8 / 20 (40.0%) | Passed, 37.96 t/s | [report](logs/gpqa_reports/gpqa_exp57_phys_pinning_28threads_repacked_iq4xs_muge_suffix_mtp_pmin015_q4kv_50q_report.md) |
| 58 | Repacked + Suffix (n_max=8, match=5) + Speculative Autotuning (--spec-autotune) + Native MTP + Q4_0 KV + SER 2,0.5 | 21.09 | 37.67 | 18 / 50 (36.0%) | 8 / 20 (40.0%) | Passed, 38.81 t/s | [report](logs/gpqa_reports/gpqa_exp58_phys_pinning_28threads_repacked_iq4xs_muge_suffix_autotune_q4kv_50q_report.md) |
| 59 | Repacked + High-Confidence Speculative Diffusion (DFlash n_max=3, p_min=0.60) + Q4_0 KV + SER 2,0.5 | 20.43 | 26.43 | 13 / 50 (26.0%) | 7 / 20 (35.0%) | Passed, 38.81 t/s | [report](logs/gpqa_reports/gpqa_exp59_phys_pinning_28threads_repacked_iq4xs_muge_dflash_pmin060_q4kv_50q_report.md) |
| 60 | Repacked + Suffix (n_max=8, match=5) + Prefix Cache Sharing (similarity=0.20) + Native MTP + Q4_0 KV + SER 2,0.5 | 20.97 | 37.60 | 18 / 50 (36.0%) | 8 / 20 (40.0%) | Passed, 38.82 t/s | [report](logs/gpqa_reports/gpqa_exp60_phys_pinning_28threads_repacked_iq4xs_muge_suffix_slot_similarity_q4kv_50q_report.md) |
| 61 | Repacked + Merged Experts + Grand Composite Champion (Suffix + MTP p=0.15 + Autotune + Sim 0.20) | 21.14 | 37.85 | 18 / 50 (36.0%) | 8 / 20 (40.0%) | Passed, 37.91 t/s | [report](logs/gpqa_reports/gpqa_exp61_phys_pinning_28threads_repacked_iq4xs_muge_grand_composite_champion_q4kv_50q_report.md) |
| 62 | Repacked + Merged Experts + Direct NUMA Map Pinning (--numa numactl) + Suffix + MTP (p=0.15) | 21.57 | 38.58 | 18 / 50 (36.0%) | 8 / 20 (40.0%) | Passed, 37.95 t/s | [report](logs/gpqa_reports/gpqa_exp62_phys_pinning_28threads_repacked_iq4xs_muge_numactl_pinning_q4kv_50q_report.md) |
| 63 | Repacked + Merged Experts + Dynamic 3-Expert Pruning (expert_used_count=int:3) + Suffix + MTP | 21.16 | 43.97 | 11 / 50 (22.0%) ❌ | 5 / 20 (25.0%) | Passed, 38.17 t/s | [report](logs/gpqa_reports/gpqa_exp63_phys_pinning_28threads_repacked_iq4xs_muge_3experts_pruning_q4kv_50q_report.md) |
| 64 | Repacked + Merged Experts + N-Gram Mod Hash Spec (n_max=10, hits=2) + MTP (p=0.15) + Autotune | 21.47 | 23.68 | 17 / 50 (34.0%) | 8 / 20 (40.0%) | Passed, 37.96 t/s | [report](logs/gpqa_reports/gpqa_exp64_phys_pinning_28threads_repacked_iq4xs_muge_ngram_mod_hybrid_q4kv_50q_report.md) |
| 65 | Repacked + Merged Experts + Grouped Expert Routing (-ger) + Suffix + MTP (p=0.15) | 21.11 | 37.84 | 18 / 50 (36.0%) | 8 / 20 (40.0%) | Passed, 37.93 t/s | [report](logs/gpqa_reports/gpqa_exp65_phys_pinning_28threads_repacked_iq4xs_muge_grouped_expert_routing_q4kv_50q_report.md) |

## 20-question sweeps

These predate the 50-question protocol. A 20-question file that was later rerun as 50 questions stays listed here because the cap and the sample both changed.

| Run | Configuration | Avg t/s | 20Q | Report |
| ---: | --- | ---: | ---: | --- |
| 1 | N-Gram Speculation | 12.19 | 5 / 20 (25.0%) | [report](logs/gpqa_reports/gpqa_exp1_ngram_report.md) |
| 2 | Native MTP Speculation | 14.50 | 7 / 20 (35.0%) | [report](logs/gpqa_reports/gpqa_exp2_native_mtp_report.md) |
| 3 | Chained Speculation (N-Gram + MTP) | 13.15 | 6 / 20 (30.0%) | [report](logs/gpqa_reports/gpqa_exp3_chained_spec_report.md) |
| 4 | Dual-Socket NUMA Memory Bandwidth Scaling | 16.00 | 5 / 20 (25.0%) | [report](logs/gpqa_reports/gpqa_exp4_numa_interleave_report.md) |
| 5 | Dual-Socket NUMA + Native MTP | 21.02 | 7 / 20 (35.0%) | [report](logs/gpqa_reports/gpqa_exp5_numa_mtp_report.md) |
| 6 | Dual-Socket NUMA + Chained Speculation | 16.86 | 7 / 20 (35.0%) | [report](logs/gpqa_reports/gpqa_exp6_numa_chained_spec_report.md) |
| 7a | Dual NUMA MTP (threads=20) | 19.94 | 7 / 20 (35.0%) | [report](logs/gpqa_reports/gpqa_exp7a_dual_numa_mtp_threads_20__report.md) |
| 7b | Dual NUMA MTP (threads=28) | 20.34 | 7 / 20 (35.0%) | [report](logs/gpqa_reports/gpqa_exp7b_dual_numa_mtp_threads_28__report.md) |
| 8 | Dual NUMA MTP (cache-ram=0) | 20.06 | 7 / 20 (35.0%) | [report](logs/gpqa_reports/gpqa_exp8_dual_numa_mtp_cache_ram_0__report.md) |
| 9 | Dual NUMA + AVX2 Prefetching Mega-Kernel (Pure Decode) | 15.96 | 5 / 20 (25.0%) | [report](logs/gpqa_reports/gpqa_exp9_mega_kernel_pure_decode_report.md) |
| 10 | Dual NUMA + AVX2 Prefetching Mega-Kernel + Native MTP | 19.98 | 7 / 20 (35.0%) | [report](logs/gpqa_reports/gpqa_exp10_mega_kernel_numa_mtp_report.md) |
| 11 | Dual NUMA + AVX2 Prefetching Mega-Kernel + Chained Speculation | 17.14 | 6 / 20 (30.0%) | [report](logs/gpqa_reports/gpqa_exp11_mega_kernel_chained_spec_report.md) |
| — | Baseline GPQA | 11.40 | 4 / 20 (20.0%) | [report](logs/gpqa_reports/gpqa_baseline_gpqa_report.md) |

## Six-check quality suite

Coding, math, facts, logic, and a 4K needle. This is the gate from the start of the campaign, not GPQA.

| Run | Result | Avg generation | Report |
| --- | --- | ---: | --- |
| Baseline No Speculation | 4 / 6 Tests Passed | 10.75 t/s | [report](logs/gpqa_reports/quality_baseline_no_speculation_report.md) |
| N-Gram Speculation (n_max=5) | 6 / 6 Tests Passed | 11.64 t/s | [report](logs/gpqa_reports/quality_exp1_ngram_speculation_report.md) |
| Native MTP (n_max=1) | 6 / 6 Tests Passed | 14.58 t/s | [report](logs/gpqa_reports/quality_exp2_native_mtp_report.md) |
| Official Baseline | 6 / 6 Tests Passed | 11.32 t/s | [report](logs/gpqa_reports/quality_official_baseline_report.md) |

## Runs without a 50-question score

- [Experiment 13: Asymmetric NUMA Speculation (Decoupled Sockets)](logs/gpqa_reports/gpqa_exp13_asymmetric_numa_spec_report.md)
- [Experiment 14: Multi-Token Prediction (MTP) Output Vocabulary Requantization](logs/gpqa_reports/gpqa_exp14_mtp_output_requant_report.md)
- [Experiment 56 Technical Post-Mortem & Diagnostic Autopsy](logs/gpqa_reports/gpqa_exp56_cascade_draft08b_postmortem.md)

Per-question JSON for the finished runs is in [`logs/raw_checkpoints/`](logs/raw_checkpoints/). The question set is [`gpqa_subset_50.json`](logs/raw_checkpoints/gpqa_subset_50.json).
