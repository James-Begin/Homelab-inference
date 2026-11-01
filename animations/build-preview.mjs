import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { marked } from 'marked';

const here = path.dirname(fileURLToPath(import.meta.url));
const output = path.resolve(here, '..');
const readme = fs.readFileSync(path.join(output, 'README.md'), 'utf8');
const manifestPath = path.join(output, 'docs/media/manifest.json');
const manifest = fs.existsSync(manifestPath)
  ? JSON.parse(fs.readFileSync(manifestPath, 'utf8'))
  : {};

const clips = {
  'numa-traffic': 'Cache, local and remote memory reads',
  'avx2-prefetch': 'Prefetch in the AVX2 kernel',
  'repack-eight-rows': 'Repacking eight rows for AVX2',
  'draft-and-verify': 'N-gram history update and verification',
  'flint-vs-qwen': 'From Qwen to Flint',
};

const escape = value => String(value).replace(/[&<>"']/g, char => ({
  '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;',
})[char]);

function manifestEntry(name) {
  if (Array.isArray(manifest)) {
    return manifest.find(item => item.id === name || item.name === name || item.slug === name) || {};
  }
  const collection = manifest.animations || manifest.clips || manifest.assets || manifest;
  if (Array.isArray(collection)) {
    return collection.find(item => item.id === name || item.name === name || item.slug === name) || {};
  }
  return collection[name] || {};
}

function assetInfo(src) {
  const file = path.join(output, src);
  if (!fs.existsSync(file)) return null;
  const buffer = fs.readFileSync(file);
  const gif = buffer.toString('ascii', 0, 3) === 'GIF';
  return {
    bytes: buffer.length,
    width: gif ? buffer.readUInt16LE(6) : undefined,
    height: gif ? buffer.readUInt16LE(8) : undefined,
  };
}

function makeFigure(src, alt) {
  const name = path.basename(src, '.gif');
  const title = clips[name] || alt || name;
  const poster = src.replace(/\.gif$/, '.png');
  const master = src.replace(/\.gif$/, '.mp4');
  const info = assetInfo(src);
  const entry = manifestEntry(name);
  const duration = entry.durationSeconds ?? entry.duration ?? entry.seconds;
  const width = info?.width || entry.width || 1600;
  const height = info?.height || entry.height || 900;
  const details = [
    Number.isFinite(Number(duration)) && Number(duration) > 0 ? `${Number(duration)} s` : null,
    info ? `${width} × ${height}` : null,
    info ? `${(info.bytes / 1024 / 1024).toFixed(1)} MiB GIF` : null,
  ].filter(Boolean).join(' · ');
  if (!info) {
    return `<figure class="animation pending"><div class="pending-image">${escape(title)}<span>Animation export pending.</span></div></figure>`;
  }
  const posterExists = fs.existsSync(path.join(output, poster));
  const masterExists = fs.existsSync(path.join(output, master));
  const revision = entry.gifSha256?.slice(0, 12);
  const assetUrl = file => revision ? `${file}?v=${revision}` : file;
  return `<figure id="${escape(name)}" class="animation" data-animation data-gif="${escape(assetUrl(src))}" data-poster="${escape(assetUrl(posterExists ? poster : src))}" data-title="${escape(title)}">
  <div class="animation-tools"><span class="asset-details">${escape(details)}</span><span class="animation-actions"><a href="${escape(assetUrl(src))}">GIF</a>${masterExists ? `<a href="${escape(assetUrl(master))}">MP4</a>` : ''}<button type="button" class="clip-toggle" aria-pressed="false" aria-label="Play ${escape(title)} animation">Play</button></span></div>
  <img src="${escape(assetUrl(posterExists ? poster : src))}" alt="${escape(alt || title)}" width="${width}" height="${height}" decoding="async">
</figure>`;
}

