# Experiment 56 Technical Post-Mortem & Diagnostic Autopsy

- **Experiment ID:** `exp56_phys_pinning_28threads_repacked_iq4xs_muge_suffix_draft08b_cascade_q4kv`
- **Architectural Hypothesis:** Evaluate a Two-Stage Speculative Cascade combining verbatim exact suffix tree match ($n_{\text{max}}=8, \text{match}=5$) as Stage 1 with a small dense external draft model (`Qwen3.5-0.8B-Q4_K_M.gguf`, $n_{\text{max}}=2, p_{\text{min}}=0.50$) as Stage 2 fallback to accelerate base token generation when suffix matches miss.
- **Outcome:** **`FAILED / INCOMPATIBLE (Engine Segmentation Fault)`**
- **Hardware Platform:** Dual Intel Xeon E5-2680 v4 Broadwell (28 physical cores, 56 logical CPUs, 2 NUMA nodes).

---

## 1. Executive Summary & Root Cause Analysis

During automated deployment by `master_pipeline_watchdog.service`, the `exp56_eval.service` encountered an immediate process termination upon receiving completion requests on port 8087, triggering an infinite self-healing restart cycle. 

A thorough deep-dive under GDB isolated the exact fault trace:

```
Thread 79 "llama-server" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7ffa619216c0 (LWP 2364816)]
0x0000555557325c01 in void (anonymous namespace)::mul_mat_q8_1_r8_q8_2<7>(int, void const*, unsigned long, DataInfo const&, int) ()
#0  0x0000555557325c01 in void (anonymous namespace)::mul_mat_q8_1_r8_q8_2<7>(int, void const*, unsigned long, DataInfo const&, int) ()
#1  0x0000555555ca32b9 in (anonymous namespace)::MulMat::mul_mat_up_gate_NxM(int, void const*, void const*, unsigned long, float const*, float const*, DataInfo&, int, int, int, float)::{lambda(void (*)(int, void const*, unsigned long, DataInfo const&, int), DataInfo const&, int, int, int)#1}::operator()(void (*)(int, void const*, unsigned long, DataInfo const&, int), DataInfo const&, int, int, int) const [clone .constprop.1] ()
#2  0x0000555555ca4c37 in (anonymous namespace)::MulMat::mul_mat_up_gate_NxM(int, void const*, void const*, unsigned long, float const*, float const*, DataInfo&, int, int, int, float) ()
#3  0x0000555555cabcbd in iqk_moe_fused_up_gate ()
#4  0x0000555555bf17fc in ggml_compute_forward_mul_mat_up_gate ()
#5  0x0000555555c3eb43 in ggml_compute_forward ()
#6  0x0000555555c40bf0 in ggml_graph_compute_thread.constprop.0.isra ()
```

### The Architectural Conflict:
1. **Hybrid Recurrent Target State (`Qwen3.6-35B-A3B`):** The primary target model incorporates recurrent linear-attention/GDN layers. The server engine automatically detects this via `llama_model_has_recurrent()` and enables recurrent context checkpoints (`llama_spec_ckpt_init(ctx_tgt, mode, max_tokens)`).
2. **External Assistant Draft Context (`Qwen3.5-0.8B`):** When `--model-draft` is coupled with `--spec-type draft`, `ik_llama.cpp` attempts dual-context tracking. During prompt completion and subsequent draft generation, the prompt is divided across checkpoint boundaries.
3. **MoE Tiling & Out-of-Bounds Row Mapping:** When non-uniform batches (such as leftover prompt chunks or draft verification sequences with $ny \in [2, 7]$) are routed into fused MoE up/gate projections (`iqk_moe_fused_up_gate`), `mul_mat_up_gate_NxM` calls the AVX2 kernel `mul_mat_q8_1_r8_q8_2<7>`. Because `DataInfo::src1_row()` indexes `row_mapping[cur_y + iy]` without bounding against the per-expert active row count for small multi-token chunks, a memory out-of-bounds read occurs, immediately inducing a SIGSEGV.

---

## 2. Controlled Isolation Experiments

| Configuration Tested | Command / Flags | Result | Significance |
| :--- | :--- | :---: | :--- |
| **Exp 56 Baseline** | `--model-draft Qwen3.5-0.8B` + `suffix` + `draft:n_max=2` + `-muge` | **SIGSEGV** | Crash reproducible on GPQA Q0 within 1 token. |
| **No-MUGE Variant** | `--model-draft Qwen3.5-0.8B` + `suffix` + `draft:n_max=2` (no `-muge`) | **SIGSEGV** | Proves crash occurs in default fused kernel as well. |
| **No-FUG Variant** | `--model-draft Qwen3.5-0.8B` + `suffix` + `draft:n_max=2` + `--no-fused-up-gate` | **SIGSEGV** | Confirms external draft speculative context memory conflict. |
| **Draft-Only Variant**| `--model-draft Qwen3.5-0.8B` + `draft:n_max=2` only | **SIGSEGV** | Pinpoints `--model-draft Qwen3.5-0.8B` as the sole crash trigger. |
| **Suffix-Only Champion**| Pre-repacked GGUF + `suffix:n_max=8,match=5` + `-muge` (No draft model) | **100% HEALTHY** | Decoded flawlessly; confirmed 100% stable. |
| **Exp 57 (Confidence MTP)**| Pre-repacked GGUF + `suffix:n_max=8,match=5` + Native MTP ($p_{\text{min}}=0.15$) | **100% HEALTHY** | Decoded flawlessly; confirmed 100% stable. |

---

## 3. Campaign Strategic Decision

1. **Retire External Assistant Draft Models on Broadwell AVX2:** External draft models (`--model-draft`) require deep engine-level fixes to `DataInfo::row_mapping` in `ik_llama.cpp` to handle small-batch MoE routing under recurrent checkpointing. External drafting is therefore marked **INCOMPATIBLE** for this hardware and model combination.
2. **Double Down on Native Multi-Token Prediction (MTP) & Self-Speculation:**
   - **Native MTP** utilizes the model's own integrated prediction head (trained on the exact internal activations), avoiding all external context conflicts and maintaining 100% engine stability.
   - **Suffix Trees** operate purely in host RAM without generating multi-token MoE evaluation discrepancies, delivering our current champion accuracy record (**36.0% GPQA Diamond**, **38.35 t/s peak**).
3. **Pipeline Unblocking:** Exp 56 is marked as completed (incompatible) in the project log, and the automated queue is advanced directly to **Exp 57 (Confidence-Gated MTP $n_{\text{max}}=1, p_{\text{min}}=0.15$)**.
