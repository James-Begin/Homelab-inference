# Extreme Context Needle Retrieval Ladder: Exp87_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Suffix_Match4_Autotune_Ceiling4096_Q4KV

- **Timestamp:** `2026-10-23 04:25:09`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --slot-save-path /tmp/slots/ --slot-prompt-similarity 0.50 --spec-type suffix:n_max=4,suffix_min_match_len=4,suffix_max_depth=32 --spec-autotune -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.15 -ctk q4_0 -ctv q4_0 -ser 2,0.5 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,063 | **PASSED (100%)** | **`136.78 t/s`** | 175.9s | `16.61 t/s` | 21708.6 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`91.07 t/s`** | 527.8s | `14.68 t/s` | 21708.7 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`65.10 t/s`** | 1475.6s | `11.80 t/s` | 21708.7 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`36.85 t/s`** | 5211.7s | `8.54 t/s` | 21709.5 MB |

## Detailed Needle Extractions

### 16K Context (24,063 tokens)
- **Expected Passkey:** `8546`
- **Decoded Snippet:** `The pass key is 8546.

<think>

</think>

The pass key is **

main: decoded 16 tokens in 0.99 s, speed: 16.17 t/s

llama_print_timings:        load time =  199201.14 ms
llama_print_timings:      samp`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `41975`
- **Decoded Snippet:** `The pass key is 41975.`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `43938`
- **Decoded Snippet:** `The pass key is 43938.

-`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `37235`
- **Decoded Snippet:** `The pass key is 37235.

The pass key is 372

main: decoded 16 tokens in 1.90 s, speed: 8.42 t/s

llama_print_timings:        load time = 5235619.52 ms
llama_print_timings:      sample time =       5.`
- **Status:** MATCH - ZERO REGRESSION

