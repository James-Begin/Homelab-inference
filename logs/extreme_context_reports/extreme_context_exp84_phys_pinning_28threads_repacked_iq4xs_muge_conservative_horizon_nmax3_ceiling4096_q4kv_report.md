# Extreme Context Needle Retrieval Ladder: Exp84_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Conservative_Horizon_nmax3_Ceiling4096_Q4KV

- **Timestamp:** `2026-10-13 11:56:57`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --slot-save-path /tmp/slots/ --slot-prompt-similarity 0.50 --spec-type suffix:n_max=3,suffix_min_match_len=5,suffix_max_depth=24 --spec-autotune -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.15 -ctk q4_0 -ctv q4_0 -ser 2,0.5 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`138.48 t/s`** | 173.8s | `16.92 t/s` | 21709.0 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`102.31 t/s`** | 469.8s | `14.74 t/s` | 21709.0 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`65.46 t/s`** | 1467.4s | `11.87 t/s` | 21708.8 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`37.88 t/s`** | 5071.0s | `8.51 t/s` | 21709.5 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `14447`
- **Decoded Snippet:** `The pass key is 14447.

<think>
Here

</think>

The pass

main: decoded 16 tokens in 0.97 s, speed: 16.47 t/s

llama_print_timings:        load time =  196521.33 ms
llama_print_timings:      sample t`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `26199`
- **Decoded Snippet:** `The pass key is 26199.`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `15909`
- **Decoded Snippet:** `The pass key is 15909.

<think>
The user wants me to extract

main: decoded 16 tokens in 1.37 s, speed: 11.65 t/s

llama_print_timings:        load time = 1491206.89 ms
llama_print_timings:      samp`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `33334`
- **Decoded Snippet:** `The pass key is 33334.



main: decoded 8 tokens in 0.95 s, speed: 8.39 t/s

llama_print_timings:        load time = 5094407.22 ms
llama_print_timings:      sample time =       3.08 ms /     9 runs`
- **Status:** MATCH - ZERO REGRESSION

