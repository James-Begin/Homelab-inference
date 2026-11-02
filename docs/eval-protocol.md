# Evaluation notes

The repository has task runners, a throughput runner, and output-comparison helpers. Their presence does not establish that every historical experiment used the same procedure. A result should link its saved manifest and raw artifacts. [reproduction.md](reproduction.md) gives the build and offline-check commands.

## Coding tasks

[code_eval.py](../benchmarks/code_eval.py) generates EvalPlus HumanEval+ samples, saves full final and reasoning content, and extracts Python code. Generation runs no model-generated Python by default. Evaluating saved samples is a separate operation requiring `--evaluate-run` and `--allow-host-execution`. The harness provides no isolation; use a disposable environment for that step.

The saved Qwen and Flint comparison covers 164 tasks with one sample per task. HumanEval+ success requires both base and extra tests to pass: 106/164 for Qwen and 148/164 for Flint. Base-only successes are 109 and 159. Counting extra-test status alone gave the old 107 and 149 totals.

Decode tokens/s comes from server timing. Saved task means require a finite positive rate and more than one generated token. Qwen’s one-token `HumanEval/111` row reports 1,000,000 tokens/s; it remains in the raw records, pass counts, and elapsed times, but is excluded from the decode-rate mean (163 timing rows). Flint has 164 timing rows. Elapsed time per task includes the whole request and, in the README comparison, includes failed tasks. Different prompts, extraction rules, quantization, and serving settings make the saved comparison a local-pipeline result. It is not an isolated architecture comparison or an estimate over repeated model seeds.

Before a fresh EvalPlus execution, the runner moves the previous result into `evaluation-history/` and records the sample hash and EvalPlus version. [summarize_runs.py](../benchmarks/summarize_runs.py) can rebuild scores from existing results without executing samples. It verifies task IDs, agreement between samples and rows, and agreement between evaluated and saved solutions before counting the base-and-extra intersection.

## Throughput

[bench_throughput.py](../benchmarks/bench_throughput.py) reads the twelve plain prompts in [prompts/tput](../benchmarks/prompts/tput/), warms the server, shuffles repeated requests deterministically, and asks for fixed-length generation with `ignore_eos`. It saves per-request timing and reports aggregate decode rate, median, and IQR.

Short, failed, repetitive, or missing-timing responses are excluded from every timing aggregate. An incomplete run exits with failure, and exclusions remain visible in the output. The repetition heuristic is a diagnostic, not a quality grader.

This runner does not automatically construct exact 2K, 8K, and 32K token contexts, measure streaming time to first token, capture RSS, or record draft acceptance. A non-streaming request's elapsed time is not TTFT. For a kernel comparison, hold the target model and request settings fixed. For an assistant comparison, include natural stopping, test outcomes, and elapsed task time.

## Output comparison and quantization

[check_equivalence.py](../benchmarks/check_equivalence.py) sends greedy requests to two servers and requires nonempty integer token-ID sequences. It fails on a mismatch, missing token IDs, or a request error. It does not accept text fallback or apply a “near-tie pass” rule. A match over the checked prompts is a regression check, not a proof of equality for all inputs.

[kld.sh](../benchmarks/kld.sh) takes a reference model, candidate, corpus, and output directory. It keys the reference cache on the reference model, corpus, binary, and fixed flags, then requires a finite mean KL-divergence value. It sets no quality acceptance threshold. The previously described 150K-token corpus and published KL table have no matching saved measurement records here, so no KL result is claimed for the shipped configurations.

## Resume and timing

New task runs record model and server hashes, project shared libraries and CMake caches, engine changes, prompts, dataset, request settings, resolved launch arguments, and host topology and placement settings. Resume rejects a changed identity or a legacy manifest. `--force-new-run` preserves previous records in their existing directory and starts a separate timestamped run.

Missing decode timing is stored as missing, rather than replaced with request wall rate. New rows retain raw stopping flags. A reported length stop or token count at the configured ceiling is a limit hit; a below-ceiling legacy row without stopping metadata is not proof of natural completion.

## Historical GPQA and context tests

The older GPQA campaign repeatedly tuned against a 50-question subset. Many responses hit a token ceiling, and older checkpoints often retain only previews. Some historical parsers accepted answer-like text from unfinished reasoning. Those scores cannot all be regraded from the remaining artifacts.

The [context probe](../benchmarks/benchmark_extreme_context.py) is a separate passkey experiment. The old ladder mixed prompt and decode timing. Some advertised “128K” rows used about 192K prompt tokens, and passing server speculation flags to the passkey binary did not establish that the server speculation loop ran. Treat those reports as experiment history until a matching endpoint, exact prompt-token count, successful exit status, generated answer, and timing record are available.

The [archived audit](../archive/docs/experiment-audit.md) documents these failure cases. New GPQA runs use an explicitly chosen chat or raw endpoint, save the request identity and full response, and retain stop metadata. They do not silently switch endpoints after an error.
