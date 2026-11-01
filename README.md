# A coding assistant on two 2016 Xeons

I wanted a local coding assistant on Talos, my Dell PowerEdge T630. It has two Xeon E5-2680 v4 CPUs, 28 physical cores, and 256 GB of DDR4. Plenty of room to load a model. Getting answers back quickly took more work.

I spent months tuning Qwen3.6-35B-A3B: thread counts, memory placement, quantization, speculative decoding, and changes to the C++ engine. Then I added support for a newer model, Flint, and got better coding answers at almost the same token rate.

This repo contains the patches, experiment scripts, and saved runs. The engine is [ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp). Its kernels, repacked formats, and speculation implementations are upstream work; I built the experiment tooling, tested configurations on Talos, modified engine and server code, and ported Flint's architecture.

## Which socket owns the memory?

Talos has AVX2, but no AVX-512, VNNI, or AMX. Each socket has its own 35 MiB L3 and local RAM. A core can read RAM attached to either CPU; a read from the other socket crosses QPI, the link between them. Using both sockets gives the model more cores and memory channels, but the threads and pages still need sensible placement.

![Cache hits, local DRAM reads, and remote reads over QPI, labeled with reference latencies and theoretical bandwidth ceilings](docs/media/numa-traffic.gif)

Cache figures are Intel architectural references; RAM and QPI figures are theoretical ceilings. Packet timing is illustrative. [Sources and calculations](docs/memory-speeds.md) · [MP4](docs/media/numa-traffic.mp4).

The current DIMM inventory reports **1866 MT/s across three populated channels per socket**, giving a raw bus ceiling of about **44.8 GB/s per socket**. The CPU's advertised DDR4-2400 maximum assumes four channels. This is a hardware-configuration calculation, rather than measured application read bandwidth.

