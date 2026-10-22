# Extreme Context Needle Retrieval Ladder: Exp82_Phys_Pinning_28decode_26batch_Threads_Repacked_IQ4XS_MUGE_Heterogeneous_Threads_Ceiling4096_Q4KV

- **Timestamp:** `2026-10-13 02:18:16`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 26 --slot-save-path /tmp/slots/ --slot-prompt-similarity 0.50 --spec-type suffix:n_max=4,suffix_min_match_len=5,suffix_max_depth=32 --spec-autotune -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.15 -ctk q4_0 -ctv q4_0 -ser 2,0.5 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`140.78 t/s`** | 170.9s | `16.76 t/s` | 21708.6 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`105.60 t/s`** | 455.2s | `13.25 t/s` | 21709.0 MB |
| **64K Context** | 96,063 | **PASSED (100%)** | **`69.60 t/s`** | 1380.1s | `9.20 t/s` | 21708.8 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`41.77 t/s`** | 4598.5s | `8.22 t/s` | 21709.2 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `37550`
- **Decoded Snippet:** `The pass key is 37550.



main: decoded 8 tokens in 0.49 s, speed: 16.30 t/s

llama_print_timings:        load time =  193593.33 ms
llama_print_timings:      sample time =       2.84 ms /     9 runs`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `40710`
- **Decoded Snippet:** `The pass key is 40710.

<think>
Here's a thinking process:

main: decoded 16 tokens in 1.23 s, speed: 12.98 t/s

llama_print_timings:        load time =  478738.29 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,063 tokens)
- **Expected Passkey:** `6598`
- **Decoded Snippet:** `The pass key is 6598.

main: decoded 6 tokens in 0.66 s, speed: 9.04 t/s

llama_print_timings:        load time = 1404020.15 ms
llama_print_timings:      sample time =       2.25 ms /     7 runs   (`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `24801`
- **Decoded Snippet:** `The pass key is 24801.

main: decoded 7 tokens in 0.86 s, speed: 8.10 t/s

llama_print_timings:        load time = 4622354.47 ms
llama_print_timings:      sample time =       2.82 ms /     8 runs   (`
- **Status:** MATCH - ZERO REGRESSION

