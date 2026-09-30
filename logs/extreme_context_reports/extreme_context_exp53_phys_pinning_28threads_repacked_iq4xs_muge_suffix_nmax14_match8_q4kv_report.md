# Extreme Context Needle Retrieval Ladder: Exp53_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Suffix_Nmax14_Match8_Q4KV

- **Timestamp:** `2026-09-28 02:53:26`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=14,suffix_min_match_len=8,suffix_max_depth=64 -muge -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`150.55 t/s`** | 159.8s | `150.55 t/s` | 21107.9 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`109.25 t/s`** | 439.9s | `109.25 t/s` | 21107.9 MB |
| **64K Context** | 96,063 | **PASSED (100%)** | **`68.18 t/s`** | 1409.0s | `68.18 t/s` | 21108.4 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`38.84 t/s`** | 4945.3s | `38.84 t/s` | 21109.2 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `16982`
- **Decoded Snippet:** `The pass key is 16982. Remember it. 16982

main: decoded 16 tokens in 1.02 s, speed: 15.68 t/s

llama_print_timings:        load time =  182224.51 ms
llama_print_timings:      sample time =       5.7`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `44220`
- **Decoded Snippet:** `The pass key is 44220.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.14 s, speed: 14.00 t/s

llama_print_timings:        load time =  463072.69 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,063 tokens)
- **Expected Passkey:** `7644`
- **Decoded Snippet:** `The pass key is 7644.

main: decoded 6 tokens in 0.53 s, speed: 11.40 t/s

llama_print_timings:        load time = 1431873.35 ms
llama_print_timings:      sample time =       2.25 ms /     7 runs   (`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `39970`
- **Decoded Snippet:** `The pass key is 39970.

The pass key is 399

main: decoded 16 tokens in 1.93 s, speed: 8.28 t/s

llama_print_timings:        load time = 4967996.98 ms
llama_print_timings:      sample time =       5.`
- **Status:** MATCH - ZERO REGRESSION

