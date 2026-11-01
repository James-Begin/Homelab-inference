# Records behind the README

The README uses saved runs from repository snapshot `e72afab125d7bb5bf844e1c2d23ff3a204ba1727`. The hardware and tensor observations below were collected during the local project review. The earlier projection/capacity calculation is retained here for reference; its standalone animation is no longer in the README. Current memory-speed labels and the DIMM inventory are documented in [memory-speeds.md](memory-speeds.md).

## Expert size

The recorded file is `Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`. Its `blk.0.ffn_up_exps.weight` tensor has shape `[2048, 512, 256]`, type 202 (`Q4_0_R8`), and stored size 150,994,944 bytes. The last dimension counts experts.

One expert's projection therefore occupies:

```text
2048 × 512 = 1,048,576 quantized weights
1,048,576 / 32 × 18 = 589,824 bytes = 576 KiB
150,994,944 / 256 = 589,824 bytes per expert
```

The recorded metadata is in [talos-observations.json](talos-observations.json). The model metadata came from the earlier Talos GGUF inspection; it was retained during the October 31 cache verification, rather than scanned again. This mixed-quantization file also contains other tensor types.

The 576 KiB comparison does not require the whole projection to be resident at once. It gives the scale of one real projection relative to a core's L2. A moving cache window illustrates processing portions; it is not a measured sequence of cache misses.

## Cache sizes

Read-only `lscpu -C` and cpu0 cache sysfs inspection on Talos, October 31, 2026, recorded:

| Cache instance | Bytes | Binary capacity | Line size |
| --- | ---: | ---: | ---: |
| L1 data, per core | 32,768 | 32 KiB | 64 B |
| L1 instruction, per core | 32,768 | 32 KiB | 64 B |
| L2, per core | 262,144 | 256 KiB | 64 B |
| L3, per socket | 36,700,160 | 35 MiB | 64 B |

There are two separate L3 domains. The 32-byte AVX2 register width describes a different quantity from both line size and cache capacity. Ways, sets, and shared CPU lists are retained in the JSON record.

## Coding results

The [Qwen exp50 run](https://github.com/James-Begin/Homelab-inference/tree/e72afab125d7bb5bf844e1c2d23ff3a204ba1727/logs/runs/code_exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv) uses `Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`. The [Flint exp94 run](https://github.com/James-Begin/Homelab-inference/tree/e72afab125d7bb5bf844e1c2d23ff3a204ba1727/logs/runs/code_exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv) uses `RecursiveSI_flint-Q4_0_Repacked.gguf`.

Each directory contains `manifest.json`, `summary.json`, `samples.jsonl`, and `samples_eval_results.json`. The regenerated summaries supply mean decode rates and elapsed times. Rate means require finite positive saved rates and more than one generated token: Qwen uses 163 rows, excluding the one-token `HumanEval/111` response, and Flint uses 164. All 164 tasks remain in scoring and elapsed times. The README counts a task as passing when its saved result has both `base_status == "pass"` and `plus_status == "pass"`.

| Aggregation | Qwen | Flint |
| --- | ---: | ---: |
| Base tests pass | 109/164 | 159/164 |
| Extra tests pass, counted alone | 107/164 | 149/164 |
| Both base and extra tests pass | 106/164 | 148/164 |

The last row is the combined success count used in the README and regenerated summaries' `plus_pass_pct`. The original snapshot counted extra-test status alone; regenerated summaries retain that count separately as `extra_only_pass_count`. The selected XOR example comes from each run's `HumanEval/11` saved solution; it is one example rather than an explanation of every failure.

These are two tuned local pipelines. Quantization, prompting, extraction, and serving settings differ. The result does not isolate a model-only effect or a single engine patch.

## Speculation example

The new clip shows the actual history-update guard from [patch 0004](https://github.com/James-Begin/Homelab-inference/blob/e72afab125d7bb5bf844e1c2d23ff3a204ba1727/patches/0004-speculative-decoding-enhancements.patch). Its example uses `i_last = 0`, `cur_len = 8`, and `n = 4`: the old condition `32 < 8` is false, while the new `0 < 4` is true. The loop adds context starts 0 through 3, each with four context tokens and the following token. The final four positions supply the subsequent lookup context.

Labels `h0` through `h7` identify positions, not distinct token IDs. Repeated token values can make a history lookup useful. The animation's indexed positions and successful proposal/acceptance sequence are examples, not a saved token trace.

The full exp94 setting is `ngram-mod:n_max=4,ngram_size_n=4,ngram_min_hits=4`. The inspected MOD implementation uses the four-token context and drafts up to four tokens. Its lookup path does not consult `ngram_min_hits`; that threshold is used by the separate map implementation. The README displays only the relevant context/depth settings and links the full manifest.

The MOD table contains `4 × 1024 × 1024` entries of type `int32_t`: 16 MiB of payload. It is direct mapped and can have hash collisions. That size does not establish cache residency. Any depicted accepted prefix is illustrative; the repo has no token-level trace supporting a specific animation outcome.

## AVX2-kernel prefetch example

The displayed addition is the guarded `_mm_prefetch` in [patch 0002](https://github.com/James-Begin/Homelab-inference/blob/e72afab125d7bb5bf844e1c2d23ff3a204ba1727/patches/0002-avx2-64byte-alignment-and-repacking.patch). `ix` advances by eight output rows, `nrc_x` is the row count, and `bx` is the byte stride used to address those rows. The illustrative 24-row loop visits starts 0, 8, and 16. At the last group, `16 + 8 < 24` is false.

The hint targets the cache line containing the next group's starting address. It does not prefetch all eight rows or guarantee residency. The cache fill and overlapping compute shown are schematic. The prefetch is an x86 cache hint added inside an existing AVX2 kernel; the upstream vector arithmetic is not presented as newly written code.


## Qwen-to-Flint attention animation

The additional clip uses pinned model configurations and patch 0003. [The architecture note](flint-attention.md) gives the layer indices, sliding-window count, and RoPE behavior. It explains graph support, rather than assigning the coding-test difference to a particular architecture choice.
