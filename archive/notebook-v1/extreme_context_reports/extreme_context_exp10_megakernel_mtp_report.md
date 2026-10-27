# Extreme Context Needle Retrieval Ladder: Exp10_MegaKernel_MTP

- **Timestamp:** `2026-09-06 18:14:02`
- **Model:** `/home/james/ik_llama.cpp/build/models/Qwen3.6-35B-A3B-UD-Q6_K_MoE_Q4_0.gguf`
- **Configuration:** `numactl --interleave=all ... -t 14 -tb 28 --numa distribute --override-kv qwen35moe.nextn_predict_layers=int:1 --spec-type mtp:n_max=1`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 24,065 | **PASSED (100%)** | **`108.36 t/s`** | 222.1s | `108.36 t/s` | 26047.3 MB |
| **32K Context** | 48,065 | **PASSED (100%)** | **`78.24 t/s`** | 614.3s | `78.24 t/s` | 26050.0 MB |
| **64K Context** | 96,065 | **PASSED (100%)** | **`51.61 t/s`** | 1861.5s | `51.61 t/s` | 26051.1 MB |
| **128K Context** | 192,063 | **PASSED (100%)** | **`29.83 t/s`** | 6437.7s | `29.83 t/s` | 26061.9 MB |

## Detailed Needle Extractions

### 16K Context (24,065 tokens)
- **Expected Passkey:** `41671`
- **Decoded Snippet:** `The pass key is 41671.

<think>

</think>

4167

main: decoded 16 tokens in 1.39 s, speed: 11.51 t/s

llama_print_timings:        load time =  243509.66 ms
llama_print_timings:      sample time =`
- **Status:** MATCH - ZERO REGRESSION

### 32K Context (48,065 tokens)
- **Expected Passkey:** `12173`
- **Decoded Snippet:** `The pass key is 12173.

main: decoded 7 tokens in 0.80 s, speed: 8.76 t/s

llama_print_timings:        load time =  634706.78 ms
llama_print_timings:      sample time =       2.55 ms /     8 runs   (`
- **Status:** MATCH - ZERO REGRESSION

### 64K Context (96,065 tokens)
- **Expected Passkey:** `36539`
- **Decoded Snippet:** `The pass key is 36539.

The pass key is **365

main: decoded 16 tokens in 2.65 s, speed: 6.04 t/s

llama_print_timings:        load time = 1882674.14 ms
llama_print_timings:      sample time =`
- **Status:** MATCH - ZERO REGRESSION

### 128K Context (192,063 tokens)
- **Expected Passkey:** `7626`
- **Decoded Snippet:** `The pass key is 7626.

main: decoded 6 tokens in 1.60 s, speed: 3.74 t/s

llama_print_timings:        load time = 6459005.26 ms
llama_print_timings:      sample time =       2.26 ms /     7 runs   (`
- **Status:** MATCH - ZERO REGRESSION

