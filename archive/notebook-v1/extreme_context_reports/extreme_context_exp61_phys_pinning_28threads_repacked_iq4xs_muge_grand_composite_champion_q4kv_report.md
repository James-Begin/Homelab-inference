# Extreme Context Needle Retrieval Ladder: Exp61_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Grand_Composite_Champion_Q4KV

- **Timestamp:** `2026-10-02 13:13:51`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=8,suffix_min_match_len=5,suffix_max_depth=48 --spec-autotune -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.15 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,063 | **PASSED (100%)** | **`138.47 t/s`** | 173.8s | `138.47 t/s` | 21708.6 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`102.11 t/s`** | 470.7s | `102.11 t/s` | 21708.5 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`65.37 t/s`** | 1469.6s | `65.37 t/s` | 21708.7 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`37.91 t/s`** | 5065.8s | `37.91 t/s` | 21709.5 MB |

## Detailed Needle Extractions

### 16K Context (24,063 tokens)
- **Expected Passkey:** `2717`
- **Decoded Snippet:** `The pass key is 2717.

A 2717
B 

main: decoded 16 tokens in 1.02 s, speed: 15.72 t/s

llama_print_timings:        load time =  196525.08 ms
llama_print_timings:      sample time =       5.67 ms /`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `39718`
- **Decoded Snippet:** `The pass key is 39718.



main: decoded 8 tokens in 0.58 s, speed: 13.84 t/s

llama_print_timings:        load time =  493575.48 ms
llama_print_timings:      sample time =       3.00 ms /     9 runs`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `40180`
- **Decoded Snippet:** `The pass key is 40180.



main: decoded 8 tokens in 0.70 s, speed: 11.49 t/s

llama_print_timings:        load time = 1492438.77 ms
llama_print_timings:      sample time =       3.05 ms /     9 runs`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `28677`
- **Decoded Snippet:** `The pass key is 28677.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.93 s, speed: 8.31 t/s

llama_print_timings:        load time = 5089877.04 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

