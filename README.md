# Homelab-inference
https://open.substack.com/pub/james908142/p/teaching-an-old-xeon-new-tricks-a?r=2i1s82&utm_campaign=post-expanded-share&utm_medium=web

This is meant to be a space for the raw results and any other appendix like material. While thats being added, see a copy of the substack article.

I happen to have two Intel Xeon E5-2680 v4 chips sitting in a Dell PowerEdge T630. Broadwell. Released in 2016. No AVX-512 (a wider 512-bit SIMD instruction set that pushes twice the data through each instruction compared to this chip’s 256-bit AVX2). No AMX (Intel’s dedicated matrix-multiply accelerator on newer Xeons). No VNNI, a single instruction that does an 8-bit integer multiply-and-accumulate in one shot. Without it, every quantized dot product on this chip needs a software workaround, and that becomes its own subplot later. Just 14 cores per socket, plus a memory controller that tops out at 76.8 GB/s on paper (less in practice).

And that’s the box I decided to run a 35-billion-parameter Mixture-of-Experts model on, as my daily long-context coding assistant. I wanted actual 256k token coding sessions, the kind where you paste in a whole codebase and ask for a rewrite (and it doesn’t work at all but looks good).

The target model was Qwen 3.6 35B (MoE architecture, various quant levels along the way), served through ik_llama.cpp (a performance-focused llama.cpp fork with its own hand-tuned “IQK” kernel library). The goal was to get token generation comfortably past 20 tokens/second on a single CPU socket.

TLDR baseline was 7.96 t/s. The best config I’ve landed on so far sits at 24.53 t/s, a +208% speedup, on hardware that AVX-512 forgot existed, and I’m still actively testing to pin these numbers down further.



1. Setup

Before touching a single flag, here’s exactly what I was working with:





CPU: 2× Intel Xeon E5-2680 v4 (Broadwell), 14 physical cores / 28 threads each, 35MB L3 cache per socket, AVX2 + FMA3 only.



Memory: 4-channel DDR4-2400 per socket → theoretical peak bandwidth of 76.8 GB/s on Socket 0 alone (4 × 8 bytes × 2.4 GHz).



Model: Qwen 3.6 35B, a MoE model that only activates a fraction of its parameters per token. That sparsity is the entire reason any of this is possible.

Back of the envelope, a dense 35B model at Q6_K quantization is about 27.3GB. To generate one token, you have to stream the entire weight set through RAM at least once. 76.8 GB/s ÷ 27.3 GB ≈ 2.81 tokens/second. That’s the physical ceiling for a dense model this size on this hardware. Code can’t move it. Only sparsity can.



A cheat sheet for the quant names, since they come up constantly: the number after the Q is roughly how many bits each weight averages out to (Q6_K is about 6 bits per weight, Q4_0 about 4, down from 16 or 32 bits unquantized). Formats with a _K suffix (”k-quants”) use extra layers of per-block scale factors for better accuracy per bit, at the cost of a more complex unpacking step. Formats like _0 (q4_0, q8_0) use an older, simpler flat scale, less accurate bit-for-bit, but cheaper to unpack. You’ll also see _M/_S suffixes like Q4_K_M, just “medium”/”small” variants that shade bits toward different tensors.

The only reason double-digit token/sec numbers were even on the table is that Qwen 3.6 is sparse. Each token only routes through a handful of “expert” sub-networks, activating roughly 3B parameters (~2.3GB) instead of the full 35B.

Under the hood, every layer has a small “router” that looks at each token’s hidden state and scores all 8 available experts, then picks the top few. Only the weight matrices for those chosen experts get pulled out of RAM for that token. The rest just sit in memory, completely untouched. That’s why MoE models can be huge on disk but still fast on a bandwidth-starved CPU. You’re only paying the RAM-read cost for a slice of the model. It’s also a preview of the biggest win in this whole post (Section 6). Fewer chosen experts per token means fewer weight matrices dragged through the memory bus per token.

The strategy was to lock everything to Socket 0 with numactl --cpunodebind=0 --membind=0. The short version of why that matters is that on a dual-socket system, each CPU has its own local bank of RAM (that’s what NUMA, Non-Uniform Memory Access, means), and the two sockets are connected by a much slower inter-socket link, Intel’s QuickPath Interconnect (QPI). A thread on Socket 0 reading memory that physically lives on Socket 1 has to hop across that link. On this chip, QPI runs at 9.6 GT/s across two links, which works out to roughly 19.2 GB/s in one direction per link, against the 76.8 GB/s each socket has to its own local DRAM. So a cross-socket read stream tops out at around a quarter of local bandwidth before you even count the extra latency of the hop. numactl pins both threads and memory allocations to Socket 0 so every read is forced local.



