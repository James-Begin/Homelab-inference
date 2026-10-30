# Inference Benchmark Results

Dual Intel Xeon E5-2680 v4 (28 physical cores, Broadwell AVX2), 256 GB DDR4-2400 NUMA.
All measurements adhere to the certified protocols defined in [`docs/eval-protocol.md`](docs/eval-protocol.md).
Historical exploratory runs (Runs 0–65) are archived in [`archive/README.md`](archive/README.md).

## 1. Certified Protocol C-code-v1 Coding Suite (EvalPlus HumanEval+ 164 Problems)

Evaluated on the full 164 coding tasks using the EvalPlus sandbox verification suite (`evalplus` v0.3.1). Pass@1 greedy decoding with full physical core pinning and NUMA interleaving.

| Exp | Model | Architecture | Base Pass@1 | Plus Pass@1 | Decode Speed | Avg Time / Task | Total Time | Report |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| 50 | `Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf` | Qwen 3.6 35B MoE | **66.5%** | **65.2%** | 21.31 t/s | 194.4s | 531.4 min | [report](logs/runs/code_exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv/report.md) |
| 94 | `RecursiveSI_flint-Q4_0_Repacked.gguf` | Recursive Flint 40B MoE | **97.0%** | **90.8%** | 20.77 t/s | 109.5s | 299.2 min | [report](logs/runs/code_exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv/report.md) |

## 2. Certified Protocol C-gpqa-v2 Reasoning Suite: 8K vs. 16K Runway Scaling

Evaluated on the standardized 50-Question GPQA Diamond subset under strict parsing (`Final answer: X` outside reasoning blocks) and audited lenient parsing. Comparing 8,192-token runway (`-c 16384`) vs. 16,384-token runway (`-c 32768`).

| Exp | Model | Runway | Decode t/s | Strict Score | Strict % | Lenient % | Natural Completions | Truncated % | Report |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 50 | `Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf` | 8K (8,192) | 19.18 | **13/50** | **26.0%** | 40.0% | **13/13** (100.0%) | 54.0% | [report](logs/runs/run_exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv/report.md) |
| 50 | `Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf` | 16K (16,384) | 17.60 | **19/50** | **38.0%** | 46.0% | **19/25** (76.0%) | 42.0% | [report](logs/runs/run_exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv_16k_runway/report.md) |
| 94 | `RecursiveSI_flint-Q4_0_Repacked.gguf` | 8K (8,192) | 17.14 | **18/50** | **36.0%** | 44.0% | **18/21** (85.7%) | 0.0% | [report](logs/runs/run_exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv/report.md) |
| 94 | `RecursiveSI_flint-Q4_0_Repacked.gguf` | 16K (16,384) | 15.99 | **23/50** | **46.0%** | 58.0% | **23/31** (74.2%) | 38.0% | [report](logs/runs/run_exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv_16k_runway/report.md) |

## 3. Audited & Regraded Historical Task Evaluations (Runs 66–95)

Evaluated on the 50-Question GPQA Diamond subset under strict parsing (`^\s*Final answer:\s*\(?([A-D])\)?\s*$`). Text within reasoning blocks is excluded; unclosed chains of thought evaluate strictly to `None`.

