# Extreme Context Needle Retrieval Ladder: Exp46_Phys_Pinning_28threads_IQ4XS_Dense_MTP_Q4KV

- **Timestamp:** `2026-09-21 12:59:52`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`150.63 t/s`** | 159.8s | `150.63 t/s` | 20609.4 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`108.97 t/s`** | 441.1s | `108.97 t/s` | 20633.0 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`68.13 t/s`** | 1409.9s | `68.13 t/s` | 20682.3 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`38.81 t/s`** | 4948.3s | `38.81 t/s` | 20778.1 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `28420`
- **Decoded Snippet:** `The pass key is 28420.`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `29807`
- **Decoded Snippet:** `The pass key is 29807.

<think>

<think>
The user wants me

main: decoded 16 tokens in 1.09 s, speed: 14.73 t/s

llama_print_timings:        load time =  458724.12 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `30383`
- **Decoded Snippet:** `The pass key is 30383.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.33 s, speed: 12.01 t/s

llama_print_timings:        load time = 1426716.23 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `10206`
- **Decoded Snippet:** `The pass key is 10206.

<think>

</think>

1020

main: decoded 16 tokens in 1.87 s, speed: 8.56 t/s

llama_print_timings:        load time = 4964710.95 ms
llama_print_timings:      sample time =`
- **Status:** MATCH - ZERO REGRESSION

