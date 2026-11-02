#!/usr/bin/env python3
"""
Generate publication-quality SVG figures for Homelab-inference documentation.
Implements Tasks for Phase 5.4, Phase 6, Phase 7, and Phase 8.
Produces:
  1. docs/figures/waterfall.svg (Ablation Waterfall)
  2. docs/figures/roofline.svg (Empirical Roofline vs Achieved Decode)
  3. docs/figures/accuracy_vs_budget.svg (Reasoning Accuracy vs Wall-Clock Budget)
  4. docs/figures/speculation_workload.svg (Speculation by Workload Class)
"""

from pathlib import Path
import math

FIGURES_DIR = Path("/home/james/Homelab-inference/docs/figures")
FIGURES_DIR.mkdir(parents=True, exist_ok=True)


def generate_waterfall_svg(out_path: Path):
    """Generates the ablation waterfall chart from baseline to final optimization."""
    # Data sequence: (Label, delta, is_total, is_lossy, color)
    # Using live measured Protocol A data from logs/runs/ablation_sweep/ablation_summary.json
    steps = [
        ("Upstream Baseline\n(Single Socket, Q6_K)", 7.14, True, False, "#64748b"),
        ("+ Dual-Socket NUMA\nInterleave", 3.27, False, False, "#3b82f6"),
        ("+ 28 Physical Core\nPinning", -0.13, False, False, "#3b82f6"),
        ("+ IQ4_XS Dense +\nQ4_0 Experts", 1.33, False, True, "#8b5cf6"),
        ("+ AVX2 64-Byte Row\nRepacking", 7.49, False, False, "#0ea5e9"),
        ("+ Merged Up/Gate\nExperts (-muge 1)", 0.39, False, False, "#0ea5e9"),
        ("+ Suffix Speculation\n(MTP Drafting)", 4.00, False, False, "#10b981"),
        ("Final Qwen Config\n(Step 6)", 23.49, True, False, "#059669"),
        ("Flint 40B Port\n(ik_llama + MUGE)", 21.15, True, False, "#f59e0b"),
    ]

    width = 1100
    height = 560
    margin_l = 80
    margin_r = 40
    margin_t = 60
    margin_b = 100

    plot_w = width - margin_l - margin_r
    plot_h = height - margin_t - margin_b

    max_val = 30.0
    bar_w = plot_w / len(steps) - 16

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">')
    svg.append('<defs>')
    svg.append('<style>')
    svg.append('  text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }')
    svg.append('  .title { font-size: 18px; font-weight: bold; fill: #1e293b; }')
    svg.append('  .subtitle { font-size: 13px; fill: #64748b; }')
    svg.append('  .axis-label { font-size: 12px; fill: #475569; }')
    svg.append('  .bar-label { font-size: 12px; font-weight: bold; fill: #0f172a; text-anchor: middle; }')
    svg.append('  .x-label { font-size: 10.5px; fill: #334155; text-anchor: middle; }')
    svg.append('  .grid { stroke: #e2e8f0; stroke-width: 1; stroke-dasharray: 4,4; }')
    svg.append('</style>')
    svg.append('</defs>')

    # Background
    svg.append(f'<rect width="{width}" height="{height}" fill="#ffffff" rx="8"/>')

    # Title
    svg.append(f'<text x="{margin_l}" y="32" class="title">Optimization Waterfall: Decoding Throughput Progression (Broadwell Dual-Xeon)</text>')
    svg.append(f'<text x="{margin_l}" y="48" class="subtitle">Protocol A-tput-v1 Controlled Benchmark (Tokens/Second). Gray/Blue: Lossless Engine &amp; Topology; Purple: Quantization; Green: Speculation; Amber: Flint 40B</text>')

    # Gridlines and Y-axis
    for y_val in [0, 5, 10, 15, 20, 25, 30]:
        y_pos = margin_t + plot_h - (y_val / max_val) * plot_h
        svg.append(f'<line x1="{margin_l}" y1="{y_pos}" x2="{width - margin_r}" y2="{y_pos}" class="grid" />')
        svg.append(f'<text x="{margin_l - 12}" y="{y_pos + 4}" class="axis-label" text-anchor="end">{y_val} t/s</text>')

    # Axis line
    svg.append(f'<line x1="{margin_l}" y1="{margin_t + plot_h}" x2="{width - margin_r}" y2="{margin_t + plot_h}" stroke="#94a3b8" stroke-width="1.5" />')

    # Draw Bars
    accum = 0.0
    for idx, (label, val, is_total, is_lossy, color) in enumerate(steps):
        x = margin_l + idx * (plot_w / len(steps)) + 8

        if is_total:
            start_val = 0.0
            end_val = val
            accum = val
        else:
            start_val = accum
            end_val = accum + val
            accum = end_val

        y_top = margin_t + plot_h - (end_val / max_val) * plot_h
        y_bot = margin_t + plot_h - (start_val / max_val) * plot_h
        h = max(2.0, y_bot - y_top)

        # Bar rect
        svg.append(f'<rect x="{x}" y="{y_top}" width="{bar_w}" height="{h}" fill="{color}" rx="3" opacity="0.9" />')

        # Top label
        disp_txt = f"{val:.2f}" if is_total else f"+{val:.2f}"
        svg.append(f'<text x="{x + bar_w/2}" y="{y_top - 6}" class="bar-label">{disp_txt}</text>')

        # X-axis multiline label
        lines = label.split("\n")
        y_label_start = margin_t + plot_h + 16
        for l_idx, line in enumerate(lines):
            svg.append(f'<text x="{x + bar_w/2}" y="{y_label_start + l_idx * 13}" class="x-label">{line}</text>')

    svg.append('</svg>')
    out_path.write_text("\n".join(svg), encoding="utf-8")
    print(f"Generated {out_path}")


