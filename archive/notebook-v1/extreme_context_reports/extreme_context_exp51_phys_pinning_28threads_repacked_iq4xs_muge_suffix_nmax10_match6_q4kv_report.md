# Extreme Context Needle Retrieval Ladder: Exp51_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Suffix_Nmax10_Match6_Q4KV

- **Timestamp:** `2026-09-27 20:53:33`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=10,suffix_min_match_len=6,suffix_max_depth=48 -muge -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`151.16 t/s`** | 159.2s | `151.16 t/s` | 21108.3 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`109.12 t/s`** | 440.5s | `109.12 t/s` | 21108.2 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`68.22 t/s`** | 1408.2s | `68.22 t/s` | 21108.1 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`38.87 t/s`** | 4941.5s | `38.87 t/s` | 21108.8 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `10950`
- **Decoded Snippet:** `The pass key is 10950. Remember it. 10950

main: decoded 16 tokens in 1.01 s, speed: 15.90 t/s

llama_print_timings:        load time =  181144.01 ms
llama_print_timings:      sample time =       5.6`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `35335`
- **Decoded Snippet:** `The pass key is 35335.

main: decoded 7 tokens in 0.50 s, speed: 13.97 t/s

llama_print_timings:        load time =  462199.40 ms
llama_print_timings:      sample time =       2.61 ms /     8 runs`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `37275`
- **Decoded Snippet:** `The pass key is 37275.



main: decoded 8 tokens in 0.70 s, speed: 11.42 t/s

llama_print_timings:        load time = 1430004.40 ms
llama_print_timings:      sample time =       2.81 ms /     9 runs`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `30149`
- **Decoded Snippet:** `The pass key is 30149.

<think>

</think>final

The pass key

main: decoded 16 tokens in 1.92 s, speed: 8.34 t/s

llama_print_timings:        load time = 4964754.74 ms
llama_print_timings:      sampl`
- **Status:** MATCH - ZERO REGRESSION

