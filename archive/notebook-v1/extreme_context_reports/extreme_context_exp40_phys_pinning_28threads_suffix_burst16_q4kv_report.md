# Extreme Context Needle Retrieval Ladder: Exp40_Phys_Pinning_28threads_Suffix_Burst16_Q4KV

- **Timestamp:** `2026-09-19 16:12:33`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=16,suffix_min_match_len=5,suffix_max_depth=64 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`149.70 t/s`** | 160.8s | `149.70 t/s` | 20967.4 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`107.73 t/s`** | 446.2s | `107.73 t/s` | 20990.4 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`67.70 t/s`** | 1419.0s | `67.70 t/s` | 21038.3 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`38.64 t/s`** | 4970.7s | `38.64 t/s` | 21137.2 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `14034`
- **Decoded Snippet:** `The pass key is 14034. Remember it. 14034

main: decoded 16 tokens in 1.11 s, speed: 14.36 t/s

llama_print_timings:        load time =  177919.11 ms
llama_print_timings:      sample time =       5.7`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `49500`
- **Decoded Snippet:** `The pass key is 49500.

The pass key is 495

main: decoded 16 tokens in 1.25 s, speed: 12.83 t/s

llama_print_timings:        load time =  463352.42 ms
llama_print_timings:      sample time =       5`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `13101`
- **Decoded Snippet:** `The pass key is 13101.`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `21655`
- **Decoded Snippet:** `The pass key is 21655.

main: decoded 7 tokens in 0.89 s, speed: 7.85 t/s

llama_print_timings:        load time = 4988371.65 ms
llama_print_timings:      sample time =       2.59 ms /     8 runs   (`
- **Status:** MATCH - ZERO REGRESSION