2. SIMD

Almost everything in this post traces back to instructions the CPU does or doesn’t have.

What SIMD is

A normal, scalar CPU instruction takes two numbers and produces one. Multiply a by b and get one result. SIMD, Single Instruction Multiple Data, takes two vectors of numbers and applies the same operation to every element at once, one “lane” per element. A single SIMD multiply can do 8 or 16 multiplies in the time a scalar one does a single multiply, because the hardware has wide registers and enough parallel multipliers to fill them.

This matters for inference because inference is almost entirely matrix multiplication, a matrix multiply is just a huge pile of dot products, and a dot product is “multiply these two rows element by element, then add up the results.” That is the most SIMD-friendly shape a workload can have. The same operation, repeated across a long array, with no data-dependent branching in the inner loop. So how wide your vectors are and which multiply-accumulate instructions you have translates almost directly into how fast the compute-bound parts of inference run.

AVX2: 256 bits at a time

AVX2 gives you 16 vector registers (named YMM0 through YMM15), each 256 bits wide. What fits in 256 bits depends on the data type. 8 FP32 floats, or 16 FP16/BF16 values, or 8 32-bit integers, or 16 16-bit integers, or 32 8-bit integers. One AVX2 instruction can therefore chew through up to 32 quantized 8-bit weights in a single shot.

The workhorse instruction for float inference is FMA3, the fused multiply-add. _mm256_fmadd_ps computes a * b + c across all 8 FP32 lanes at once, with a single rounding step at the end instead of two. A dot product is nothing more than a running FMA marched down a row, so FMA is vital to float matmul. Broadwell has two FMA-capable execution ports that can each issue a 256-bit FMA every cycle, so at full tilt one core can do 2 × 8 = 16 fused multiply-adds per cycle.

For quantized inference the picture gets a lil muddier. The closest AVX2 has to an integer dot product is _mm256_maddubs_epi16. It takes 32 pairs of 8-bit values, one operand unsigned and one signed, multiplies each pair, and adds adjacent pairs together into 16 signed 16-bit results. There is no AVX2 instruction that multiplies 8-bit values and accumulates straight into a 32-bit total. You have to build that out of maddubs plus a second widening-add step, and you have to make sure the intermediate 16-bit accumulator from overflowing (citing the school of hard knocks on that one). This will be important in section 5.

AVX-512 / VNNI / AMX

I listed three things this chip doesn’t have. They are separate features, which can be useful for inference.

AVX-512: the obvious one, twice the width. Registers grow from 256 to 512 bits (now called ZMM), the count doubles from 16 to 32, and you also get 8 dedicated mask registers. Width alone means one instruction handles 16 FP32 or 64 int8 values, so on a comparable core you get up to double the compute per instruction issued. The extra registers let a matmul microkernel keep a bigger block of the running total in registers instead of moving it to memory, which is a big part of what makes a fast GEMM fast. The mask registers add per-lane predication, so you can process “just the last 5 elements” of a ragged row, or apply a routing decision, without a scalar cleanup loop or a branch. Inference produces a lot of ragged, not-a-multiple-of-the-vector-width shapes, so branch-free tails can be useful.

VNNI: AVX-512-VNNI adds VPDPBUSD, and that single instruction does the entire int8 dot product. It takes unsigned 8-bit values and signed 8-bit values, multiplies them pairwise, sums each group of four, and accumulates the result directly into 32-bit lanes. Directly into 32-bit means there is no 16-bit accumulator to overflow and no sign trick to set up. It’s exactly the operation Section 5 has to fix in two or three instructions. Every quantized dot product on Broadwell pays that multiple, and quantized dot products are most of what quantized inference does. (Intel did eventually backport this to 256-bit vectors as “AVX-VNNI” on Alder Lake and later client chips, but Broadwell came before all of that.)

AMX: Rather than wider vectors, AMX adds 2D tile registers and a matrix-multiply instruction that takes two tiles, multiplies them, and accumulates into a third, doing a whole small matrix multiply per instruction instead of one row’s worth of multiply-adds. On Sapphire Rapids and newer it pushes int8 and bf16 matmul throughput far past what even AVX-512 manages lane by lane, and it’s a big boost for prefill-heavy or batched serving. Broadwell, of course, does not feature this.

This hurts prefill, not decode

Every instruction above accelerates compute, the raw rate of multiply-accumulates. None of them do anything for memory bandwidth. And which of those two is your bottleneck flips completely between the two phases of inference.

