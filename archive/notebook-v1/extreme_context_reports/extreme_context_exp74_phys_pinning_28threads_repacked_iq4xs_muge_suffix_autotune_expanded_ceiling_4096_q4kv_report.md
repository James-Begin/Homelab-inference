# Extreme Context Needle Retrieval Ladder: Exp74_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Suffix_Autotune_Expanded_Ceiling_4096_Q4KV

- **Timestamp:** `2026-10-05 11:48:34`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=4,suffix_min_match_len=5,suffix_max_depth=32 --spec-autotune -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.15 -ctk q4_0 -ctv q4_0 -ser 2,0.5 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`138.30 t/s`** | 174.0s | `16.56 t/s` | 21708.6 MB |
| **32K Context** | 48,063 | **PASSED (100%)** | **`101.95 t/s`** | 471.5s | `14.35 t/s` | 21708.5 MB |
| **64K Context** | 96,063 | **PASSED (100%)** | **`65.38 t/s`** | 1469.3s | `11.83 t/s` | 21708.8 MB |
| **128K Context** | 192,059 | **PASSED (100%)** | **`37.90 t/s`** | 5067.9s | `8.31 t/s` | 21709.5 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `20168`
- **Decoded Snippet:** `The pass key is 20168.

main: decoded 7 tokens in 0.44 s, speed: 16.09 t/s

llama_print_timings:        load time =  196691.77 ms
llama_print_timings:      sample time =       2.77 ms /     8 runs`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,063 tokens)
- **Expected Passkey:** `7480`
- **Decoded Snippet:** `The pass key is 7480.`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,063 tokens)
- **Expected Passkey:** `6818`
- **Decoded Snippet:** `The pass key is 6818.



main: decoded 7 tokens in 0.60 s, speed: 11.59 t/s

llama_print_timings:        load time = 1492874.24 ms
llama_print_timings:      sample time =       2.59 ms /     8 runs`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,059 tokens)
- **Expected Passkey:** `19`
- **Decoded Snippet:** `The pass key is 19.

The pass key is 19.

main: decoded 13 tokens in 1.59 s, speed: 8.19 t/s

llama_print_timings:        load time = 5091265.65 ms
llama_print_timings:      sample time =       4.51`
- **Status:** MATCH - ZERO REGRESSION

