# Extreme Context Needle Retrieval Ladder: Exp28_Window_Chained_Q4KV

- **Timestamp:** `2026-09-15 19:26:03`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all ... -t 14 -tb 28 --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type ngram-mod:n_max=16,n_min=3,ngram_size_n=8,ngram_size_m=8,ngram_min_hits=3 --spec-type mtp:n_max=1,p_min=0.0 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`133.02 t/s`** | 180.9s | `133.02 t/s` | 21995.3 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`98.45 t/s`** | 488.2s | `98.45 t/s` | 22001.0 MB |
| **64K Context** | 96,063 | **PASSED (100%)** | **`63.39 t/s`** | 1515.3s | `63.39 t/s` | 21999.7 MB |
| **128K Context** | 192,063 | **PASSED (100%)** | **`37.08 t/s`** | 5179.9s | `37.08 t/s` | 22011.3 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `10227`
- **Decoded Snippet:** `The pass key is 10227.

The pass key is 102

main: decoded 16 tokens in 1.23 s, speed: 12.98 t/s

llama_print_timings:        load time =  198537.72 ms
llama_print_timings:      sample time =       5`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `23140`
- **Decoded Snippet:** `The pass key is 23140.

main: decoded 7 tokens in 0.66 s, speed: 10.63 t/s

llama_print_timings:        load time =  505889.13 ms
llama_print_timings:      sample time =       2.60 ms /     8 runs`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,063 tokens)
- **Expected Passkey:** `2522`
- **Decoded Snippet:** `The pass key is 2522.



main: decoded 7 tokens in 0.85 s, speed: 8.26 t/s

llama_print_timings:        load time = 1533102.69 ms
llama_print_timings:      sample time =       2.52 ms /     8 runs`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,063 tokens)
- **Expected Passkey:** `1571`
- **Decoded Snippet:** `The pass key is 1571. Remember it. 1571 is the

main: decoded 16 tokens in 2.85 s, speed: 5.62 t/s

llama_print_timings:        load time = 5197785.54 ms
llama_print_timings:      sample time =`
- **Status:** MATCH - ZERO REGRESSION