Token generation, decode, streams the active weights out of RAM one token at a time, and it’s bandwidth-bound (the whole argument from Section 1). The math units already sit idle waiting on data most of the time, so a chip that could do the arithmetic twice as fast would simply wait twice as long between numbers. AVX-512 and VNNI would barely move single-stream decode, because decode isn’t waiting on the ALU.

Prompt processing, prefill, is the mirror image. It runs one big matrix multiply across the entire prompt at once, the weights get pulled into cache once and reused across every token in the batch, and the bottleneck slides off the memory bus and onto raw FMA and int8 throughput. That is precisely the regime AVX-512, VNNI, and AMX were designed for.

So the missing instructions cost me a lot of prefill speed I would have loved to have, and they cost decode, the number you actually stare at while waiting for a response, almost nothing. Prefill on this box tops out around 120 t/s and gladly eats every thread I give it (Section 4). Decode lives in the low tens of tokens per second no matter how clever the kernel gets, because the wall there is a 76.8 GB/s memory bus and no instruction set changes that. That asymmetry is the entire reason a decade-old Broadwell is a sane place to run a model at all.



3. Baseline and basic tests

The starting line

Default settings, 14 threads, Flash Attention on (a memory-efficient way of computing attention in small tiles instead of materializing the full attention matrix, standard enough that it stayed on for the entire project), F16 KV cache:

ContextPrompt ProcessingToken Generation8k94.25 t/s7.64 t/s16k79.19 t/s6.90 t/s

Generation speed barely moved between 8k and 16k context (7.64 → 6.90 t/s), a strong early signal that token generation is memory-bandwidth bound, not compute or attention bound. That single observation quietly predicted almost everything that mattered for the rest of this project. Moving fewer bytes per token would buy more than doing less math per token.

Thread count

Conventional wisdom says hyperthreading/SMT hurts memory-bound workloads, since you’re contending for the same cache lines and memory ports with twice the logical threads. Cranking threads from 14 (physical) to 28 (SMT) made things 6% faster instead (78.36 → 83.12 t/s combined pp+tg speed).

The reason that’s not as crazy as it sounds is that a physical core has several execution ports that can each start a math operation per cycle, but a thread stalls those ports whenever it’s waiting on data from memory. A second hardware thread (SMT) can slot its own instructions into those same idle ports during the stall, backfilling wasted cycles. That only helps if there’s compute sitting around waiting to fill the gap, which MoE’s branchy routing apparently provides. It won’t be the whole story though (see Section 4). Decode turns out to have no spare compute to backfill with, just contention for the same bytes off the memory bus.

KV cache quant

A bit of background first. Generating each token means computing attention against every prior token in the conversation. Recomputing Key/Value vectors for the whole history at every step would be absurd, so llama.cpp caches them in what’s called the “KV cache,” appending only the newest token’s K/V each step. But that entire cache still has to be read back from RAM every step, so it competes for the same 76.8 GB/s as everything else. At 32k context that’s gigabytes of K/V vectors, and shrinking them via quantization directly shrinks what gets re-read every token.

Sweeping K/V cache precision (f16, q8_0, q4_0) turned up a nice, slightly counter-intuitive result. Quantizing the Key cache to q8_0 gave a solid +3.6% speedup, but quantizing the Value cache did almost nothing on its own. Why K and V responded so differently isn’t fully clear from these logs, plausibly something specific to how ik_llama‘s attention kernel accesses each buffer, but it held consistently across every sweep. Going further to q4_0 for both was actually slower than q8_0. On CPU, unpacking 4-bit nibbles and rescaling them costs enough extra instructions to eat the memory-bandwidth savings. q8_0/q8_0 won as the sweet spot, real bandwidth savings, minimal unpacking tax.

Batch size, MoE flags





Micro-batch size (-ub): controls how many tokens get processed together in one pass through the compute graph (mainly matters during prompt ingestion). Bigger batches mean more math gets done per weight-load from RAM, better efficiency, as long as the batch’s working set still fits in cache. 512 → 1024 gave a small +0.7% bump. Pushing to 2048 made things slightly worse. With only 35MB of L3 per socket shared across everything running, a large enough batch’s activations stop fitting comfortably alongside the weight tiles also competing for that space, so you start evicting data you still need and paying for it in RAM round-trips instead of cache hits.



--defer-experts / -ger (MoE scheduling flags): each gave modest, independent ~0.8-0.9% gains by reducing thread contention on the currently-active experts. Combining them was not additive. They stepped on each other slightly. Take the better one, not both.



