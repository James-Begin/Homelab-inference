# Coding results: exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv

Saved run: `code_exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv`. Model: `RecursiveSI_flint-Q4_0_Repacked.gguf`.

| Metric | Result |
| --- | ---: |
| HumanEval base | 159/164 (96.95%) |
| HumanEval+ (base and extra) | 148/164 (90.24%) |
| Mean decode rate | 20.77 tokens/s |
| Mean request elapsed time | 109.48 s |
| Sum of request elapsed times | 17955.0 s |

Elapsed times include failed tasks. Decode rates use 164 saved timing rows and exclude 0 rows. A rate must be finite and positive, with more than one generated token. Startup is excluded.

These are local end-to-end configurations, with different quantization, prompting, extraction and serving settings. They do not isolate model architecture or an individual patch.

Regenerated from `rows.jsonl` and `samples_eval_results.json` with `python3 benchmarks/summarize_runs.py --write`. The earlier report counted extra tests alone (149/164); HumanEval+ here requires both base and extra tests. Raw rows, samples, results and manifests are unchanged.
