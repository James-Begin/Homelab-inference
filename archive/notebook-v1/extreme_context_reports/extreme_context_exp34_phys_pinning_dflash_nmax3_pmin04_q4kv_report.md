# Extreme Context Needle Retrieval Ladder: Exp34_Phys_Pinning_DFlash_nmax3_pmin04_Q4KV

- **Timestamp:** `2026-09-17 22:42:16`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 14 -tb 28 --model-draft /home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-DFlash-Q8_0.gguf --spec-type dflash:n_max=3,p_min=0.40,cross_ctx=512 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`149.62 t/s`** | 160.8s | `149.62 t/s` | 20966.3 MB |
| **32K Context** | 48,063 | **PASSED (100%)** | **`108.02 t/s`** | 444.9s | `108.02 t/s` | 20991.5 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`67.74 t/s`** | 1418.1s | `67.74 t/s` | 21038.4 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`38.72 t/s`** | 4959.9s | `38.72 t/s` | 21137.1 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `44280`
- **Decoded Snippet:** `The pass key is 44280.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.22 s, speed: 13.13 t/s

llama_print_timings:        load time =  178256.30 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,063 tokens)
- **Expected Passkey:** `6273`
- **Decoded Snippet:** `The pass key is 6273.

<think>
The "important info" hidden in

main: decoded 16 tokens in 1.45 s, speed: 11.04 t/s

llama_print_timings:        load time =  462225.80 ms
llama_print_timings:      sam`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `19080`
- **Decoded Snippet:** `The pass key is

main: decoded 0 tokens in 0.00 s, speed: 0.00 t/s

llama_print_timings:        load time = 1435635.63 ms
llama_print_timings:      sample time =       0.30 ms /     1 runs   (    0.3`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `38907`
- **Decoded Snippet:** `The pass key is 38907. Remember it. 38907

main: decoded 16 tokens in 2.86 s, speed: 5.60 t/s

llama_print_timings:        load time = 4977528.77 ms
llama_print_timings:      sample time =       5.34`
- **Status:** MATCH - ZERO REGRESSION

