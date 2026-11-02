# Flint and Qwen attention

The 22-second animation compares the models' attention patterns, then connects Flint's pattern to the graph code in the port. It uses the released model configurations and the saved engine patch.

## Layer layout

| Text trunk | Qwen 3.6 35B | Flint |
| --- | --- | --- |
| Layers | 40 | 49 |
| Attention types | 30 gated linear, 10 full | 35 sliding, 14 full |
| Full-attention layers, zero based | 3, 7, 11, 15, 19, 23, 27, 31, 35, 39 | 0, 1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 48 |
| Position encoding | Partial RoPE in full-attention layers | RoPE in sliding layers; none in full-attention layers |

Qwen's [released configuration](https://huggingface.co/Qwen/Qwen3.6-35B-A3B/blob/7da1103/config.json) lists 40 text layers with three linear-attention layers followed by one full-attention layer. The engine implements the linear path through gated DeltaNet. Its [graph builder](https://github.com/ikawrakow/ik_llama.cpp/blob/87fc8701ff4da81a7d2a91ec0695f95eb3066a47/src/graphs/build_qwen35.cpp#L45-L52) selects the recurrent or standard attention path per layer.

The Talos Qwen GGUF contains 41 blocks because it also carries one multi-token prediction block. The ordinary graph subtracts `nextn_predict_layers`; the saved [Qwen run](https://github.com/James-Begin/Homelab-inference/blob/e72afab125d7bb5bf844e1c2d23ff3a204ba1727/logs/runs/code_exp50_phys_pinning_28threads_repacked_iq4xs_muge_suffix_q4kv/manifest.json#L28) sets that count to one. The animation shows the 40-layer trunk and excludes the prediction block.

Flint's [released configuration](https://huggingface.co/RecursiveSI/flint/blob/2a247be0c0aec895ccb0ac7ca92229ec6df37288/config.json) supplies an explicit 49-layer pattern. Its 35 sliding layers use a **513-position window: the current token and up to 512 previous tokens**. The 14 full-attention layers have no RoPE; their indices match `no_rope_layer_indices`. The [Transformers implementation notes](https://huggingface.co/docs/transformers/main/model_doc/flint) describe the same distinction.

## The port

The port reads Flint's per-layer sliding and RoPE arrays from GGUF metadata, then selects the mask and position-encoding behavior for each layer:

```cpp
const bool is_swa = hparams.swa_layers[il];
const bool do_rope = hparams.has_rope(il);
auto KQ_mask_l = is_swa ? KQ_mask_swa : KQ_mask;
```

These are the actual expressions in [patch 0003, lines 46–48](https://github.com/James-Begin/Homelab-inference/blob/e72afab125d7bb5bf844e1c2d23ff3a204ba1727/patches/0003-flint-40b-moe-architecture-port.patch#L46-L48). The following `build_std_attention` call receives `KQ_mask_l`, the sliding-window length when applicable, and `do_rope`. The [metadata-loading changes](https://github.com/James-Begin/Homelab-inference/blob/e72afab125d7bb5bf844e1c2d23ff3a204ba1727/patches/0003-flint-40b-moe-architecture-port.patch#L258-L271) supply those settings. This snippet covers one part of the port; tokenizer, tensor loading, feed-forward branches, and architecture registration also required changes.

## Reading the motion

The illustrative timeline spans positions 0–1280. The current position moves from 1024 to 1152. A sliding layer's visible window therefore moves from 512–1024 to 640–1152, inclusive. A full causal layer can attend to all earlier positions through the current position. Future positions remain masked in both views.

Older positions fade to show the sliding attention mask. They are not erased from the sequence, and the animation makes no claim about physical KV-cache eviction. The position numbers, selected layer, and motion are an explanatory example rather than a captured inference trace.

The clip omits feed-forward and expert-routing differences to keep the attention change readable. Its travel times do not encode runtime, memory bandwidth, or a measured speedup. The architecture contrast alone does not explain the coding-score difference between the saved runs.
