# Extreme Context Needle Retrieval Ladder: Exp39_Phys_Pinning_28threads_Tuned_Chained_Spec_Q4KV

- **Timestamp:** `2026-09-18 22:19:27`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type ngram-mod:n_max=10,ngram_size_n=8,ngram_size_m=16,ngram_min_hits=2 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`149.87 t/s`** | 160.6s | `149.87 t/s` | 20966.3 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`107.52 t/s`** | 447.0s | `107.52 t/s` | 20991.4 MB |
| **64K Context** | 96,063 | **PASSED (100%)** | **`67.51 t/s`** | 1422.9s | `67.51 t/s` | 21039.3 MB |
| **128K Context** | 192,063 | **PASSED (100%)** | **`38.71 t/s`** | 4962.1s | `38.71 t/s` | 21136.3 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `25801`
- **Decoded Snippet:** `The pass key is 25801. Remember it. 25801

main: decoded 16 tokens in 1.11 s, speed: 14.40 t/s

llama_print_timings:        load time =  177971.34 ms
llama_print_timings:      sample time =       5.6`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `44483`
- **Decoded Snippet:** `The pass key is 44483. Remember it. 44483

main: decoded 16 tokens in 1.25 s, speed: 12.77 t/s

llama_print_timings:        load time =  464162.70 ms
llama_print_timings:      sample time =       5.6`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,063 tokens)
- **Expected Passkey:** `4268`
- **Decoded Snippet:** `The pass key is 4268.

Based on the text provided, the pass key

main: decoded 16 tokens in 1.50 s, speed: 10.69 t/s

llama_print_timings:        load time = 1440213.86 ms
llama_print_timings:      s`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,063 tokens)
- **Expected Passkey:** `3291`
- **Decoded Snippet:** `The pass key is 3291.

main: decoded 6 tokens in 0.76 s, speed: 7.87 t/s

llama_print_timings:        load time = 4980044.75 ms
llama_print_timings:      sample time =       2.31 ms /     7 runs   (`
- **Status:** MATCH - ZERO REGRESSION

