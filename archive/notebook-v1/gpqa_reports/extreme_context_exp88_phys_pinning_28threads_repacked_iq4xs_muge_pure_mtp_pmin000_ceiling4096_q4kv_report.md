# Extreme Context Needle Retrieval Ladder: Exp88_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Pure_MTP_pmin000_Ceiling4096_Q4KV

- **Timestamp:** `2026-10-23 09:46:11`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 -muge --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1,p_min=0.0 -ctk q4_0 -ctv q4_0 -ser 2,0.5 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`138.77 t/s`** | 173.4s | `16.92 t/s` | 21708.6 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`101.16 t/s`** | 475.1s | `15.12 t/s` | 21708.7 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`64.36 t/s`** | 1492.5s | `12.03 t/s` | 21708.7 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`37.94 t/s`** | 5061.8s | `8.68 t/s` | 21709.5 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `22679`
- **Decoded Snippet:** `The pass key is 22679.`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `15842`
- **Decoded Snippet:** `The pass key is 15842.



main: decoded 8 tokens in 0.54 s, speed: 14.74 t/s

llama_print_timings:        load time =  498529.06 ms
llama_print_timings:      sample time =       2.88 ms /     9 runs`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `16562`
- **Decoded Snippet:** `The pass key is 16562.



main: decoded 8 tokens in 0.68 s, speed: 11.78 t/s

llama_print_timings:        load time = 1515963.84 ms
llama_print_timings:      sample time =       3.00 ms /     9 runs`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `22858`
- **Decoded Snippet:** `The pass key is 22858.



main: decoded 8 tokens in 0.94 s, speed: 8.55 t/s

llama_print_timings:        load time = 5085535.28 ms
llama_print_timings:      sample time =       2.92 ms /     9 runs`
- **Status:** MATCH - ZERO REGRESSION

