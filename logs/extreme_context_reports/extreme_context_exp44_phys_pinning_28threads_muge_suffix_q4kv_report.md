# Extreme Context Needle Retrieval Ladder: Exp44_Phys_Pinning_28threads_MUGE_Suffix_Q4KV

- **Timestamp:** `2026-09-20 19:19:41`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=8,suffix_min_match_len=4,suffix_max_depth=32 -muge -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,063 | **PASSED (100%)** | **`149.54 t/s`** | 160.9s | `149.54 t/s` | 21458.1 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`107.83 t/s`** | 445.8s | `107.83 t/s` | 21458.1 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`67.64 t/s`** | 1420.1s | `67.64 t/s` | 21458.7 MB |
| **128K Context** | 192,063 | **PASSED (100%)** | **`38.69 t/s`** | 4963.8s | `38.69 t/s` | 21459.1 MB |

## Detailed Needle Extractions

### 16K Context (24,063 tokens)
- **Expected Passkey:** `6151`
- **Decoded Snippet:** `The pass key is 6151.

<think>
Here's
</think>

The pass

main: decoded 16 tokens in 1.13 s, speed: 14.20 t/s

llama_print_timings:        load time =  185449.94 ms
llama_print_timings:      sample t`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `12968`
- **Decoded Snippet:** `The pass key is 12968.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.24 s, speed: 12.91 t/s

llama_print_timings:        load time =  470289.40 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `19603`
- **Decoded Snippet:** `The pass key is 19603.



main: decoded 8 tokens in 0.75 s, speed: 10.72 t/s

llama_print_timings:        load time = 1444711.36 ms
llama_print_timings:      sample time =       2.92 ms /     9 runs`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,063 tokens)
- **Expected Passkey:** `7971`
- **Decoded Snippet:** `The pass key is 7971.

main: decoded 6 tokens in 0.77 s, speed: 7.84 t/s

llama_print_timings:        load time = 4988662.38 ms
llama_print_timings:      sample time =       2.38 ms /     7 runs   (`
- **Status:** MATCH - ZERO REGRESSION

