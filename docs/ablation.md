# Experiment comparisons

The experiment history contains useful comparisons, but it is not a controlled additive ablation. Many runs change several settings, target weights, or generated outputs. Saved equivalence and KL-divergence records are also missing, so the tables below do not classify the configurations as lossless.

The table below keeps a few comparisons that explain later choices. Rates are the arithmetic means reported by the saved runs, in tokens/s. They are configuration results; a difference between two rows is not an isolated kernel gain.

| Runs | Reported decode rate | What the comparison supports |
| --- | ---: | --- |
| 0 → 4 | 11.16 → 15.72 | The early dual-socket configuration was faster; engine and configuration changes also occurred. |
| 4 → 5 | 15.72 → 19.26 | Native MTP was worth testing further in this campaign. |
| 24 → 30 | 20.00 → 20.02 | Explicit physical-core binding alone was effectively flat in these saved runs. |
| 35 → 46 | 20.81 → 22.50 | The mixed dense-tensor quantization configuration was a useful candidate, with separate quality checks required. |
| 47 → 48 → 50 | 21.30 → 21.30 → 21.33 | Added MUGE and offline repacking produced little change over these already-tuned configurations. |
| 51–55, 57–60 | 20.28–22.06 | Further suffix and confidence sweeps did not produce another large gain. |

These figures come from the [saved report directory](../logs/gpqa_reports/) and the [historical artifact audit](../archive/docs/experiment-audit.md). That audit also reconstructs aggregate decode rates from saved token counts. Its table covers an older snapshot and retains the historical labels and parser observations.

## A fast failure

Experiment 42 includes a roughly 66 tokens/s peak whose saved output falls into repeated punctuation. It returns no parsed answer. That makes it a useful failure case for speculation, but it is not useful coding throughput. The [checkpoint](../logs/raw_checkpoints/exp42_phys_pinning_28threads_suffix_pmin015_burst16_q4kv_checkpoint.json) retains the output preview.

A rate can rise because the output became easier to predict. For comparisons that change speculation, record output quality and acceptance behavior alongside timing. For comparisons that change routing, weights, or KV precision, treat the candidate as a changed model configuration.

## What a new isolated comparison needs

Keep the model file, prompt bytes, request settings, context, engine revision, and CPU placement fixed. Change one setting, warm the server, then repeat both configurations in randomized order. Save full output, server timing, failure counts, and the run manifest. Report decode and request elapsed time separately.

A claim that a change preserves output needs a saved comparison against the same target. An exact token match applies to the checked prompts and settings; it does not establish equality for every input. A divergence needs investigation, including batch-dependent numerical differences and state rollback. The current checks are described in [eval-protocol.md](eval-protocol.md).