Transparent Huge Pages (-thp): a dead end, included because “I tried the obvious thing and it did nothing” is still useful. The reason it should have helped is that the CPU translates virtual to physical addresses through the TLB (Translation Lookaside Buffer), where each entry normally covers a 4KB page. A model with tens of gigabytes of weights spans millions of such pages, causing constant TLB misses while walking through them. Huge pages (2MB each) mean one TLB entry covers 512x more memory, in theory cutting that miss rate a lot. In practice, the allocation failed (mmap ... Cannot allocate memory, because fragmentation meant no contiguous 2MB blocks were available), and even when it worked later, a direct A/B comparison showed zero statistically significant difference. In this workload, weights and KV cache get walked sequentially enough that the CPU’s hardware prefetcher (which predicts and pulls in the next cache line before you ask for it) already hides most of that page-walk latency, making huge pages redundant here. Nice theory, no payoff, so I buried it and moved on.

run-time tensor repacking

Then, almost as an afterthought in a sweep of assorted advanced engine flags, one flag beat everything else in the sweep by a wide margin:

FlagResult-rcache 1 (RoPE cache)no difference-mqkv 1 (merged QKV)slightly worse-muge 1 (merged up/gate experts)+2.6%, but ballooned memory from 27.3GB → 43.7GB-sas 1 (async scheduler)slightly worse-rtr 1 (run-time tensor repack)+6.75%, zero extra memory

-rtr physically rewrites the model’s tensors in RAM once at load time, into exactly the byte order the AVX2 kernels want to stream through during a dot product. Without it, weights sit in the layout the GGUF file format uses for compact on-disk storage, fine for loading, but not necessarily the order the compute kernel actually walks through them in, which means occasional strided or misaligned reads the CPU’s prefetcher can’t predict well. Repacking removes that mismatch entirely. It was the single best free lunch of the entire early sweep phase, free as in it didn’t cost a single extra byte of RAM, unlike -muge‘s tempting-but-expensive alternative.

Milestone check: stacking everything from this phase (28 threads, q8_0/q8_0 KV cache, -ub 1024, --defer-experts, -rtr 1) took the 16k-context combined speed from 73.24 t/s → 90.36 t/s. A 23.4% speedup, worth about 43 seconds per 16k-token interaction. Not bad for flag-tuning alone. But token generation, which is the number you actually feel while waiting on a response, was still stuck in single digits. Time to bring out speculative decoding.



4. Speculative decoding

This is where flag-tuning stopped being enough and the pipeline itself needed some finagling.

MTP

ik_llama.cpp supports Multi-Token Prediction (MTP) speculative decoding, where a small auxiliary head predicts a few tokens ahead, and the main model verifies them in a single batched pass instead of generating them one at a time. Since MTP speculation only runs inside llama-server (not the benchmark tool), this meant switching to full server benchmarks for the rest of the project.

Every speculation method below leans on the same trick, so I’ll spell it out once here. Generating tokens one at a time means streaming the entire active weight set out of RAM for every single token, the actual bottleneck, per Section 1. But running a forward pass over a batch of several candidate tokens costs almost the same one RAM read as running it over a single token, because the weights get pulled into cache once and reused across the batch, and only the (much cheaper) compute scales up. So if you can cheaply guess a few likely next tokens and verify them all in one batched pass, you get several tokens for close to the bandwidth price of one. Everything below is really just “how do we guess well, and as cheaply as possible.”

Turning on a single MTP head took generation from 7.96 t/s → 10.61 t/s, a +33% speedup for almost nothing, since verification of an accepted draft token is much cheaper than generating it token-by-token.

Threading, again

The SMT result from Section 3 didn’t hold up once I split it by phase instead of measuring combined pp+tg speed:





Prompt processing (compute-bound, matrix-math heavy): 28 threads (SMT) beats 14 physical threads, 124.24 t/s vs 118.13 t/s.



Token generation (bandwidth-bound, one token at a time): 14 physical threads beats 28, 8.26 t/s vs 7.96 t/s. SMT causes L3 cache contention that actively hurts when you’re not compute-bound anymore. During decode, both hyperthreads pull from the same shared L1/L2 cache and issue their own memory requests against the same 76.8 GB/s pipe. There’s no idle compute to backfill, so the second hyperthread just halves the same trickle of bytes off the bus.

The earlier number held up. It just hid a split I hadn’t measured. It had been taken on a combined pp+tg metric that masked the two phases wanting opposite thread counts. The fix is to stop measuring them together. ik_llama.cpp exposes separate knobs for this (-t for generation threads, -tb for batch/prefill threads), so I set each to what its phase wanted. Running generation on physical cores only pushed things to 10.98 t/s, a +37.9% total gain over the SMT-only no-MTP baseline. This asymmetric-threading setup (-t 14 -tb 28) stuck around in every config for the rest of the project.

