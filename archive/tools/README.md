# Retired tools

These scripts are preserved from the benchmark-era repository at `e72afab125d7bb5bf844e1c2d23ff3a204ba1727`. They are excluded from the supported setup and CI. Some contain hard-coded host paths, old directory assumptions, or incomplete checks.

| Files | Why they were retired |
| --- | --- |
| `run_stage1.py`, `run_stage2.py`, `run_stage3.py`, `run_gpqa_16k.py`, `run_16k_probe.py` | One-off campaign launchers that duplicate the task runners and embed old launch settings. |
| `master_watchdog_pipeline.py` | Watches legacy checkpoint paths while the current runner writes per-run JSONL records. Its restart behavior does not match the maintained harness. |
| `run_ablation_sweep.py` | Preserves the actual six-prompt configuration sequence behind the historical waterfall. It changes several settings and is not a fixed-weight engine ablation. |
| `bytes_per_token.py` | Chooses hard-coded byte totals from a filename, with an all-layer KV estimate. It does not inspect a GGUF or measure DRAM traffic. |
| `make_figures.py` | Uses hard-coded arrays, including unsupported roofline and workload claims. The old SVGs remain in [archive/figures](../figures/). |

The six duplicated ablation prompt files were byte-identical to the corresponding files in [the throughput corpus](../../benchmarks/prompts/tput/). Their original paths can be recovered from the historical commit.

Use [the current setup](../../docs/reproduction.md) for supported commands. The archived scripts are records of what was tried; their relocated paths are not intended to be executable entry points.
