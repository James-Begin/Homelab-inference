# Extreme Context Needle Retrieval Ladder: Exp80_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Expanded_Horizon_Autotune_Ceiling_4096_Q4KV

- **Timestamp:** `2026-10-07 22:33:05`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=5,suffix_min_match_len=4,suffix_max_depth=36 --spec-autotune -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.10 -ctk q4_0 -ctv q4_0 -ser 2,0.5 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`138.71 t/s`** | 173.5s | `16.73 t/s` | 21708.6 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`102.26 t/s`** | 470.0s | `14.63 t/s` | 21708.7 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`65.49 t/s`** | 1466.9s | `11.93 t/s` | 21708.8 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`37.94 t/s`** | 5062.9s | `8.48 t/s` | 21709.5 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `37277`
- **Decoded Snippet:** `The pass key is 37277.`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `29206`
- **Decoded Snippet:** `The pass key is 29206.



main: decoded 8 tokens in 0.56 s, speed: 14.28 t/s

llama_print_timings:        load time =  492667.97 ms
llama_print_timings:      sample time =       2.92 ms /     9 runs`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `46065`
- **Decoded Snippet:** `The pass key is 46065.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.37 s, speed: 11.71 t/s

llama_print_timings:        load time = 1489696.04 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `43745`
- **Decoded Snippet:** `The pass key is 43745.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.91 s, speed: 8.36 t/s

llama_print_timings:        load time = 5085991.10 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