Tuning draft depth (n_max)

MTP can recursively feed its own predicted hidden state back into itself to draft multiple tokens before a single verification pass. Sweeping the draft depth (n_max) found a genuine sweet spot.

The mechanics matter here, because they explain the sweet spot. The main model verifies a draft position by position, and the instant there’s a mismatch, every drafted token after that point gets discarded, even if the draft continued further. Acceptance compounds multiplicatively. If there’s an 85% chance the model agrees with any single drafted token, the odds it agrees with all 5 in a row are only about 0.85⁵, roughly 44%. Draft too deep and you’re increasingly paying for speculative passes on tokens that get thrown away before you ever reach them.

n_maxToken Genvs no-MTP baseline110.44 t/s+31.1%211.85 t/s+48.9%312.76 t/s+60.3%413.77 t/s+73.0%514.21 t/s+78.5%613.10 t/s+64.6%713.28 t/s+66.8%

Speed climbs steadily, then falls back off past 5. Drafting further ahead means running more speculative forward passes, but the model’s confidence in tokens that far ahead drops, acceptance rate collapses, and you’re burning compute on guesses that get thrown away. n_max=5 landed as the best trade-off for this model.

Hadamard transforms

Layering Hadamard transforms onto the quantized KV cache (-khad -vhad) squeezed out another +4% (14.53 t/s) while improving accuracy relative to plain q8_0. This one is worth unpacking, because it’s a genuinely cool bit of math.

Quantizing a block of numbers means picking one scale factor for the whole block and rounding every value to the nearest step of that scale. The catch is that the scale has to be large enough to represent the biggest value in the block, so a single outlier, one weight 50x larger than its neighbors, forces a coarse scale on everyone else. The common small values then get rounded brutally, and most of your bit budget gets spent describing the empty gap between the outlier and everything else. Transformer activations are full of these outliers, so this is exactly where quantization accuracy tends to die.

A Hadamard transform attacks the outlier directly. A Hadamard matrix is a square matrix whose entries are all +1 or -1, arranged so that every row is orthogonal to every other row. The smallest is the 2×2 [[1, 1], [1, -1]], and larger ones are built by tiling that pattern recursively, so a 4×4 is that 2×2 block repeated with one copy negated, and so on upward in powers of two. Normalize the whole thing by 1/√n and it becomes an orthonormal matrix, which geometrically is just a rotation-and-reflection of the vector. It doesn’t change the vector’s length, only its direction.

The property that matters is what that rotation does to a single big value. Multiplying a vector by a Hadamard matrix makes every output element a sum of every input element, each one flipped to plus or minus by the matrix. So one large spike in the input doesn’t survive as a spike. It gets smeared with equal weight across all the outputs, coming out as many medium-sized values instead of one giant value surrounded by small ones. The block’s dynamic range collapses, a single scale factor now fits everybody well, and the same number of bits buys far less rounding error. This is the same core trick behind recent quantization work like QuaRot and QuIP#, which rotate weights and activations to crush outliers before quantizing.

Two things make it close to free. First, it’s exactly reversible. An orthonormal Hadamard matrix built this way is its own inverse, so applying the same transform a second time undoes the rotation exactly, leaving only the rounding error, which is now far smaller than it would have been without the rotation. Second, you never actually build or multiply by the full matrix. Because of its recursive structure there’s a Fast Walsh-Hadamard Transform that computes the whole thing in n·log(n) steps using only additions and subtractions, no multiplies at all, which is about as cheap as an operation gets on a CPU. You pay a tiny slice of compute to move the outliers out of the way, and you get real bits back in return.

Going further to a plain q4_0 cache (no Hadamard) was even faster (+8.3%, 15.13 t/s), but at a real quality cost from the more aggressive quantization.

This is the point where the project split into two philosophies that persisted to the end:





Quality-first: q8_0 cache + Hadamard. Near-f16 accuracy, still very fast.



Speed-first: q4_0 cache, no Hadamard. Faster, measurably lossier.

The best trick in the whole project: predicting code with no compute at all

Then came the discovery that reframed the entire speculation strategy. Instead of (or alongside) a neural MTP head, ik_llama.cpp supports N-gram speculative decoding, a purely statistical lookup against your own recent context, with zero floating-point operations. No forward pass, no neural prediction, just “have I seen this exact sequence of tokens before in this conversation?” Functionally it’s autocomplete. The engine keeps a rolling index of short token sequences it’s already seen in this conversation, and whenever the tokens it just generated match one, it bets that whatever followed last time will follow again. No matrix multiplication involved, just a lookup.

