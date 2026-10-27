# Live Measured Protocol A Ablation Waterfall

| Step | Configuration | Class | Token-Weighted TPS | Median TPS | IQR | Marginal Delta |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **0** | Upstream Baseline (Single-Socket, Q6_K) | Lossless | **7.14 t/s** | 7.14 t/s | 0.01 | **—** |
| **1** | + Dual-Socket NUMA Interleave | Lossless | **10.41 t/s** | 10.41 t/s | 0.05 | **+3.27 t/s** |
| **2** | + 28 Physical Core Pinning | Lossless | **10.28 t/s** | 10.27 t/s | 0.04 | **-0.13 t/s** |
| **3** | + IQ4_XS Dense + Q4_0 MoE (Unrepacked) | Lossless | **11.61 t/s** | 11.62 t/s | 0.11 | **+1.33 t/s** |
| **4** | + AVX2 64-Byte Row Repacking | Lossless | **19.10 t/s** | 19.10 t/s | 0.05 | **+7.49 t/s** |
| **5** | + Merged Up/Gate Experts (-muge 1) | Lossless | **19.49 t/s** | 19.50 t/s | 0.05 | **+0.39 t/s** |
| **6** | + Suffix Speculation (MTP Drafting) | Lossless | **23.49 t/s** | 23.38 t/s | 1.38 | **+4.00 t/s** |
| **7** | Flint 40B MoE Production (ik_llama + MUGE) | Lossless | **21.15 t/s** | 20.98 t/s | 1.75 | **-2.34 t/s** |
