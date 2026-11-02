# Extreme Context Needle Retrieval Ladder: Exp60_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_Suffix_Slot_Similarity_Q4KV

- **Timestamp:** `2026-10-01 06:23:31`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=8,suffix_min_match_len=5,suffix_max_depth=48 -muge -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`150.67 t/s`** | 159.7s | `150.67 t/s` | 21107.9 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`108.91 t/s`** | 441.3s | `108.91 t/s` | 21107.9 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`68.01 t/s`** | 1412.4s | `68.01 t/s` | 21108.4 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`38.82 t/s`** | 4948.2s | `38.82 t/s` | 21108.8 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `34637`
- **Decoded Snippet:** `The pass key is 34637.

<think>
The user wants to extract the

main: decoded 16 tokens in 1.01 s, speed: 15.84 t/s

llama_print_timings:        load time =  181795.25 ms
llama_print_timings:      sam`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `13031`
- **Decoded Snippet:** `The pass key is 13031.

Who is the current US president

<think>

main: decoded 16 tokens in 1.14 s, speed: 13.99 t/s

llama_print_timings:        load time =  464473.03 ms
llama_print_timings:`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `24346`
- **Decoded Snippet:** `The pass key is 24346.



main: decoded 8 tokens in 0.71 s, speed: 11.31 t/s

llama_print_timings:        load time = 1434959.13 ms
llama_print_timings:      sample time =       2.88 ms /     9 runs`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `32473`
- **Decoded Snippet:** `The pass key is 32473.

ID:

<think>

</think>

The

main: decoded 16 tokens in 1.94 s, speed: 8.27 t/s

llama_print_timings:        load time = 4971676.91 ms
llama_print_timings:      sample time =`
- **Status:** MATCH - ZERO REGRESSION

