# Extreme Context Needle Retrieval Ladder: Exp76_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Concise_Steering_Autotune_Expanded_Ceiling_4096_Q4KV

- **Timestamp:** `2026-10-07 03:02:45`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=4,suffix_min_match_len=5,suffix_max_depth=32 --spec-autotune -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.15 -ctk q4_0 -ctv q4_0 -ser 2,0.5 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`138.58 t/s`** | 173.7s | `16.52 t/s` | 21708.6 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`102.16 t/s`** | 470.5s | `14.48 t/s` | 21709.0 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`65.42 t/s`** | 1468.5s | `11.79 t/s` | 21708.8 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`37.88 t/s`** | 5070.2s | `8.43 t/s` | 21709.5 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `29998`
- **Decoded Snippet:** `The pass key is 29998.

main: decoded 7 tokens in 0.44 s, speed: 16.05 t/s

llama_print_timings:        load time =  196468.78 ms
llama_print_timings:      sample time =       2.63 ms /     8 runs`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `24693`
- **Decoded Snippet:** `The pass key is 24693.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.13 s, speed: 14.14 t/s

llama_print_timings:        load time =  493252.62 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `48442`
- **Decoded Snippet:** `The pass key is 48442.`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `47666`
- **Decoded Snippet:** `The pass key is 47666.

main: decoded 7 tokens in 0.84 s, speed: 8.31 t/s

llama_print_timings:        load time = 5093107.88 ms
llama_print_timings:      sample time =       2.56 ms /     8 runs   (`
- **Status:** MATCH - ZERO REGRESSION