ConfigToken GenBaseline (MTP n_max=5, p_min=0.1)12.91 t/sSpeculative auto-tuning13.31 t/sN-gram speculation15.89 t/s

+100% over the no-speculation baseline, and it works because source code is extremely repetitive. Braces, indentation, variable names, boilerplate loop structures. An N-gram cache built from the conversation’s own recent history predicts these near-perfectly, and because it costs zero compute, it never competes with the main model’s forward pass for AVX2 execution units. It’s the one speculation method here that has basically no downside.

Chaining strategies also helped. Falling back to MTP whenever the N-gram cache came up empty added another +13.5% on top later in the project (Section 6), best of both worlds, N-gram for the repetitive stretches, neural drafting for the genuinely novel ones.



5. Patching the kernel directly

At this point, flag-tuning was mostly exhausted. So I opened up iqk_mul_mat.cpp, the hand-written AVX2 kernel library underneath ik_llama.cpp, to see what the CPU was actually doing.

The 71% idle problem

Qwen 3.6 35B routes each token through 4 active experts (Nx = 4). During single-token decode, the existing thread-partitioning code divides the row dimension across threads:

auto nrc_x = (Nx/num_rows + nth - 1)/nth;   // Nx=4, nth=14 → nrc_x = 1

With only 4 rows of work and 14 threads wanting a piece of it, threads 0-3 get one expert each, and threads 4 through 13 get nothing and sit idle. That’s a 71.4% thread starvation rate, ten of your fourteen physical cores doing nothing during exactly the phase (MoE decode) that dominates generation latency.

The fix: split columns instead of rows

The fix flips the partitioning strategy specifically for this small-batch case. Instead of handing each thread a whole row (expert), group threads and have each group split the inner dot-product dimension (K, ~4096+ features) of a single expert’s row. With 14 threads and 4 rows, that’s roughly 3 threads cooperating per expert, each computing a partial dot product over a slice of the row, then reducing their partial sums together.

if (Nx < nth) {
    int threads_per_row = nth / Nx;
    int row_idx = ith / threads_per_row;
    int group_tid = ith % threads_per_row;
    // ...partition K across group_tid, then reduce...
}

This raised CPU utilization during MoE decode from 28% to 100%. While generation speed itself was already saturating the memory bus by this point (so the headline t/s gain was modest), the follow-on 64-byte memory alignment pass is worth a word on why 64 specifically. On this CPU, like nearly all x86 chips, data moves between RAM and cache in fixed 64-byte chunks (cache lines). An AVX2 register loads 32 bytes at a time, so two loads should fit neatly in one cache line. But if a buffer starts at an arbitrary unaligned address, a 32-byte load can straddle the boundary between two 64-byte lines, forcing the CPU to fetch both and stitch them together instead of grabbing everything from one. That “cache-line split” costs a handful of extra cycles per load, and across millions of loads during MoE decode, it adds up. Explicitly requesting 64-byte-aligned memory for thread-local scratch buffers and row strides, instead of the compiler’s default 16/32-byte alignment, guarantees every AVX2 load lands cleanly inside one line. That pass added a clean +1.5% to prompt processing and +2.1% to cached prompt processing on top of everything before it. Small numbers, but earned the hard way, at the instruction level.

(One more rabbit hole for anyone curious why quantized dot products need a “sign trick” at all. AVX2’s _mm256_maddubs_epi16 requires one signed and one unsigned 8-bit operand, but both weights and activations are naturally signed. The standard fix, offsetting everything by +128, requires tracking and subtracting a compensation term, and risks 16-bit accumulator overflow. The accumulate instruction sums adjacent products into a 16-bit integer, and two max-sized products under the offset method (255 × 127 = 32,385 each) already blow past the signed 16-bit limit of 32,767, which is silent corruption. The trick used here, w·x = |w| · (x · sign(w)), keeps every value in the signed range (max 127 × 127 = 16,129 per product), so even two summed (32,258) stay safely under the limit. That one move solves the overflow risk and the compensation-term bookkeeping at once, and it was already load-bearing in the kernels touched during this pass.)



6. Quantization surgery

Finding out where the time actually goes

Rather than keep guessing, I instrumented ggml‘s (the low-level C tensor-math library underneath both llama.cpp and ik_llama.cpp) own thread-dispatch loop to time each operator directly. First attempt, a data race (ten threads all appending to a shared timing array with no atomics) inflated numbers to nonsense, a 1.1-second kernel reported as 14.7 seconds. Fixed by only measuring from thread 0. Second attempt gave real numbers:

