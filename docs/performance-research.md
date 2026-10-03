**Homelab inference: where the next substantial gain could come from**

Reviewed October 2, 2026. Scope: keep the Dell T630, both E5-2680 v4 CPUs, and Qwen3.6-35B-A3B. Repository snapshot: `761092b`. Upstream source inspected: ik_llama.cpp `5f89bfc81268b4d56d2af63ccbed59de17c64c09`.

**My recommendation is to stop the suffix-threshold campaign, establish a trustworthy coding baseline, then test NUMA scheduling/locality and corpus-backed speculation.** For a larger engineering project, investigate an expert-cost-aware speculative controller and a CPU backend that keeps work and state local to each socket. Those change the amount or location of work. Most of runs 38–60 rearrange parameters around essentially the same work.

There is credible room for improvement, but the repository does not establish that this machine can sustain 50 useful tokens/sec with unchanged target behavior. Going from 22.5 to 50 requires a 2.22× gain. I would make 30 useful tokens/sec the first milestone and treat 50 as a research objective, measured on held-out coding tasks. These are proposed goals, not predictions.

This review covers the 49 standardized 50-question report files, 45 checkpoint files, early sweeps and technical postmortems, the experiment catalog, benchmark scripts, and pending runs 61–65. The [artifact audit](experiment-audit.md) contains the complete standardized leaderboard and recomputed checkpoint metrics. I did not run inference on the T630; the machine, GGUF files, and customized engine checkout are not part of this repository.

The [audit script](../benchmarks/reproduce_audit.py) reads the saved artifacts and reproduces the parser failure cases without launching inference. From the repository root, run `python3 benchmarks/reproduce_audit.py .` to print the audit. The committed audit reflects the reviewed snapshot; later experiment data or parser fixes may change its output.

**What the experiments actually show**

| Comparison | Published result | Interpretation |
| --- | --- | --- |
| Run 0 → 4 | 11.16 → 15.72 t/s | A major early gain from the dual-socket configuration; historical kernel/config changes prevent calling this a perfectly isolated NUMA experiment. |
| Run 4 → 5 | 15.72 → 19.26 t/s | Native one-token MTP is the strongest demonstrated speculation direction in the standardized early campaign. |
| Runs 15–18 | 18.41–19.17 t/s | SER, barrier/concat changes, and combinations did not produce another step change. |
| Run 24 → 30 | 20.00 → 20.02 t/s | Explicit physical-core binding alone was effectively flat in this comparison. |
| Run 30 → 35 | 20.02 → 20.81 t/s | More decode threads bought a modest short-context improvement; the long-context snippets show a larger effect, subject to the ladder's limitations. |
| Run 35 → 46 | 20.81 → 22.50 t/s | IQ4_XS dense-tensor quantization is worth retaining as a speed candidate, with quality revalidation. |
| Runs 47 → 48 → 50 | 21.30 → 21.30 → 21.33 t/s | Merged experts and offline repacking added almost nothing over the already-repacked setup. |
| Runs 51–55, 57–60 | 20.28–22.06 t/s | No demonstrated breakthrough from longer suffixes, confidence changes, autotuning, or slot similarity. |
| Run 13 | External draft 8.93 t/s; MTP socket split 14.24 t/s | Poor draft acceptance and loss of target bandwidth make this particular socket-separation strategy unattractive. |
| Run 14 | MTP output requantization 14.68 → 14.41 t/s | Not worth making the next priority without new evidence that this operator dominates. |
| Run 56 | Segmentation fault | A software failure, not evidence that external drafting is fundamentally impossible on Broadwell. |

The recorded best GPQA score is still run 5's 22/50, versus run 50's 18/50 and run 46's 16/50. These scores need revalidation. Equality to the original 16/50 does not establish preserved quality, and a two-question improvement on repeatedly tuned 50-item data is not convincing evidence of a real gain. [Published results](https://github.com/James-Begin/Homelab-inference/blob/761092b/RESULTS.md).

