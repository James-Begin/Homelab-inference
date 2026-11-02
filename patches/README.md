# Engine patches

The historical patches apply to upstream [ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp) at `87fc8701ff4da81a7d2a91ec0695f95eb3066a47`. They preserve the engine changes used in this project. Filenames describe the original grouping; some names overstate or misidentify what the diff does.

These patches reuse upstream quantized arithmetic, repacked formats, merged up/gate operations, and speculation infrastructure. The repository's changes are the local diffs described below. Saved experiments often change several settings, so there is no isolated throughput-gain claim for each patch.

## Historical patch set

| Patch | What the diff changes |
| --- | --- |
| [0001: matrix partitioning and scratch buffer](0001-moe-k-split-thread-partitioning.patch) | Guards empty row assignments, adds a 64-byte-aligned scratch-buffer wrapper, and adds a path that partitions output rows/columns across workers for small shapes. `Nx` is an output-row count; this is not a split of the inner reduction dimension and does not assign one thread per expert. |
| [0002: prefetch, alignment, and GGML changes](0002-avx2-64byte-alignment-and-repacking.patch) | Adds prefetch hints in existing AVX2 kernels, separates shared synchronization fields onto cache-line boundaries, changes concat and threshold-sort paths, and adds operation timing. It does not implement the upstream R8 format or guarantee that every subsequent vector load avoids a cache-line split. |
| [0003: Flint port](0003-flint-40b-moe-architecture-port.patch) | Adds architecture registration, metadata and tensor loading, the Flint BPE pre-tokenizer, and a graph with per-layer sliding masks and RoPE choices, initial dense layers, and later MoE branches. Uses the upstream merged up/gate path. |
| [0004: n-gram and compatibility changes](0004-speculative-decoding-enhancements.patch) | Updates the MOD n-gram history as new contexts become available, relaxes BOS-ID comparison when no BOS is added, adjusts example batch sizing, supports hexadecimal escapes in Jinja strings, and relaxes a matrix example's relative sum tolerance from `1e-6` to `0.02`. |
| [0005: chat-parser fallback](0005-catch-server-peg-parser-exception.patch) | Preserves raw content when PEG/chat parsing fails and catches parser exceptions in the server chat path. |
| [0006: JSON serialization](0006-fix-server-safe-json-to-str-utf8-truncation.patch) | Uses `safe_json_to_str` in the success-response handler so invalid UTF-8 is replaced during serialization. This can preserve a response containing malformed bytes; it does not repair the original text or prevent every server error. |

[0000](0000-all-homelab-optimizations.patch) is the combined historical diff. Apply it once, or apply patches 0001–0006 in order; do not apply both forms.

[Patch 0007](0007-fix-buffer-capacity-and-moe-partitioning.patch) corrects aligned-buffer capacity accounting, removes the unsafe column-slicing path in favor of block-aligned row partitioning, restores complete threshold sorting, and guards profiling code for builds without the IQK backend. The historical diffs remain intact so the earlier engine can still be identified. Use [build_engine.sh](../scripts/build_engine.sh) and the [reproduction notes](../docs/reproduction.md) for the current build path and regression checks.

## The n-gram change

The MOD history-update guard changes from `i_last + 32 < cur_len` to `i_last < cur_len - n`. The following loop adds each newly available n-token context and its following token. This removes the old 32-position batching threshold; it does not add a four-hit acceptance gate. The target still verifies the proposed draft.

## What is not established

Prefetch is a hint, and its benefit depends on access patterns and the machine. Aligned allocation does not align every offset within a buffer. A parser fallback handles a particular error path, rather than certifying the server against all malformed output. The relaxed matrix-example tolerance is not evidence of exact kernel equivalence. Exact greedy equivalence and per-patch gains require saved checks against fixed target settings; the historical reports do not provide those checks for the whole patch set.
