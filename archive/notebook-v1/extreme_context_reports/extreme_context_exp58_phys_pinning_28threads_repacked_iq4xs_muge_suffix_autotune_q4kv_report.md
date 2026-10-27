# Extreme Context Needle Retrieval Ladder: Exp58_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Suffix_Autotune_Q4KV

- **Timestamp:** `2026-10-01 00:20:03`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=8,suffix_min_match_len=5,suffix_max_depth=48 -muge -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`150.73 t/s`** | 159.7s | `150.73 t/s` | 21108.6 MB |
| **32K Context** | 48,063 | **PASSED (100%)** | **`108.95 t/s`** | 441.1s | `108.95 t/s` | 21107.9 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`68.00 t/s`** | 1412.7s | `68.00 t/s` | 21108.1 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`38.81 t/s`** | 4949.2s | `38.81 t/s` | 21108.8 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `45704`
- **Decoded Snippet:** `The pass key is 45704.



main: decoded 8 tokens in 0.51 s, speed: 15.75 t/s

llama_print_timings:        load time =  181938.28 ms
llama_print_timings:      sample time =       3.05 ms /     9 runs`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,063 tokens)
- **Expected Passkey:** `9532`
- **Decoded Snippet:** `The pass key is 9532.

<think>

</think>

The pass key is 

main: decoded 16 tokens in 1.15 s, speed: 13.86 t/s

llama_print_timings:        load time =  463400.32 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `12377`
- **Decoded Snippet:** `The pass key is 12377.

main: decoded 7 tokens in 0.62 s, speed: 11.35 t/s

llama_print_timings:        load time = 1435976.40 ms
llama_print_timings:      sample time =       2.61 ms /     8 runs`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `22024`
- **Decoded Snippet:** `The pass key is 22024.

<think>
The user wants to extract the

main: decoded 16 tokens in 1.92 s, speed: 8.33 t/s

llama_print_timings:        load time = 4971756.45 ms
llama_print_timings:      samp`
- **Status:** MATCH - ZERO REGRESSION

