# Coding results: exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv

Saved run: `code_exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv`. Model: `Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`.

| Metric | Result |
| --- | ---: |
| HumanEval base | 109/164 (66.46%) |
| HumanEval+ (base and extra) | 106/164 (64.63%) |
| Mean decode rate | 21.31 tokens/s |
| Mean request elapsed time | 194.41 s |
| Sum of request elapsed times | 31883.5 s |

Elapsed times include failed tasks. Decode rates use 163 saved timing rows and exclude 1 rows. A rate must be finite and positive, with more than one generated token. Startup is excluded.

These are local end-to-end configurations, with different quantization, prompting, extraction and serving settings. They do not isolate model architecture or an individual patch.

Regenerated from `rows.jsonl` and `samples_eval_results.json` with `python3 benchmarks/summarize_runs.py --write`. The earlier report counted extra tests alone (107/164); HumanEval+ here requires both base and extra tests. Raw rows, samples, results and manifests are unchanged.