def generate_roofline_svg(out_path: Path):
    """Generates the empirical roofline model vs achieved decode throughput chart."""
    width = 900
    height = 500
    margin_l = 80
    margin_r = 50
    margin_t = 60
    margin_b = 70

    plot_w = width - margin_l - margin_r
    plot_h = height - margin_t - margin_b
    max_tps = 32.0

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">')
    svg.append('<defs>')
    svg.append('<style>')
    svg.append('  text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }')
    svg.append('  .title { font-size: 17px; font-weight: bold; fill: #0f172a; }')
    svg.append('  .subtitle { font-size: 12.5px; fill: #475569; }')
    svg.append('  .axis-label { font-size: 12px; fill: #334155; }')
    svg.append('  .grid { stroke: #e2e8f0; stroke-width: 1; stroke-dasharray: 4,4; }')
    svg.append('  .roofline-dual { stroke: #dc2626; stroke-width: 2.5; stroke-dasharray: 6,4; }')
    svg.append('  .roofline-single { stroke: #9333ea; stroke-width: 2; stroke-dasharray: 4,4; }')
    svg.append('  .roofline-flint { stroke: #f59e0b; stroke-width: 2; stroke-dasharray: 5,3; }')
    svg.append('  .curve-qwen { fill: none; stroke: #2563eb; stroke-width: 3; }')
    svg.append('  .curve-flint { fill: none; stroke: #d97706; stroke-width: 3; }')
    svg.append('  .point-label { font-size: 11px; font-weight: bold; fill: #1e293b; }')
    svg.append('</style>')
    svg.append('</defs>')

    svg.append(f'<rect width="{width}" height="{height}" fill="#ffffff" rx="8"/>')
    svg.append(f'<text x="{margin_l}" y="32" class="title">Empirical DRAM Roofline vs. Measured Autoregressive Decode</text>')
    svg.append(f'<text x="{margin_l}" y="48" class="subtitle">Dell PowerEdge T630 (STREAM Triad: Dual-Socket 35.22 GB/s, Single-Socket 21.44 GB/s)</text>')

    # Y-axis
    for y_val in [0, 5, 10, 15, 20, 25, 30]:
        y_pos = margin_t + plot_h - (y_val / max_tps) * plot_h
        svg.append(f'<line x1="{margin_l}" y1="{y_pos}" x2="{width - margin_r}" y2="{y_pos}" class="grid" />')
        svg.append(f'<text x="{margin_l - 10}" y="{y_pos + 4}" class="axis-label" text-anchor="end">{y_val} t/s</text>')

    # X-axis points: 2K, 8K, 32K, 128K
    ctx_points = ["2,048", "8,192", "32,768", "131,072"]
    x_positions = [margin_l + i * (plot_w / 3) for i in range(4)]

    for x_pos, label in zip(x_positions, ctx_points):
        svg.append(f'<line x1="{x_pos}" y1="{margin_t}" x2="{x_pos}" y2="{margin_t + plot_h}" class="grid" />')
        svg.append(f'<text x="{x_pos}" y="{margin_t + plot_h + 20}" class="axis-label" text-anchor="middle">{label}</text>')

    svg.append(f'<text x="{margin_l + plot_w/2}" y="{margin_t + plot_h + 45}" class="axis-label" text-anchor="middle" font-weight="bold">Context Length (Tokens)</text>')
    svg.append(f'<line x1="{margin_l}" y1="{margin_t + plot_h}" x2="{width - margin_r}" y2="{margin_t + plot_h}" stroke="#94a3b8" stroke-width="1.5" />')

    # Horizontal Roofline Limits
    # Qwen Dual Ceiling: 20.82 t/s
    y_qwen_dual = margin_t + plot_h - (20.82 / max_tps) * plot_h
    svg.append(f'<line x1="{margin_l}" y1="{y_qwen_dual}" x2="{width - margin_r}" y2="{y_qwen_dual}" class="roofline-dual" />')
    svg.append(f'<text x="{width - margin_r - 5}" y="{y_qwen_dual - 6}" font-size="11" fill="#dc2626" font-weight="bold" text-anchor="end">Qwen Dual-Socket Memory Ceiling (20.82 t/s)</text>')

    # Flint Dual Ceiling: 16.51 t/s
    y_flint_dual = margin_t + plot_h - (16.51 / max_tps) * plot_h
    svg.append(f'<line x1="{margin_l}" y1="{y_flint_dual}" x2="{width - margin_r}" y2="{y_flint_dual}" class="roofline-flint" />')
    svg.append(f'<text x="{width - margin_r - 5}" y="{y_flint_dual - 6}" font-size="11" fill="#d97706" font-weight="bold" text-anchor="end">Flint 40B Q4_0 Memory Ceiling (16.51 t/s)</text>')

    # Qwen Single Ceiling: 12.67 t/s
    y_qwen_single = margin_t + plot_h - (12.67 / max_tps) * plot_h
    svg.append(f'<line x1="{margin_l}" y1="{y_qwen_single}" x2="{width - margin_r}" y2="{y_qwen_single}" class="roofline-single" />')
    svg.append(f'<text x="{width - margin_r - 5}" y="{y_qwen_single - 6}" font-size="11" fill="#9333ea" font-weight="bold" text-anchor="end">Qwen Single-Socket Memory Ceiling (12.67 t/s)</text>')

    # Empirical Curves
    # Qwen Achieved (Speculative: 24.53, 23.80, 21.40, 18.20)
    qwen_pts = [(x_positions[0], 24.53), (x_positions[1], 23.80), (x_positions[2], 21.40), (x_positions[3], 18.20)]
    qwen_path = "M " + " L ".join(f"{x},{margin_t + plot_h - (y/max_tps)*plot_h}" for x, y in qwen_pts)
    svg.append(f'<path d="{qwen_path}" class="curve-qwen" />')
    for x, y in qwen_pts:
        yp = margin_t + plot_h - (y / max_tps) * plot_h
        svg.append(f'<circle cx="{x}" cy="{yp}" r="5" fill="#2563eb" stroke="#ffffff" stroke-width="2"/>')
        svg.append(f'<text x="{x}" y="{yp - 10}" class="point-label" text-anchor="middle">{y:.1f} t/s</text>')

    # Flint Achieved (Exp 94: 18.42, 18.05, 17.20, 14.80)
    flint_pts = [(x_positions[0], 18.42), (x_positions[1], 18.05), (x_positions[2], 17.20), (x_positions[3], 14.80)]
    flint_path = "M " + " L ".join(f"{x},{margin_t + plot_h - (y/max_tps)*plot_h}" for x, y in flint_pts)
    svg.append(f'<path d="{flint_path}" class="curve-flint" />')
    for x, y in flint_pts:
        yp = margin_t + plot_h - (y / max_tps) * plot_h
        svg.append(f'<circle cx="{x}" cy="{yp}" r="5" fill="#d97706" stroke="#ffffff" stroke-width="2"/>')
        svg.append(f'<text x="{x}" y="{yp + 18}" class="point-label" text-anchor="middle" fill="#92400e">{y:.1f} t/s</text>')

    svg.append('</svg>')
    out_path.write_text("\n".join(svg), encoding="utf-8")
    print(f"Generated {out_path}")


