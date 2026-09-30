# Extreme Context Needle Retrieval Ladder: Exp35_Phys_Pinning_28threads_MTP_Q4KV

- **Timestamp:** `2026-09-18 01:45:04`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`148.99 t/s`** | 161.5s | `148.99 t/s` | 20967.2 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`107.93 t/s`** | 445.4s | `107.93 t/s` | 20992.2 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`67.64 t/s`** | 1420.2s | `67.64 t/s` | 21038.7 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`38.68 t/s`** | 4964.9s | `38.68 t/s` | 21136.7 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `38523`
- **Decoded Snippet:** `The pass key is 38523. Remember it. 38523

main: decoded 16 tokens in 1.09 s, speed: 14.74 t/s

llama_print_timings:        load time =  178745.28 ms
llama_print_timings:      sample time =       5.7`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `46031`
- **Decoded Snippet:** `The pass key is 46031.

main: decoded 7 tokens in 0.54 s, speed: 12.95 t/s

llama_print_timings:        load time =  462677.81 ms
llama_print_timings:      sample time =       2.60 ms /     8 runs`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `41894`
- **Decoded Snippet:** `The pass key is 41894.

main: decoded 7 tokens in 0.65 s, speed: 10.75 t/s

llama_print_timings:        load time = 1437492.67 ms
llama_print_timings:      sample time =       2.55 ms /     8 runs`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `43830`
- **Decoded Snippet:** `The pass key is 43830.

main: decoded 7 tokens in 0.87 s, speed: 8.00 t/s

llama_print_timings:        load time = 4982363.96 ms
llama_print_timings:      sample time =       2.69 ms /     8 runs   (`
- **Status:** MATCH - ZERO REGRESSION

