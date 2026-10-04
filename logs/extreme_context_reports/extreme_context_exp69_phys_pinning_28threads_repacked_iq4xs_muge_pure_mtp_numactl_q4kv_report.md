# Extreme Context Needle Retrieval Ladder: Exp69_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Pure_MTP_Numactl_Q4KV

- **Timestamp:** `2026-10-04 06:39:42`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.15 -ctk q4_0 -ctv q4_0 -ser 2,0.5 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,063 | **PASSED (100%)** | **`138.44 t/s`** | 173.8s | `16.95 t/s` | 21708.6 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`102.30 t/s`** | 469.8s | `14.84 t/s` | 21708.5 MB |
| **64K Context** | 96,063 | **PASSED (100%)** | **`65.43 t/s`** | 1468.3s | `12.00 t/s` | 21708.7 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`37.94 t/s`** | 5062.9s | `8.49 t/s` | 21709.4 MB |

## Detailed Needle Extractions

### 16K Context (24,063 tokens)
- **Expected Passkey:** `1915`
- **Decoded Snippet:** `The pass key is 1915.

<think>

</think>

The pass key is 

main: decoded 16 tokens in 0.97 s, speed: 16.50 t/s

llama_print_timings:        load time =  196474.50 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `22732`
- **Decoded Snippet:** `The pass key is 22732.

main: decoded 7 tokens in 0.48 s, speed: 14.46 t/s

llama_print_timings:        load time =  492567.63 ms
llama_print_timings:      sample time =       2.65 ms /     8 runs`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,063 tokens)
- **Expected Passkey:** `5134`
- **Decoded Snippet:** `The pass key is 5134.



main: decoded 7 tokens in 0.60 s, speed: 11.76 t/s

llama_print_timings:        load time = 1492229.49 ms
llama_print_timings:      sample time =       2.59 ms /     8 runs`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `30773`
- **Decoded Snippet:** `The pass key is 30773.



main: decoded 8 tokens in 0.96 s, speed: 8.37 t/s

llama_print_timings:        load time = 5086224.76 ms
llama_print_timings:      sample time =       2.82 ms /     9 runs`
- **Status:** MATCH - ZERO REGRESSION

