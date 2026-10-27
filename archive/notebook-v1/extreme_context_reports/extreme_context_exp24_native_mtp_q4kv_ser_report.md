# Extreme Context Needle Retrieval Ladder: Exp24_Native_MTP_Q4KV_SER

- **Timestamp:** `2026-09-12 12:50:48`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all ... -t 14 -tb 28 --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.0 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`134.48 t/s`** | 178.9s | `134.48 t/s` | 21995.2 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`98.82 t/s`** | 486.4s | `98.82 t/s` | 22000.0 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`63.72 t/s`** | 1507.6s | `63.72 t/s` | 21998.1 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`37.21 t/s`** | 5162.2s | `37.21 t/s` | 22009.9 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `49950`
- **Decoded Snippet:** `The pass key is 49950.

The pass key is 499

main: decoded 16 tokens in 1.22 s, speed: 13.15 t/s

llama_print_timings:        load time =  196873.55 ms
llama_print_timings:      sample time =       5`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `28240`
- **Decoded Snippet:** `The pass key is 28240. Remember it. 28240

main: decoded 16 tokens in 1.47 s, speed: 10.89 t/s

llama_print_timings:        load time =  503516.49 ms
llama_print_timings:      sample time =       5.5`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `45008`
- **Decoded Snippet:** `The pass key is 45008.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.90 s, speed: 8.41 t/s

llama_print_timings:        load time = 1524962.40 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `42712`
- **Decoded Snippet:** `The pass key is 42712.

main: decoded 7 tokens in 1.24 s, speed: 5.64 t/s

llama_print_timings:        load time = 5179879.69 ms
llama_print_timings:      sample time =       2.59 ms /     8 runs   (`
- **Status:** MATCH - ZERO REGRESSION

