# Experiment 13: Asymmetric NUMA Speculation (Decoupled Sockets)

- **Target Architecture:** Qwen 3.6-35B-A3B-UD-Q6_K_MoE_Q4_0 (35.5B params, 256 experts, 4 active per layer, 41 layers)
- **Draft Engine Tested:**
  - **13A:** Separate Autoregressive Drafter: `Qwen3.5-0.8B-Q4_K_M.gguf` (532 MB, 248,320-token BPE)
  - **13B:** Decoupled Native MTP Drafter (`-td 14` for MTP context on Node 1)
- **Hardware Platform:** Dual Intel Xeon E5-2680 v4 (28 cores total, 56 vCPUs, 2 NUMA nodes, 8-channel DDR4 memory bus)
- **Evaluation Baseline:** 50-Question GPQA Diamond Standard (1,536 tokens max, unconstrained reasoning)

---

## 1. Hypothesis & Architectural Motivation

On dual-socket NUMA systems, cross-socket memory traffic over the Intel QPI bus (capped at ~38.4 GB/s bi-directional) can create bus contention between the target verification engine and the draft speculation engine.
- **Hypothesis:** By isolating the 35B target model to Socket 0 (14 physical cores, Node 0 local memory, 50 GB/s bandwidth) and isolating the draft engine to Socket 1 (14 physical cores, Node 1 local memory, 50 GB/s bandwidth), both engines would achieve zero-QPI weight access and dedicated memory channels, preventing bus contention and boosting generation speed toward $\ge 50$ TPS.

---

## 2. Experimental Setup & Execution

### Configuration 13A: Asymmetric Separate Draft Model (Qwen 3.5 0.8B)
- **Target Model:** Socket 0 (`numactl --cpunodebind=0 --membind=0 -t 14`)
- **Draft Model:** Socket 1 (`-md Qwen3.5-0.8B-Q4_K_M.gguf -td 14 -cd 2048`)
- **Server Flag:** `--spec-type draft:n_max=2 -fa 1`

#### Empirical Results:
- **Standalone 0.8B Draft Speed:** `37.60 tokens/second` (eval time: `26.60 ms/token` on Node 1).
- **Draft Acceptance Rate (General Prose):** `51.6%` (32 accepted / 62 generated).
- **Draft Acceptance Rate (Scientific Reasoning / GPQA):** **`8.56%`** (37 accepted / 432 drafted at $n_{\text{draft}}=16$).
- **Target Model Single-Socket Bandwidth:** Restricted to Node 0 (4 DDR4 channels $\approx 50\text{ GB/s}$). Pure decode speed dropped from **15.72 t/s** (interleaved dual-socket) down to **11.16 t/s** (single socket).
- **End-to-End Generation Speed:** **`8.93 tokens/second`** (drop of **-53.6%** compared to Native MTP at 19.26 t/s).

---

### Configuration 13B: Asymmetric MTP Context Execution
- **Target Execution:** 14 cores on Node 0
- **MTP Drafting Execution:** 14 cores on Node 1 (`-td 14`)

#### Empirical Results & Physical Analysis:
1. **Sequential Decode Dependency:**
   - In speculative decoding, Target Decode and Draft Prediction run in strict sequence: $\text{Target Token Verification} \rightarrow \text{MTP Draft Step} \rightarrow \text{Target Batch Verification}$.
   - Because target and MTP never execute simultaneously, memory bus contention during generation is mathematically zero.
2. **QPI Penalty on Node Isolation:**
   - The MTP head (`nextn.0.*`) and output projection matrix are located within the target GGUF file.
   - If target weights are pinned to Node 0 memory, threads running on Node 1 must read the 417 MB output projection tensor and Layer 40 weights *across the high-latency QPI interconnect*, increasing draft latency rather than reducing it.
3. **Core Underutilization:**
   - Pinning target to Node 0 leaves Node 1's 14 cores 100% idle during target decode.
   - Pinning MTP to Node 1 leaves Node 0's 14 cores 100% idle during drafting.
   - Distributing all 28 cores and interleaving memory (`numactl --interleave=all --numa distribute -t 14/28 -tb 28`) doubles effective memory bandwidth to 100 GB/s across all 8 memory channels.

---

## 3. Master Comparison Matrix

| Architecture | Draft Engine | Hardware Topology | Avg Gen Speed | Peak Gen Speed | Acceptance Rate | Verdict |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Exp 0 Baseline** | None (Pure Decode) | Single Node (Node 0) | 11.16 t/s | 11.27 t/s | N/A | Bandwidth limited (50 GB/s) |
| **Exp 4 Interleaved** | None (Pure Decode) | Dual Node Interleaved | 15.72 t/s | 15.89 t/s | N/A | +40.9% speedup (100 GB/s) |
| **Exp 13A Decoupled** | Qwen 3.5 0.8B | Node 0 Tgt / Node 1 Dft | **8.93 t/s** | 9.21 t/s | **8.5% - 51.6%** | **FAILED (-53.6% regression)** |
| **Exp 13B Decoupled** | Native MTP Head | Node 0 Tgt / Node 1 MTP | **14.24 t/s** | 14.68 t/s | 89.7% | **REGRESSION (-26.1% vs Exp 5)** |
| **Exp 5 Native MTP** | Native MTP Head | Dual Node Interleaved | **19.26 t/s** | **21.10 t/s** | **89.7%** | **OPTIMAL TOPOLOGY** |

---

## 4. Key Takeaways & Architectural Lessons

1. **The Small-Model Acceptance Trap:**
   - Small autoregressive draft models (0.8B) fail completely on complex reasoning tasks (8.5% acceptance on GPQA). Even when running at 37.6 t/s, 91.5% of generated tokens are discarded, causing a net throughput collapse.
2. **The Dual-Channel Bandwidth Imperative:**
   - Isolating the target model to a single socket slashes available DRAM bandwidth by 50%. The target model requires the combined bandwidth of all 8 DDR4 channels across both sockets to exceed 15+ t/s pure decode.
3. **Symmetric NUMA Interleaving is Optimal:**
   - `numactl --interleave=all` and `--numa distribute` provide the lowest total step latency by maximizing aggregate memory bandwidth for both target layers and the MTP projection.
