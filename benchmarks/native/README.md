# Native regression tests

These tests call the patched `iqk_mul_mat_moe` and `iqk_moe_fused_up_gate` functions in `libggml`. They use synthetic Q8_0 weights and Q8_2_X4 activations, with scalar dot products as the reference. No model download is needed.

Start with an engine checkout containing the historical patch set and patch `0007`, then build a separate test library on an x86-64 AVX2 machine:

```sh
python3 benchmarks/native/run_native_tests.py \
  --engine /path/to/ik_llama.cpp \
  --build-dir /path/to/ik_llama.cpp/build-native-tests \
  --configure --sanitizers --jobs 4
```

The runner builds only the `ggml` target. ASan and UBSan instrument both the library and the test executable. Omit `--configure` to test an existing shared-library build; keep `--sanitizers` when that library was instrumented.

Coverage:

- The exact `AlignedBuffer` definition is extracted from the checkout, compiled, and checked for alignment, growth, and writes across its entire reported capacity.
- Ordinary and fused MoE calls run with 1, 7, 14, and 28 workers, both sequentially and concurrently.
- `Nx=8` covers the former small-matrix failure. `Nx=24/40` covers block tails; `Nx=512/2048` covers the inspected models' output-row dimensions.
- `Ny=31/32/64/65` crosses the Q8_0 conversion threshold and exercises column tails. `K=256/512/1024` exercises work-buffer growth.
- Permuted row mappings, two output planes, bias vectors, untouched output padding, and outer guards are checked.
- A real `ggml_top_k_thresh` graph checks sorting and masking beyond rank 16, including `min_entries=20`.

The numerical reference uses exactly representable quantized values. It checks outputs within `1e-4`; it does not allow a percentage error. This suite covers these native contracts and formats, not full-model inference correctness or performance.

The buffer contract can also run on machines without AVX2:

```sh
python3 benchmarks/native/run_native_tests.py --engine /path/to/ik_llama.cpp --contract-only
```

Python test discovery runs that contract when `HOMELAB_ENGINE_DIR` is set and reports a skip otherwise. It never substitutes a NumPy simulation for a native kernel test.

The [Talos validation log](validation/talos-asan-ubsan.log) records the instrumented AVX2 run on 2026-10-31. [Metadata](validation/talos-asan-ubsan.json) includes source, patch, and library hashes. Paths in the log are replaced with `$TEST_ROOT` and `$TEST_TMP`. The deployed inference engine was left unchanged.