I compared keeping work and memory on one socket with using both. The [dual-socket configuration](https://github.com/James-Begin/Homelab-inference/blob/e72afab125d7bb5bf844e1c2d23ff3a204ba1727/logs/runs/code_exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv/manifest.json) uses one logical CPU per physical core and interleaves memory pages across both nodes. That spreads the pages around; it does not make every read local.

## Eight rows at a time

I also tested the upstream repacked weight formats. Q4_0_R8 prepares eight rows for the vector kernel: eight two-byte scales, followed by four groups of 32 packed bytes. Each group takes four bytes from each source row.

The tile holds **256 quantized weights in 144 bytes**, before and after repacking. The upstream [repack function](https://github.com/ikawrakow/ik_llama.cpp/blob/87fc8701ff4da81a7d2a91ec0695f95eb3066a47/ggml/src/iqk/iqk_quantize.cpp) changes their order without quantizing them again. The [AVX2 unpacker](https://github.com/ikawrakow/ik_llama.cpp/blob/87fc8701ff4da81a7d2a91ec0695f95eb3066a47/ggml/src/iqk/iqk_gemm_legacy_quants.cpp) reads the packed values in four 32-byte loads.

<details>
<summary>See the upstream eight-row layout</summary>

[![Eight Q4_0 rows gather into a 16-byte scale prefix and four 32-byte groups](docs/media/repack-eight-rows.png)](docs/media/repack-eight-rows.gif)

Repacking preserves the 144-byte total. Row colors track the source rows. Select the image to watch the GIF, or open the [MP4](docs/media/repack-eight-rows.mp4).

</details>

## Prefetching the next eight rows

My [local AVX2 patch](https://github.com/James-Begin/Homelab-inference/blob/e72afab125d7bb5bf844e1c2d23ff3a204ba1727/patches/0002-avx2-64byte-alignment-and-repacking.patch) changes how the kernel requests upcoming weights. In `mul_mat_q4_0_r8_q8_2_avx2`, I added a prefetch for the next eight-row group:

![The current eight-row group is computed while a prefetch hint requests the next group's starting cache line; the final group skips the hint](docs/media/avx2-prefetch.gif)

The added hint is real code. The 24-row example, cache arrival, and timing are illustrative. [MP4](docs/media/avx2-prefetch.mp4).

```diff
         for (int ix = 0; ix < nrc_x; ix += 8) {
+            if (ix + 8 < nrc_x) {
+                _mm_prefetch((const char *)vx + (ix + 8)*bx, _MM_HINT_T0);
+            }
             const block_iq4_nl_r8 * iq4 = (const block_iq4_nl_r8 *)((const char *)vx + ix*bx);
             auto acc1 = _mm256_setzero_ps();
             auto acc2 = _mm256_setzero_ps();
```

The loop advances eight rows at a time. While it processes one group, the added hint requests the cache line containing the next group's starting address. The bounds check skips the request at the last group. It does not fetch the whole group or guarantee that the data will be in L1 when needed. The vector arithmetic and repacked format are upstream; the added lines show my change.

The same patch separates shared barrier counters onto cache-line boundaries:

```cpp
__attribute__((aligned(CACHE_LINE_SIZE))) atomic_int n_barrier;
__attribute__((aligned(CACHE_LINE_SIZE))) atomic_int n_barrier_passed;
```

When cores update different variables on the same cache line, their writes can invalidate each other's cached copies. This is false sharing. Giving these counters separate 64-byte boundaries keeps them from sharing a line, although threads still have to coordinate on each counter. The saved configuration results combine several changes, so they do not establish an isolated speedup for either edit.

## Guess a few tokens, then check them

I tried speculative decoding to get more tokens out of each expensive verification step. A cheaper mechanism proposes a continuation; the main model checks it and keeps an accepted prefix. Bad guesses add work, so draft acceptance matters.

The Qwen experiments included MTP, which uses an auxiliary prediction head. The saved Flint exp94 run uses the engine's history-based `ngram-mod` lookup instead. These are the relevant settings from its [manifest](https://github.com/James-Begin/Homelab-inference/blob/e72afab125d7bb5bf844e1c2d23ff3a204ba1727/logs/runs/code_exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv/manifest.json):

```text
--spec-type ngram-mod:n_max=4,ngram_size_n=4
```

It looks up a four-token context and proposes up to four continuation tokens for verification. One [local change](https://github.com/James-Begin/Homelab-inference/blob/e72afab125d7bb5bf844e1c2d23ff3a204ba1727/patches/0004-speculative-decoding-enhancements.patch) updates the history table as new n-grams become available, replacing the old chunk guard:

![The old history guard rejects an eight-token example; the new guard adds four available contexts, then lookup proposes tokens for Flint to verify](docs/media/draft-and-verify.gif)

The guard change and settings are from the repo; token positions and the acceptance outcome are examples. [MP4](docs/media/draft-and-verify.mp4).

```diff
- if (i_last + 32 < cur_len) {
+ if (i_last < cur_len - n) {
```

Speculation also produced some misleadingly good numbers. [Experiment 42](https://github.com/James-Begin/Homelab-inference/blob/e72afab125d7bb5bf844e1c2d23ff3a204ba1727/logs/raw_checkpoints/exp42_phys_pinning_28threads_suffix_pmin015_burst16_q4kv_checkpoint.json) includes a roughly 66-token/s result whose output falls into repeated punctuation and supplies no parsed answer. I had made punctuation very fast.

There were less entertaining failures in the serving path. Malformed UTF-8 could make JSON serialization throw after generation. [Patch 0006](https://github.com/James-Begin/Homelab-inference/blob/e72afab125d7bb5bf844e1c2d23ff3a204ba1727/patches/0006-fix-server-safe-json-to-str-utf8-truncation.patch) switches from `data.dump()` to `safe_json_to_str(data)`, which substitutes replacement characters for malformed bytes. I also patched a [parser exception path](https://github.com/James-Begin/Homelab-inference/blob/e72afab125d7bb5bf844e1c2d23ff3a204ba1727/patches/0005-catch-server-peg-parser-exception.patch).

## Flint needed an engine port

Trying Flint meant implementing its architecture in this engine build: metadata and tensor loading, vocabulary handling, and the computation graph. Qwen uses gated linear attention in 30 of its 40 layers and full attention in the other 10. Flint uses a 513-position sliding window in 35 of its 49 layers, with full attention in the other 14.

Flint's sliding layers apply rotary position embeddings (RoPE); its full-attention layers skip them. The graph has to select both the attention mask and the RoPE setting for each layer:

![Qwen and Flint's exact attention-layer patterns, followed by Flint switching between a 513-position sliding window with RoPE and full causal attention without RoPE](docs/media/flint-vs-qwen.gif)

The window includes the current position and the previous 512. Layer patterns and settings are exact; context positions and motion are illustrative. [Architecture sources](docs/flint-attention.md) · [MP4](docs/media/flint-vs-qwen.mp4).

These lines from the [port](https://github.com/James-Begin/Homelab-inference/blob/e72afab125d7bb5bf844e1c2d23ff3a204ba1727/patches/0003-flint-40b-moe-architecture-port.patch) make those choices:

```cpp
const bool is_swa = hparams.swa_layers[il];
const bool do_rope = hparams.has_rope(il);
auto KQ_mask_l = is_swa ? KQ_mask_swa : KQ_mask;
```

The port let me run Flint with the upstream repacked kernels and merged up/gate path. I could then evaluate it with the same experiment tooling used for Qwen.

## About 21 tokens a second, either way

These are the saved [Qwen exp50](https://github.com/James-Begin/Homelab-inference/tree/e72afab125d7bb5bf844e1c2d23ff3a204ba1727/logs/runs/code_exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv) and [Flint exp94](https://github.com/James-Begin/Homelab-inference/tree/e72afab125d7bb5bf844e1c2d23ff3a204ba1727/logs/runs/code_exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv) coding runs, each covering 164 tasks:

| Metric | Qwen3.6-35B-A3B | Flint 40B |
| --- | ---: | ---: |
| Mean decode rate | 21.31 tokens/s | 20.77 tokens/s |
| Mean elapsed time per task | 194.41 s | 109.48 s |
| Tasks passing both HumanEval base and extra tests | 106/164 | 148/164 |

These compare two locally tuned pipelines, with different quantization, prompting, extraction, and serving settings. Elapsed time includes failed tasks. The Qwen rate excludes one single-token response with an unusable saved timing; all 164 tasks remain in pass counts and elapsed times. Flint uses 164 timing rows. Pass counts above require both test sets to pass, counted from the saved per-task outcomes.

On one selected task, `HumanEval/11`, the model has to XOR two binary strings while preserving their width. Qwen's saved answer converts through integers:

```python
return bin(int(a, 2) ^ int(b, 2))[2:]
```

For inputs `"01"` and `"01"`, that returns `"0"`; the expected answer is `"00"`. Flint's saved answer pads the strings and compares their characters, preserving the leading zero.

After all that Qwen tuning, Flint emitted tokens slightly more slowly and still finished tasks sooner, with more answers passing the tests. Getting Flint running took the architecture port; the Xeons stayed put.

## Code and records

- [Setup and regression checks](docs/reproduction.md), including the [build script](scripts/build_engine.sh)
- [Engine and server patches](patches/README.md), including [native corrections added after these runs](patches/0007-fix-buffer-capacity-and-moe-partitioning.patch)
- [Benchmark scripts](benchmarks/) and [saved experiment records](logs/runs/)
- [Results and measurement limits](RESULTS.md)
- [Historical experiments](archive/README.md)
- [Animation source and render instructions](animations/README.md)