def generate_accuracy_budget_svg(out_path: Path):
    """Generates accuracy vs wall-clock budget curve."""
    width = 900
    height = 500
    margin_l = 80
    margin_r = 50
    margin_t = 60
    margin_b = 70

    plot_w = width - margin_l - margin_r
    plot_h = height - margin_t - margin_b

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">')
    svg.append('<defs>')
    svg.append('<style>')
    svg.append('  text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }')
    svg.append('  .title { font-size: 17px; font-weight: bold; fill: #0f172a; }')
    svg.append('  .subtitle { font-size: 12.5px; fill: #475569; }')
    svg.append('  .axis-label { font-size: 12px; fill: #334155; }')
    svg.append('  .grid { stroke: #e2e8f0; stroke-width: 1; stroke-dasharray: 4,4; }')
    svg.append('  .curve-flint { fill: none; stroke: #d97706; stroke-width: 3.5; }')
    svg.append('  .curve-qwen { fill: none; stroke: #2563eb; stroke-width: 3.5; }')
    svg.append('</style>')
    svg.append('</defs>')

    svg.append(f'<rect width="{width}" height="{height}" fill="#ffffff" rx="8"/>')
    svg.append(f'<text x="{margin_l}" y="32" class="title">Strict Reasoning Accuracy vs. Wall-Clock Budget</text>')
    svg.append(f'<text x="{margin_l}" y="48" class="subtitle">Protocol C Benchmark: Flint 40B vs. Qwen 3.6 35B under Wall-Clock Thinking Limits</text>')

    # Y-axis (0% to 60%)
    for y_val in [0, 10, 20, 30, 40, 50, 60]:
        y_pos = margin_t + plot_h - (y_val / 60.0) * plot_h
        svg.append(f'<line x1="{margin_l}" y1="{y_pos}" x2="{width - margin_r}" y2="{y_pos}" class="grid" />')
        svg.append(f'<text x="{margin_l - 10}" y="{y_pos + 4}" class="axis-label" text-anchor="end">{y_val}%</text>')

    budgets = ["30s", "60s", "120s", "300s", "600s", "1200s (20m)"]
    x_positions = [margin_l + i * (plot_w / 5) for i in range(6)]

    for x_pos, label in zip(x_positions, budgets):
        svg.append(f'<line x1="{x_pos}" y1="{margin_t}" x2="{x_pos}" y2="{margin_t + plot_h}" class="grid" />')
        svg.append(f'<text x="{x_pos}" y="{margin_t + plot_h + 20}" class="axis-label" text-anchor="middle">{label}</text>')

    svg.append(f'<text x="{margin_l + plot_w/2}" y="{margin_t + plot_h + 45}" class="axis-label" text-anchor="middle" font-weight="bold">Thinking Time Budget per Problem (Wall-Clock Seconds)</text>')
    svg.append(f'<line x1="{margin_l}" y1="{margin_t + plot_h}" x2="{width - margin_r}" y2="{margin_t + plot_h}" stroke="#94a3b8" stroke-width="1.5" />')

    # Data: Flint strict accuracy vs budget (Protocol C-gpqa-v2 16K Runway)
    # <=30s: 4.0%, <=60s: 12.0%, <=120s: 14.0%, <=300s: 26.0%, <=600s: 38.0%, <=1200s: 46.0%
    flint_data = [(x_positions[0], 4.0), (x_positions[1], 12.0), (x_positions[2], 14.0), (x_positions[3], 26.0), (x_positions[4], 38.0), (x_positions[5], 46.0)]
    flint_path = "M " + " L ".join(f"{x},{margin_t + plot_h - (y/60.0)*plot_h}" for x, y in flint_data)
    svg.append(f'<path d="{flint_path}" class="curve-flint" />')
    for x, y in flint_data:
        yp = margin_t + plot_h - (y / 60.0) * plot_h
        svg.append(f'<circle cx="{x}" cy="{yp}" r="6" fill="#d97706" stroke="#ffffff" stroke-width="2"/>')
        svg.append(f'<text x="{x}" y="{yp - 10}" font-size="11" font-weight="bold" fill="#92400e" text-anchor="middle">{y:.1f}%</text>')

    # Data: Qwen strict accuracy vs budget (Protocol C-gpqa-v2 16K Runway)
    # <=30s: 0.0%, <=60s: 4.0%, <=120s: 18.0%, <=300s: 20.0%, <=600s: 28.0%, <=1200s: 38.0%
    qwen_data = [(x_positions[0], 0.0), (x_positions[1], 4.0), (x_positions[2], 18.0), (x_positions[3], 20.0), (x_positions[4], 28.0), (x_positions[5], 38.0)]
    qwen_path = "M " + " L ".join(f"{x},{margin_t + plot_h - (y/60.0)*plot_h}" for x, y in qwen_data)
    svg.append(f'<path d="{qwen_path}" class="curve-qwen" />')
    for x, y in qwen_data:
        yp = margin_t + plot_h - (y / 60.0) * plot_h
        svg.append(f'<circle cx="{x}" cy="{yp}" r="6" fill="#2563eb" stroke="#ffffff" stroke-width="2"/>')
        svg.append(f'<text x="{x}" y="{yp + 18}" font-size="11" font-weight="bold" fill="#1e40af" text-anchor="middle">{y:.1f}%</text>')

    # Legend
    svg.append(f'<rect x="{margin_l + 20}" y="{margin_t + 20}" width="240" height="60" fill="#f8fafc" stroke="#cbd5e1" rx="4"/>')
    svg.append(f'<circle cx="{margin_l + 35}" cy="{margin_t + 38}" r="5" fill="#d97706" />')
    svg.append(f'<text x="{margin_l + 50}" y="{margin_t + 42}" font-size="12" font-weight="bold" fill="#0f172a">Flint 40B MoE (A2.5B)</text>')
    svg.append(f'<circle cx="{margin_l + 35}" cy="{margin_t + 60}" r="5" fill="#2563eb" />')
    svg.append(f'<text x="{margin_l + 50}" y="{margin_t + 64}" font-size="12" font-weight="bold" fill="#0f172a">Qwen 3.6 35B MoE (A3B)</text>')

    svg.append('</svg>')
    out_path.write_text("\n".join(svg), encoding="utf-8")
    print(f"Generated {out_path}")


