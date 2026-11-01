# Saved benchmark results

These are recorded configurations on a Dell PowerEdge T630 with two Xeon E5-2680 v4 CPUs (28 physical cores total) and 256 GB RAM. The current DIMM inventory runs at 1866 MT/s; historical manifests do not establish the DIMM rate for every run.

No inference or generated code is executed by this report generator. Regenerate derived run reports with `python3 benchmarks/summarize_runs.py --write`, then run `python3 benchmarks/build_results.py`.

## Coding

Each run contains one completion per HumanEval task. HumanEval+ success requires **both base and extra tests**. Earlier reports counted extra tests alone (107 Qwen, 149 Flint); the corrected counts are 106 and 148. Raw samples and EvalPlus result files are unchanged.

| Run | Model | Base passed | Base + extra passed | Mean decode tokens/s | Mean request s | Sum request min | Report |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv | `Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf` | 109/164 | 106/164 | 21.31 | 194.41 | 531.4 | [report](logs/runs/code_exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv/report.md) |
| exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv | `RecursiveSI_flint-Q4_0_Repacked.gguf` | 159/164 | 148/164 | 20.77 | 109.48 | 299.2 | [report](logs/runs/code_exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv/report.md) |

Mean request times include failed tasks. Decode rate is an arithmetic mean of finite positive saved rates for completions longer than one token. Qwen uses 163 timing rows: `HumanEval/111` generated one token with a saved rate of 1,000,000 tokens/s and is excluded from the rate mean. All 164 tasks remain in pass counts and elapsed times. Flint uses all 164 timing rows. Elapsed time and test success measure different things. The models use different quantization, prompts, extraction and serving settings. These runs compare the local pipelines; they do not isolate model architecture or individual patch gains.

## GPQA Diamond subset

The saved subset has 50 questions. Strict grading accepts an explicit final-answer line or boxed letter outside reasoning tags; a lenient parser is retained for comparison. Scores below retain the recorded grading flags.

| Run | Output ceiling | Mean decode tokens/s | Strict score | Lenient score | Token-limit rows | No final answer at truncation | Report |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv | 8,192 | 19.18 | 13/50 | 20/50 | 37/50 | 27/50 | [report](logs/runs/run_exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv/report.md) |
| exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv_16k_runway | 16,384 | 17.60 | 19/50 | 23/50 | 25/50 | 21/50 | [report](logs/runs/run_exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv_16k_runway/report.md) |
| exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv | 8,192 | 17.14 | 18/50 | 22/50 | 29/50 | 0/50 | [report](logs/runs/run_exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv/report.md) |
| exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv_16k_runway | 16,384 | 15.99 | 23/50 | 29/50 | 19/50 | 19/50 | [report](logs/runs/run_exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv_16k_runway/report.md) |

Token-limit rows reached the recorded output ceiling or report `finish_reason=length`. A final answer can still appear in such a row, so this count differs from no-answer truncations. Older rows lack raw stopping flags; responses below the ceiling are not established natural completions.

## Historical regrades

These regrades audit saved answers from the earlier exploratory runs. They do not establish controlled throughput, output equivalence, or an isolated optimization effect. [Archived notebook](archive/README.md) retains the original observations and their limits.

