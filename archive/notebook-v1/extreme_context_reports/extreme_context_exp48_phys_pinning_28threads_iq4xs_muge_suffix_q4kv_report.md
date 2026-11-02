# Extreme Context Needle Retrieval Ladder: Exp48_Phys_Pinning_28threads_IQ4XS_MUGE_Suffix_Q4KV

- **Timestamp:** `2026-09-21 19:00:56`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=8,suffix_min_match_len=5,suffix_max_depth=48 -muge -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`150.97 t/s`** | 159.4s | `150.97 t/s` | 21101.9 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`108.87 t/s`** | 441.5s | `108.87 t/s` | 21102.4 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`68.17 t/s`** | 1409.1s | `68.17 t/s` | 21102.5 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`38.83 t/s`** | 4946.9s | `38.83 t/s` | 21103.1 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `36212`
- **Decoded Snippet:** `The pass key is 36212.

<think>

</think>

The pass key is

main: decoded 16 tokens in 0.99 s, speed: 16.21 t/s

llama_print_timings:        load time =  182962.78 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `41146`
- **Decoded Snippet:** `The pass key is 41146.



main: decoded 8 tokens in 0.57 s, speed: 14.02 t/s

llama_print_timings:        load time =  464570.19 ms
llama_print_timings:      sample time =       2.95 ms /     9 runs`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `22020`
- **Decoded Snippet:** `The pass key is 22020.`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `12766`
- **Decoded Snippet:** `The pass key is 12766.

<think>
The user wants me to identify

main: decoded 16 tokens in 1.94 s, speed: 8.25 t/s

llama_print_timings:        load time = 4971870.71 ms
llama_print_timings:      samp`
- **Status:** MATCH - ZERO REGRESSION

