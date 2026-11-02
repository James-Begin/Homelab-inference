# Memory-path labels

The animation separates configured hardware, published architectural references, and calculated ceilings. It does not claim measured cache, RAM, or QPI latency on Talos.

## The current DIMM configuration

A read-only SMBIOS inventory on Talos on October 31, 2026 reports 18 populated DIMMs: fourteen 16 GB modules rated at 2400 MT/s and four 8 GB modules rated at 2133 MT/s. Every populated module reports a **configured speed of 1866 MT/s**. The filtered inventory is saved in [talos-memory-inventory.json](talos-memory-inventory.json); serial numbers are omitted.

Slots A2/A6/A10 and B2/B6/B10 are empty. Dell's [T630 channel map](https://www.dell.com/support/manuals/en-us/poweredge-t630/t630_om/system-memory?guid=guid-77d112e3-72cf-40bf-bcf6-6a61e3a2520d&lang=en-us) places each of those sets on one channel, leaving **three populated channels per socket**. The same table lists 1866 MT/s for three RDIMMs per channel.

Each populated socket has 128 GB, distributed as 48, 0, 40, and 40 GB across its four channels. The combined data-bus ceiling for the three populated channels is approximately:

```text
1.866 billion transfers/s × 8 data bytes/transfer × 3 channels
= 44.784 GB/s per socket ≈ 44.8 GB/s
```

That is a nominal bus calculation, not sustained application read bandwidth. Unequal channel capacities also mean full three-channel interleaving cannot apply uniformly to every address. This inventory describes the current machine; it does not independently establish the DIMM configuration during every historical experiment.

The E5-2680 v4's [published maximum](https://www.intel.com/content/www/us/en/products/sku/91754/intel-xeon-processor-e52680-v4-35m-cache-2-40-ghz/specifications.html) is four DDR4-2400 channels and 76.8 GB/s per socket. That maximum is not the configuration reported here. No BIOS settings or DIMM placement were changed during this check.

## QPI

The CPU specification lists **two QPI links, up to 9.6 GT/s each**. This is a transfer-rate specification; the current negotiated link rate was not separately measured.

Intel's [Broadwell uncore documentation](https://perfmon-events.intel.com/platforms/broadwellx/uncore-events/uncore/) describes four physical transfers per 80-bit flit at full link width. A 64-byte read response takes nine flits: one header and eight data flits. Using both links at the specified rate gives this packet-format ceiling:

```text
9.6 billion transfers/s ÷ 4 transfers/flit × 64 bytes/9 flits × 2 links
= 34.133 billion bytes/s ≈ 34.1 GB/s
```

The label is **one direction, both links, 64-byte responses**. Each physical link is bidirectional; the two drawn paths distinguish a request and its returning data. Other protocol traffic, coherence, stalls, and contention lower usable bandwidth. It is not a measured remote-read result. A remote cache hit may avoid DRAM; the remote path drawn in this clip specifically shows a request served from the other socket's RAM.

## Cache reads

The cache labels come from Intel's [Optimization Reference Manual, Volume 1, v050](https://cdrdv2-public.intel.com/821612/248966-Optimization-Reference-Manual-V1-050.pdf), Table 2-11, printed pages 2-27 and 2-28:

| Broadwell cache | Reference load-hit latency |
| --- | ---: |
| L1 data | 4–6 core cycles |
| L2 | 12 core cycles |
| L3 | 50–60 core cycles |

These are architectural reference values. Core/uncore clocks, addresses, instructions, contention, and cache state affect observed behavior. They are not Talos timing measurements or a fixed nanosecond conversion.

For read throughput, the core can execute two 32-byte loads per cycle with suitable instructions and L1 hits: **up to 64 B/cycle per core**. Intel's [Optimization Manual, Volume 2](https://cdrdv2-public.intel.com/821614/356477-Software-Optimization-Manual_V2.pdf), section 1.4.1 and Table 1-4, describes those load ports for Haswell; section 1.6 describes the Broadwell successor. The 96 B/cycle total in the cache table includes stores and must not be labeled read bandwidth.

## Motion

The diagram uses separate phases for an L3 hit, a local DRAM read, and a remote request/response over QPI. Travel times are chosen for legibility. Their ratios do not encode measured latency or bandwidth.

The standalone L2 capacity clip has been removed from the README. Cache capacities and the earlier projection calculation remain in [the technical evidence note](readme-evidence.md) for reference.
