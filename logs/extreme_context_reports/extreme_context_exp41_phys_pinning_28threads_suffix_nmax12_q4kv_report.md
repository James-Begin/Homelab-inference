# Extreme Context Needle Retrieval Ladder: Exp41_Phys_Pinning_28threads_Suffix_Nmax12_Q4KV

- **Timestamp:** `2026-09-19 19:19:05`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=12,suffix_min_match_len=4,suffix_max_depth=48 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,063 | **PASSED (100%)** | **`149.45 t/s`** | 161.0s | `149.45 t/s` | 20965.3 MB |
| **32K Context** | 48,063 | **PASSED (100%)** | **`107.84 t/s`** | 445.7s | `107.84 t/s` | 20989.8 MB |
| **64K Context** | 96,063 | **PASSED (100%)** | **`67.67 t/s`** | 1419.6s | `67.67 t/s` | 21039.0 MB |
| **128K Context** | 192,063 | **PASSED (100%)** | **`38.70 t/s`** | 4963.2s | `38.70 t/s` | 21136.3 MB |

## Detailed Needle Extractions

### 16K Context (24,063 tokens)
- **Expected Passkey:** `7767`
- **Decoded Snippet:** `The pass key is 7767.

<think>

</think>

The pass key is **

main: decoded 16 tokens in 1.11 s, speed: 14.38 t/s

llama_print_timings:        load time =  178357.88 ms
llama_print_timings:      samp`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,063 tokens)
- **Expected Passkey:** `6077`
- **Decoded Snippet:** `The pass key is 6077.

6077 is the pass key.

main: decoded 16 tokens in 1.25 s, speed: 12.79 t/s

llama_print_timings:        load time =  463116.91 ms
llama_print_timings:      sample time =`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,063 tokens)
- **Expected Passkey:** `2927`
- **Decoded Snippet:** `The pass key is 2927.



main: decoded 7 tokens in 0.66 s, speed: 10.61 t/s

llama_print_timings:        load time = 1436990.96 ms
llama_print_timings:      sample time =       2.71 ms /     8 runs`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,063 tokens)
- **Expected Passkey:** `8268`
- **Decoded Snippet:** `The pass key is 8268.



main: decoded 7 tokens in 0.89 s, speed: 7.85 t/s

llama_print_timings:        load time = 4980910.22 ms
llama_print_timings:      sample time =       2.61 ms /     8 runs`
- **Status:** MATCH - ZERO REGRESSION

