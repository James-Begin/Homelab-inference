# Extreme Context Needle Retrieval Ladder: Exp25_DFlash_nmax4_Q4KV

- **Timestamp:** `2026-09-12 15:58:45`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all ... -t 14 -tb 28 --model-draft /home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-DFlash-Q8_0.gguf --spec-type dflash:n_max=4,cross_ctx=512 -ctk q4_0 -ctv q4_0 -ser 2,0.5`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`145.40 t/s`** | 165.5s | `145.40 t/s` | 20958.9 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`104.82 t/s`** | 458.5s | `104.82 t/s` | 20984.9 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`65.91 t/s`** | 1457.4s | `65.91 t/s` | 21034.7 MB |
| **128K Context** | 192,065 | **PASSED (100%)** | **`37.82 t/s`** | 5077.8s | `37.82 t/s` | 21130.3 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `34828`
- **Decoded Snippet:** `The pass key is 34828.`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `14102`
- **Decoded Snippet:** `The pass key is 14102.

The pass key is 141

main: decoded 16 tokens in 1.47 s, speed: 10.89 t/s

llama_print_timings:        load time =  475499.07 ms
llama_print_timings:      sample time =       5`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `36342`
- **Decoded Snippet:** `The pass key is 36342.

The pass key is 363

main: decoded 16 tokens in 1.95 s, speed: 8.23 t/s

llama_print_timings:        load time = 1474302.44 ms
llama_print_timings:      sample time =       5.`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,065 tokens)
- **Expected Passkey:** `17755`
- **Decoded Snippet:** `The pass key is 17755.

<think>

</think>
</think>

The pass

main: decoded 16 tokens in 2.86 s, speed: 5.59 t/s

llama_print_timings:        load time = 5094768.15 ms
llama_print_timings:      sampl`
- **Status:** MATCH - ZERO REGRESSION

