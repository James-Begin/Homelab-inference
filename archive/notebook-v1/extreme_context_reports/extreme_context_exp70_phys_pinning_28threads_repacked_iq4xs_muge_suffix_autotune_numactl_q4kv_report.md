# Extreme Context Needle Retrieval Ladder: Exp70_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Suffix_Autotune_Numactl_Q4KV

- **Timestamp:** `2026-10-04 09:45:10`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=6,suffix_min_match_len=4,suffix_max_depth=40 --spec-autotune -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.15 -ctk q4_0 -ctv q4_0 -ser 2,0.5 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`138.44 t/s`** | 173.8s | `16.39 t/s` | 21708.6 MB |
| **32K Context** | 48,063 | **FAILED** | **`102.16 t/s`** | 470.5s | `0.00 t/s` | 21709.1 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`65.46 t/s`** | 1467.6s | `11.76 t/s` | 21708.7 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`37.88 t/s`** | 5070.8s | `8.41 t/s` | 21709.5 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `11276`
- **Decoded Snippet:** `The pass key is 11276. Here is the pass key.

What is

main: decoded 16 tokens in 1.00 s, speed: 15.96 t/s

llama_print_timings:        load time =  196521.05 ms
llama_print_timings:      sample time`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,063 tokens)
- **Expected Passkey:** `6947`
- **Decoded Snippet:** `The pass key is

main: decoded 0 tokens in 0.00 s, speed: 0.00 t/s

llama_print_timings:        load time =  493980.76 ms
llama_print_timings:      sample time =       0.29 ms /     1 runs   (    0.2`
- **Status:** MISMATCH

### 64K Context (96,065 tokens)
- **Expected Passkey:** `33058`
- **Decoded Snippet:** `The pass key is 33058.

The pass key is 330

main: decoded 16 tokens in 1.39 s, speed: 11.54 t/s

llama_print_timings:        load time = 1491481.49 ms
llama_print_timings:      sample time =       5`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `12313`
- **Decoded Snippet:** `The pass key is 12313.

The pass key is 123

main: decoded 16 tokens in 1.93 s, speed: 8.29 t/s

llama_print_timings:        load time = 5094849.53 ms
llama_print_timings:      sample time =       5.`
- **Status:** MATCH - ZERO REGRESSION

