# Extreme Context Needle Retrieval Ladder: Exp77_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Pure_MTP_pmin005_Expanded_Ceiling_4096_Q4KV

- **Timestamp:** `2026-10-07 08:24:32`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.05 -ctk q4_0 -ctv q4_0 -ser 2,0.5 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`137.84 t/s`** | 174.6s | `16.98 t/s` | 21709.0 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`102.19 t/s`** | 470.3s | `15.02 t/s` | 21708.7 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`65.47 t/s`** | 1467.4s | `12.15 t/s` | 21708.7 MB |
| **128K Context** | 192,063 | **PASSED (100%)** | **`37.97 t/s`** | 5058.8s | `8.67 t/s` | 21709.5 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `47607`
- **Decoded Snippet:** `The pass key is 47607.`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `33223`
- **Decoded Snippet:** `The pass key is 33223.

<think>

The provided text is a test

main: decoded 16 tokens in 1.09 s, speed: 14.66 t/s

llama_print_timings:        load time =  493024.36 ms
llama_print_timings:      samp`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `24462`
- **Decoded Snippet:** `The pass key is 24462.`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,063 tokens)
- **Expected Passkey:** `4244`
- **Decoded Snippet:** `The pass key is 4244.

<think>

**

Step 1: Identify

main: decoded 16 tokens in 1.87 s, speed: 8.55 t/s

llama_print_timings:        load time = 5082741.61 ms
llama_print_timings:      sample time =`
- **Status:** MATCH - ZERO REGRESSION