Reweighting by generated tokens also changes the apparent ranking:

| Run | Published arithmetic mean | Reconstructed aggregate decode | Tokens / saved request wall time | At 1,536-token ceiling |
| --- | ---: | ---: | ---: | ---: |
| 40, suffix depth 16 | 20.97 | 19.17 | 18.61 | 46/50 |
| 42, confidence-gated suffix | 18.84 | 17.56 | 17.10 | 48/50 |
| 46, IQ4_XS + MTP | 22.50 | 22.46 | 21.75 | 48/50 |
| 50, IQ4_XS + suffix/MTP | 21.33 | 21.10 | 20.46 | 49/50 |
| 58, autotuning | 21.09 | 20.87 | 20.25 | 49/50 |
| 60, slot similarity | 20.97 | 20.74 | 20.13 | 49/50 |

All rates are t/s. Aggregate decode is `sum(tokens) / sum(tokens / saved_tps)`, reconstructed rather than a fresh measurement. Different generated answers still make these imperfect kernel comparisons. Use run 46 and run 50 as separate performance controls; do not assume the most complicated configuration is best.

**The benchmark needs repair before further promotion decisions**

1. **The 66 t/s peaks are repetitive failed outputs.** Runs 40 and 42 peak on `gpqa_128`, generate 1,536 tokens, return no parsed answer, and save previews consisting of “The.” followed by repeated punctuation. Suffix speculation can accelerate a loop extremely well. Neither peak demonstrates useful coding throughput. See the [run 42 checkpoint](https://github.com/James-Begin/Homelab-inference/blob/761092b/logs/raw_checkpoints/exp42_phys_pinning_28threads_suffix_pmin015_burst16_q4kv_checkpoint.json).

2. **GPQA can score unfinished reasoning.** The runner strips only closed `<think>...</think>` blocks, then falls back to the original completion. Its regex accepts the first occurrence of `option B`, or even a standalone A–D. On a capped response it can score a hypothesis mentioned during reasoning as the final answer. The current checkpoints generally omit full output and finish reason, so we cannot repair all historical scores retrospectively. I reproduced this with the actual extracted parser. Save full completions, token IDs, finish reason, and reasoning completion status; require an explicit final-answer field outside reasoning. Count truncations separately. [Runner](https://github.com/James-Begin/Homelab-inference/blob/761092b/benchmarks/gpqa_eval.py#L102).

3. **The needle pass check has a guaranteed false-positive path.** It extracts the expected key from combined process output, then accepts the key appearing anywhere in that same output. That includes the diagnostic it just parsed. It also ignores nonzero process exit status. A synthetic failed subprocess with a wrong generated answer is marked PASSED. Some saved snippets visibly contain the right key, so this does not prove the model failed those cases; it means the automated certification is invalid. Parse only generated output, require a successful process exit, and compare the generated key exactly. [Needle runner](https://github.com/James-Begin/Homelab-inference/blob/761092b/benchmarks/benchmark_extreme_context.py#L38).

4. **The ladder mixes context labels, prefill, decode, and execution paths.** Its decode regex matches the substring inside `prompt eval time`. RESULTS.md repairs many older rows using the snippet, but the 37.96–38.82 t/s “128K” figures for runs 57–60 repeat prefill rates; their saved 192K snippets do not contain decode timing. Those decode rates are unverified. The “128K” prompts actually contain about 192,065 tokens. In current upstream, `llama-passkey` overrides the requested context with a training-context-derived size and uses ordinary one-token greedy decoding, not the server speculation loop. Passing suffix/MTP flags to that binary does not benchmark those server strategies. Use the same server endpoint, exact tokenized lengths, and 256–512 generated tokens for meaningful long-context timing. [Run 60 ladder](https://github.com/James-Begin/Homelab-inference/blob/761092b/logs/extreme_context_reports/extreme_context_exp60_phys_pinning_28threads_repacked_iq4xs_muge_suffix_slot_similarity_q4kv_report.md), [upstream passkey source](https://github.com/ikawrakow/ik_llama.cpp/blob/5f89bfc81268b4d56d2af63ccbed59de17c64c09/examples/passkey/passkey.cpp).

5. **The tuned engine is missing from the reproducible record.** The repository describes kernel patches but includes neither their diffs nor a per-run engine SHA/build manifest. Checkpoint resume keys only on experiment identity/question IDs, so a changed binary or configuration can inherit old results. Preserve engine SHA and dirty diff, compiler/CMake options, GGUF hash and metadata, dataset hash, prompt/template, request parameters, CPU topology, and raw timing. Reject resume on a manifest mismatch. The old profile's overlapping 52% + 39% + 21% timings cannot support a quantitative bottleneck claim.

Exact speculation should preserve the target distribution with a correct verifier; at greedy temperature, substantial divergence is a diagnostic signal. Batch-dependent floating-point differences can still change near-tie decisions, so compare first divergent token and logit margin before concluding there is a bug. Keep target quantization, expert routing, cache, prompt, and penalties fixed. Investigate recurrent-state rollback, batch kernels, and parsing before accepting “longer drafts reduce intelligence” as inherent. [Speculative decoding paper](https://arxiv.org/abs/2211.17192).

**First experiment: NUMA scheduling and memory placement**

This is the most concrete systems opportunity I found. The upstream build enables `GGML_EXPERT_CHUNKING` by default. Its expert kernels distribute chunks through a shared atomic counter, which can send work to a different socket from the one that first touched its weights. Upstream NUMA discussion explicitly identifies this interaction. It is relevant to your custom changes that spread expert work across idle cores: higher utilization can coexist with worse locality. [Build option](https://github.com/ikawrakow/ik_llama.cpp/blob/5f89bfc81268b4d56d2af63ccbed59de17c64c09/ggml/CMakeLists.txt#L98), [dispatch implementation](https://github.com/ikawrakow/ik_llama.cpp/blob/5f89bfc81268b4d56d2af63ccbed59de17c64c09/ggml/src/ggml.c#L18643), [NUMA implementation discussion](https://github.com/ikawrakow/ik_llama.cpp/pull/2396).

Build the same source revision twice, changing only `-DGGML_EXPERT_CHUNKING=ON/OFF`. First benchmark with speculation off, then repeat the winner with MTP. Cross that with two placement policies: your current explicit interleave, and worker-local first-touch with `--numa distribute` and no explicit interleave. Use identical 28-core topology-derived affinity and equal prefill/decode thread counts initially. Inspect actual page placement; file-backed page cache, loading, and repacking can invalidate assumptions about first touch. Warm to stable placement and separately record cold startup. Never infer physical-core IDs from numeric ordering alone; check socket/core/thread topology.

Measure socket DRAM reads, QPI traffic, cycles stalled, and time waiting at barriers alongside latency. Intel PCM provides memory/interconnect monitoring; use what the Broadwell platform exposes. Compare sustained measured bandwidth to a local/remote bandwidth microbenchmark, not the theoretical DDR4 specification. [Intel PCM](https://github.com/intel/pcm).

If the dynamic queue is the problem, a better kernel design is one queue per socket with rows/expert work assigned to local weight pages. Permit cross-socket stealing only if the load imbalance justifies it. First prove this in the fused up/gate and down-projection kernels, including single-token and small verification batches, before altering the full backend. This is a hypothesis requiring your actual engine and machine.

Weight mirroring is worth a bounded A/B, but I would not promise a leap. An open ik PR reports only about +4.6% CPU gain for Qwen3.6-35B-A3B on its tested single-socket NUMA topology; dual-socket reports are mixed. A separate llama.cpp PR corrected earlier dramatic results and found warmed distribute and mirror broadly tied on its tested models. Mirroring costs extra RAM and leaves state/attention locality unresolved. [ik PR](https://github.com/ikawrakow/ik_llama.cpp/pull/2396), [corrected llama.cpp measurements](https://github.com/ggml-org/llama.cpp/pull/27986).

**Second experiment: give suffix speculation useful code to retrieve**

Your campaign sweeps how to search history, but the catalog does not use `suffix_corpus`. Current ik supports preloading a JSON corpus, and its implementation can tokenize a list of strings. Populate a small corpus with source files already present in the working repository and earlier accepted edits. Exclude held-out target patches and benchmark solutions. This changes the available draft information instead of repeatedly changing confidence thresholds. [Source and options](https://github.com/ikawrakow/ik_llama.cpp/blob/5f89bfc81268b4d56d2af63ccbed59de17c64c09/docs/speculative.md), [corpus loader](https://github.com/ikawrakow/ik_llama.cpp/blob/5f89bfc81268b4d56d2af63ccbed59de17c64c09/common/suffix-tree.cpp#L227).

Compare MTP alone, current suffix+MTP, and corpus suffix+MTP on code editing, fresh function generation, and debugging. Start with the existing depth 8/match 5 settings; expand to 16/32 only if accepted tokens per millisecond improve. The research motivation is reuse of earlier outputs in repeated workloads; published SuffixDecoding gains on other systems are not estimates for this Xeon. [SuffixDecoding research](https://arxiv.org/abs/2411.04975).

An illustrative stage configuration, subject to your pinned binary supporting the inspected syntax:

```text
--spec-type suffix:n_max=16,n_min=2,suffix_min_match_len=5,suffix_max_depth=64,suffix_corpus=/absolute/path/to/code-corpus.json
--spec-type mtp:n_max=1,p_min=0.0
```

Keep the target model and other controls unchanged. Reset suffix/cache state between cold tests and measure warm sessions separately. Record draft calls, accepted tokens, verification milliseconds, rollback milliseconds, and fallback fraction. Reject output loops from useful-throughput metrics rather than celebrating them as peaks.

**Third experiment: account for expert traffic when choosing draft length**

The crucial MoE limitation is that verifying four tokens can touch the union of four different sets of experts. It need not cost anything close to one target pass. Confidence alone misses that cost. This explains why more aggressive speculation can plateau even if the draft itself is cheap.

Instrument unique experts per layer per verification batch, weight bytes touched, accepted token count, and total cycle time. Optimize:

```text
accepted output tokens / (draft time + target verification time + rollback time)
```

Start with a lightweight controller using measured costs for depths 1/2/4/8 and a rolling acceptance estimate. Only add a learned routing predictor if the simple controller demonstrates a benefit. With suffix drafting the future target routes are not available for free; predicting them must cost less than it saves.

S²-MoE is directly relevant research: it combines routing-aware expansion, shared-context self-drafting, and expert reuse. Its reported average gain is approximately 2× over autoregressive baselines on GPU/edge systems, not over your already-optimized MTP configuration. Crucially, its full reuse-aware gating changes target routing and is explicitly approximate. Borrow the cost-aware controller first, keeping your target routing unchanged. Qwen3.6's recurrent Gated DeltaNet state also needs correct checkpoint/rollback handling; ordinary KV sharing alone is insufficient. [S²-MoE paper, including quality caveat](https://arxiv.org/html/2608.15018v2), [implementation](https://github.com/angerybob/S2-MoE).

For a second prototype, make a **draft-only** reduced-expert execution of the same checkpoint: e.g. 2 or 4 routed experts in the draft, with the full configured target expert set verifying every output. Share read-only weights where possible and keep mutable draft/target state correctly isolated or restored. This differs from globally clamping the model to three experts. It may fail economically because a full-backbone draft still costs much more than the MTP head; require a measured win over MTP before investing further.

DraftExpert is another useful reference for the expert-expansion problem and full-target verification, but it trains extra draft experts and evaluates offloaded GPU/NPU systems. It is a longer-term research reference, not a ready-made no-training Broadwell optimization. [DraftExpert](https://arxiv.org/abs/2607.24434).

**Fourth experiment: spend the quantization budget on expert traffic, with calibration**

Most late runs keep routed experts at Q4_0 and change dense tensors or speculation. Test expert-only IQ4_KS and supported non-trellis three-bit formats, starting with IQ3_S/IQ3_KS microbenchmarks. Keep the router, shared experts, attention, recurrent tensors, and output head at the chosen reference precision initially. Quantize from original high-precision weights with representative code calibration rather than repeatedly requantizing an already-lossy file. Validate actual tensor types and AVX2 dispatch, then test end-to-end.

The upstream author specifically warns that trellis quants are slower on vanilla AVX2; a smaller file is not sufficient evidence of a faster model. [Qwen-specific quantization discussion](https://github.com/ikawrakow/ik_llama.cpp/discussions/1663). T-MAC's lookup-table approach is a possible kernel research direction, but its published gains are on other models and implementations; establish that unpack/dot-product compute is material before considering a port. [T-MAC](https://github.com/microsoft/T-MAC).

This is likely an incremental step alone. If experts account for 60% of latency and their byte cost drops ideally by 25%, the upper-bound speedup under that simplified model is only `1 / (0.4 + 0.6 × 0.75) = 1.18×`. The 60% share is illustrative, not measured here. Quantization also changes target behavior, so it needs a genuine quality gate. Your fixed-model requirement is respected at the checkpoint/model-family level; use exact-target experiments above if identical target numerics are required.

**For long-context coding, reuse the prompt and recurrent state**

This may yield the largest improvement in time to a useful answer without increasing decode t/s at all. Run 60's 192,065-token prefill took about 4,948 seconds. Avoiding repeated processing of a largely unchanged repository is much more valuable than a small decode improvement.

Changing `--slot-prompt-similarity` on unrelated GPQA questions does not test this opportunity. Build a multi-turn trace with a stable repository prefix, a changing question/edit suffix, and an explicit stable slot. Compare cold requests to `cache_prompt=true`, inspect the number of prompt tokens actually evaluated, and verify restored recurrent state as well as attention KV. Current ik exposes recurrent checkpoints and slot save/restore; confirm support in the pinned binary. [Server cache semantics](https://github.com/ikawrakow/ik_llama.cpp/blob/5f89bfc81268b4d56d2af63ccbed59de17c64c09/examples/server/README.md#L539), [recurrent checkpoint options](https://github.com/ikawrakow/ik_llama.cpp/blob/5f89bfc81268b4d56d2af63ccbed59de17c64c09/docs/parameters.md#L118).

Measure time to first token, total task completion time, and test-passing patches per hour. Keep a separate cold-prefill benchmark so the reuse gain is not confused with a faster kernel. At genuinely long context, profile full-attention scanning and recurrent-state operations separately; this model combines 30 linear-attention and 10 full-attention layers, so treating all 40 layers as conventional attention is misleading. [Official architecture](https://huggingface.co/Qwen/Qwen3.6-35B-A3B).

**The larger systems bet: a socket-local CPU backend**

If counters show persistent cross-socket and barrier costs after placement fixes, prototype per-socket worker pools with local tensor shards and local attention/recurrent state. Partition independent heads and expert work, and exchange only the activations/reductions required by the graph. Upstream maintainers identify this split-backend approach as the structural fix that weight-only mirrors cannot supply. [Maintainer discussion](https://github.com/ikawrakow/ik_llama.cpp/discussions/2030).

Start with a single representative layer and compare its complete latency—including reductions—to the existing implementation. Do not double the same computation on each socket. Expert dispatch must balance selected experts dynamically without forcing weight reads across QPI. This is substantial backend work; proceed only if measured waiting/remote traffic offers enough recoverable time to justify it. It is a credible high-upside research project, not an existing flag.

**What I would change in the queued campaign**

| Queued run | Recommendation |
| --- | --- |
| 61, composite champion | Defer. Components 57/58/60 did not individually beat run 50; their combination is not an evidence-backed new champion. |
| 62, `--numa numactl` | Retain as a cheap control within the placement experiment, not a standalone architecture change. |
| 63, three experts | Defer as a quality-altering experiment. The official model uses eight routed experts, while the current baseline command has no four-expert override. Inspect GGUF/runtime metadata before claiming a 4→3, 25% saving. It is never automatically a 25% total-latency saving. |
| 64, n-gram composite | Replace with the corpus-backed coding experiment. Earlier related n-gram sweeps provide little reason to expect a leap from this combination. |
| 65, `-ger` | Skip unless your custom engine changed its meaning. In inspected upstream source, grouped routing is guarded for BailingMoE2/3 and does not apply to Qwen. |

The current upstream SER threshold selection is also commented out in the inspected common MoE builder, although the flag is parsed and logged. Your notebook describes local threshold-kernel modifications, so this does **not** prove historical SER was inactive; it makes exporting the customized engine and counting actual expert executions essential. [Routing implementation](https://github.com/ikawrakow/ik_llama.cpp/blob/5f89bfc81268b4d56d2af63ccbed59de17c64c09/src/llama-build-context.cpp#L1600), [queued configurations](https://github.com/James-Begin/Homelab-inference/blob/761092b/benchmarks/experiments.json).

**A bounded next campaign**

| Order | Experiment | Promotion rule proposed for this project |
| ---: | --- | --- |
| 1 | Repair measurement and reproduce controls 5, 46, 50 | Save complete output and manifests; explicit final-answer parsing; no false-positive needle tests. Establish run-to-run variability. |
| 2 | Chunking ON/OFF × interleave/first-touch | At least 10% reproducible end-to-end improvement with controlled target behavior; counters should explain the gain. |
| 3 | Stable-prefix multi-turn cache test | Material reduction in time to first token and task completion; inspect actual reused tokens and state correctness. |
| 4 | MTP vs suffix/MTP vs corpus suffix/MTP | At least 20% lower time to completed, test-passing edits on held-out tasks; no credit for repetitive output. |
| 5 | Expert quantization microbenchmark, then winning quant | At least 10% end-to-end gain with a predeclared quality non-inferiority margin and adequate validation. |
| 6 | Cost-aware draft controller, then draft-only expert reduction | At least 20% beyond the best matched speculative control before further implementation work. |
| 7 | Socket-local layer prototype | Proceed to a backend only if complete layer timing and measured bottleneck share support a substantial overall gain. |

The thresholds above are proposed engineering cutoffs to stop low-value sweeps, not statistical guarantees or forecast gains. Run matched prompts in randomized A/B order with several repetitions, and report aggregate throughput and latency distributions. Separate 2K, 8K, 32K, and genuinely measured 128K contexts. Use fixed-length performance traces and a distinct semantic-quality suite, so altered answer length does not masquerade as a faster kernel.

For quality, add a held-out collection of your actual code-edit/debug tasks with executable tests, plus HumanEval+/MBPP+ where relevant. Keep GPQA as a secondary reasoning check; do not use it as the sole coding metric. EvalPlus offers stronger executable tests for those coding benchmarks. [EvalPlus](https://evalplus.github.io/). Use an explicitly selected thinking mode and the correct model template; greedy decoding is useful for equivalence diagnostics, but it is a separate protocol from the official task-specific sampling recommendations. [Model usage guidance](https://huggingface.co/Qwen/Qwen3.6-35B-A3B).

The immediate decision is therefore practical: repair the scorekeeping, test locality with the exact existing model, and give speculation real code reuse to exploit. Reserve the expensive work for expert-cost-aware verification and socket-local execution. Those are the mechanisms with a plausible route beyond the current plateau.
