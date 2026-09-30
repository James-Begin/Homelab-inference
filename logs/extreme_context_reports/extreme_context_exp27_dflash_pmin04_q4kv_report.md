# Extreme Context Needle Retrieval Ladder: Exp27_DFlash_pmin04_Q4KV

- **Timestamp:** `2026-09-15 00:51:55`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all ... -t 14 -tb 28 --model-draft /home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-DFlash-Q8_0.gguf --spec-type dflash:n_max=3,p_min=0.4,cross_ctx=512 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`144.61 t/s`** | 166.4s | `144.61 t/s` | 20958.9 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`104.09 t/s`** | 461.8s | `104.09 t/s` | 20984.9 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`65.84 t/s`** | 1459.1s | `65.84 t/s` | 21032.3 MB |
| **128K Context** | 192,063 | **PASSED (100%)** | **`37.82 t/s`** | 5079.0s | `37.82 t/s` | 21130.2 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `43914`
- **Decoded Snippet:** `The pass key is

<think>
The
</think>

The user wants me to identify the passkey

main: decoded 16 tokens in 1.22 s, speed: 13.13 t/s

llama_print_timings:        load time =  183599.83 ms
llama_prin`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `44091`
- **Decoded Snippet:** `The pass key is

main: decoded 0 tokens in 0.00 s, speed: 0.00 t/s

llama_print_timings:        load time =  479004.50 ms
llama_print_timings:      sample time =       0.32 ms /     1 runs   (    0.3`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `28637`
- **Decoded Snippet:** `The pass key is 28637.

main: decoded 7 tokens in 0.85 s, speed: 8.24 t/s

llama_print_timings:        load time = 1476832.98 ms
llama_print_timings:      sample time =       2.46 ms /     8 runs   (`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,063 tokens)
- **Expected Passkey:** `9939`
- **Decoded Snippet:** `The pass key is 9939. Remember it. 9939 is the

main: decoded 16 tokens in 2.97 s, speed: 5.39 t/s

llama_print_timings:        load time = 5096537.13 ms
llama_print_timings:      sample time =`
- **Status:** MATCH - ZERO REGRESSION

