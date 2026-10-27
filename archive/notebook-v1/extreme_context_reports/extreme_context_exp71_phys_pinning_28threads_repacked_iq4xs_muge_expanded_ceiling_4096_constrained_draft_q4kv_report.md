# Extreme Context Needle Retrieval Ladder: Exp71_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Expanded_Ceiling_4096_Constrained_Draft_Q4KV

- **Timestamp:** `2026-10-04 21:02:32`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=4,suffix_min_match_len=5,suffix_max_depth=32 -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.15 -ctk q4_0 -ctv q4_0 -ser 2,0.5 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`138.82 t/s`** | 173.3s | `16.52 t/s` | 21708.6 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`102.18 t/s`** | 470.4s | `14.35 t/s` | 21708.7 MB |
| **64K Context** | 96,063 | **PASSED (100%)** | **`65.36 t/s`** | 1469.7s | `11.76 t/s` | 21708.8 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`37.95 t/s`** | 5061.7s | `8.47 t/s` | 21709.5 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `19736`
- **Decoded Snippet:** `The pass key is 19736.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.00 s, speed: 16.08 t/s

llama_print_timings:        load time =  196220.69 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `19552`
- **Decoded Snippet:** `The pass key is 19552.`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,063 tokens)
- **Expected Passkey:** `1460`
- **Decoded Snippet:** `The pass key is 1460.`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `35001`
- **Decoded Snippet:** `The pass key is 35001.



main: decoded 8 tokens in 0.96 s, speed: 8.35 t/s

llama_print_timings:        load time = 5085427.81 ms
llama_print_timings:      sample time =       2.81 ms /     9 runs`
- **Status:** MATCH - ZERO REGRESSION

