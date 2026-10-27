# Extreme Context Needle Retrieval Ladder: Exp59_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_DFlash_Pmin060_Q4KV

- **Timestamp:** `2026-10-01 03:21:49`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --model-draft /home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-DFlash-Q8_0.gguf --spec-type dflash:n_max=3,p_min=0.60,cross_ctx=512 -muge -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`150.37 t/s`** | 160.0s | `150.37 t/s` | 21107.9 MB |
| **32K Context** | 48,063 | **PASSED (100%)** | **`108.65 t/s`** | 442.4s | `108.65 t/s` | 21108.7 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`67.96 t/s`** | 1413.5s | `67.96 t/s` | 21108.4 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`38.81 t/s`** | 4949.3s | `38.81 t/s` | 21108.8 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `43107`
- **Decoded Snippet:** `The pass key is 43107.

What is the first sentence of the text

main: decoded 16 tokens in 0.99 s, speed: 16.13 t/s

llama_print_timings:        load time =  182273.08 ms
llama_print_timings:      sa`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,063 tokens)
- **Expected Passkey:** `1030`
- **Decoded Snippet:** `The pass key is 1030.

Please tell me knows the pass key?



main: decoded 16 tokens in 1.11 s, speed: 14.40 t/s

llama_print_timings:        load time =  465353.19 ms
llama_print_timings:      sampl`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `30703`
- **Decoded Snippet:** `The pass key is 30703.

<think>

</think>

   

The pass

main: decoded 16 tokens in 1.36 s, speed: 11.75 t/s

llama_print_timings:        load time = 1436072.49 ms
llama_print_timings:      sample t`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `47832`
- **Decoded Snippet:** `The pass key is 47832.

<think>

</think>

The pass key is

main: decoded 16 tokens in 1.89 s, speed: 8.47 t/s

llama_print_timings:        load time = 4971589.24 ms
llama_print_timings:      sample`
- **Status:** MATCH - ZERO REGRESSION

