# Extreme Context Needle Retrieval Ladder: Exp78_Phys_Pinning_26threads_Repacked_IQ4XS_MUGE_OS_Jitter_Isolation_Expanded_Ceiling_4096_Q4KV

- **Timestamp:** `2026-10-07 13:13:34`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=2,4,6,8,10,12,14,16,18,20,22,24,26,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 26 -tb 26 --spec-type suffix:n_max=4,suffix_min_match_len=5,suffix_max_depth=32 --spec-autotune -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.15 -ctk q4_0 -ctv q4_0 -ser 2,0.5 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`139.98 t/s`** | 171.9s | `16.63 t/s` | 21708.6 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`105.62 t/s`** | 455.1s | `14.71 t/s` | 21709.1 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`69.92 t/s`** | 1373.9s | `12.01 t/s` | 21708.7 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`41.66 t/s`** | 4610.2s | `8.66 t/s` | 21709.5 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `29172`
- **Decoded Snippet:** `The pass key is 29172.

<think>

</think>

The pass key is

main: decoded 16 tokens in 0.99 s, speed: 16.18 t/s

llama_print_timings:        load time =  195512.89 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `46180`
- **Decoded Snippet:** `The pass key is 46180. Remember it. 46180

main: decoded 16 tokens in 1.11 s, speed: 14.36 t/s

llama_print_timings:        load time =  478848.48 ms
llama_print_timings:      sample time =       5.6`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `32829`
- **Decoded Snippet:** `The pass key is 32829.

main: decoded 7 tokens in 0.60 s, speed: 11.76 t/s

llama_print_timings:        load time = 1397701.25 ms
llama_print_timings:      sample time =       2.60 ms /     8 runs`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `27883`
- **Decoded Snippet:** `The pass key is 27883.

The pass key is 278

main: decoded 16 tokens in 1.87 s, speed: 8.54 t/s

llama_print_timings:        load time = 4633569.85 ms
llama_print_timings:      sample time =       5.`
- **Status:** MATCH - ZERO REGRESSION

