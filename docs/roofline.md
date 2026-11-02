# Memory traffic estimates

Weight size is useful for deciding what to inspect. It does not tell us how many bytes reached DRAM during inference. The saved records do not establish a measured memory ceiling or show that decode saturated it.

## What the tensor inventory can count

A logical weight-volume estimate could sum tensor storage, scale routed-expert tensors by the selected fraction, replace the embedding table with a lookup row, and omit a prediction block when the ordinary decode graph does not execute it. The [evidence note](readme-evidence.md) records one inspected Qwen expert projection and its stored size; it does not provide a complete tensor-volume audit for either model.

That is a model of selected stored weights. Cache reuse, repeated reads, quantized activations, scratch buffers, recurrent state, attention, prefetching, and NUMA traffic can make physical memory traffic differ from it. Routing can also vary across tokens in a speculative verification batch: the union of selected experts may cost more than one token's expert set.

The old filename-based estimator has been moved to [archive/tools](../archive/tools/). It used hardcoded model sizes and a conventional all-layer KV formula despite these models' hybrid attention. It should not be used as a GGUF audit or a measured bandwidth calculation.

## What the hardware specification can bound

The current memory inventory reports three populated channels per socket at 1866 MT/s. Their combined nominal data-bus ceiling is about 44.8 GB/s per socket. That is a bus calculation, not sustained inference bandwidth. QPI has a separate packet-format ceiling and carries coherence traffic as well as responses. See [memory-speeds.md](memory-speeds.md) for the arithmetic and sources.

A bandwidth divided by bytes-per-token estimate can be useful only when both quantities describe the workload being modeled. STREAM Triad includes its own read/write mix; even a reproducible STREAM result would not establish a universal limit for every decode kernel. This repository currently has no saved STREAM output, memory-controller counter trace, or cycle breakdown sufficient to calculate an empirical decode roofline.

## What to measure next

Record local and remote memory microbenchmarks, then collect socket DRAM and QPI traffic during a fixed decode workload. Save clocks, placement, context length, routing settings, and speculation state with those counters. Compare the traffic to the logical tensor estimate to see which assumptions survive.

For speculation, measure accepted tokens and verification time. Several candidates can share some work, but the speedup is not simply the accepted draft length multiplied by a single-token rate. Different expert routes, attention state, draft cost, and rejected candidates all contribute.