| Run | Experiment ID | Unique Qs | Strict Score | Strict % | Lenient % | Report |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 66 | `exp66_phys_pinning_28threads_repacked_iq4xs_muge_first_touch_numa_q4kv_checkpoint` | 50 | **1/50** | **2.0%** | 4.0% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp66_phys_pinning_28threads_repacked_iq4xs_muge_first_touch_numa_q4kv_checkpoint_50q_report.md) |
| 67 | `exp67_phys_pinning_28threads_repacked_iq4xs_muge_corpus_suffix_spec_q4kv_checkpoint` | 50 | **0/50** | **0.0%** | 8.0% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp67_phys_pinning_28threads_repacked_iq4xs_muge_corpus_suffix_spec_q4kv_checkpoint_50q_report.md) |
| 68 | `exp68_phys_pinning_28threads_repacked_iq4xs_muge_cost_aware_constrained_draft_q4kv_checkpoint` | 50 | **0/50** | **0.0%** | 8.0% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp68_phys_pinning_28threads_repacked_iq4xs_muge_cost_aware_constrained_draft_q4kv_checkpoint_50q_report.md) |
| 69 | `exp69_phys_pinning_28threads_repacked_iq4xs_muge_pure_mtp_numactl_q4kv_checkpoint` | 49 | **1/49** | **2.0%** | 16.3% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp69_phys_pinning_28threads_repacked_iq4xs_muge_pure_mtp_numactl_q4kv_checkpoint_50q_report.md) |
| 70 | `exp70_phys_pinning_28threads_repacked_iq4xs_muge_suffix_autotune_numactl_q4kv_checkpoint` | 50 | **1/50** | **2.0%** | 6.0% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp70_phys_pinning_28threads_repacked_iq4xs_muge_suffix_autotune_numactl_q4kv_checkpoint_50q_report.md) |
| 71 | `exp71_phys_pinning_28threads_repacked_iq4xs_muge_expanded_ceiling_4096_constrained_draft_q4kv_checkpoint` | 50 | **3/50** | **6.0%** | 18.0% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp71_phys_pinning_28threads_repacked_iq4xs_muge_expanded_ceiling_4096_constrained_draft_q4kv_checkpoint_50q_report.md) |
| 72 | `exp72_phys_pinning_28threads_repacked_iq4xs_muge_pure_mtp_expanded_ceiling_4096_q4kv_checkpoint` | 46 | **7/46** | **15.2%** | 23.9% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp72_phys_pinning_28threads_repacked_iq4xs_muge_pure_mtp_expanded_ceiling_4096_q4kv_checkpoint_50q_report.md) |
| 73 | `exp73_phys_pinning_28threads_repacked_iq4xs_muge_corpus_suffix_expanded_ceiling_4096_q4kv_checkpoint` | 50 | **3/50** | **6.0%** | 12.0% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp73_phys_pinning_28threads_repacked_iq4xs_muge_corpus_suffix_expanded_ceiling_4096_q4kv_checkpoint_50q_report.md) |
| 74 | `exp74_phys_pinning_28threads_repacked_iq4xs_muge_suffix_autotune_expanded_ceiling_4096_q4kv_checkpoint` | 50 | **3/50** | **6.0%** | 18.0% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp74_phys_pinning_28threads_repacked_iq4xs_muge_suffix_autotune_expanded_ceiling_4096_q4kv_checkpoint_50q_report.md) |
| 75 | `exp75_phys_pinning_28threads_repacked_iq4xs_muge_persistent_slot_cache_expanded_ceiling_4096_q4kv_checkpoint` | 50 | **3/50** | **6.0%** | 18.0% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp75_phys_pinning_28threads_repacked_iq4xs_muge_persistent_slot_cache_expanded_ceiling_4096_q4kv_checkpoint_50q_report.md) |
| 76 | `exp76_phys_pinning_28threads_repacked_iq4xs_muge_concise_steering_autotune_expanded_ceiling_4096_q4kv_checkpoint` | 50 | **9/50** | **18.0%** | 22.0% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp76_phys_pinning_28threads_repacked_iq4xs_muge_concise_steering_autotune_expanded_ceiling_4096_q4kv_checkpoint_50q_report.md) |
| 77 | `exp77_phys_pinning_28threads_repacked_iq4xs_muge_pure_mtp_pmin005_expanded_ceiling_4096_q4kv_checkpoint` | 46 | **7/46** | **15.2%** | 23.9% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp77_phys_pinning_28threads_repacked_iq4xs_muge_pure_mtp_pmin005_expanded_ceiling_4096_q4kv_checkpoint_50q_report.md) |
| 78 | `exp78_phys_pinning_26threads_repacked_iq4xs_muge_os_jitter_isolation_expanded_ceiling_4096_q4kv_checkpoint` | 50 | **7/50** | **14.0%** | 16.0% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp78_phys_pinning_26threads_repacked_iq4xs_muge_os_jitter_isolation_expanded_ceiling_4096_q4kv_checkpoint_50q_report.md) |
| 79 | `exp79_phys_pinning_28threads_repacked_iq4xs_muge_slot_similarity_050_expanded_ceiling_4096_q4kv_checkpoint` | 50 | **3/50** | **6.0%** | 18.0% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp79_phys_pinning_28threads_repacked_iq4xs_muge_slot_similarity_050_expanded_ceiling_4096_q4kv_checkpoint_50q_report.md) |
| 80 | `exp80_phys_pinning_28threads_repacked_iq4xs_muge_expanded_horizon_autotune_ceiling_4096_q4kv_checkpoint` | 50 | **6/50** | **12.0%** | 16.0% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp80_phys_pinning_28threads_repacked_iq4xs_muge_expanded_horizon_autotune_ceiling_4096_q4kv_checkpoint_50q_report.md) |
| 81 | `exp81_phys_pinning_28threads_repacked_iq4xs_muge_unified_champion_steering_slot050_ceiling4096_q4kv_checkpoint` | 50 | **9/50** | **18.0%** | 22.0% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp81_phys_pinning_28threads_repacked_iq4xs_muge_unified_champion_steering_slot050_ceiling4096_q4kv_checkpoint_50q_report.md) |
| 82 | `exp82_phys_pinning_28decode_26batch_threads_repacked_iq4xs_muge_heterogeneous_threads_ceiling4096_q4kv_checkpoint` | 50 | **7/50** | **14.0%** | 16.0% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp82_phys_pinning_28decode_26batch_threads_repacked_iq4xs_muge_heterogeneous_threads_ceiling4096_q4kv_checkpoint_50q_report.md) |
| 83 | `exp83_phys_pinning_28threads_repacked_iq4xs_muge_calibrated_temperature_slot050_ceiling4096_q4kv_checkpoint` | 50 | **6/50** | **12.0%** | 14.0% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp83_phys_pinning_28threads_repacked_iq4xs_muge_calibrated_temperature_slot050_ceiling4096_q4kv_checkpoint_50q_report.md) |
| 84 | `exp84_phys_pinning_28threads_repacked_iq4xs_muge_conservative_horizon_nmax3_ceiling4096_q4kv_checkpoint` | 50 | **8/50** | **16.0%** | 14.0% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp84_phys_pinning_28threads_repacked_iq4xs_muge_conservative_horizon_nmax3_ceiling4096_q4kv_checkpoint_50q_report.md) |
| 85 | `exp85_phys_pinning_28threads_repacked_iq4xs_muge_corpus_suffix_slot050_ceiling4096_q4kv_checkpoint` | 50 | **3/50** | **6.0%** | 12.0% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp85_phys_pinning_28threads_repacked_iq4xs_muge_corpus_suffix_slot050_ceiling4096_q4kv_checkpoint_50q_report.md) |
| 86 | `exp86_phys_pinning_28decode_26batch_repacked_iq4xs_muge_triple_champion_ceiling4096_q4kv_checkpoint` | 50 | **6/50** | **12.0%** | 12.0% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp86_phys_pinning_28decode_26batch_repacked_iq4xs_muge_triple_champion_ceiling4096_q4kv_checkpoint_50q_report.md) |
| 87 | `exp87_phys_pinning_28threads_repacked_iq4xs_muge_suffix_match4_autotune_ceiling4096_q4kv_checkpoint` | 50 | **6/50** | **12.0%** | 14.0% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp87_phys_pinning_28threads_repacked_iq4xs_muge_suffix_match4_autotune_ceiling4096_q4kv_checkpoint_50q_report.md) |
| 88 | `exp88_phys_pinning_28threads_repacked_iq4xs_muge_pure_mtp_pmin000_ceiling4096_q4kv_checkpoint` | 46 | **7/46** | **15.2%** | 23.9% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp88_phys_pinning_28threads_repacked_iq4xs_muge_pure_mtp_pmin000_ceiling4096_q4kv_checkpoint_50q_report.md) |
| 89 | `exp89_phys_pinning_28threads_repacked_iq4xs_muge_slot_similarity_070_ceiling4096_q4kv_checkpoint` | 50 | **3/50** | **6.0%** | 18.0% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp89_phys_pinning_28threads_repacked_iq4xs_muge_slot_similarity_070_ceiling4096_q4kv_checkpoint_50q_report.md) |
| 90 | `exp90_flint_baseline_40b_a2_5b_q4_0_numa_phys_pinning_checkpoint` | 50 | **13/50** | **26.0%** | 34.0% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp90_flint_baseline_40b_a2_5b_q4_0_numa_phys_pinning_checkpoint_50q_report.md) |
| 91 | `exp91_flint_composite_champion_ngram_mod_slot050_decoupled26_ceiling4096_q4kv_checkpoint` | 50 | **9/50** | **18.0%** | 40.0% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp91_flint_composite_champion_ngram_mod_slot050_decoupled26_ceiling4096_q4kv_checkpoint_50q_report.md) |
| 92 | `exp92_flint_expanded_horizon_ngram_nmax8_match5_slot050_decoupled26_ceiling4096_q4kv_checkpoint` | 50 | **11/50** | **22.0%** | 32.0% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp92_flint_expanded_horizon_ngram_nmax8_match5_slot050_decoupled26_ceiling4096_q4kv_checkpoint_50q_report.md) |
| 93 | `exp93_flint_dense_drafter_qwen08b_slot050_decoupled26_ceiling4096_q4kv_checkpoint` | 50 | **13/50** | **26.0%** | 34.0% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp93_flint_dense_drafter_qwen08b_slot050_decoupled26_ceiling4096_q4kv_checkpoint_50q_report.md) |
| 94 | `exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv_checkpoint` | 50 | **12/50** | **24.0%** | 38.0% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv_checkpoint_50q_report.md) |
| 95 | `exp95_flint_unsloth_ud_q3kxl_repacked_muge_ngram_mod_slot050_decoupled26_ceiling4096_q4kv_checkpoint` | 50 | **12/50** | **24.0%** | 34.0% | [report](archive/notebook-v1/gpqa_reports/gpqa_exp95_flint_unsloth_ud_q3kxl_repacked_muge_ngram_mod_slot050_decoupled26_ceiling4096_q4kv_checkpoint_50q_report.md) |

## 4. Standard Controlled Protocols

- **Protocol A (Controlled Throughput):** Standardized 12-prompt suite, fixed 512 tokens, 5 repetitions, median & IQR.
- **Protocol B (Lossless Equivalence):** Greedy token match against reference.
- **Protocol Q (Lossy KLD Divergence):** 150K-token reference perplexity shift.
- **Protocol C-code (Coding Capabilities):** EvalPlus HumanEval+ pass@1 greedy.
- **Protocol C-gpqa (Scientific Reasoning):** GPQA Diamond 50 questions strict parsing.

See [`archive/REGRADED_SUMMARY.md`](archive/REGRADED_SUMMARY.md) for full breakdown of dropped duplicate IDs in historical checkpoints.
