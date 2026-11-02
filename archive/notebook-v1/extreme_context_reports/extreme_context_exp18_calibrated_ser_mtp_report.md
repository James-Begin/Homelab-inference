# Extreme Context Needle Retrieval Ladder: Exp18_Calibrated_SER_MTP

- **Timestamp:** `2026-09-10 20:21:53`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all ... -t 14 -tb 28 --numa distribute -ctk q8_0 -ctv q8_0 --defer-experts -ser 2,0.5 --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.0`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`133.59 t/s`** | 180.1s | `133.59 t/s` | 23415.2 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`102.35 t/s`** | 469.6s | `102.35 t/s` | 23432.7 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`67.57 t/s`** | 1421.8s | `67.57 t/s` | 23455.5 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`40.61 t/s`** | 4729.2s | `40.61 t/s` | 23515.0 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `40615`
- **Decoded Snippet:** `The pass key is 40615.`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `32760`
- **Decoded Snippet:** `The pass key is 32760.

main: decoded 7 tokens in 0.69 s, speed: 10.21 t/s

llama_print_timings:        load time =  487941.04 ms
llama_print_timings:      sample time =       2.58 ms /     8 runs`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `43456`
- **Decoded Snippet:** `The pass key is 43456.

The pass key is 434

main: decoded 16 tokens in 2.09 s, speed: 7.67 t/s

llama_print_timings:        load time = 1439920.39 ms
llama_print_timings:      sample time =       5.`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `18932`
- **Decoded Snippet:** `The pass key is 18932.

main: decoded 7 tokens in 1.42 s, speed: 4.94 t/s

llama_print_timings:        load time = 4747747.15 ms
llama_print_timings:      sample time =       2.53 ms /     8 runs   (`
- **Status:** MATCH - ZERO REGRESSION

