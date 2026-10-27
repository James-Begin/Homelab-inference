# Extreme Context Needle Retrieval Ladder: Exp50_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Suffix_Q4KV

- **Timestamp:** `2026-09-22 01:08:37`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=8,suffix_min_match_len=5,suffix_max_depth=48 -muge -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`151.06 t/s`** | 159.3s | `151.06 t/s` | 21108.2 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`108.87 t/s`** | 441.5s | `108.87 t/s` | 21107.9 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`68.20 t/s`** | 1408.7s | `68.20 t/s` | 21108.4 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`38.84 t/s`** | 4945.2s | `38.84 t/s` | 21109.2 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `33942`
- **Decoded Snippet:** `The pass key is 33942.

<think>
Here's a thinking process:

main: decoded 16 tokens in 1.00 s, speed: 15.94 t/s

llama_print_timings:        load time =  182184.73 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `21585`
- **Decoded Snippet:** `The pass key is 21585.`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `49072`
- **Decoded Snippet:** `The pass key is 49072.

<think>

</think>

Based on the text

main: decoded 16 tokens in 1.40 s, speed: 11.45 t/s

llama_print_timings:        load time = 1431676.16 ms
llama_print_timings:      samp`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `47081`
- **Decoded Snippet:** `The pass key is 47081.



main: decoded 8 tokens in 0.97 s, speed: 8.23 t/s

llama_print_timings:        load time = 4968567.63 ms
llama_print_timings:      sample time =       2.98 ms /     9 runs`
- **Status:** MATCH - ZERO REGRESSION

