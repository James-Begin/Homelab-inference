# Extreme Context Needle Retrieval Ladder: Exp45_Phys_Pinning_28threads_MUGE_Suffix_Nmax9_Match5_Q4KV

- **Timestamp:** `2026-09-20 22:22:06`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=9,suffix_min_match_len=5,suffix_max_depth=48 -muge -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`149.92 t/s`** | 160.5s | `149.92 t/s` | 21458.5 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`107.87 t/s`** | 445.6s | `107.87 t/s` | 21458.5 MB |
| **64K Context** | 96,063 | **PASSED (100%)** | **`67.35 t/s`** | 1426.3s | `67.35 t/s` | 21458.8 MB |
| **128K Context** | 192,063 | **PASSED (100%)** | **`38.71 t/s`** | 4961.5s | `38.71 t/s` | 21459.8 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `39226`
- **Decoded Snippet:** `The pass key is 39226.`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `24327`
- **Decoded Snippet:** `The pass key is 24327.`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,063 tokens)
- **Expected Passkey:** `7435`
- **Decoded Snippet:** `The pass key is 7435.

main: decoded 6 tokens in 0.56 s, speed: 10.72 t/s

llama_print_timings:        load time = 1450883.03 ms
llama_print_timings:      sample time =       2.24 ms /     7 runs   (`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,063 tokens)
- **Expected Passkey:** `4430`
- **Decoded Snippet:** `The pass key is 4430.

main: decoded 6 tokens in 0.76 s, speed: 7.87 t/s

llama_print_timings:        load time = 4986567.18 ms
llama_print_timings:      sample time =       2.25 ms /     7 runs   (`
- **Status:** MATCH - ZERO REGRESSION

