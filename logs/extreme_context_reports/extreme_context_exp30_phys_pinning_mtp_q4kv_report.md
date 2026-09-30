# Extreme Context Needle Retrieval Ladder: Exp30_Phys_Pinning_MTP_Q4KV

- **Timestamp:** `2026-09-16 12:19:50`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 14 -tb 28 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`138.25 t/s`** | 174.1s | `138.25 t/s` | 20966.8 MB |
| **32K Context** | 48,063 | **PASSED (100%)** | **`107.83 t/s`** | 445.7s | `107.83 t/s` | 20990.3 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`67.65 t/s`** | 1420.0s | `67.65 t/s` | 21038.9 MB |
| **128K Context** | 192,063 | **PASSED (100%)** | **`38.69 t/s`** | 4964.3s | `38.69 t/s` | 21136.7 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `18054`
- **Decoded Snippet:** `The pass key is 18054.

<think>
Here's a thinking process"

main: decoded 16 tokens in 1.21 s, speed: 13.22 t/s

llama_print_timings:        load time =  192318.65 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,063 tokens)
- **Expected Passkey:** `8379`
- **Decoded Snippet:** `The pass key is 8379.`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `18524`
- **Decoded Snippet:** `The pass key is 18524.

main: decoded 7 tokens in 0.85 s, speed: 8.28 t/s

llama_print_timings:        load time = 1437177.04 ms
llama_print_timings:      sample time =       2.58 ms /     8 runs   (`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,063 tokens)
- **Expected Passkey:** `2987`
- **Decoded Snippet:** `The pass key is 2987.

main: decoded 6 tokens in 1.07 s, speed: 5.62 t/s

llama_print_timings:        load time = 4982159.78 ms
llama_print_timings:      sample time =       2.24 ms /     7 runs   (`
- **Status:** MATCH - ZERO REGRESSION

