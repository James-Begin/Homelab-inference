# Extreme Context Needle Retrieval Ladder: Exp42_Phys_Pinning_28threads_Suffix_Pmin015_Burst16_Q4KV

- **Timestamp:** `2026-09-19 22:29:16`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --spec-type suffix:n_max=16,p_min=0.15,suffix_min_match_len=4,suffix_max_depth=64 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`149.51 t/s`** | 161.0s | `149.51 t/s` | 20966.2 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`107.95 t/s`** | 445.3s | `107.95 t/s` | 20990.8 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`67.75 t/s`** | 1418.0s | `67.75 t/s` | 21038.4 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`38.70 t/s`** | 4962.5s | `38.70 t/s` | 21136.0 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `38002`
- **Decoded Snippet:** `The pass key is 38002.

Based on the text provided, the pass

main: decoded 16 tokens in 1.06 s, speed: 15.10 t/s

llama_print_timings:        load time =  178189.18 ms
llama_print_timings:      samp`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `16808`
- **Decoded Snippet:** `The pass key is 16808.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.21 s, speed: 13.27 t/s

llama_print_timings:        load time =  462781.73 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `27977`
- **Decoded Snippet:** `The pass key is 27977.

<think>
The user wants me to extract

main: decoded 16 tokens in 1.46 s, speed: 10.93 t/s

llama_print_timings:        load time = 1435333.45 ms
llama_print_timings:      samp`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `14141`
- **Decoded Snippet:** `The pass key is 14141.

main: decoded 7 tokens in 0.87 s, speed: 8.04 t/s

llama_print_timings:        load time = 4980192.79 ms
llama_print_timings:      sample time =       2.60 ms /     8 runs   (`
- **Status:** MATCH - ZERO REGRESSION

