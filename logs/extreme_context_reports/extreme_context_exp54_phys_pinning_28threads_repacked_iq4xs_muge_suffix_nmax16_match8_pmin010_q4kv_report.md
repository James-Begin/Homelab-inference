# Extreme Context Needle Retrieval Ladder: Exp54_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Suffix_Nmax16_Match8_Pmin010_Q4KV

- **Timestamp:** `2026-09-28 05:54:28`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=16,suffix_min_match_len=8,p_min=0.10,suffix_max_depth=64 -muge -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,063 | **PASSED (100%)** | **`151.01 t/s`** | 159.3s | `151.01 t/s` | 21107.9 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`109.24 t/s`** | 440.0s | `109.24 t/s` | 21107.9 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`68.20 t/s`** | 1408.6s | `68.20 t/s` | 21108.4 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`38.75 t/s`** | 4955.9s | `38.75 t/s` | 21108.8 MB |

## Detailed Needle Extractions

### 16K Context (24,063 tokens)
- **Expected Passkey:** `8939`
- **Decoded Snippet:** `The pass key is 8939.



main: decoded 7 tokens in 0.45 s, speed: 15.62 t/s

llama_print_timings:        load time =  181263.40 ms
llama_print_timings:      sample time =       2.73 ms /     8 runs`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `36251`
- **Decoded Snippet:** `The pass key is 36251.



main: decoded 8 tokens in 0.57 s, speed: 13.94 t/s

llama_print_timings:        load time =  463088.85 ms
llama_print_timings:      sample time =       3.08 ms /     9 runs`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `39910`
- **Decoded Snippet:** `The pass key is 39910. Remember it. 39910

main: decoded 16 tokens in 1.39 s, speed: 11.49 t/s

llama_print_timings:        load time = 1431663.40 ms
llama_print_timings:      sample time =       5.6`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `14160`
- **Decoded Snippet:** `The pass key is 14160.

The pass key is 141

main: decoded 16 tokens in 1.95 s, speed: 8.21 t/s

llama_print_timings:        load time = 4979284.83 ms
llama_print_timings:      sample time =       5.`
- **Status:** MATCH - ZERO REGRESSION

