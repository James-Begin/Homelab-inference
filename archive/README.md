# Historical experiments

This directory keeps the exploratory runs, old runners, and superseded explanations. Their original wording and measurements are preserved as records. Claims such as “certified,” “lossless,” or “100% utilization” in those files are historical claims, rather than conclusions of the current README.

Start with [the current results](../RESULTS.md) and [evaluation notes](../docs/eval-protocol.md) for the retained comparison and its limits.

| Directory | Contents |
| --- | --- |
| [notebook-v1/raw_checkpoints](notebook-v1/raw_checkpoints/) | Original exploratory checkpoints. Early runs often retain only a preview, so their answers cannot all be regraded. |
| [notebook-v1/gpqa_reports](notebook-v1/gpqa_reports/) | Generated reports from the older question-answering campaign. |
| [notebook-v1/extreme_context_reports](notebook-v1/extreme_context_reports/) | Historical passkey/context reports. These do not establish equivalent server speculation behavior. |
| [notebook-v1/optimization_tracker](notebook-v1/optimization_tracker/) | The running experiment notebook, including failed configurations. |
| [harness](harness/) | Historical runner snapshots recovered from Talos. |
| [regraded](regraded/) | Previously derived strict and lenient grading of runs with saved full text. |
| [docs](docs/README.md) | Superseded writeups and the earlier audit. |
| [figures](figures/) | Old plots whose assumptions or supporting measurements were not established. |
| [tools](tools/README.md) | Retired orchestration and analysis scripts. |
| [plans](plans/) | The earlier implementation plan, including status assertions that did not match the reviewed code. |

The [historical regrade table](REGRADED_SUMMARY.md) is retained separately from the current coding and GPQA results. Regrading text can change an extraction decision; it does not recover missing completions, stopping metadata, or engine provenance.

Compatibility links under `logs/` still point into this archive. The README uses one of them to link experiment 42's punctuation loop. They are aliases, not extra copies of the records.

The cleanup removed two byte-identical copies of the exp94/exp95 context reports from `gpqa_reports/`; their originals remain in `extreme_context_reports/`. The duplicated GPQA subset is kept once at [benchmarks/data/gpqa_subset_50.json](../benchmarks/data/gpqa_subset_50.json). Raw checkpoint responses were not edited.
