# Extreme Context Needle Retrieval Ladder: Exp36_Phys_Pinning_28threads_Chained_Spec_Q4KV

- **Timestamp:** `2026-09-18 04:43:54`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type ngram-mod:n_max=8,ngram_size_n=8,ngram_size_m=12,ngram_min_hits=2 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`149.76 t/s`** | 160.7s | `149.76 t/s` | 20966.0 MB |
| **32K Context** | 48,063 | **PASSED (100%)** | **`107.87 t/s`** | 445.6s | `107.87 t/s` | 20990.2 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`67.68 t/s`** | 1419.3s | `67.68 t/s` | 21039.3 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`38.71 t/s`** | 4961.9s | `38.71 t/s` | 21136.2 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `24379`
- **Decoded Snippet:** `The pass key is

main: decoded 0 tokens in 0.00 s, speed: 0.00 t/s

llama_print_timings:        load time =  178210.82 ms
llama_print_timings:      sample time =       0.30 ms /     1 runs   (    0.3`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,063 tokens)
- **Expected Passkey:** `4768`
- **Decoded Snippet:** `The pass key is 4768. Remember it. 4768 is the

main: decoded 16 tokens in 1.25 s, speed: 12.84 t/s

llama_print_timings:        load time =  462972.69 ms
llama_print_timings:      sample time =`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `40677`
- **Decoded Snippet:** `The pass key is 40677.

main: decoded 7 tokens in 0.67 s, speed: 10.48 t/s

llama_print_timings:        load time = 1436933.04 ms
llama_print_timings:      sample time =       2.58 ms /     8 runs`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `46422`
- **Decoded Snippet:** `The pass key is 46422.

main: decoded 7 tokens in 0.90 s, speed: 7.81 t/s

llama_print_timings:        load time = 4979425.73 ms
llama_print_timings:      sample time =       2.75 ms /     8 runs   (`
- **Status:** MATCH - ZERO REGRESSION

