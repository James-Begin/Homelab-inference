# Qwen and Flint

The saved coding runs compare the Qwen configuration I tuned with the Flint configuration I later ported to `ik_llama.cpp`. Flint passed more tasks while decoding at almost the same rate. The runs also differ in quantization, prompts, extraction, and serving settings, so the comparison describes these local pipelines. It does not isolate architecture as the cause of the result.

## The saved coding runs

| Metric | Qwen, experiment 50 | Flint, experiment 94 |
| --- | ---: | ---: |
| Tasks | 164 | 164 |
| Base tests passed | 109/164 | 159/164 |
| Base and extra tests passed | 106/164 (64.63%) | 148/164 (90.24%) |
| Mean decode rate | 21.31 tokens/s | 20.77 tokens/s |
| Mean elapsed time per task, including failures | 194.41 s | 109.48 s |

HumanEval+ success requires a task to pass both its base and extra tests. Earlier summaries counted the extra-test status alone, giving 107 and 149; those are different totals.

The records are in the [Qwen run directory](../logs/runs/code_exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv/) and [Flint run directory](../logs/runs/code_exp94_flint_ik_llama_muge_repacked_ngram_mod_slot050_decoupled26_ceiling4096_q4kv/). Each includes the manifest, samples, and EvalPlus output. See [the evaluation notes](eval-protocol.md) for metric definitions and limitations. These runs are single-sample task evaluations, not estimates over repeated model seeds.

## What changed in the model

| Text trunk | Qwen 3.6 35B | Flint |
| --- | --- | --- |
| Feed-forward blocks | 40 MoE | 2 dense, then 47 MoE |
| Attention | 30 gated linear, 10 full | 35 sliding, 14 full |
| Routed experts per MoE layer | 256 | 256 |
| Routed experts selected | Released model: 8; saved local GGUF: 4 | 6 |
| Routed expert intermediate width | 512 | 512 |
| Shared branch intermediate width | 512 | 1024 |
| Sliding window | — | Current token and up to 512 previous positions |

Flint's shared branch is one width-1024 feed-forward branch. Calling it “two shared experts” obscures how the port represents it. Qwen's saved four-expert setting is also a change to the released target behavior; it should not be described as a lossless kernel optimization.

Qwen uses gated DeltaNet for three out of each four text layers, followed by a full-attention layer. Its GGUF also carries a prediction block; that is separate from the 40-layer text trunk shown here. Flint uses an explicit per-layer attention pattern. Its full-attention layers are indices `0, 1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 48`. The other 35 use sliding attention with RoPE. Flint's full-attention layers omit RoPE.

The [attention note](flint-attention.md) links the released configurations and explains the animation. It covers mask selection and position encoding without claiming that those differences explain the coding-score gap.

## What the Flint port adds

[Patch 0003](../patches/0003-flint-40b-moe-architecture-port.patch) registers Flint's architecture, reads its metadata and tensors, adds its BPE pre-tokenizer, and builds its graph. The graph chooses each layer's attention mask and RoPE behavior, handles the initial dense feed-forward layers, and connects later MoE layers to the engine's expert operations.

The port reuses upstream quantized kernels and the merged up/gate expert path. It does not introduce Q4_0_R8, MUGE, or the speculation framework. Experiments that change engine, layout, batching, and speculation together cannot attribute their whole throughput difference to the architecture patch.

The README uses the coding runs above as its result. Older GPQA and time-budget reports remain in the run history. Their prompt, parsing, token-ceiling, and artifact differences need to be checked before using them for another headline comparison; no claim of statistical significance is made here.
