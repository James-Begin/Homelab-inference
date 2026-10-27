# Extreme Context Needle Retrieval Ladder: Exp72_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Pure_MTP_Expanded_Ceiling_4096_Q4KV

- **Timestamp:** `2026-10-05 02:25:25`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.15 -ctk q4_0 -ctv q4_0 -ser 2,0.5 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`137.93 t/s`** | 174.5s | `16.80 t/s` | 21708.6 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`102.08 t/s`** | 470.8s | `14.81 t/s` | 21708.5 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`65.40 t/s`** | 1468.8s | `11.90 t/s` | 21708.8 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`37.91 t/s`** | 5066.0s | `8.53 t/s` | 21709.5 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `19019`
- **Decoded Snippet:** `The pass key is 19019.

main: decoded 7 tokens in 0.43 s, speed: 16.31 t/s

llama_print_timings:        load time =  197928.31 ms
llama_print_timings:      sample time =       2.66 ms /     8 runs`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `33798`
- **Decoded Snippet:** `The pass key is 33798.`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `37600`
- **Decoded Snippet:** `The pass key is 37600.



main: decoded 8 tokens in 0.69 s, speed: 11.67 t/s

llama_print_timings:        load time = 1492524.03 ms
llama_print_timings:      sample time =       3.01 ms /     9 runs`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `44617`
- **Decoded Snippet:** `The pass key is 44617.



main: decoded 8 tokens in 0.95 s, speed: 8.41 t/s

llama_print_timings:        load time = 5089094.77 ms
llama_print_timings:      sample time =       3.06 ms /     9 runs`
- **Status:** MATCH - ZERO REGRESSION

