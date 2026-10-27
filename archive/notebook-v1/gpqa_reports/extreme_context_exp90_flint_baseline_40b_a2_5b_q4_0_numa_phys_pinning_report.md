# Extreme Context Needle Retrieval Ladder: Exp90_Flint_Baseline_40B_A2_5B_Q4_0_NUMA_Phys_Pinning

- **Timestamp:** `2026-10-23 22:15:35`
- **Model:** `/home/james/ik_llama.cpp/build/models/RecursiveSI_flint-Q4_0.gguf`
- **Configuration:** `numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15,17,19,21,23,25,27 ... -t 28 -tb 28 -ctk q4_0 -ctv q4_0 --numa numactl`

## Benchmark Results

| Context Depth | Tokens Evaluated | Needle Found? | Prompt Processing Speed | Prompt Time | Decode Speed | Peak RAM (RSS) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **16K Context** | 25,000 | **FAILED** | **`0.00 t/s`** | 720.3s | `0.00 t/s` | 43580.6 MB |
| **32K Context** | 50,000 | **FAILED** | **`0.00 t/s`** | 2385.4s | `0.00 t/s` | 43619.2 MB |
| **64K Context** | 0 | **FAILED** | **`0.00 t/s`** | 0.0s | `0.00 t/s` | 0.0 MB |
| **128K Context** | 200,000 | **FAILED** | **`0.00 t/s`** | 1051.5s | `0.00 t/s` | 43302.6 MB |

## Detailed Needle Extractions

### 16K Context (25,000 tokens)
- **Expected Passkey:** `30887`
- **Decoded Snippet:** `The pass key is11.57.953.011 I main: decoded 16 tokens in 2.89 s, speed: 5.53 t/s
	Command being timed: "numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15`
- **Status:** MISMATCH

### 32K Context (50,000 tokens)
- **Expected Passkey:** `30887`
- **Decoded Snippet:** `The pass key is39.43.120.113 I main: decoded 16 tokens in 5.07 s, speed: 3.15 t/s
	Command being timed: "numactl --interleave=all --physcpubind=0,2,4,6,8,10,12,14,16,18,20,22,24,26,1,3,5,7,9,11,13,15`
- **Status:** MISMATCH

### 64K Context (0 tokens)
- **Expected Passkey:** `None`
- **Decoded Snippet:** `ERROR`
- **Status:** MISMATCH

### 128K Context (200,000 tokens)
- **Expected Passkey:** `None`
- **Decoded Snippet:** ``
- **Status:** MISMATCH

