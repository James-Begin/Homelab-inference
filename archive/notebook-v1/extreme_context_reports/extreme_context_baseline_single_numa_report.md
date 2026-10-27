# Extreme Context Needle Retrieval Ladder: Baseline_Single_NUMA

- **Timestamp:** `2026-09-05 18:06:52`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Configuration:** `numactl --cpunodebind=0 --membind=0 ... -t 10 -tb 28 --numa isolate`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`90.04 t/s`** | 267.3s | `90.04 t/s` | 24647.9 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`60.80 t/s`** | 790.6s | `60.80 t/s` | 24668.3 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`36.71 t/s`** | 2616.7s | `36.71 t/s` | 24712.7 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `45357`
- **Decoded Snippet:** `The pass key is 45357.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.81 s, speed: 8.84 t/s

llama_print_timings:        load time =  285131.55 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `36433`
- **Decoded Snippet:** `The pass key is 36433.

main: decoded 7 tokens in 1.11 s, speed: 6.28 t/s

llama_print_timings:        load time =  807473.67 ms
llama_print_timings:      sample time =       2.52 ms /     8 runs   (`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `28020`
- **Decoded Snippet:** `The pass key is 28020.

<think>

</think>

The pass key is

main: decoded 16 tokens in 3.56 s, speed: 4.49 t/s

llama_print_timings:        load time = 2633920.68 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