def generate_speculation_workload_svg(out_path: Path):
    """Generates speculative decoding speedup breakdown across workload classes."""
    width = 850
    height = 460
    margin_l = 80
    margin_r = 40
    margin_t = 60
    margin_b = 60

    plot_w = width - margin_l - margin_r
    plot_h = height - margin_t - margin_b
    max_tps = 32.0

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">')
    svg.append('<defs>')
    svg.append('<style>')
    svg.append('  text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }')
    svg.append('  .title { font-size: 17px; font-weight: bold; fill: #0f172a; }')
    svg.append('  .subtitle { font-size: 12.5px; fill: #475569; }')
    svg.append('  .axis-label { font-size: 12px; fill: #334155; }')
    svg.append('  .grid { stroke: #e2e8f0; stroke-width: 1; stroke-dasharray: 4,4; }')
    svg.append('</style>')
    svg.append('</defs>')

    svg.append(f'<rect width="{width}" height="{height}" fill="#ffffff" rx="8"/>')
    svg.append(f'<text x="{margin_l}" y="32" class="title">Speculation Throughput Gain by Workload Class</text>')
    svg.append(f'<text x="{margin_l}" y="48" class="subtitle">Protocol A-tput-v1 Controlled 512-Token Generations (Non-Degenerate Useful Throughput)</text>')

    for y_val in [0, 5, 10, 15, 20, 25, 30]:
        y_pos = margin_t + plot_h - (y_val / max_tps) * plot_h
        svg.append(f'<line x1="{margin_l}" y1="{y_pos}" x2="{width - margin_r}" y2="{y_pos}" class="grid" />')
        svg.append(f'<text x="{margin_l - 10}" y="{y_pos + 4}" class="axis-label" text-anchor="end">{y_val} t/s</text>')

    classes = [
        ("Code Edit\n(High repetition)", 17.02, 26.85, 2.74),
        ("Fresh Code Gen\n(Medium repetition)", 17.02, 23.40, 2.12),
        ("Prose / Reasoning\n(Low repetition)", 17.02, 19.80, 1.45),
    ]

    grp_w = plot_w / len(classes)
    b_w = 48

    for idx, (label, non_spec, spec, draft_len) in enumerate(classes):
        cx = margin_l + idx * grp_w + grp_w / 2

        # Non-spec bar
        y_ns = margin_t + plot_h - (non_spec / max_tps) * plot_h
        h_ns = (non_spec / max_tps) * plot_h
        svg.append(f'<rect x="{cx - b_w - 4}" y="{y_ns}" width="{b_w}" height="{h_ns}" fill="#94a3b8" rx="3" />')
        svg.append(f'<text x="{cx - b_w/2 - 4}" y="{y_ns - 6}" font-size="11.5" font-weight="bold" fill="#334155" text-anchor="middle">{non_spec:.1f}</text>')

        # Spec bar
        y_s = margin_t + plot_h - (spec / max_tps) * plot_h
        h_s = (spec / max_tps) * plot_h
        svg.append(f'<rect x="{cx + 4}" y="{y_s}" width="{b_w}" height="{h_s}" fill="#10b981" rx="3" />')
        svg.append(f'<text x="{cx + b_w/2 + 4}" y="{y_s - 6}" font-size="11.5" font-weight="bold" fill="#065f46" text-anchor="middle">{spec:.1f}</text>')

        # Gain badge
        gain = ((spec - non_spec) / non_spec) * 100
        svg.append(f'<rect x="{cx - 36}" y="{y_s - 32}" width="72" height="18" fill="#dcfce7" stroke="#86efac" rx="9" />')
        svg.append(f'<text x="{cx}" y="{y_s - 19}" font-size="10.5" font-weight="bold" fill="#15803d" text-anchor="middle">+{gain:.1f}%</text>')

        # Label
        lines = label.split("\n")
        svg.append(f'<text x="{cx}" y="{margin_t + plot_h + 20}" font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">{lines[0]}</text>')
        svg.append(f'<text x="{cx}" y="{margin_t + plot_h + 35}" font-size="11" fill="#64748b" text-anchor="middle">{lines[1]}</text>')

    # Legend
    svg.append(f'<rect x="{margin_l + 15}" y="{margin_t + 15}" width="260" height="30" fill="#f8fafc" stroke="#cbd5e1" rx="4"/>')
    svg.append(f'<rect x="{margin_l + 25}" y="{margin_t + 22}" width="14" height="14" fill="#94a3b8" rx="2" />')
    svg.append(f'<text x="{margin_l + 45}" y="{margin_t + 34}" font-size="11.5" fill="#334155">Non-Speculative Baseline</text>')
    svg.append(f'<rect x="{margin_l + 160}" y="{margin_t + 22}" width="14" height="14" fill="#10b981" rx="2" />')
    svg.append(f'<text x="{margin_l + 180}" y="{margin_t + 34}" font-size="11.5" fill="#065f46">Speculative (ngram / MTP)</text>')

    svg.append('</svg>')
    out_path.write_text("\n".join(svg), encoding="utf-8")
    print(f"Generated {out_path}")


if __name__ == "__main__":
    generate_waterfall_svg(FIGURES_DIR / "waterfall.svg")
    generate_roofline_svg(FIGURES_DIR / "roofline.svg")
    generate_accuracy_budget_svg(FIGURES_DIR / "accuracy_vs_budget.svg")
    generate_speculation_workload_svg(FIGURES_DIR / "speculation_workload.svg")
    print("All figures successfully generated in docs/figures/")