| Run | Unique questions | Strict score | Lenient score | Source regrade |
| --- | ---: | ---: | ---: | --- |
| `exp66_phys_pinning_28threads_repacked_iq4xs_muge_first_touch_numa_q4kv_checkpoint` | 50 | 1/50 | 2/50 | [JSON](archive/regraded/exp66_phys_pinning_28threads_repacked_iq4xs_muge_first_touch_numa_q4kv_checkpoint.json) |
| `exp67_phys_pinning_28threads_repacked_iq4xs_muge_corpus_suffix_spec_q4kv_checkpoint` | 50 | 0/50 | 4/50 | [JSON](archive/regraded/exp67_phys_pinning_28threads_repacked_iq4xs_muge_corpus_suffix_spec_q4kv_checkpoint.json) |
| `exp68_phys_pinning_28threads_repacked_iq4xs_muge_cost_aware_constrained_draft_q4kv_checkpoint` | 50 | 0/50 | 4/50 | [JSON](archive/regraded/exp68_phys_pinning_28threads_repacked_iq4xs_muge_cost_aware_constrained_draft_q4kv_checkpoint.json) |
| `exp69_phys_pinning_28threads_repacked_iq4xs_muge_pure_mtp_numactl_q4kv_checkpoint` | 49 | 1/49 | 8/49 | [JSON](archive/regraded/exp69_phys_pinning_28threads_repacked_iq4xs_muge_pure_mtp_numactl_q4kv_checkpoint.json) |
| `exp70_phys_pinning_28threads_repacked_iq4xs_muge_suffix_autotune_numactl_q4kv_checkpoint` | 50 | 1/50 | 3/50 | [JSON](archive/regraded/exp70_phys_pinning_28threads_repacked_iq4xs_muge_suffix_autotune_numactl_q4kv_checkpoint.json) |
| `exp71_phys_pinning_28threads_repacked_iq4xs_muge_expanded_ceiling_4096_constrained_draft_q4kv_checkpoint` | 50 | 3/50 | 9/50 | [JSON](archive/regraded/exp71_phys_pinning_28threads_repacked_iq4xs_muge_expanded_ceiling_4096_constrained_draft_q4kv_checkpoint.json) |
| `exp72_phys_pinning_28threads_repacked_iq4xs_muge_pure_mtp_expanded_ceiling_4096_q4kv_checkpoint` | 46 | 7/46 | 11/46 | [JSON](archive/regraded/exp72_phys_pinning_28threads_repacked_iq4xs_muge_pure_mtp_expanded_ceiling_4096_q4kv_checkpoint.json) |
| `exp73_phys_pinning_28threads_repacked_iq4xs_muge_corpus_suffix_expanded_ceiling_4096_q4kv_checkpoint` | 50 | 3/50 | 6/50 | [JSON](archive/regraded/exp73_phys_pinning_28threads_repacked_iq4xs_muge_corpus_suffix_expanded_ceiling_4096_q4kv_checkpoint.json) |
| `exp74_phys_pinning_28threads_repacked_iq4xs_muge_suffix_autotune_expanded_ceiling_4096_q4kv_checkpoint` | 50 | 3/50 | 9/50 | [JSON](archive/regraded/exp74_phys_pinning_28threads_repacked_iq4xs_muge_suffix_autotune_expanded_ceiling_4096_q4kv_checkpoint.json) |
| `exp75_phys_pinning_28threads_repacked_iq4xs_muge_persistent_slot_cache_expanded_ceiling_4096_q4kv_checkpoint` | 50 | 3/50 | 9/50 | [JSON](archive/regraded/exp75_phys_pinning_28threads_repacked_iq4xs_muge_persistent_slot_cache_expanded_ceiling_4096_q4kv_checkpoint.json) |
| `exp76_phys_pinning_28threads_repacked_iq4xs_muge_concise_steering_autotune_expanded_ceiling_4096_q4kv_checkpoint` | 50 | 9/50 | 11/50 | [JSON](archive/regraded/exp76_phys_pinning_28threads_repacked_iq4xs_muge_concise_steering_autotune_expanded_ceiling_4096_q4kv_checkpoint.json) |
| `exp77_phys_pinning_28threads_repacked_iq4xs_muge_pure_mtp_pmin005_expanded_ceiling_4096_q4kv_checkpoint` | 46 | 7/46 | 11/46 | [JSON](archive/regraded/exp77_phys_pinning_28threads_repacked_iq4xs_muge_pure_mtp_pmin005_expanded_ceiling_4096_q4kv_checkpoint.json) |
| `exp78_phys_pinning_26threads_repacked_iq4xs_muge_os_jitter_isolation_expanded_ceiling_4096_q4kv_checkpoint` | 50 | 7/50 | 8/50 | [JSON](archive/regraded/exp78_phys_pinning_26threads_repacked_iq4xs_muge_os_jitter_isolation_expanded_ceiling_4096_q4kv_checkpoint.json) |
| `exp79_phys_pinning_28threads_repacked_iq4xs_muge_slot_similarity_050_expanded_ceiling_4096_q4kv_checkpoint` | 50 | 3/50 | 9/50 | [JSON](archive/regraded/exp79_phys_pinning_28threads_repacked_iq4xs_muge_slot_similarity_050_expanded_ceiling_4096_q4kv_checkpoint.json) |
| `exp80_phys_pinning_28threads_repacked_iq4xs_muge_expanded_horizon_autotune_ceiling_4096_q4kv_checkpoint` | 50 | 6/50 | 8/50 | [JSON](archive/regraded/exp80_phys_pinning_28threads_repacked_iq4xs_muge_expanded_horizon_autotune_ceiling_4096_q4kv_checkpoint.json) |
| `exp81_phys_pinning_28threads_repacked_iq4xs_muge_unified_champion_steering_slot050_ceiling4096_q4kv_checkpoint` | 50 | 9/50 | 11/50 | [JSON](archive/regraded/exp81_phys_pinning_28threads_repacked_iq4xs_muge_unified_champion_steering_slot050_ceiling4096_q4kv_checkpoint.json) |
| `exp82_phys_pinning_28decode_26batch_threads_repacked_iq4xs_muge_heterogeneous_threads_ceiling4096_q4kv_checkpoint` | 50 | 7/50 | 8/50 | [JSON](archive/regraded/exp82_phys_pinning_28decode_26batch_threads_repacked_iq4xs_muge_heterogeneous_threads_ceiling4096_q4kv_checkpoint.json) |
| `exp83_phys_pinning_28threads_repacked_iq4xs_muge_calibrated_temperature_slot050_ceiling4096_q4kv_checkpoint` | 50 | 6/50 | 7/50 | [JSON](archive/regraded/exp83_phys_pinning_28threads_repacked_iq4xs_muge_calibrated_temperature_slot050_ceiling4096_q4kv_checkpoint.json) |
| `exp84_phys_pinning_28threads_repacked_iq4xs_muge_conservative_horizon_nmax3_ceiling4096_q4kv_checkpoint` | 50 | 8/50 | 7/50 | [JSON](archive/regraded/exp84_phys_pinning_28threads_repacked_iq4xs_muge_conservative_horizon_nmax3_ceiling4096_q4kv_checkpoint.json) |
| `exp85_phys_pinning_28threads_repacked_iq4xs_muge_corpus_suffix_slot050_ceiling4096_q4kv_checkpoint` | 50 | 3/50 | 6/50 | [JSON](archive/regraded/exp85_phys_pinning_28threads_repacked_iq4xs_muge_corpus_suffix_slot050_ceiling4096_q4kv_checkpoint.json) |
| `exp86_phys_pinning_28decode_26batch_repacked_iq4xs_muge_triple_champion_ceiling4096_q4kv_checkpoint` | 50 | 6/50 | 6/50 | [JSON](archive/regraded/exp86_phys_pinning_28decode_26batch_repacked_iq4xs_muge_triple_champion_ceiling4096_q4kv_checkpoint.json) |
| `exp87_phys_pinning_28threads_repacked_iq4xs_muge_suffix_match4_autotune_ceiling4096_q4kv_checkpoint` | 50 | 6/50 | 7/50 | [JSON](archive/regraded/exp87_phys_pinning_28threads_repacked_iq4xs_muge_suffix_match4_autotune_ceiling4096_q4kv_checkpoint.json) |
| `exp88_phys_pinning_28threads_repacked_iq4xs_muge_pure_mtp_pmin000_ceiling4096_q4kv_checkpoint` | 46 | 7/46 | 11/46 | [JSON](archive/regraded/exp88_phys_pinning_28threads_repacked_iq4xs_muge_pure_mtp_pmin000_ceiling4096_q4kv_checkpoint.json) |
| `exp89_phys_pinning_28threads_repacked_iq4xs_muge_slot_similarity_070_ceiling4096_q4kv_checkpoint` | 50 | 3/50 | 9/50 | [JSON](archive/regraded/exp89_phys_pinning_28threads_repacked_iq4xs_muge_slot_similarity_070_ceiling4096_q4kv_checkpoint.json) |
| `exp90_flint_baseline_40b_a2_5b_q4_0_numa_phys_pinning_checkpoint` | 50 | 13/50 | 17/50 | [JSON](archive/regraded/exp90_flint_baseline_40b_a2_5b_q4_0_numa_phys_pinning_checkpoint.json) |
| `exp91_flint_composite_champion_ngram_mod_slot050_decoupled26_ceiling4096_q4kv_checkpoint` | 50 | 9/50 | 20/50 | [JSON](archive/regraded/exp91_flint_composite_champion_ngram_mod_slot050_decoupled26_ceiling4096_q4kv_checkpoint.json) |
| `exp92_flint_expanded_horizon_ngram_nmax8_match5_slot050_decoupled26_ceiling4096_q4kv_checkpoint` | 50 | 11/50 | 16/50 | [JSON](archive/regraded/exp92_flint_expanded_horizon_ngram_nmax8_match5_slot050_decoupled26_ceiling4096_q4kv_checkpoint.json) |
| `exp93_flint_dense_drafter_qwen08b_slot050_decoupled26_ceiling4096_q4kv_checkpoint` | 50 | 13/50 | 17/50 | [JSON](archive/regraded/exp93_flint_dense_drafter_qwen08b_slot050_decoupled26_ceiling4096_q4kv_checkpoint.json) |
| `exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv_checkpoint` | 50 | 12/50 | 19/50 | [JSON](archive/regraded/exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv_checkpoint.json) |
| `exp95_flint_unsloth_ud_q3kxl_repacked_muge_ngram_mod_slot050_decoupled26_ceiling4096_q4kv_checkpoint` | 50 | 12/50 | 17/50 | [JSON](archive/regraded/exp95_flint_unsloth_ud_q3kxl_repacked_muge_ngram_mod_slot050_decoupled26_ceiling4096_q4kv_checkpoint.json) |

See [evaluation methods](docs/eval-protocol.md) and [historical deduplication](archive/REGRADED_SUMMARY.md). Throughput, token-equivalence and KL-divergence tools are available, but the presence of a tool is not a completed validation result.
