# Extreme Context Needle Retrieval Ladder: Exp79_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Slot_Similarity_050_Expanded_Ceiling_4096_Q4KV

- **Timestamp:** `2026-10-07 17:51:08`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --slot-save-path /tmp/slots/ --slot-prompt-similarity 0.50 --spec-type suffix:n_max=4,suffix_min_match_len=5,suffix_max_depth=32 -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.15 -ctk q4_0 -ctv q4_0 -ser 2,0.5 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`138.74 t/s`** | 173.5s | `16.81 t/s` | 21708.6 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`102.22 t/s`** | 470.2s | `14.78 t/s` | 21708.7 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`65.40 t/s`** | 1468.9s | `11.73 t/s` | 21708.7 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`37.95 t/s`** | 5060.8s | `8.60 t/s` | 21709.9 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `12371`
- **Decoded Snippet:** `The pass key is 12371. Remember it. 12371

main: decoded 16 tokens in 0.98 s, speed: 16.36 t/s

llama_print_timings:        load time =  196265.79 ms
llama_print_timings:      sample time =       5.5`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `46189`
- **Decoded Snippet:** `The pass key is 46189.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.11 s, speed: 14.42 t/s

llama_print_timings:        load time =  492966.50 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `24823`
- **Decoded Snippet:** `The pass key is 24823.

The pass key is 248

main: decoded 16 tokens in 1.39 s, speed: 11.51 t/s

llama_print_timings:        load time = 1491571.44 ms
llama_print_timings:      sample time =       5`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `49213`
- **Decoded Snippet:** `The pass key is 49213.

0/1M

Do /dev

main: decoded 16 tokens in 1.89 s, speed: 8.48 t/s

llama_print_timings:        load time = 5084897.42 ms
llama_print_timings:      sample time =       5.69 ms`
- **Status:** MATCH - ZERO REGRESSION

