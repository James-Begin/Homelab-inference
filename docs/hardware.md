# Platform Record & Hardware Characterization

Status: Certified empirical measurements on host `talos` (Dell PowerEdge T630).
Implements Phase 5 (Tasks 5.1 & 5.2) of [`improvement-plan.md`](../improvement-plan.md).

---

## 1. Compute & Processor Topology

- **Server Model:** Dell PowerEdge T630
- **Processors:** 2× Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40 GHz (Broadwell-EP, 14nm)
- **Sockets:** 2
- **Physical Cores:** 28 total (14 physical cores per socket)
- **Logical Threads:** 56 total (SMT / Hyperthreading enabled, 2 threads per core)
- **Base Frequency:** 2.40 GHz
- **All-Core Turbo:** ~2.90 GHz | Max Single-Core Turbo: 3.30 GHz
- **Instruction Extensions:** AVX2, FMA3, F16C, BMI1, BMI2, AES-NI (Broadwell AVX2 without AVX-512)

### Cache Hierarchy
- **L1 Data Cache (L1d):** 32 KiB × 28 instances = **896 KiB** (8-way associative, 64-byte line size)
- **L1 Instruction Cache (L1i):** 32 KiB × 28 instances = **896 KiB** (8-way associative, 64-byte line size)
- **L2 Cache:** 256 KiB × 28 instances = **7 MiB** (8-way associative, 64-byte line size)
- **L3 Smart Cache:** 35 MiB × 2 instances = **70 MiB** shared LLC (20-way associative)

---

## 2. Memory Subsystem & NUMA Topology

- **Total RAM:** 256 GB DDR4 Registered ECC
- **Topology:** 2 NUMA nodes (128 GB per socket)
  - **NUMA Node 0:**
    - Physical Cores: `0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26`
    - Hyperthreads: `28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54`
    - Memory: 128,808 MB
  - **NUMA Node 1:**
    - Physical Cores: `1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27`
    - Hyperthreads: `29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55`
    - Memory: 129,010 MB
- **NUMA Distance Matrix:**
  | Node | 0 | 1 |
  | :---: | :---: | :---: |
  | **0** | 10 | 21 |
  | **1** | 21 | 10 |
  - Interconnect: Dual Intel QPI links (9.6 GT/s) with a NUMA latency penalty factor of $2.1\times$.

---

## 3. Measured Memory Bandwidth (STREAM Triad)

Rather than citing theoretical peak numbers (e.g. 76.8 GB/s per socket based on idealized bus arithmetic), actual sustainable memory bandwidth was measured on this machine using a standard OpenMP AVX2 STREAM Triad benchmark ($N = 80,000,000$ doubles, 1.92 GB active footprint, $\gg 70\text{ MB}$ LLC):

| NUMA Configuration | Physical Cores | Pinned Command | Measured Bandwidth | Relative vs. Single Socket |
| :--- | :---: | :--- | :---: | :---: |
| **Local Single Socket (Node 0)** | 14 | `numactl --cpunodebind=0 --membind=0` | **`21.44 GB/s`** | 1.00× (Baseline) |
| **Remote Access (CPU 0 → Mem 1)** | 14 | `numactl --cpunodebind=0 --membind=1` | **`14.52 GB/s`** | **0.68× (-32.3%)** |
| **Dual Socket Interleaved (`--interleave=all`)** | 28 | `numactl --interleave=all --physcpubind=0,2..26,1,3..27` | **`35.22 GB/s`** | **1.64× (+64.3%)** |

### Key Takeaways for Model Serving
1. **Remote Memory Penalty:** Accessing weights allocated on the opposite socket incurs a **32.3% bandwidth penalty** over the QPI interconnect. Single-socket configurations must never span across remote memory.
2. **Dual-Socket Interleaving Benefit:** Distributing model weights round-robin across both sockets via `numactl --interleave=all` aggregates memory channels across both Broadwell memory controllers, unlocking **`35.22 GB/s` sustainable DRAM bandwidth** (+64.3% higher throughput than a single socket).

---

## 4. Operating System & Kernel Environment

- **OS:** Ubuntu 24.04.1 LTS (Linux 6.8.0-147-generic, x86_64)
- **CPU Scaling Governor:** `schedutil`
- **Transparent Hugepages (THP):** `always [madvise] never` (configured to `madvise` to eliminate kernel page-fault tail latencies during active tensor mapping)
- **Compiler:** GCC 13.2.0 / Clang 18.1.3 with `-O3 -mavx2 -mfma -mf16c -fopenmp`
