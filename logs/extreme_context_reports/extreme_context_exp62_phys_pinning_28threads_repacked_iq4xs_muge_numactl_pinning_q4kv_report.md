# Extreme Context Needle Retrieval Ladder: Exp62_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Numactl_Pinning_Q4KV

- **Timestamp:** `2026-10-02 16:17:32`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=8,suffix_min_match_len=5,suffix_max_depth=48 -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.15 -ctk q4_0 -ctv q4_0 -ser 2,0.5 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`138.34 t/s`** | 174.0s | `138.34 t/s` | 21708.4 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`102.17 t/s`** | 470.4s | `102.17 t/s` | 21708.7 MB |
| **64K Context** | 96,063 | **PASSED (100%)** | **`65.34 t/s`** | 1470.1s | `65.34 t/s` | 21708.2 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`37.95 t/s`** | 5061.3s | `37.95 t/s` | 21709.5 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `18067`
- **Decoded Snippet:** `The pass key is 18067.

You will be given a question also key

main: decoded 16 tokens in 1.01 s, speed: 15.79 t/s

llama_print_timings:        load time =  196752.80 ms
llama_print_timings:      sam`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `13243`
- **Decoded Snippet:** `The pass key is 13243.`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,063 tokens)
- **Expected Passkey:** `1738`
- **Decoded Snippet:** `The pass key is 1738.

main: decoded 6 tokens in 0.52 s, speed: 11.45 t/s

llama_print_timings:        load time = 1494006.94 ms
llama_print_timings:      sample time =       2.26 ms /     7 runs   (`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `39687`
- **Decoded Snippet:** `The pass key is 39687.`
- **Status:** MATCH - ZERO REGRESSION

