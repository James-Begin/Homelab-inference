# Extreme Context Needle Retrieval Ladder: Exp31_Phys_Pinning_DFlash_nmax4_Q4KV

- **Timestamp:** `2026-09-16 15:22:53`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 14 -tb 28 --model-draft /home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-DFlash-Q8_0.gguf --spec-type dflash:n_max=4,p_min=0.45,cross_ctx=512 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`149.60 t/s`** | 160.9s | `149.60 t/s` | 20966.8 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`107.84 t/s`** | 445.7s | `107.84 t/s` | 20991.4 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`66.81 t/s`** | 1437.9s | `66.81 t/s` | 21039.2 MB |
| **128K Context** | 192,063 | **PASSED (100%)** | **`38.63 t/s`** | 4971.6s | `38.63 t/s` | 21136.9 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `35763`
- **Decoded Snippet:** `The pass key is 35763.

Based on the text provided, the pass

main: decoded 16 tokens in 1.23 s, speed: 13.02 t/s

llama_print_timings:        load time =  178059.21 ms
llama_print_timings:      samp`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `46263`
- **Decoded Snippet:** `The pass key is 46263.

The pass key is 462

main: decoded 16 tokens in 1.46 s, speed: 11.00 t/s

llama_print_timings:        load time =  463007.54 ms
llama_print_timings:      sample time =       5`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `16746`
- **Decoded Snippet:** `The pass key is 16746.

main: decoded 7 tokens in 0.94 s, speed: 7.46 t/s

llama_print_timings:        load time = 1455285.03 ms
llama_print_timings:      sample time =       2.68 ms /     8 runs   (`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,063 tokens)
- **Expected Passkey:** `8684`
- **Decoded Snippet:** `The pass key is 8684.

main: decoded 6 tokens in 1.06 s, speed: 5.66 t/s

llama_print_timings:        load time = 4988986.29 ms
llama_print_timings:      sample time =       2.23 ms /     7 runs   (`
- **Status:** MATCH - ZERO REGRESSION

