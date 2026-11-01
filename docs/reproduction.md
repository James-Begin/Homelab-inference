# Build and reproduce

Run these commands from the repository root. The offline checks need Python 3.11 or 3.12 and the standard library. Building and running the inference engine needs Linux on an x86-64 CPU with AVX2, a C++ compiler, CMake, Git, OpenMP, and NUMA support. On Ubuntu, the build packages are `build-essential cmake git libnuma-dev numactl`.

## Check the saved artifacts

```bash
python3 -m unittest discover -s benchmarks/tests -v
python3 benchmarks/reproduce_audit.py .
python3 benchmarks/summarize_runs.py --write
python3 benchmarks/build_results.py
python3 scripts/check_repo.py
```

These commands test the harness, inspect saved records, and regenerate derived summaries and `RESULTS.md`. They do not start inference or execute generated model solutions. The historical audit retains the old report labels; the regenerated coding summary uses base-and-extra success.

## Prepare the engine

```bash
export IK_LLAMA_HOME="$PWD/.build/ik_llama.cpp"
bash scripts/build_engine.sh --prepare-only
bash scripts/build_engine.sh --check
bash scripts/build_engine.sh
```

The script checks out upstream `87fc8701ff4da81a7d2a91ec0695f95eb3066a47`, applies the combined historical diff and [patch 0007](../patches/0007-fix-buffer-capacity-and-moe-partitioning.patch), and builds the server and CLI tools. Repeating it accepts the pinned base, historical patch state, or corrected state and applies only the missing patches. It refuses source trees with unrelated changes. `--check` validates the source state without modifying it; `--prepare-only` skips compilation.

`IK_LLAMA_BUILD` selects another build directory. `HOMELAB_BUILD_JOBS` sets build parallelism. When binaries or models live elsewhere, set `IK_LLAMA_BIN` and `IK_LLAMA_MODELS` explicitly:

```bash
export IK_LLAMA_BIN="$IK_LLAMA_HOME/build/bin"
export IK_LLAMA_MODELS="/absolute/path/to/gguf-files"
```

The [experiment catalog](../benchmarks/experiments.json) names the required model files. The saved run manifests record their identity and launch settings. Exact local repacked GGUFs are not shipped with this repository; matching a historical run requires the corresponding file and preparation recipe. The build alone does not reconstruct those weights.

## Test the native changes

On Linux x86-64 with AVX2:

```bash
python3 benchmarks/native/run_native_tests.py   --engine "$IK_LLAMA_HOME"   --build-dir "$IK_LLAMA_HOME/build-native-tests"   --configure --sanitizers --jobs 4
```

This builds a separate instrumented GGML library and calls the patched kernels. The buffer contract also compiles the actual `AlignedBuffer` definition with address and undefined-behavior sanitizers. The [native test note](../benchmarks/native/README.md) records the covered formats and the Talos validation. On an ARM machine, add `--contract-only` to run just that portable buffer check; it does not exercise the AVX2 matrix kernels.

## Generate another coding run

Create a virtual environment and install the optional task-evaluation dependency:

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements-eval.txt
python3 benchmarks/code_eval.py --exp 94 --run-suffix _check --dry-run
```

The dry run resolves the command and manifest, including model and binary hashes. Remove `--dry-run` to generate the 164 HumanEval+ samples. Generation saves completions and extracted solutions; it leaves test execution for a separate step. `--max-tokens` defaults to 4096.

To execute those solutions, copy the run into a disposable VM or another environment you have isolated, install the same pinned dependency there, and run:

```bash
python3 benchmarks/code_eval.py   --evaluate-run /absolute/path/to/copied-run   --allow-host-execution
```

That flag permits Python execution on the current host. The harness creates no sandbox. It moves an old EvalPlus result into `evaluation-history/` before evaluating again and records the sample hash and EvalPlus version.

For GPQA, use `python3 benchmarks/gpqa_eval.py --exp 94 --dataset /absolute/path/to/subset.json --run-suffix _check`. The default endpoint is chat and the default output ceiling is 8192 tokens. `--endpoint raw` selects a separate request path; there is no automatic fallback between endpoints.

## Resume and compare

New run manifests bind the model, engine tree, server binary, project libraries and build configuration, prompts, dataset, request parameters, resolved arguments, and recorded host settings. Resume requires those identities to match. Legacy manifests are refused. `--force-new-run` creates a separate timestamped directory and retains existing records.

Decode rate requires valid server timing; missing timing stays missing. New rows retain stopping flags, and a reported length stop or a count at the configured ceiling is counted as a limit hit. Neither request elapsed time nor an old `truncated: false` field proves a natural stop.

See [evaluation notes](eval-protocol.md) for the throughput and output-comparison helpers. A successful tool run applies to its saved inputs and settings; no new model evaluation was performed during the repository cleanup.
