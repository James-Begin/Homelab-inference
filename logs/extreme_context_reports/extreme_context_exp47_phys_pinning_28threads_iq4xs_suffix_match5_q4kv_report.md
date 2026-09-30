# Extreme Context Needle Retrieval Ladder: Exp47_Phys_Pinning_28threads_IQ4XS_Suffix_Match5_Q4KV

- **Timestamp:** `2026-09-21 16:00:12`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=8,suffix_min_match_len=5,suffix_max_depth=48 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`151.14 t/s`** | 159.2s | `151.14 t/s` | 20608.9 MB |
| **32K Context** | 48,063 | **PASSED (100%)** | **`108.89 t/s`** | 441.4s | `108.89 t/s` | 20631.7 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`67.83 t/s`** | 1416.2s | `67.83 t/s` | 20680.7 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`38.85 t/s`** | 4943.5s | `38.85 t/s` | 20779.4 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `40262`
- **Decoded Snippet:** `The pass key is 40262.

main: decoded 7 tokens in 0.44 s, speed: 15.92 t/s

llama_print_timings:        load time =  176473.17 ms
llama_print_timings:      sample time =       2.67 ms /     8 runs`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,063 tokens)
- **Expected Passkey:** `1727`
- **Decoded Snippet:** `The pass key is 1727.`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `17840`
- **Decoded Snippet:** `The pass key is 17840.

17840

The first

main: decoded 16 tokens in 1.38 s, speed: 11.59 t/s

llama_print_timings:        load time = 1433122.14 ms
llama_print_timings:      sample time =       5.49`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `17929`
- **Decoded Snippet:** `The pass key is 17929.



main: decoded 8 tokens in 0.96 s, speed: 8.29 t/s

llama_print_timings:        load time = 4959980.75 ms
llama_print_timings:      sample time =       2.86 ms /     9 runs`
- **Status:** MATCH - ZERO REGRESSION

