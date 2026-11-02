# Extreme Context Needle Retrieval Ladder: Exp55_Phys_Pinning_28threads_Repacked_IQ4XS_MUGE_DFlash_Nmax3_Pmin045_Q4KV

- **Timestamp:** `2026-09-29 01:17:37`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-IQ4_XS_MoE_Q4_0_Repacked.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 --model-draft /home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-DFlash-Q8_0.gguf --spec-type dflash:n_max=3,p_min=0.45,cross_ctx=512 -muge -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`129.40 t/s`** | 186.0s | `129.40 t/s` | 21107.9 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`108.56 t/s`** | 442.7s | `108.56 t/s` | 21107.9 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`67.95 t/s`** | 1413.8s | `67.95 t/s` | 21108.6 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`38.78 t/s`** | 4952.1s | `38.78 t/s` | 21108.8 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `25264`
- **Decoded Snippet:** `The pass key is <think>

</think>

```python ```markdown
  2526

main: decoded 16 tokens in 0.99 s, speed: 16.17 t/s

llama_print_timings:        load time =  208737.20 ms
llama_print_timings:      s`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `21346`
- **Decoded Snippet:** `The pass key is 21346.

The pass key is 213

main: decoded 16 tokens in 1.11 s, speed: 14.39 t/s

llama_print_timings:        load time =  465518.24 ms
llama_print_timings:      sample time =       5`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `34051`
- **Decoded Snippet:** `The pass key is 34051.`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `44318`
- **Decoded Snippet:** `The pass key is 44318.



In a small, sun-drenched

main: decoded 16 tokens in 1.93 s, speed: 8.28 t/s

llama_print_timings:        load time = 4975565.12 ms
llama_print_timings:      sample time =`
- **Status:** MATCH - ZERO REGRESSION

