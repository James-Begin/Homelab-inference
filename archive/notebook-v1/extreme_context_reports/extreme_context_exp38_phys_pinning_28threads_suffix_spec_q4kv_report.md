# Extreme Context Needle Retrieval Ladder: Exp38_Phys_Pinning_28threads_Suffix_Spec_Q4KV

- **Timestamp:** `2026-09-18 19:19:36`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=8,suffix_min_match_len=4,suffix_max_depth=32 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`149.70 t/s`** | 160.8s | `149.70 t/s` | 20965.8 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`107.87 t/s`** | 445.6s | `107.87 t/s` | 20989.3 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`67.70 t/s`** | 1419.0s | `67.70 t/s` | 21039.7 MB |
| **128K Context** | 192,063 | **PASSED (100%)** | **`38.69 t/s`** | 4964.0s | `38.69 t/s` | 21137.4 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `42624`
- **Decoded Snippet:** `The pass key is 42624. Remember it. 42624

main: decoded 16 tokens in 1.14 s, speed: 14.06 t/s

llama_print_timings:        load time =  177725.37 ms
llama_print_timings:      sample time =       5.6`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `22272`
- **Decoded Snippet:** `The pass key is 22272.

22272

main: decoded 13 tokens in 1.03 s, speed: 12.57 t/s

llama_print_timings:        load time =  462840.81 ms
llama_print_timings:      sample time =       4.60 ms /    14`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `37288`
- **Decoded Snippet:** `The pass key is 37288.

main: decoded 7 tokens in 0.67 s, speed: 10.52 t/s

llama_print_timings:        load time = 1436380.05 ms
llama_print_timings:      sample time =       2.73 ms /     8 runs`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,063 tokens)
- **Expected Passkey:** `8788`
- **Decoded Snippet:** `The pass key is 8788.

main: decoded 6 tokens in 0.76 s, speed: 7.85 t/s

llama_print_timings:        load time = 4981511.88 ms
llama_print_timings:      sample time =       2.27 ms /     7 runs   (`
- **Status:** MATCH - ZERO REGRESSION

