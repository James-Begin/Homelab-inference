# Extreme Context Needle Retrieval Ladder: Exp37_Phys_Pinning_28threads_DFlash_nmax3_pmin04_Q4KV

- **Timestamp:** `2026-09-18 16:14:27`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --model-draft /home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-DFlash-Q8_0.gguf --spec-type dflash:n_max=3,p_min=0.40,cross_ctx=512 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`149.35 t/s`** | 161.1s | `149.35 t/s` | 20964.8 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`107.52 t/s`** | 447.0s | `107.52 t/s` | 20991.2 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`67.60 t/s`** | 1421.1s | `67.60 t/s` | 21039.6 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`38.61 t/s`** | 4974.2s | `38.61 t/s` | 21135.8 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `30359`
- **Decoded Snippet:** `The pass key is

<think>
The user wants me to identify the pass key from the provided text

main: decoded 16 tokens in 1.09 s, speed: 14.74 t/s

llama_print_timings:        load time =  178542.60 ms`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `29479`
- **Decoded Snippet:** `The pass key is 29479.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.23 s, speed: 13.05 t/s

llama_print_timings:        load time =  464474.19 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `23372`
- **Decoded Snippet:** `The pass key is 23372. Remember it. 23372

main: decoded 16 tokens in 1.47 s, speed: 10.91 t/s

llama_print_timings:        load time = 1438596.91 ms
llama_print_timings:      sample time =       5.5`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `31301`
- **Decoded Snippet:** `The pass key is 31301.

The pass key is 313

main: decoded 16 tokens in 1.98 s, speed: 8.09 t/s

llama_print_timings:        load time = 4991626.40 ms
llama_print_timings:      sample time =       5.`
- **Status:** MATCH - ZERO REGRESSION

