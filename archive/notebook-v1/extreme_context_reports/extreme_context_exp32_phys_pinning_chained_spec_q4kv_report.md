# Extreme Context Needle Retrieval Ladder: Exp32_Phys_Pinning_Chained_Spec_Q4KV

- **Timestamp:** `2026-09-16 18:24:51`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 14 -tb 28 --spec-type ngram-mod:n_max=8,ngram_size_n=8,ngram_size_m=12,ngram_min_hits=2 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`150.07 t/s`** | 160.4s | `150.07 t/s` | 20966.4 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`108.09 t/s`** | 444.7s | `108.09 t/s` | 20990.5 MB |
| **64K Context** | 96,063 | **PASSED (100%)** | **`67.72 t/s`** | 1418.5s | `67.72 t/s` | 21039.7 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`38.69 t/s`** | 4964.3s | `38.69 t/s` | 21137.9 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `26221`
- **Decoded Snippet:** `The pass key is 26221. Remember it. 26221

main: decoded 16 tokens in 1.22 s, speed: 13.07 t/s

llama_print_timings:        load time =  177723.97 ms
llama_print_timings:      sample time =       5.6`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `13496`
- **Decoded Snippet:** `The pass key is



main: decoded 1 tokens in 0.11 s, speed: 9.34 t/s

llama_print_timings:        load time =  462779.34 ms
llama_print_timings:      sample time =       0.69 ms /     2 runs   (    0`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,063 tokens)
- **Expected Passkey:** `6728`
- **Decoded Snippet:** `The pass key is 6728.

main: decoded 6 tokens in 0.75 s, speed: 8.03 t/s

llama_print_timings:        load time = 1436121.63 ms
llama_print_timings:      sample time =       2.26 ms /     7 runs   (`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `13268`
- **Decoded Snippet:** `The pass key is 13268.

main: decoded 7 tokens in 1.27 s, speed: 5.49 t/s

llama_print_timings:        load time = 4981829.86 ms
llama_print_timings:      sample time =       2.59 ms /     8 runs   (`
- **Status:** MATCH - ZERO REGRESSION

