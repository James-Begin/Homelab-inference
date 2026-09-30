# Homelab Inference

Qwen 3.6 35B-A3B on a 2016 Dell PowerEdge T630. Two Xeon E5-2680 v4s, AVX2 only, no AMX, and one socket of DDR4-2400. This repo is the lab notebook for getting that box to serve a long-context coding model at more than 20 tokens per second.

[Writeup](docs/writeup.md) · [Substack](https://open.substack.com/pub/james908142/p/teaching-an-old-xeon-new-tricks-a) · [Full results](RESULTS.md)

## Hardware

| | |
| --- | --- |
| **Machine** | Dell PowerEdge T630 |
| **CPUs** | 2× Intel Xeon E5-2680 v4, 14 cores / 28 threads, 35 MB L3, AVX2 and FMA3 |
| **Memory** | 4-channel DDR4-2400 per socket, 76.8 GB/s theoretical on one node |
| **Engine** | [ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp) |
| **Model** | Qwen3.6-35B-A3B, mixture-of-experts, about 3B parameters active per token |

A dense 35B model at Q6_K is about 27 GB of weights. One socket can stream that once in roughly a third of a second, which is under 3 tokens per second. The model is runnable here because each token only pulls a few experts through RAM.

## Results

The standardized runs are GPQA Diamond, 50 questions, 1,536 token ceiling. Earlier sweeps used 20 questions and a 384 token cap, so those scores are a different test. Every figure in this section is taken from the report files, which are tabulated in [RESULTS.md](RESULTS.md).

| | Run | Avg generation | GPQA |
| --- | ---: | ---: | ---: |
| Single-NUMA baseline | 0 | 11.16 t/s | 16 / 50 |
| Best accuracy | 5 | 19.26 t/s | 22 / 50 |
| Fastest average that held the baseline score | 46 | 22.50 t/s | 16 / 50 |
| Best later score | 47, 48, 50 | 21.30–21.33 t/s | 18 / 50 |

The highest peak in the 50-question set is **66.30 t/s** on run 42, at 14 / 50. Deeper suffix drafts are what produce those bursts, and they give the score back.

Every needle ladder that reached 128K context passed. Generation after that prompt sits around 8 t/s on the 28-thread runs. The single-NUMA baseline ladder passed 16K, 32K, and 64K and was not run at 128K. The writeup's separate short bench, with active experts cut from 8 to 4, measured **24.53 t/s**. That pass is not the GPQA protocol above.

## Config that held the later score

Run 50 is the repacked form of the 18 / 50 cluster: IQ4_XS attention, Q4_0 experts, merged up/gate, suffix speculation (`n_max=8`, match 5), native MTP, Q4_0 KV cache. **18 / 50**, **21.33 t/s** average, **38.23 t/s** peak. Runs 47 and 48 scored the same 18 / 50 without the offline repack.

`PHYS` is the 28 physical cores, SMT siblings left out.

```bash
PHYS=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27

numactl --interleave=all --physcpubind=$PHYS \
  "$IK_LLAMA_HOME/build/bin/llama-server" \
  -m "$IK_LLAMA_HOME/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf" \
  --port 8087 -c 8192 -t 28 -tb 28 \
  -ctk q4_0 -ctv q4_0 \
  --defer-experts --numa distribute -fa 1 \
  -ser 2,0.5 --slot-prompt-similarity 0.0 -muge \
  --spec-type suffix:n_max=8,suffix_min_match_len=5,suffix_max_depth=48 \
  --override-kv qwen35moe.nextn_predict_layers=int:1 \
  --spec-type mtp:n_max=1,p_min=0.0
```

The repacked GGUF is produced with `llama-quantize --repack` from `Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0.gguf`. The harness does that when the file is missing.

## What moved the number

From the [writeup](docs/writeup.md), in the order they mattered on that bench:

1. **Active experts, 8 to 4.** About a 2× decode jump (12.22 to 24.53 t/s). Two experts was worse, because speculation stopped accepting drafts.
2. **Speculation matched to the text.** N-gram and suffix caches are free on code. Native MTP is the reliable fallback. A separate 0.8B drafter lost to memory contention, and run 56 crashed the server. The [postmortem](logs/gpqa_reports/gpqa_exp56_cascade_draft08b_postmortem.md) is in the reports.
3. **Threads split by phase.** SMT helps prefill. Physical cores help decode. The later campaign pinned 28 physical cores and left SMT off.
4. **Quantize the experts, and repack for AVX2.** Runtime repack was an early free 6.8%. Offline repack (run 50) kept the run 47 score.
5. **Deeper drafts are not free.** Suffix `n_max` of 12 to 16 posted the highest peaks and dropped GPQA as low as 12 / 50.

## Repository

| Path | What it is |
| --- | --- |
| [RESULTS.md](RESULTS.md) | Every scored run, read from the report files |
| [docs/writeup.md](docs/writeup.md) | The long writeup |
| [logs/gpqa_reports/](logs/gpqa_reports/) | Per-question GPQA reports |
| [logs/extreme_context_reports/](logs/extreme_context_reports/) | 16K–128K needle ladders |
| [logs/optimization_tracker/optimization_log_50tps.md](logs/optimization_tracker/optimization_log_50tps.md) | Lab notebook |
| [logs/raw_checkpoints/](logs/raw_checkpoints/) | Per-question JSON and the 50-question set |
| [benchmarks/experiments.json](benchmarks/experiments.json) | One entry per eval: model, flags, and any quantize or repack step |
| [benchmarks/gpqa_eval.py](benchmarks/gpqa_eval.py) | The runner |

## Run a benchmark

Point `IK_LLAMA_HOME` at a local ik_llama.cpp checkout with `build/bin` and `build/models`. The GGUF names are the ones in the catalog.

```bash
export IK_LLAMA_HOME="$HOME/ik_llama.cpp"
python benchmarks/gpqa_eval.py --list
python benchmarks/gpqa_eval.py --exp 50 --dry-run
python benchmarks/gpqa_eval.py --exp 50
```

A run resumes from `logs/raw_checkpoints/<id>_checkpoint.json` and writes its report under `logs/gpqa_reports/`. Needle ladders:

```bash
python benchmarks/benchmark_extreme_context.py --help
```

`benchmarks/master_watchdog_pipeline.py` walks `logs/raw_checkpoints/pipeline_queue.json` on the homelab. It restarts a stalled GPQA run through `systemd --user`, then launches the needle ladder for that config.
