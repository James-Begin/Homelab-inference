# Extreme Context Needle Retrieval Ladder: Exp26_Precision_Chained_Q4KV

- **Timestamp:** `2026-09-14 20:30:45`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all ... -t 14 -tb 28 --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type ngram-mod:n_max=16,n_min=3,ngram_size_n=8,ngram_min_hits=3 --spec-type mtp:n_max=1,p_min=0.0 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`133.50 t/s`** | 180.3s | `133.50 t/s` | 21993.6 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`97.17 t/s`** | 494.7s | `97.17 t/s` | 21998.3 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`62.54 t/s`** | 1536.1s | `62.54 t/s` | 21997.7 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`37.12 t/s`** | 5173.8s | `37.12 t/s` | 22010.7 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `31650`
- **Decoded Snippet:** `The pass key is 31650.`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `39624`
- **Decoded Snippet:** `The pass key is 39624.

main: decoded 7 tokens in 0.66 s, speed: 10.67 t/s

llama_print_timings:        load time =  512368.23 ms
llama_print_timings:      sample time =       2.87 ms /     8 runs`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `22530`
- **Decoded Snippet:** `The pass key is 22530. Remember it. 22530

main: decoded 16 tokens in 1.93 s, speed: 8.31 t/s

llama_print_timings:        load time = 1554037.32 ms
llama_print_timings:      sample time =       5.52`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `32489`
- **Decoded Snippet:** `The pass key is 32489.

main: decoded 7 tokens in 1.29 s, speed: 5.44 t/s

llama_print_timings:        load time = 5191867.02 ms
llama_print_timings:      sample time =       2.70 ms /     8 runs   (`
- **Status:** MATCH - ZERO REGRESSION