OperatorShare of Eval TimeMUL_MAT (attention Q/K/V, output projections)52%MOE_FUSED_UP_GATE (MoE expert up/gate)39%MUL_MAT_ID (MoE expert down-proj)21%*

(percentages overlap slightly by measurement boundary, but the takeaway was unambiguous. Attention and MoE FFN dominate, and both are ultimately paying the same memory-bandwidth tax.)

Mixed-precision quantization

Dropping the dense attention layers to Q4_K actually made things slower. Broadwell’s Q4_K bit-unpacking path has more CPU overhead than Q6_K‘s, so you’d be trading memory bandwidth for compute, a bad trade when compute is already the secondary cost. But Q4_0 has a highly optimized AVX2 fallback path, and applying it specifically to the MoE expert weights while leaving attention/dense layers at Q6_K gave the best of both:





Pure Q6_K: 8.33 tokens/sec (no speculation, raw eval)



Q6_K dense + Q4_0 MoE experts: 10.50 tokens/sec, +26%

The MoE expert tensors are both the largest memory consumers and the least sensitive to precision loss, since each token only exercises a handful of them, so that’s exactly where the quantization budget belongs.

The biggest win in the entire project

And then the biggest win of the whole project turned out to be a one-line config change, and it barely felt like one at the time. How many experts does each token get routed to?

Qwen 3.6 35B defaults to 8 active experts per token. You can override that at load time:

--override-kv qwen35moe.expert_used_count=int:4

(with a small gotcha along the way, the override silently failed the first time because the internal architecture string is qwen35moe, not the more common qwen2moe, so the flag needs the exact right namespace)

Result: 12.22 t/s → 24.53 t/s, a +100.7% speedup from changing one config value.

Halving the active experts halves both the memory traffic and the FFN math for the heaviest layers in the model, and llama.cpp automatically renormalizes the routing weights of the surviving top-4 experts (the original scores were fractions of a sum across all 8, so without rescaling them back to sum to 1, the combined output would come out smaller than the rest of the network expects, quietly throwing off scale downstream), so the cut isn’t arbitrary. It falls back on the router’s four most-confident picks and degrades gracefully from there. Going further to 2 experts looked tempting on paper but backfired (11.80 t/s). Too aggressive a cut shifts the output logit distribution enough that N-gram speculation’s acceptance rate collapses, and you lose more from broken speculation than you gain from a smaller compute footprint. Four experts was the number that actually mattered.



7. A small stumble

Combining N-gram speculation with the new mixed-precision model (Q6_K dense + Q4_0 experts) caused llama-server to intermittently drop connections. Root cause was N-gram speculation performing rapid internal state rollbacks whenever a drafted token gets rejected, and those rollbacks were hitting misaligned memory strides specific to the mixed-precision tensor layout.

Fix: forcing --run-time-repack (the same -rtr flag from Section 3, now doing double duty) and --defer-experts together ensures the mixed-precision tensors are physically laid out in contiguous memory before speculative rollback ever has a chance to touch a bad stride.

(There were more stumbles, I just need to figure out why!)



8. Sanity Check

Every optimization so far has been in service of a number going up. None of it matters if the model got dumber along the way, so I ran the exact same prompts against the old baseline config (Q6_K, 8 experts) and the new optimized config (Q4_0 experts, 4 active) side by side:





Topological sort with cycle handling: baseline produced a correct Kahn’s-algorithm implementation at 8.53 t/s. Optimized produced an equally correct implementation (with visibly more deliberate reasoning about complexity trade-offs in its thinking trace) at 12.46 t/s.



Thread-safe LRU cache: both versions correctly reached for std::mutex + hashmap + doubly-linked-list, at 8.49 vs 12.45 t/s.



Multi-step arithmetic word problem: both landed on the correct answer (72,000 requests/minute) with correct intermediate reasoning, at 8.53 vs 12.49 t/s.

Three prompts are not an eval suite, and a broader pass is still running. Still, all three told a similar story, near-identical reasoning quality at roughly 1.5x the speed.



9. Testing some ceilings

With the throughput side of things settled, the last open question was about scale. How far could this setup actually go on truly long context, and where would it break?

Three tests specifically to check whether a model can actually use information buried deep in a long context, the classic needle-in-a-haystack, bury one fact in thousands of tokens of junk and ask for it back), and a hard-logic suite (competition math, graduate-level QA).

The reasoning check held up so far, 100% accuracy on the RULER needle-in-a-haystack test at 4k tokens. The aggressive 4-expert clamping and Q4_0 quantization hadn’t broken the model’s ability to trace a specific fact buried in thousands of tokens of distractor text. Sweeps at deeper context (16k and beyond, which is really the scale that matters for this use case) are still actively running as of this writing.

