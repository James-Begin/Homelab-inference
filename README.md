# Homelab Inference

Qwen 3.6 35B-A3B on a 2016 Dell PowerEdge T630. Two Xeon E5-2680 v4s, AVX2 only, no AMX, and one socket of DDR4-2400. This repo is the lab notebook for getting that box to serve a long-context coding model at more than 20 tokens per second.

[What moved the tokens](#what-moved-the-tokens) · [Writeup](docs/writeup.md) · [Substack](https://open.substack.com/pub/james908142/p/teaching-an-old-xeon-new-tricks-a) · [Full results](RESULTS.md)

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

## What moved the tokens

Decode on this box is a bandwidth problem. Each token has to pull its active weights out of DDR4, so the changes that mattered either move fewer bytes or get more than one token out of one trip to RAM. The sweeps that did nothing, and the reasoning behind the ones that did, are in the [writeup](docs/writeup.md).

| Change | Result |
| --- | --- |
| Active experts, 8 → 4 | 12.22 → 24.53 t/s on the short bench |
| MoE kernel split across idle cores | Decode utilization 28% → 100% |
| Q6_K attention, Q4_0 experts | 8.33 → 10.50 t/s, speculation off |
| IQ4_XS attention, Q4_0 experts | 22.50 t/s, GPQA 16 / 50 (run 46) |
| AVX2 tensor repack | +6.75%, no extra RAM |
| N-gram lookup in place of a neural draft | 12.91 → 15.89 t/s on that sweep |

### Active experts, 8 to 4

The largest single jump. Qwen 3.6 35B routes each token through 8 experts by default. Clamping that to the router's top 4 halves the expert traffic and the FFN math, and llama.cpp renormalizes the surviving weights so the layer's scale stays put.

```bash
--override-kv qwen35moe.expert_used_count=int:4
```

The architecture string is `qwen35moe`. On the short bench this went from 12.22 t/s to **24.53 t/s**. Two experts came out at 11.80 t/s, because the draft acceptance rate collapsed. Runs 46 through 50 leave the expert count at the model default. That 24.53 is a different measurement.

### The MoE kernel was leaving cores idle

With 4 experts and 14 threads, `iqk_mul_mat.cpp` handed each thread a whole expert row. Threads 0–3 each got one expert. Threads 4–13 got nothing: 10 of 14 physical cores idle in the phase that dominates generation.

```cpp
auto nrc_x = (Nx/num_rows + nth - 1)/nth;   // Nx=4, nth=14 → nrc_x = 1
```

The local patch is in that file, which is not part of this repo. When there are fewer expert rows than threads, the threads form a group per row and each one owns a slice of K, about 4096 features. With `nth / Nx == 3`, three threads share an expert. Each writes a partial dot, and one of them reduces the group after the barrier.

```cpp
// Nx = 4 expert rows, nth = 14 threads, ith = this thread.
// K is the dot-product length of one expert row.
if (Nx < nth) {
    const int threads_per_row = nth / Nx;             // 3
    const int row_idx         = ith / threads_per_row;
    const int group_tid       = ith % threads_per_row;
    if (row_idx >= Nx) {
        return;
    }

    const int k_per = K / threads_per_row;
    const int k0    = group_tid * k_per;
    const int k1    = (group_tid + 1 == threads_per_row) ? K : k0 + k_per;

    // w[] and the scratch row are 64-byte aligned. An AVX2 load is 32 bytes
    // and a cache line is 64, so the load stays inside one line.
    float partial = dot_i8(w[row_idx] + k0, x + k0, k1 - k0);
    group_partial[row_idx][group_tid] = partial;

    barrier();
    if (group_tid == 0) {
        float sum = 0.f;
        for (int t = 0; t < threads_per_row; ++t) {
            sum += group_partial[row_idx][t];
        }
        y[row_idx] = sum;
    }
}
```

Utilization during MoE decode went from 28% to 100%. Generation was already near the memory ceiling, so the tokens-per-second change was modest. The alignment pass on the scratch buffers and row strides was +1.5% prompt processing and +2.1% cached prompt processing. The longer account is in the [kernel section](docs/writeup.md#5-patching-the-kernel-directly) of the writeup.

`dot_i8` is the existing Broadwell sequence in [iqk_gemm_legacy_quants.cpp](https://github.com/ikawrakow/ik_llama.cpp/blob/main/ggml/src/iqk/iqk_gemm_legacy_quants.cpp). `_mm256_maddubs_epi16` wants one unsigned operand and one signed, and it accumulates adjacent products into a 16-bit lane. Offsetting both sides by 128 makes one product 255 × 127 = 32,385, already past the signed 16-bit limit of 32,767. `w·x = |w| · (x · sign(w))` keeps each product at most 127 × 127 = 16,129, and two of them sum to 32,258. In `SignedDot` the first argument is the weight: `_mm256_sign_epi8(x, x)` is its absolute value, and the second `sign` paints that sign onto the activation. The widening `_mm256_madd_epi16` by 1 then lifts the 16-bit pairs into 32-bit lanes. There is no VNNI on this chip, so this is the whole int8 dot product.

```cpp
struct DotHelper {
    const __m256i m1 = _mm256_set1_epi16(1);
    inline __m256i dot(__m256i x, __m256i y) const {
        return _mm256_madd_epi16(m1, _mm256_maddubs_epi16(x, y));
    }
};

struct SignedDot {
    DotHelper helper;
    inline __m256i compute(__m256i x, __m256i y) const {
        return helper.dot(_mm256_sign_epi8(x, x), _mm256_sign_epi8(y, x));
    }
};
```

### Custom quant: bits on the tensors that are large

Timing each operator from thread 0 put attention matmul at 52% of eval time, MoE up/gate at 39%, and the expert down projection at 21%. The shares overlap at the measurement boundary. Attention and the expert feed-forward are where the time goes, and both are paying the bandwidth bill. The expert tensors are the bulky ones, and each token only touches a few of them.

Q4_K on the dense attention layers was slower. Broadwell's Q4_K unpack costs more CPU than Q6_K, and decode is waiting on RAM. Q4_0 has a tight AVX2 path. Leaving attention at Q6_K and putting the experts in Q4_0 went from 8.33 t/s to **10.50 t/s** (+26%) on a raw eval with speculation off.

The scored campaign took that split further: IQ4_XS on attention and `ssm_out`, Q4_0 on the expert tensors. Run 46, that file plus native MTP, is the fastest average that held the baseline GPQA score: **22.50 t/s**, 16 / 50. The quant is a regex passed to `llama-quantize`:

```bash
llama-quantize --allow-requantize \
  --custom-q '.*attn_.*=iq4_xs,.*ssm_out.*=iq4_xs,.*ffn_.*_exps.*=q4_0' \
  Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf \
  Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0.gguf \
  Q6_K 28
```

The lab notes name the AVX2 kernel that consumes the attention tensors, `mul_mat_iq4_xs_r8_q8_k_avx2`. The same recipe with IQ4_NL (run 49) scored 17 / 50 at 20.91 t/s.

KV cache had its own split. q8_0 plus a Hadamard rotation on K and V reached 14.53 t/s and held accuracy closer to f16, because the rotation smears outliers so one scale factor fits the block. Plain q4_0, without the rotation, was faster still (15.13 t/s) and measurably lossier. The run 50 config takes that speed side: `-ctk q4_0 -ctv q4_0`.

### Repack into the order AVX2 streams

`--run-time-repack` rewrites the tensors in RAM at load, into the byte order the AVX2 dot product walks, instead of the order the GGUF uses on disk. In the early flag sweep that was **+6.75%** and cost no extra memory. It also stopped mixed-precision speculation from rolling back onto a misaligned stride. Run 50 does the rewrite once, offline, and then skips the flag:

```bash
llama-quantize --repack \
  Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0.gguf \
  Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf \
  COPY 28
```

Runs 47 and 48 scored the same 18 / 50 with the repack at load time. The offline file is the one in the config below.

### Speculation that issues no multiply

An n-gram cache, and later a suffix cache, is a lookup against tokens already in the conversation. Source code repeats, so the lookup hits, and it never issues a matmul. On that sweep, n-gram speculation reached 15.89 t/s against 12.91 t/s for MTP alone at `n_max=5`. Native MTP is the fallback when the lookup misses: a small head drafts a token, the main model verifies a batch, and several tokens share one read of the weights. Turning a single MTP head on took an early baseline from 7.96 t/s to 10.61 t/s.

Draft depth has a peak and then a giveback. MTP `n_max=5` was the sweet spot at 14.21 t/s; 6 and 7 were slower. The same shape shows up in the GPQA peaks. Suffix `n_max` of 12 to 16 posted **66.30 t/s** on run 42 (14 / 50) and **66.25 t/s** on run 40 (12 / 50). The config below stays at suffix `n_max=8`, with MTP behind it.

A separate 0.8B drafter on the same bus lost to memory contention, and run 56 segfaulted the server. The [postmortem](logs/gpqa_reports/gpqa_exp56_cascade_draft08b_postmortem.md) is with the reports.

### Threads, split by phase

SMT helped prefill (124.24 t/s at 28 threads, 118.13 t/s at 14 physical) and hurt decode (7.96 t/s with SMT, 8.26 t/s on physical cores). The early setup was `-t 14 -tb 28`. The later campaign pinned all 28 physical cores, left SMT off, and set both knobs to 28, interleaved across both sockets.

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
