# Extreme Context Needle Retrieval Ladder: Exp66_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_First_Touch_NUMA_Q4KV

- **Timestamp:** `2026-10-03 21:27:51`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --localalloc --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=8,suffix_min_match_len=5,suffix_max_depth=48 -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.15 -ctk q4_0 -ctv q4_0 -ser 2,0.5 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`133.63 t/s`** | 180.1s | `9.73 t/s` | 21709.0 MB |
| **32K Context** | 48,063 | **PASSED (100%)** | **`100.20 t/s`** | 479.7s | `8.71 t/s` | 21708.5 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`64.50 t/s`** | 1489.5s | `7.27 t/s` | 21708.8 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`37.40 t/s`** | 5134.8s | `5.36 t/s` | 21709.0 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `17257`
- **Decoded Snippet:** `The pass key is 17257.

The pass key is 172

main: decoded 16 tokens in 1.67 s, speed: 9.58 t/s

llama_print_timings:        load time =  199911.35 ms
llama_print_timings:      sample time =       5.`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,063 tokens)
- **Expected Passkey:** `6842`
- **Decoded Snippet:** `The pass key is 6842.`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `38603`
- **Decoded Snippet:** `The pass key is 38603.

The pass key is 386

main: decoded 16 tokens in 2.23 s, speed: 7.19 t/s

llama_print_timings:        load time = 1510268.49 ms
llama_print_timings:      sample time =       5.`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `17052`
- **Decoded Snippet:** `The pass key is 17052.

The pass key is 170

main: decoded 16 tokens in 3.01 s, speed: 5.32 t/s

llama_print_timings:        load time = 5156058.15 ms
llama_print_timings:      sample time =       5.`
- **Status:** MATCH - ZERO REGRESSION

