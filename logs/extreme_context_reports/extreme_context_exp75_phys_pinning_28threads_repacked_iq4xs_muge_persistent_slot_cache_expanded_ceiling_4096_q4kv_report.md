# Extreme Context Needle Retrieval Ladder: Exp75_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Persistent_Slot_Cache_Expanded_Ceiling_4096_Q4KV

- **Timestamp:** `2026-10-05 16:28:11`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --slot-save-path /tmp/slots/ --slot-prompt-similarity 0.20 --spec-type suffix:n_max=4,suffix_min_match_len=5,suffix_max_depth=32 -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.15 -ctk q4_0 -ctv q4_0 -ser 2,0.5 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`137.86 t/s`** | 174.6s | `16.38 t/s` | 21708.6 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`102.16 t/s`** | 470.5s | `14.42 t/s` | 21708.7 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`65.46 t/s`** | 1467.4s | `11.68 t/s` | 21708.8 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`37.94 t/s`** | 5062.1s | `8.50 t/s` | 21709.9 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `47824`
- **Decoded Snippet:** `The pass key is 47824.

The pass key is 478

main: decoded 16 tokens in 1.00 s, speed: 15.94 t/s

llama_print_timings:        load time =  197538.57 ms
llama_print_timings:      sample time =       5`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `15035`
- **Decoded Snippet:** `The pass key is 15035.

Based on the text provided, the pass

main: decoded 16 tokens in 1.14 s, speed: 14.09 t/s

llama_print_timings:        load time =  493217.49 ms
llama_print_timings:      samp`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `39760`
- **Decoded Snippet:** `The pass key is 39760.

39760

main: decoded 13 tokens in 1.13 s, speed: 11.46 t/s

llama_print_timings:        load time = 1490398.93 ms
llama_print_timings:      sample time =       4.59 ms /    14`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `49574`
- **Decoded Snippet:** `The pass key is 49574.



main: decoded 8 tokens in 0.96 s, speed: 8.37 t/s

llama_print_timings:        load time = 5085977.30 ms
llama_print_timings:      sample time =       2.95 ms /     9 runs`
- **Status:** MATCH - ZERO REGRESSION

