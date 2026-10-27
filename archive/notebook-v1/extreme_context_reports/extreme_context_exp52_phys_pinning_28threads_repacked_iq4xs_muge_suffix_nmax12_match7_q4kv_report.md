# Extreme Context Needle Retrieval Ladder: Exp52_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Suffix_Nmax12_Match7_Q4KV

- **Timestamp:** `2026-09-27 23:53:51`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=12,suffix_min_match_len=7,suffix_max_depth=64 -muge -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`150.89 t/s`** | 159.5s | `150.89 t/s` | 21108.2 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`109.05 t/s`** | 440.7s | `109.05 t/s` | 21108.2 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`68.20 t/s`** | 1408.6s | `68.20 t/s` | 21108.1 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`38.83 t/s`** | 4946.9s | `38.83 t/s` | 21109.2 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `20422`
- **Decoded Snippet:** `The pass key is 20422.

The pass key is 204

main: decoded 16 tokens in 1.02 s, speed: 15.71 t/s

llama_print_timings:        load time =  181543.49 ms
llama_print_timings:      sample time =       5`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `37951`
- **Decoded Snippet:** `The pass key is 37951.

Please tell me the pass key

<think>

main: decoded 16 tokens in 1.15 s, speed: 13.97 t/s

llama_print_timings:        load time =  463646.27 ms
llama_print_timings:      samp`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `39749`
- **Decoded Snippet:** `The pass key is 39749.

The pass key is 397

main: decoded 16 tokens in 1.39 s, speed: 11.51 t/s

llama_print_timings:        load time = 1431529.71 ms
llama_print_timings:      sample time =       5`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `11499`
- **Decoded Snippet:** `The pass key is 11499.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.93 s, speed: 8.29 t/s

llama_print_timings:        load time = 4969384.96 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