I’d gone into this expecting RAM to be the limiting factor. 264GB sounds like a lot, but KV cache scales with context length, and I half expected an out-of-memory crash somewhere in the six-figure token range. Instead, thanks to Grouped Query Attention (GQA, several attention “query” heads share one Key/Value head instead of each head getting its own, cutting KV cache size by that sharing factor), the KV cache at the model’s absolute maximum context (262,144 tokens, its own hardcoded architectural limit) is only 5.1GB. Memory was never the bottleneck. The wall turned out to be the context window Qwen was trained on.

Prompt processing speed degrades quadratically with context length as expected, from ~120 t/s near zero context down to a still-very-respectable 19.4 t/s at 192,000 tokens, roughly a novel’s worth of text, on every single request, while staying within shouting distance of the original 20 t/s target. And when I deliberately pushed past the model’s native limit using RoPE scaling (RoPE, Rotary Position Embedding, encodes each token’s position by rotating its Query/Key vectors by an angle that grows with position, and scaling stretches that rotation to represent positions further out than the model ever trained on, essentially asking it to extrapolate a pattern past the range it learned), feeding it roughly 384,000 tokens, well beyond the trained 262K ceiling, I got a llama_decode() failed error and am working on fixing it. Pushing further into more aggressive RoPE-scaled territory is where the server crashed outright. I don’t have a clean read yet on exactly where that edge sits or whether it’s a memory limit or a numerical one, so that sweep is still running before I’d call it a real finding.



10. The numbers so far

One thing to explain before the table. Milestone 4’s jump came from tightening NUMA locking further, from numactl --membind=0 to also passing --numa isolate to llama-server directly. The reason the wrapper alone wasn’t enough is NUMA’s default “first-touch” behavior, where a memory page gets physically placed on whichever socket’s CPU first writes to it, not necessarily the one you intended. Even with numactl binding the whole process to Socket 0, some of llama-server‘s internal parallel-reduction buffers were still occasionally getting first-touched in a way that landed on the wrong node, forcing a slow cross-socket hop on every later access. --numa isolate enforces the binding inside the engine itself, guaranteeing every buffer, not just the ones numactl happened to catch, stays local.

The whole arc, milestone by milestone:

StageModel QuantWhat ChangedToken Gen SpeedGainBaselineQ6_KDefault settings, no speculation7.96 t/sN/AMilestone 1Q6_KKernel thread-scheduling fix + N-gram speculation15.86 t/s+99.2%Milestone 2Q4_K_MDown-quantization (30% less memory traffic)19.63 t/s+146.6%Milestone 3Q4_K_MStep-by-step N-gram database updates19.66 t/s+147.0%Milestone 4Q4_K_MStrict NUMA memory isolation + 10 threads23.54 t/s+195.7%

Current best config (Q6_K, near-full precision, 24.53 t/s):

numactl --cpunodebind=0 --membind=0 ./bin/llama-server \
  -m Qwen3.6-35B-A3B-UD-Q6_K.gguf \
  -c 8192 -t 10 -tb 28 \
  -ctk q8_0 -ctv q8_0 -khad -vhad \
  -ub 1024 --defer-experts --run-time-repack \
  --spec-type ngram-mod:n_max=5,ngram_size_n=8 \
  --override-kv qwen35moe.expert_used_count=int:4 \
  --numa isolate -fa 1

What actually mattered

If I had to boil this down to what’s worth actually using so far, cutting active experts from 8 to 4 outweighed every other change put together. After that, matching the speculation strategy to the workload mattered a lot, N-gram beat neural MTP here specifically because code repeats itself, though that won’t hold for something like creative writing. Splitting thread count by phase (SMT for prefill, physical cores for decode) was a smaller but free win once I noticed the two phases wanted opposite things. Mixed-precision quantization, full precision on attention and aggressive quantization on the MoE experts, beat quantizing everything uniformly. And profiling before guessing paid for itself. The flag-tuning phase got 23%, but once I knew where the time was actually going, going into the C++ got a lot more.



11. What I’m Testing Next

None of the numbers above are final, they’re just where things stand right now. What’s still queued up or actively running:





Deeper RULER sweeps, and the fuller suite, not just 4k.



Mapping the RoPE-scaling breaking point properly instead of the one crash I hit jumping straight to an extreme value.



A real quality eval (GSM8K, HumanEval) instead of three hand-picked prompts.



Concurrency and a long soak test. Everything so far is one request at a time on a short run, and this box is old enough to worry about thermal throttling under sustained load.

I’ll keep this post updated as those are done.
