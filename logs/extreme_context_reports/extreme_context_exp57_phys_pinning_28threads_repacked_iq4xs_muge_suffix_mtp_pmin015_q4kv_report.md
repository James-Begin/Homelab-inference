# Extreme Context Needle Retrieval Ladder: Exp57_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Suffix_MTP_Pmin015_Q4KV

- **Timestamp:** `2026-09-30 21:18:44`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=8,suffix_min_match_len=5,suffix_max_depth=48 -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.15 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`138.28 t/s`** | 174.0s | `138.28 t/s` | 21708.6 MB |
| **32K Context** | 48,063 | **PASSED (100%)** | **`102.03 t/s`** | 471.0s | `102.03 t/s` | 21708.5 MB |
| **64K Context** | 96,063 | **PASSED (100%)** | **`65.38 t/s`** | 1469.3s | `65.38 t/s` | 21708.5 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`37.96 t/s`** | 5060.2s | `37.96 t/s` | 21709.5 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `15494`
- **Decoded Snippet:** `The pass key is 15494.

What is the color of the sun?

main: decoded 16 tokens in 1.02 s, speed: 15.75 t/s

llama_print_timings:        load time =  197509.71 ms
llama_print_timings:      sample time`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,063 tokens)
- **Expected Passkey:** `3183`
- **Decoded Snippet:** `The pass key is 3183.`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,063 tokens)
- **Expected Passkey:** `6969`
- **Decoded Snippet:** `The pass key is 6969.

main: decoded 6 tokens in 0.53 s, speed: 11.29 t/s

llama_print_timings:        load time = 1492689.54 ms
llama_print_timings:      sample time =       2.31 ms /     7 runs   (`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `30004`
- **Decoded Snippet:** `The pass key is 30004.



main: decoded 8 tokens in 0.96 s, speed: 8.34 t/s

llama_print_timings:        load time = 5084023.31 ms
llama_print_timings:      sample time =       2.90 ms /     9 runs`
- **Status:** MATCH - ZERO REGRESSION

