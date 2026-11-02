# Extreme Context Needle Retrieval Ladder: Exp5_Dual_NUMA_MTP

- **Timestamp:** `2026-09-05 17:04:30`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all ... -t 14 -tb 28 --numa distribute --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`119.38 t/s`** | 201.6s | `119.38 t/s` | 26047.9 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`83.52 t/s`** | 575.5s | `83.52 t/s` | 26049.6 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`52.29 t/s`** | 1837.3s | `52.29 t/s` | 26049.3 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`29.96 t/s`** | 6411.0s | `29.96 t/s` | 26060.4 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `24197`
- **Decoded Snippet:** `The pass key is 24197.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.40 s, speed: 11.46 t/s

llama_print_timings:        load time =  221753.99 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `11515`
- **Decoded Snippet:** `The pass key is 11515.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.83 s, speed: 8.74 t/s

llama_print_timings:        load time =  595107.53 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `14674`
- **Decoded Snippet:** `The pass key is 14674.

<think>

</think>

The pass key is

main: decoded 16 tokens in 2.62 s, speed: 6.10 t/s

llama_print_timings:        load time = 1857982.28 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `47305`
- **Decoded Snippet:** `The pass key is 47305.

main: decoded 7 tokens in 1.88 s, speed: 3.72 t/s

llama_print_timings:        load time = 6432246.53 ms
llama_print_timings:      sample time =       2.71 ms /     8 runs   (`
- **Status:** MATCH - ZERO REGRESSION

