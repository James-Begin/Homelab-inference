# Extreme Context Needle Retrieval Ladder: Exp64_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Ngram_Mod_Hybrid_Q4KV

- **Timestamp:** `2026-10-02 22:17:19`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type ngram-mod:n_max=10,ngram_size_n=8,ngram_size_m=16,ngram_min_hits=2 --spec-autotune -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.15 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`138.22 t/s`** | 174.1s | `138.22 t/s` | 21709.0 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`102.18 t/s`** | 470.4s | `102.18 t/s` | 21709.1 MB |
| **64K Context** | 96,063 | **PASSED (100%)** | **`65.39 t/s`** | 1469.0s | `65.39 t/s` | 21708.7 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`37.96 t/s`** | 5059.6s | `37.96 t/s` | 21709.5 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `28827`
- **Decoded Snippet:** `The pass key is 28827.`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `10838`
- **Decoded Snippet:** `The pass key is 10838.

The pass key is 108

main: decoded 16 tokens in 1.11 s, speed: 14.40 t/s

llama_print_timings:        load time =  493252.94 ms
llama_print_timings:      sample time =       5`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,063 tokens)
- **Expected Passkey:** `6419`
- **Decoded Snippet:** `The pass key is 6419.



main: decoded 7 tokens in 0.60 s, speed: 11.62 t/s

llama_print_timings:        load time = 1491876.90 ms
llama_print_timings:      sample time =       2.64 ms /     8 runs`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `43353`
- **Decoded Snippet:** `The pass key is 43353.

main: decoded 7 tokens in 0.83 s, speed: 8.42 t/s

llama_print_timings:        load time = 5082681.66 ms
llama_print_timings:      sample time =       2.55 ms /     8 runs   (`
- **Status:** MATCH - ZERO REGRESSION

