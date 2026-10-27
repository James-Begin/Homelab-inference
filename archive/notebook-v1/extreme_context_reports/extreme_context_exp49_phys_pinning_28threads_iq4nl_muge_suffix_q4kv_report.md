# Extreme Context Needle Retrieval Ladder: Exp49_Phys_Pinning_28threads_IQ4NL_MUGE_Suffix_Q4KV

- **Timestamp:** `2026-09-21 22:07:37`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_NL_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=8,suffix_min_match_len=5,suffix_max_depth=48 -muge -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`138.15 t/s`** | 174.2s | `138.15 t/s` | 21139.4 MB |
| **32K Context** | 48,063 | **PASSED (100%)** | **`101.92 t/s`** | 471.6s | `101.92 t/s` | 21140.5 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`65.40 t/s`** | 1468.9s | `65.40 t/s` | 21139.6 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`37.93 t/s`** | 5063.6s | `37.93 t/s` | 21142.5 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `42000`
- **Decoded Snippet:** `The pass key is 42000.

Please answer the questions presented process:



main: decoded 16 tokens in 1.02 s, speed: 15.66 t/s

llama_print_timings:        load time =  197612.93 ms
llama_print_timing`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,063 tokens)
- **Expected Passkey:** `2207`
- **Decoded Snippet:** `The pass key is 2207.

main: decoded 6 tokens in 0.44 s, speed: 13.73 t/s

llama_print_timings:        load time =  494886.07 ms
llama_print_timings:      sample time =       2.27 ms /     7 runs   (`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `46785`
- **Decoded Snippet:** `The pass key is 46785.

main: decoded 7 tokens in 0.61 s, speed: 11.39 t/s

llama_print_timings:        load time = 1492406.03 ms
llama_print_timings:      sample time =       2.59 ms /     8 runs`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `32299`
- **Decoded Snippet:** `The pass key is 32299.

main: decoded 7 tokens in 0.85 s, speed: 8.25 t/s

llama_print_timings:        load time = 5087214.59 ms
llama_print_timings:      sample time =       2.65 ms /     8 runs   (`
- **Status:** MATCH - ZERO REGRESSION

