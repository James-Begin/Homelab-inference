# Hardware

The server is a Dell PowerEdge T630 with two Intel Xeon E5-2680 v4 processors. Each socket has 14 physical cores and its own memory controller. Talos exposes 28 physical cores, 56 logical CPUs, and two NUMA nodes.

| Component | Configuration |
| --- | --- |
| CPU | 2 × E5-2680 v4, Broadwell-EP |
| Clock | 2.4 GHz base, up to 3.3 GHz turbo; actual frequency varies with load |
| Vector instructions | AVX2, FMA3, F16C; no AVX-512, VNNI, or AMX |
| Installed memory | 256 GB registered ECC DDR4 |
| Populated DIMMs | 18: fourteen 16 GB and four 8 GB modules |
| Configured DIMM rate | 1866 MT/s on every populated module |
| Populated memory channels | Three per socket |
| Interconnect | Two bidirectional QPI links, rated up to 9.6 GT/s each |

The DIMM layout comes from a read-only SMBIOS inventory taken on October 31, 2026. Each socket has 128 GB spread across its channels as 48, 0, 40, and 40 GB. The empty channel matters: the CPU supports four DDR4-2400 channels, but that specification does not describe the installed configuration. The inventory does not establish the memory layout during every earlier run.

## Cache and memory paths

| Cache | Capacity | Sharing |
| --- | ---: | --- |
| L1 data | 32 KiB per core | The core's two hardware threads |
| L1 instruction | 32 KiB per core | The core's two hardware threads |
| L2 | 256 KiB per core | The core's two hardware threads |
| L3 | 35 MiB per socket | Cores on that socket |

All reported cache line sizes are 64 bytes. The two L3 domains add to 70 MiB of installed cache; they are separate socket-local caches. An AVX2 register holds 32 bytes. Neither quantity is a 64 KiB cache limit.

A read served from the other socket's RAM crosses QPI. NUMA placement can therefore change where traffic travels, although core affinity alone does not prove page locality. Talos's NUMA distance table reports local distance 10 and remote distance 21; those are scheduler distance values, not measured load-latency ratios.

The populated channels give a nominal data-bus ceiling of `1.866e9 × 8 × 3 = 44.784 GB/s` per socket. This arithmetic excludes controller overhead and contention. Unequal channel capacities also prevent uniform three-channel interleaving over all installed memory.

The [memory-path note](memory-speeds.md) separates configured DIMM rates, Intel's cache references, and the derived QPI packet ceiling. It includes the filtered inventory and primary sources. No reproducible STREAM output or memory-controller counter capture was found in the saved project records, so this repository does not claim a measured DRAM bandwidth ceiling.

## CPU affinity

On the inspected host, node 0's first hardware threads have logical IDs `0, 2, …, 26`; node 1's have `1, 3, …, 27`. Their SMT siblings are 28 IDs higher. This numbering is host-specific. Check socket, core, and sibling IDs before reusing an affinity list on another machine.

Per-run settings belong in the saved manifests. The source and build assumptions are described in [reproduction.md](reproduction.md).
