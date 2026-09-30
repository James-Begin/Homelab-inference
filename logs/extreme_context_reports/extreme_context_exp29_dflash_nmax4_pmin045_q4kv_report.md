# Extreme Context Needle Retrieval Ladder: Exp29_DFlash_nmax4_pmin045_Q4KV

- **Timestamp:** `2026-09-16 03:34:01`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all ... -t 14 -tb 28 --model-draft /home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-DFlash-Q8_0.gguf --spec-type dflash:n_max=4,p_min=0.45,cross_ctx=512 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`143.43 t/s`** | 167.8s | `143.43 t/s` | 20960.6 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`104.15 t/s`** | 461.5s | `104.15 t/s` | 20985.4 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`65.81 t/s`** | 1459.7s | `65.81 t/s` | 21032.7 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`37.79 t/s`** | 5082.4s | `37.79 t/s` | 21130.5 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `14116`
- **Decoded Snippet:** `The pass key is 14116.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.22 s, speed: 13.12 t/s

llama_print_timings:        load time =  185255.52 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `41597`
- **Decoded Snippet:** `The pass key is

main: decoded 0 tokens in 0.00 s, speed: 0.00 t/s

llama_print_timings:        load time =  478873.07 ms
llama_print_timings:      sample time =       0.30 ms /     1 runs   (    0.3`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `44118`
- **Decoded Snippet:** `The pass key is 44118.

main: decoded 7 tokens in 0.85 s, speed: 8.21 t/s

llama_print_timings:        load time = 1476765.57 ms
llama_print_timings:      sample time =       2.50 ms /     8 runs   (`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `38368`
- **Decoded Snippet:** `The pass key is 38368.

main: decoded 7 tokens in 1.30 s, speed: 5.40 t/s

llama_print_timings:        load time = 5099930.30 ms
llama_print_timings:      sample time =       2.49 ms /     8 runs   (`
- **Status:** MATCH - ZERO REGRESSION

