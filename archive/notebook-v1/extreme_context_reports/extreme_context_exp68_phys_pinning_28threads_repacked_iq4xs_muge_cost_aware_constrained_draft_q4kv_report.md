# Extreme Context Needle Retrieval Ladder: Exp68_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Cost_Aware_Constrained_Draft_Q4KV

- **Timestamp:** `2026-10-04 03:35:14`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=4,suffix_min_match_len=5,suffix_max_depth=32 -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.15 -ctk q4_0 -ctv q4_0 -ser 2,0.5 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`138.06 t/s`** | 174.3s | `16.31 t/s` | 21708.6 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`102.08 t/s`** | 470.8s | `14.45 t/s` | 21708.5 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`65.37 t/s`** | 1469.6s | `11.57 t/s` | 21708.7 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`37.93 t/s`** | 5063.9s | `8.49 t/s` | 21709.5 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `22787`
- **Decoded Snippet:** `The pass key is 22787.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.01 s, speed: 15.89 t/s

llama_print_timings:        load time =  197134.42 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `49180`
- **Decoded Snippet:** `The pass key is 49180.

The pass key is 491

main: decoded 16 tokens in 1.13 s, speed: 14.12 t/s

llama_print_timings:        load time =  494247.36 ms
llama_print_timings:      sample time =       5`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `48158`
- **Decoded Snippet:** `The pass key is 48158.

The pass key is 481

main: decoded 16 tokens in 1.41 s, speed: 11.36 t/s

llama_print_timings:        load time = 1492832.26 ms
llama_print_timings:      sample time =       5`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `49175`
- **Decoded Snippet:** `The pass key is 49175.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.91 s, speed: 8.38 t/s

llama_print_timings:        load time = 5087150.19 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

