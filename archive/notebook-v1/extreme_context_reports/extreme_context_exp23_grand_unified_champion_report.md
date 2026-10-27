# Extreme Context Needle Retrieval Ladder: Exp23_Grand_Unified_Champion

- **Timestamp:** `2026-09-11 20:03:41`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all ... -t 14 -tb 28 --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type ngram-mod:n_max=16,n_min=3,ngram_size_n=4,ngram_min_hits=2 --spec-type mtp:n_max=1,p_min=0.0 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,063 | **PASSED (100%)** | **`134.68 t/s`** | 178.7s | `134.68 t/s` | 21997.5 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`99.08 t/s`** | 485.1s | `99.08 t/s` | 21999.9 MB |
| **64K Context** | 96,063 | **PASSED (100%)** | **`63.73 t/s`** | 1507.4s | `63.73 t/s` | 21998.0 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`37.10 t/s`** | 5176.8s | `37.10 t/s` | 22011.9 MB |

## Detailed Needle Extractions

### 16K Context (24,063 tokens)
- **Expected Passkey:** `4488`
- **Decoded Snippet:** `The pass key is

main: decoded 0 tokens in 0.00 s, speed: 0.00 t/s

llama_print_timings:        load time =  196121.82 ms
llama_print_timings:      sample time =       0.29 ms /     1 runs   (    0.2`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `33859`
- **Decoded Snippet:** `The pass key is 33859.



main: decoded 8 tokens in 0.74 s, speed: 10.83 t/s

llama_print_timings:        load time =  502576.05 ms
llama_print_timings:      sample time =       2.91 ms /     9 runs`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,063 tokens)
- **Expected Passkey:** `8459`
- **Decoded Snippet:** `The pass key is

main: decoded 0 tokens in 0.00 s, speed: 0.00 t/s

llama_print_timings:        load time = 1524718.57 ms
llama_print_timings:      sample time =       0.29 ms /     1 runs   (    0.2`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `48778`
- **Decoded Snippet:** `The pass key is 48778.

main: decoded 7 tokens in 1.56 s, speed: 4.50 t/s

llama_print_timings:        load time = 5194263.30 ms
llama_print_timings:      sample time =       3.46 ms /     8 runs   (`
- **Status:** MATCH - ZERO REGRESSION

