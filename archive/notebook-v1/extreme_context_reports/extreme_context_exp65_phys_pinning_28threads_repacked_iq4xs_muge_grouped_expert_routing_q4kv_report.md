# Extreme Context Needle Retrieval Ladder: Exp65_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Grouped_Expert_Routing_Q4KV

- **Timestamp:** `2026-10-03 01:22:18`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=8,suffix_min_match_len=5,suffix_max_depth=48 -muge -ger --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.15 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`137.98 t/s`** | 174.4s | `137.98 t/s` | 21709.0 MB |
| **32K Context** | 48,063 | **PASSED (100%)** | **`102.27 t/s`** | 470.0s | `102.27 t/s` | 21708.7 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`65.37 t/s`** | 1469.6s | `65.37 t/s` | 21708.7 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`37.93 t/s`** | 5063.4s | `37.93 t/s` | 21709.9 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `41348`
- **Decoded Snippet:** `The pass key is 41348.`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,063 tokens)
- **Expected Passkey:** `5376`
- **Decoded Snippet:** `The pass key is 5376.

5376

main: decoded 11 tokens in 0.78 s, speed: 14.04 t/s

llama_print_timings:        load time =  492733.36 ms
llama_print_timings:      sample time =       3.92 ms /    12 r`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `34397`
- **Decoded Snippet:** `The pass key is 34397.`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `42221`
- **Decoded Snippet:** `The pass key is 42221.

42221 is the pass

main: decoded 16 tokens in 1.92 s, speed: 8.35 t/s

llama_print_timings:        load time = 5087204.25 ms
llama_print_timings:      sample time =       5.61`
- **Status:** MATCH - ZERO REGRESSION

