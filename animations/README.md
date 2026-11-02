# README animations

Four main GIFs accompany the README: memory paths, the AVX2-kernel prefetch, the n-gram history-update change, and the Qwen-to-Flint attention graph. An optional expandable clip explains the upstream weight layout. The animation source draws vector frames, renders them with Sharp, and encodes them with FFmpeg. This is the same geometric style used in the earlier films; the implementation does not use Manim.

Each GIF is 1920 × 1080 at 25 frames/s. The MP4 masters use H.264 at 1920 × 1080 and 60 frames/s. PNG and SVG posters preserve the final explanation without playback. All clips loop, with a hold before returning to their opening state.

| Clip | Duration | What moves |
| --- | ---: | --- |
| `numa-traffic` | 18 s | An L3 hit, a local DRAM read, and a remote request/response over QPI, with sourced rate and latency labels |
| `avx2-prefetch` | 16 s | Current AVX2 work overlaps the added next-group prefetch; the final loop iteration skips it |
| `draft-and-verify` | 16 s | The real history guard change adds available contexts, then lookup proposes a continuation for target verification |
| `flint-vs-qwen` | 22 s | Exact attention-layer strips, then Flint’s sliding/full mask and RoPE choices alongside the port code |
| `repack-eight-rows` | 14 s | Optional: eight scales and four-byte chunks gather into the upstream Q4_0_R8 layout |

The memory clip uses the current SMBIOS-reported configuration: three populated channels per socket at 1866 MT/s. Cache latencies are Intel architectural references; RAM and QPI bandwidth labels are theoretical ceilings. See [memory sources and calculations](../docs/memory-speeds.md). Loop indices, cache arrival, and accepted draft prefixes are illustrations. Q4_0_R8, vector arithmetic, and the speculation framework come from upstream ik_llama.cpp. The code changes shown are the project's guarded prefetch and history-table update. Additional sources are in [the evidence note](../docs/readme-evidence.md).

The Flint comparison uses pinned model configurations and the native port patch. It compares attention behavior, with feed-forward blocks omitted. See [the architecture evidence](../docs/flint-attention.md). It does not assign the coding-test result to an isolated architecture choice.

## Render

Use Node.js 22 or newer and an FFmpeg build with H.264 and GIF palette support. From this directory:

```bash
npm install
npm run render
npm run preview
```

Set `FFMPEG` to the executable path if it is not on `PATH`. To render one clip, pass its ID after `--`, for example `npm run render -- repack-eight-rows`. `--stills` renders posters and sampled frames without encoding video. Sampled frames go to a temporary directory; the media files go to `../docs/media/`.

The renderer refreshes each exported clip's manifest entry; the preview builder reads the README and that manifest. To view it through a local server, run this from the package root, one directory above:

```bash
python3 -m http.server 8770 --bind 127.0.0.1
```

Open `http://127.0.0.1:8770/preview.html`. The preview adds pause controls and uses posters when reduced motion is enabled. The Markdown uses ordinary GIF embeds; GitHub supplies its own layout and playback behavior.
