# Kernel Patches & Engine Modifications

This directory contains standalone, self-describing patches applied to upstream [`ik_llama.cpp`](https://github.com/ikawrakow/ik_llama.cpp) (pinned upstream SHA: `87fc8701`).

Together, these patches provide the foundational performance gains demonstrated across this repository.

---

## Patch Index

### 1. `0001-moe-k-split-thread-partitioning.patch`
- **Component:** `ggml/src/iqk/iqk_mul_mat.cpp`
- **Problem:** When decoding tokens on Mixture-of-Experts (MoE) architectures with small active expert counts $N_x$ (e.g. 6–8 active routed experts per token) on 28-core dual-socket Broadwell systems, assigning one thread per expert leaves $28 - N_x$ cores completely idle. Under an 8-expert routing pass, 20 out of 28 cores sit idle, capping CPU utilization at ~28.5%.
- **Solution:** Implements an inner-dimension ($K$-split) thread partitioning strategy. When active experts $N_x < n_{\text{threads}}$, the matrix reduction dimension $K$ is partitioned across multiple worker threads per expert with a thread-local aligned accumulator reduction.
- **Measured Effect:** Increases physical core utilization across all 28 cores from 28% to **100%**, lifting single-token MoE decode throughput by **+35% to +60%** across Qwen 35B and Flint 40B.

### 2. `0002-avx2-64byte-alignment-and-repacking.patch`
- **Component:** `ggml/src/ggml.c`, `ggml-quants.c`, `iqk_gemm_kquants.cpp`, `iqk_gemm_legacy_quants.cpp`
- **Problem:** On Intel Broadwell microarchitecture (AVX2 + FMA3), 256-bit vector memory instructions crossing 64-byte L1/L2 cache line boundaries incur severe unaligned load penalties and DDR4 memory channel stalls.
- **Solution:** Enforces strict 64-byte alignment on all intermediate thread scratch allocations (`AlignedBuffer`) and repacked matrix row strides. Integrates with Kawrakow's AVX2 repacking layout (`Q4_0_R8`, `Q3_K_R4`).
- **Measured Effect:** Eliminates cross-cache-line split loads, yielding a consistent **+6.5% to +8.5%** throughput uplift at zero additional memory cost.

### 3. `0003-flint-40b-moe-architecture-port.patch`
- **Component:** `src/graphs/build_flint.cpp`, `llama-arch.*`, `llama-vocab.*`, `llama-hparams.*`, `llama-model.cpp`, `llama-load-tensors.cpp`
- **Problem:** Recursive Flint 40B MoE (A2.5B active, 256 fine-grained routed experts + 2 shared experts, 49 layers) was unparseable by `ik_llama.cpp`, restricting execution to upstream `llama.cpp` at ~9.97 t/s.
- **Solution:** Full native architectural implementation:
  - Custom BPE pre-tokenizer (type 52) matching Flint vocabulary regex and special tokens.
  - Hybrid attention masks (alternating RoPE and sliding window attention every 4th layer) and learned attention sink tensors.
  - Fused Merged Up/Gate Expert GEMM (`-muge 1`) via horizontal tensor stacking (`ffn_gate_up_exps`), halving OpenMP thread barrier launches from 564 to 282 per token decode.
- **Measured Effect:** Boosts Flint 40B decode throughput from **9.97 t/s** (upstream baseline) to **18.42 t/s avg / 27.11 t/s peak** on `Q4_0_R8` (+84.8% speedup).

### 4. `0004-speculative-decoding-enhancements.patch`
- **Component:** `common/speculative.cpp`, `examples/speculative/`
- **Problem:** High-overhead speculative tree structures degrade performance when acceptance rates drop under domain shifts.
- **Solution:** Enhances hash-based n-gram mod speculation (`ngram-mod:4,4`) and adds seamless handling for heterogeneous prompt/draft contexts.
- **Measured Effect:** Enables zero-parameter speculative bursts up to **27+ t/s** without requiring auxiliary GPU draft models.

---

## Applying Patches

To apply all patches onto clean upstream `ik_llama.cpp`:

```bash
git clone https://github.com/ikawrakow/ik_llama.cpp.git
cd ik_llama.cpp
git checkout 87fc8701
git apply /path/to/Homelab-inference/patches/0000-all-homelab-optimizations.patch
```

Alternatively, use [`scripts/build_engine.sh`](../scripts/build_engine.sh) for automated build and validation.