const figures = [];
let markdown = readme.replace(/<!--\s*media:([a-z0-9-]+)\s*-->/g, (_, name) => {
  const index = figures.push(makeFigure(`docs/media/${name}.gif`, clips[name])) - 1;
  return `\n\nREADMEANIMATIONPLACEHOLDER${index}END\n\n`;
});
markdown = markdown.replace(/!\[([^\]]*)\]\((docs\/media\/[^\s)]+\.gif)(?:\s+"[^"]*")?\)/g, (_, alt, src) => {
  const index = figures.push(makeFigure(src, alt)) - 1;
  return `\n\nREADMEANIMATIONPLACEHOLDER${index}END\n\n`;
});
let body = marked.parse(markdown, { gfm: true });
body = body.replace(/(?:<p>)?READMEANIMATIONPLACEHOLDER(\d+)END(?:<\/p>)?/g, (_, index) => figures[Number(index)]);

const html = `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="dark">
  <title>Homelab Inference · Local README preview</title>
  <style>
    :root { color-scheme: dark; --bg: #090d12; --ink: #eeeae2; --muted: #a5adb7; --line: #303841; --link: #8eb9dc; --focus: #b4d6ee; }
    * { box-sizing: border-box; }
    html { background: var(--bg); }
    body { margin: 0; color: var(--ink); font: 17px/1.68 "Avenir Next", Avenir, "Segoe UI", sans-serif; -webkit-font-smoothing: antialiased; }
    .preview-bar { max-width: 928px; margin: 0 auto; padding: 25px 24px 20px; border-bottom: 1px solid var(--line); display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px 24px; color: var(--muted); font-size: 13px; line-height: 1.45; }
    .preview-label { display: block; color: var(--ink); font-weight: 600; }
    .preview-note { display: block; margin-top: 3px; }
    .preview-actions { display: flex; align-items: center; gap: 18px; }
    button, a { -webkit-tap-highlight-color: transparent; }
    button { min-height: 36px; padding: 5px 11px; color: var(--ink); background: transparent; border: 1px solid #46515e; border-radius: 4px; font: inherit; line-height: 1.4; cursor: pointer; }
    button:hover { border-color: #8d9bac; background: #141a22; }
    :focus-visible { outline: 2px solid var(--focus); outline-offset: 4px; }
    a { color: var(--link); text-decoration-thickness: 1px; text-underline-offset: 3px; }
    a:hover { color: #c4e0f2; }
    main { max-width: 880px; margin: 45px auto 90px; padding: 0 24px; }
    h1, h2 { font-weight: 600; letter-spacing: -.022em; line-height: 1.24; }
    h1 { margin: 0 0 27px; font-size: clamp(29px, 4vw, 37px); }
    h2 { margin: 58px 0 21px; font-size: 25px; }
    p { margin: 0 0 21px; }
    main img { max-width: 100%; height: auto; }
    strong { color: #fff9eb; font-weight: 600; }
    code, pre { font-family: Menlo, Consolas, "Liberation Mono", monospace; font-size: .85em; }
    :not(pre) > code { padding: .12em .28em; background: #181e26; border-radius: 3px; overflow-wrap: anywhere; }
    pre { overflow: auto; margin: 26px 0; padding: 18px 20px; background: #11171e; border-radius: 4px; line-height: 1.6; tab-size: 4; }
    pre code { font-size: 1em; }
    table { display: block; overflow-x: auto; width: 100%; margin: 25px 0; border-collapse: collapse; font-size: 15px; line-height: 1.5; }
    th, td { padding: 12px 13px; border-bottom: 1px solid var(--line); }
    th { color: var(--ink); font-weight: 600; text-align: left; }
    th:first-child, td:first-child { padding-left: 0; }
    th:last-child, td:last-child { padding-right: 0; }
    ul { padding-left: 22px; margin: 22px 0; }
    li { margin: 7px 0; }
    details { margin: 24px 0; }
    summary { cursor: pointer; color: var(--link); text-underline-offset: 3px; }
    summary:hover { text-decoration: underline; }
    .animation { margin: 30px -24px 23px; }
    .animation img { display: block; width: 100%; height: auto; background: #090d12; }
    .animation-tools { display: flex; align-items: center; justify-content: space-between; gap: 12px; min-height: 45px; color: var(--muted); font-size: 12px; line-height: 1.4; }
    .animation-actions { display: flex; align-items: center; gap: 17px; }
    .animation-tools button { min-width: 62px; min-height: 30px; padding: 4px 10px; }
    .animation + p:has(> em:only-child) { color: var(--muted); font-size: 14px; line-height: 1.55; margin-top: -3px; }
    .pending-image { min-height: 300px; display: flex; flex-direction: column; align-items: center; justify-content: center; border-block: 1px solid var(--line); color: var(--ink); }
    .pending-image span { color: var(--muted); font-size: 13px; margin-top: 8px; }
    @media (max-width: 940px) { .animation-tools { padding-inline: 14px; } }
    @media (max-width: 600px) { body { font-size: 16px; } main { margin-top: 32px; padding-inline: 20px; } .preview-bar { padding-inline: 20px; } h2 { font-size: 23px; margin-top: 45px; } .animation { margin-inline: -20px; } pre { margin-inline: -5px; padding: 16px 13px; } .asset-details { font-size: 11px; } }
  </style>
</head>
<body>
  <header class="preview-bar">
    <div><span class="preview-label">Local README preview</span><span class="preview-note">GitHub’s layout and playback behavior may differ.</span></div>
    <div class="preview-actions"><a href="README.md">Markdown</a><button id="motion-toggle" type="button" aria-pressed="true">Pause animations</button></div>
  </header>
  <main>${body}</main>
  <script>
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
    let motionEnabled = !reducedMotion.matches;
    const globalToggle = document.getElementById('motion-toggle');
    const animations = [...document.querySelectorAll('[data-animation]')].map(figure => ({
      figure,
      image: figure.querySelector('img'),
      button: figure.querySelector('.clip-toggle'),
      enabled: motionEnabled,
      visible: false,
      playing: false,
    }));
    function updateAnimation(animation) {
      const shouldPlay = animation.enabled && animation.visible && !document.hidden;
      if (animation.playing !== shouldPlay) {
        animation.image.src = shouldPlay ? animation.figure.dataset.gif : animation.figure.dataset.poster;
        animation.playing = shouldPlay;
      }
      animation.button.textContent = animation.enabled ? 'Pause' : 'Play';
      animation.button.setAttribute('aria-pressed', String(animation.enabled));
      animation.button.setAttribute('aria-label', (animation.enabled ? 'Pause ' : 'Play ') + animation.figure.dataset.title + ' animation');
    }
    function updateGlobal() {
      const anyEnabled = animations.some(animation => animation.enabled);
      globalToggle.textContent = anyEnabled ? 'Pause animations' : 'Play animations';
      globalToggle.setAttribute('aria-pressed', String(anyEnabled));
    }
    function setGlobal(enabled) {
      motionEnabled = enabled;
      animations.forEach(animation => { animation.enabled = enabled; updateAnimation(animation); });
      updateGlobal();
    }
    animations.forEach(animation => animation.button.addEventListener('click', () => {
      animation.enabled = !animation.enabled;
      updateAnimation(animation);
      updateGlobal();
    }));
    globalToggle.addEventListener('click', () => setGlobal(!animations.some(animation => animation.enabled)));
    const observer = new IntersectionObserver(entries => entries.forEach(entry => {
      const animation = animations.find(item => item.figure === entry.target);
      animation.visible = entry.isIntersecting;
      updateAnimation(animation);
    }), { threshold: 0.05 });
    animations.forEach(animation => { observer.observe(animation.figure); updateAnimation(animation); });
    document.addEventListener('visibilitychange', () => animations.forEach(updateAnimation));
    reducedMotion.addEventListener('change', event => setGlobal(!event.matches));
    updateGlobal();
  </script>
</body>
</html>
`;

fs.writeFileSync(path.join(output, 'preview.html'), html);
console.log(`Built ${path.join(output, 'preview.html')} (${figures.length} animation slots).`);
