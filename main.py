#!/usr/bin/env python3
"""news-image-20261120 entry.

One image summing up Friday 20 November 2026 world news: a newspaper
front page (1024x1024) with the 15 verified stories, each with its own
programmatically drawn thumbnail and its source printed beneath it.

Deterministic: no network, no clock, no randomness. Writes
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png) as JPEG.
"""

import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
PAPER = (247, 243, 232)
INK = (17, 17, 17)
MUTED = (96, 91, 80)
RED = (176, 42, 30)
RULE = (70, 66, 56)

DATE_STR = "Friday 20 November 2026"


def font(bold, size):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def wrap(d, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if not cur or d.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def _rect(d, x, y, w, h, fill):
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=fill)


def _ell(d, x, y, w, h, fill):
    d.ellipse([x, y, x + w - 1, y + h - 1], fill=fill)


# ---------------------------------------------------------------------------
# Thumbnail scenes. Each draws inside (x, y, w, h) using only fixed shapes.
# ---------------------------------------------------------------------------

def scene_kyiv(d, x, y, w, h):
    """Night skyline, river and a bridge over it (Kyiv bridges)."""
    _rect(d, x, y, w, h, (27, 42, 74))
    for fx, fy in [(0.10, 0.12), (0.30, 0.07), (0.55, 0.15), (0.80, 0.08),
                   (0.92, 0.20), (0.45, 0.05), (0.68, 0.22)]:
        _ell(d, x + w * fx, y + h * fy, 3, 3, (255, 255, 220))
    for bx, bw, bh in [(0.00, 0.14, 0.30), (0.15, 0.11, 0.42), (0.27, 0.16, 0.34),
                       (0.44, 0.12, 0.46), (0.57, 0.15, 0.32), (0.73, 0.13, 0.40),
                       (0.87, 0.13, 0.30)]:
        _rect(d, x + w * bx, y + h * (0.62 - bh), w * bw, h * bh, (12, 20, 38))
    _rect(d, x, y + h * 0.62, w, h * 0.38, (46, 94, 140))
    by = y + h * 0.62
    d.line([(x, by), (x + w, by)], fill=(205, 205, 195), width=max(2, h // 40))
    for px in (0.28, 0.68):
        _rect(d, x + w * px - 2, y + h * 0.30, 4, h * 0.32, (205, 205, 195))
        d.line([(x + w * px, y + h * 0.30), (x, by)], fill=(180, 180, 170), width=1)
        d.line([(x + w * px, y + h * 0.30), (x + w, by)], fill=(180, 180, 170), width=1)
    _ell(d, x + w * 0.47, y + h * 0.40, w * 0.12, h * 0.24, (255, 140, 40))
    _ell(d, x + w * 0.50, y + h * 0.46, w * 0.06, h * 0.12, (255, 220, 120))


def scene_riyadh(d, x, y, w, h):
    """Tall tower with an arched top, smoke and a missile streak."""
    _rect(d, x, y, w, h * 0.55, (232, 163, 76))
    _rect(d, x, y + h * 0.55, w, h * 0.45, (240, 200, 130))
    tx = x + w * 0.38
    _rect(d, tx, y + h * 0.12, w * 0.24, h * 0.88, (88, 88, 102))
    _ell(d, tx + w * 0.05, y + h * 0.16, w * 0.14, h * 0.20, (232, 163, 76))
    for row in range(6):
        for col in range(2):
            _rect(d, tx + w * (0.05 + col * 0.08), y + h * (0.42 + row * 0.08),
                  w * 0.03, h * 0.04, (255, 220, 130))
    _ell(d, x + w * 0.55, y + h * 0.10, w * 0.16, h * 0.12, (120, 120, 120))
    _ell(d, x + w * 0.62, y + h * 0.04, w * 0.13, h * 0.10, (150, 150, 150))
    d.line([(x + w * 0.05, y + h * 0.25), (x + w * 0.30, y + h * 0.05)],
           fill=(255, 255, 255), width=max(2, h // 45))
    _ell(d, x + w * 0.28, y + h * 0.03, w * 0.05, h * 0.08, (255, 120, 30))


def scene_poland(d, x, y, w, h):
    """Jets and a missile in the sky, Polish flag strip at the base."""
    _rect(d, x, y, w, h, (135, 206, 235))
    for cx, cy, cw in [(0.08, 0.18, 0.22), (0.55, 0.10, 0.26), (0.70, 0.30, 0.20)]:
        _ell(d, x + w * cx, y + h * cy, w * cw, h * 0.16, (255, 255, 255))
    for jx, jy in [(0.18, 0.45), (0.55, 0.60)]:
        px, py = x + w * jx, y + h * jy
        d.polygon([(px, py), (px + w * 0.16, py + h * 0.05),
                   (px, py + h * 0.10)], fill=(90, 95, 105))
        d.polygon([(px + w * 0.05, py + h * 0.02), (px + w * 0.10, py - h * 0.08),
                   (px + w * 0.12, py + h * 0.04)], fill=(70, 75, 85))
    d.line([(x + w * 0.05, y + h * 0.78), (x + w * 0.45, y + h * 0.70)],
           fill=(255, 255, 255), width=max(2, h // 45))
    _ell(d, x + w * 0.44, y + h * 0.67, w * 0.05, h * 0.07, (200, 40, 30))
    _rect(d, x, y + h * 0.88, w, h * 0.06, (255, 255, 255))
    _rect(d, x, y + h * 0.94, w, h * 0.06, (220, 40, 50))


def scene_estonia(d, x, y, w, h):
    """Border fence across a green field, Estonian flag in the corner."""
    _rect(d, x, y, w, h * 0.55, (198, 220, 235))
    _rect(d, x, y + h * 0.55, w, h * 0.45, (120, 170, 90))
    for i in range(6):
        px = x + w * (0.06 + i * 0.17)
        _rect(d, px, y + h * 0.42, max(2, w // 60), h * 0.42, (110, 80, 50))
    d.line([(x, y + h * 0.50), (x + w, y + h * 0.50)], fill=(70, 70, 70), width=2)
    d.line([(x, y + h * 0.66), (x + w, y + h * 0.66)], fill=(70, 70, 70), width=2)
    fx, fy, fw = x + w * 0.74, y + h * 0.08, w * 0.20
    _rect(d, fx, fy, fw, h * 0.07, (0, 114, 206))
    _rect(d, fx, fy + h * 0.07, fw, h * 0.07, (0, 0, 0))
    _rect(d, fx, fy + h * 0.14, fw, h * 0.07, (255, 255, 255))
    d.line([(fx, fy), (fx, fy - h * 0.06)], fill=(70, 70, 70), width=2)


def scene_stocks(d, x, y, w, h):
    """Red falling chart with candlesticks on a white board."""
    _rect(d, x, y, w, h, (255, 255, 255))
    for gy in (0.25, 0.50, 0.75):
        d.line([(x, y + h * gy), (x + w, y + h * gy)], fill=(225, 225, 225), width=1)
    pts = [(0.06, 0.22), (0.25, 0.30), (0.42, 0.28), (0.60, 0.48),
           (0.75, 0.62), (0.90, 0.82)]
    d.line([(x + w * px, y + h * py) for px, py in pts], fill=(200, 30, 25), width=3)
    ex, ey = x + w * 0.90, y + h * 0.82
    d.polygon([(ex, ey), (ex - w * 0.07, ey - h * 0.02),
               (ex - w * 0.02, ey - h * 0.09)], fill=(200, 30, 25))
    for cx, cy, ch in [(0.14, 0.30, 0.10), (0.34, 0.36, 0.12), (0.52, 0.50, 0.12),
                       (0.70, 0.66, 0.12)]:
        _rect(d, x + w * cx, y + h * cy, w * 0.05, h * ch, (200, 30, 25))
        d.line([(x + w * (cx + 0.025), y + h * (cy - 0.05)),
                (x + w * (cx + 0.025), y + h * (cy + ch + 0.05))],
               fill=(200, 30, 25), width=1)


def scene_gta6(d, x, y, w, h):
    """City skyline at dusk with a game controller in front."""
    _rect(d, x, y, w, h, (58, 38, 110))
    _ell(d, x + w * 0.78, y + h * 0.06, w * 0.14, h * 0.20, (255, 235, 180))
    for bx, bw, bh in [(0.00, 0.16, 0.34), (0.17, 0.13, 0.48), (0.31, 0.15, 0.38),
                       (0.47, 0.12, 0.52), (0.60, 0.14, 0.36), (0.75, 0.12, 0.44),
                       (0.88, 0.12, 0.30)]:
        _rect(d, x + w * bx, y + h * (0.72 - bh), w * bw, h * bh, (28, 20, 55))
        for wy in (0.10, 0.22):
            _rect(d, x + w * (bx + 0.04), y + h * (0.72 - bh + wy),
                  w * 0.03, h * 0.05, (255, 220, 120))
    cx, cy, cw, ch = x + w * 0.24, y + h * 0.60, w * 0.52, h * 0.34
    d.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=h * 0.08, fill=(32, 32, 44))
    d.line([(cx + w * 0.10, cy + ch * 0.50), (cx + w * 0.20, cy + ch * 0.50)],
           fill=(220, 220, 230), width=max(2, h // 40))
    d.line([(cx + w * 0.15, cy + ch * 0.30), (cx + w * 0.15, cy + ch * 0.70)],
           fill=(220, 220, 230), width=max(2, h // 40))
    for bx, by, col in [(0.36, 0.28, (70, 200, 90)), (0.42, 0.42, (220, 60, 60)),
                        (0.30, 0.42, (70, 120, 220)), (0.36, 0.56, (240, 200, 60))]:
        _ell(d, cx + cw * bx, cy + ch * by, w * 0.045, h * 0.07, col)
    _ell(d, cx + cw * 0.62, cy + ch * 0.62, w * 0.06, h * 0.10, (200, 200, 210))
    _ell(d, cx + cw * 0.74, cy + ch * 0.62, w * 0.06, h * 0.10, (200, 200, 210))


def scene_hospital(d, x, y, w, h):
    """Hospital building with a red cross under a bright sun."""
    _rect(d, x, y, w, h * 0.62, (170, 215, 240))
    _ell(d, x + w * 0.76, y + h * 0.06, w * 0.14, h * 0.20, (255, 220, 90))
    _rect(d, x, y + h * 0.62, w, h * 0.38, (110, 180, 110))
    bx, by, bw, bh = x + w * 0.22, y + h * 0.22, w * 0.56, h * 0.55
    _rect(d, bx, by, bw, bh, (245, 245, 245))
    _rect(d, bx + bw * 0.42, by + bh * 0.10, bw * 0.16, bh * 0.34, (210, 40, 40))
    _rect(d, bx + bw * 0.33, by + bh * 0.19, bw * 0.34, bh * 0.16, (210, 40, 40))
    for wx in (0.12, 0.70):
        _rect(d, bx + bw * wx, by + bh * 0.55, bw * 0.18, bh * 0.20, (140, 190, 220))
    _rect(d, bx + bw * 0.42, by + bh * 0.78, bw * 0.16, bh * 0.22, (90, 90, 100))


def scene_police(d, x, y, w, h):
    """Police badge with red and blue light bars."""
    _rect(d, x, y, w, h, (20, 30, 70))
    _rect(d, x + w * 0.10, y + h * 0.08, w * 0.34, h * 0.12, (220, 40, 40))
    _rect(d, x + w * 0.56, y + h * 0.08, w * 0.34, h * 0.12, (40, 90, 220))
    cx, cy = x + w * 0.50, y + h * 0.58
    d.polygon([(cx, cy - h * 0.30), (cx + w * 0.20, cy - h * 0.22),
               (cx + w * 0.18, cy + h * 0.08), (cx, cy + h * 0.30),
               (cx - w * 0.18, cy + h * 0.08), (cx - w * 0.20, cy - h * 0.22)],
              fill=(212, 175, 55))
    _ell(d, cx - w * 0.07, cy - h * 0.10, w * 0.14, h * 0.20, (20, 30, 70))
    d.text((cx - w * 0.035, cy - h * 0.09), "★", font=font(True, max(10, h // 5)),
           fill=(255, 255, 255))


def scene_summit(d, x, y, w, h):
    """EU and UK flags side by side above a summit table."""
    _rect(d, x, y, w, h, (232, 228, 218))
    ex, ey, ew, eh = x + w * 0.06, y + h * 0.10, w * 0.40, h * 0.52
    _rect(d, ex, ey, ew, eh, (0, 51, 153))
    import math
    for k in range(12):
        a = 2 * math.pi * k / 12
        _ell(d, ex + ew * 0.50 + ew * 0.32 * math.cos(a) - 2,
             ey + eh * 0.50 + eh * 0.30 * math.sin(a) - 2, 4, 4, (255, 204, 0))
    ux, uy = x + w * 0.54, y + h * 0.10
    _rect(d, ux, uy, ew, eh, (0, 36, 125))
    d.line([(ux, uy), (ux + ew, uy + eh)], fill=(255, 255, 255), width=max(2, h // 30))
    d.line([(ux + ew, uy), (ux, uy + eh)], fill=(255, 255, 255), width=max(2, h // 30))
    d.line([(ux + ew / 2, uy), (ux + ew / 2, uy + eh)], fill=(255, 255, 255),
           width=max(2, h // 25))
    d.line([(ux, uy + eh / 2), (ux + ew, uy + eh / 2)], fill=(255, 255, 255),
           width=max(2, h // 25))
    d.line([(ux + ew / 2, uy), (ux + ew / 2, uy + eh)], fill=(200, 16, 46),
           width=max(1, h // 50))
    d.line([(ux, uy + eh / 2), (ux + ew, uy + eh / 2)], fill=(200, 16, 46),
           width=max(1, h // 50))
    _rect(d, x, y + h * 0.74, w, h * 0.10, (120, 85, 50))
    _rect(d, x + w * 0.10, y + h * 0.84, w * 0.80, h * 0.04, (90, 60, 35))


def scene_germany(d, x, y, w, h):
    """German flag above a document stamped with a red X."""
    _rect(d, x, y, w, h, (232, 228, 218))
    _rect(d, x + w * 0.08, y + h * 0.08, w * 0.84, h * 0.14, (0, 0, 0))
    _rect(d, x + w * 0.08, y + h * 0.22, w * 0.84, h * 0.14, (221, 0, 0))
    _rect(d, x + w * 0.08, y + h * 0.36, w * 0.84, h * 0.14, (255, 206, 0))
    dx, dy, dw, dh = x + w * 0.24, y + h * 0.56, w * 0.52, h * 0.38
    _rect(d, dx, dy, dw, dh, (255, 255, 255))
    d.rectangle([dx, dy, dx + dw - 1, dy + dh - 1], outline=(150, 150, 150))
    for i in range(3):
        d.line([(dx + dw * 0.12, dy + dh * (0.22 + i * 0.18)),
                (dx + dw * 0.88, dy + dh * (0.22 + i * 0.18))],
               fill=(170, 170, 170), width=1)
    d.line([(dx + dw * 0.15, dy + dh * 0.12), (dx + dw * 0.85, dy + dh * 0.88)],
           fill=(200, 30, 25), width=3)
    d.line([(dx + dw * 0.85, dy + dh * 0.12), (dx + dw * 0.15, dy + dh * 0.88)],
           fill=(200, 30, 25), width=3)


def scene_berlin(d, x, y, w, h):
    """Brandenburg Gate silhouette with Ukraine and EU flags."""
    _rect(d, x, y, w, h * 0.60, (208, 214, 220))
    _rect(d, x, y + h * 0.60, w, h * 0.40, (150, 145, 130))
    gx, gy, gw = x + w * 0.16, y + h * 0.18, w * 0.68
    _rect(d, gx, gy, gw, h * 0.10, (176, 152, 108))
    for i in range(6):
        _rect(d, gx + gw * (0.03 + i * 0.155), gy + h * 0.10, gw * 0.09, h * 0.42,
              (176, 152, 108))
    _rect(d, gx, gy + h * 0.52, gw, h * 0.06, (176, 152, 108))
    _rect(d, gx + gw * 0.42, gy - h * 0.10, gw * 0.16, h * 0.10, (90, 80, 60))
    _rect(d, x + w * 0.10, y + h * 0.70, w * 0.32, h * 0.10, (0, 87, 183))
    _rect(d, x + w * 0.10, y + h * 0.80, w * 0.32, h * 0.10, (255, 213, 0))
    _rect(d, x + w * 0.58, y + h * 0.70, w * 0.32, h * 0.20, (0, 51, 153))
    _ell(d, x + w * 0.71, y + h * 0.77, w * 0.06, h * 0.09, (255, 204, 0))


def scene_debt(d, x, y, w, h):
    """Globe beside a bar chart rising to a dashed 100% line."""
    _rect(d, x, y, w, h, (255, 255, 255))
    _ell(d, x + w * 0.05, y + h * 0.18, w * 0.34, h * 0.55, (70, 130, 200))
    _ell(d, x + w * 0.12, y + h * 0.28, w * 0.12, h * 0.16, (90, 180, 90))
    _ell(d, x + w * 0.24, y + h * 0.48, w * 0.10, h * 0.14, (90, 180, 90))
    d.line([(x + w * 0.48, y + h * 0.18), (x + w * 0.95, y + h * 0.18)],
           fill=(200, 30, 25), width=1)
    for i in range(8):
        _rect(d, x + w * (0.48 + i * 0.06), y + h * 0.18, w * 0.03, 1, (200, 30, 25))
    for i, bh in enumerate([0.30, 0.42, 0.55, 0.68]):
        col = (200, 30, 25) if i == 3 else (120, 120, 125)
        _rect(d, x + w * (0.50 + i * 0.115), y + h * (0.86 - bh), w * 0.07, h * bh, col)
    d.line([(x + w * 0.48, y + h * 0.86), (x + w * 0.95, y + h * 0.86)],
           fill=(60, 60, 60), width=2)


def scene_meta(d, x, y, w, h):
    """Smartphone showing a photo, beside a large euro sign."""
    _rect(d, x, y, w, h, (238, 238, 240))
    px, py, pw, ph = x + w * 0.10, y + h * 0.12, w * 0.40, h * 0.76
    d.rounded_rectangle([px, py, px + pw, py + ph], radius=h * 0.05, fill=(30, 30, 38))
    _rect(d, px + pw * 0.08, py + ph * 0.10, pw * 0.84, ph * 0.68, (150, 200, 235))
    d.polygon([(px + pw * 0.15, py + ph * 0.66), (px + pw * 0.38, py + ph * 0.38),
               (px + pw * 0.55, py + ph * 0.58), (px + pw * 0.72, py + ph * 0.44),
               (px + pw * 0.85, py + ph * 0.66)], fill=(90, 140, 80))
    _ell(d, px + pw * 0.62, py + ph * 0.16, pw * 0.18, ph * 0.13, (255, 230, 120))
    _ell(d, px + pw * 0.42, py + ph * 0.82, pw * 0.16, ph * 0.08, (200, 200, 210))
    ef = font(True, max(20, int(h * 0.55)))
    d.text((x + w * 0.56, y + h * 0.22), "€", font=ef, fill=(176, 42, 30))


def scene_baseball(d, x, y, w, h):
    """Baseball diamond with a ball and a bat."""
    _rect(d, x, y, w, h, (70, 150, 80))
    d.polygon([(x + w * 0.50, y + h * 0.12), (x + w * 0.88, y + h * 0.50),
               (x + w * 0.50, y + h * 0.88), (x + w * 0.12, y + h * 0.50)],
              fill=(222, 200, 160))
    d.polygon([(x + w * 0.50, y + h * 0.22), (x + w * 0.78, y + h * 0.50),
               (x + w * 0.50, y + h * 0.78), (x + w * 0.22, y + h * 0.50)],
              fill=(110, 190, 110))
    _ell(d, x + w * 0.44, y + h * 0.42, w * 0.12, h * 0.17, (255, 255, 255))
    d.arc([x + w * 0.44, y + h * 0.42, x + w * 0.56, y + h * 0.59], 200, 340,
          fill=(200, 40, 40), width=1)
    d.polygon([(x + w * 0.66, y + h * 0.10), (x + w * 0.72, y + h * 0.06),
               (x + w * 0.86, y + h * 0.34), (x + w * 0.80, y + h * 0.38)],
              fill=(150, 105, 60))


def scene_iran(d, x, y, w, h):
    """Calendar page and an hourglass: waiting until the new year."""
    _rect(d, x, y, w, h, (245, 235, 210))
    cx, cy, cw, ch = x + w * 0.08, y + h * 0.14, w * 0.52, h * 0.72
    _rect(d, cx, cy, cw, ch, (255, 255, 255))
    d.rectangle([cx, cy, cx + cw - 1, cy + ch - 1], outline=(150, 150, 150))
    _rect(d, cx, cy, cw, h * 0.14, (176, 42, 30))
    for r in range(3):
        for c in range(4):
            gx = cx + cw * (0.10 + c * 0.22)
            gy = cy + ch * (0.30 + r * 0.20)
            if r == 1 and c == 2:
                d.ellipse([gx - 2, gy - 2, gx + w * 0.10, gy + h * 0.12],
                          outline=(200, 30, 25), width=2)
            else:
                _ell(d, gx, gy, w * 0.05, h * 0.07, (120, 120, 125))
    hx, hy = x + w * 0.68, y + h * 0.18
    d.polygon([(hx, hy), (hx + w * 0.22, hy), (hx + w * 0.11, hy + h * 0.26)],
              fill=(210, 180, 120))
    d.polygon([(hx, hy + h * 0.52), (hx + w * 0.22, hy + h * 0.52),
               (hx + w * 0.11, hy + h * 0.26)], fill=(210, 180, 120))
    d.line([(hx, hy), (hx + w * 0.22, hy)], fill=(90, 70, 40), width=2)
    d.line([(hx, hy + h * 0.52), (hx + w * 0.22, hy + h * 0.52)],
           fill=(90, 70, 40), width=2)


SCENES = {
    "kyiv": scene_kyiv,
    "riyadh": scene_riyadh,
    "poland": scene_poland,
    "estonia": scene_estonia,
    "stocks": scene_stocks,
    "gta6": scene_gta6,
    "hospital": scene_hospital,
    "police": scene_police,
    "summit": scene_summit,
    "germany": scene_germany,
    "berlin": scene_berlin,
    "debt": scene_debt,
    "meta": scene_meta,
    "baseball": scene_baseball,
    "iran": scene_iran,
}

# (scene, headline, source) — wording exactly as verified.
STORIES = [
    ("kyiv",
     "Russia strikes Kyiv bridges overnight; 8 killed, 28 injured across nine regions.",
     "Just Security"),
    ("riyadh",
     "Houthi missile damages Riyadh's sovereign wealth fund tower in the financial district.",
     "One Turn"),
    ("poland",
     "Russia violates Poland's airspace overnight with two missiles and a drone.",
     "Just Security"),
    ("estonia",
     "Estonia closes its border with Russia for at least six months.",
     "Just Security"),
    ("stocks",
     "US stocks fall a fifth straight day; Japan's Nikkei drops 4.8%.",
     "One Turn"),
    ("gta6",
     "Grand Theft Auto 6 launch tops $2.3 billion in sales.",
     "One Turn"),
    ("hospital",
     "Kenya discharges its last Ebola patient, 37 days after the first case.",
     "One Turn"),
    ("police",
     "Haiti police kill 34 suspected gang members.",
     "Open Chronicle"),
    ("summit",
     "EU and UK hold their second summit in Brussels.",
     "Open Chronicle"),
    ("germany",
     "Germany rejects a new Yalta deal over Europe's future.",
     "Open Chronicle"),
    ("berlin",
     "Ukraine's allies meet in Berlin and say Europe is ready to talk with Russia.",
     "One Turn"),
    ("debt",
     "IMF warns global public debt is nearing 100% of world GDP.",
     "Morning Briefing"),
    ("meta",
     "Italy fines Meta 805 million euros over Android photo access.",
     "Morning Briefing"),
    ("baseball",
     "Trump announces a posthumous pardon for baseball star Pete Rose.",
     "AppiSToS"),
    ("iran",
     "Trump says he will not decide the next Iran step until the new year.",
     "Just Security"),
]


def draw_thumb(d, kind, x, y, w, h):
    SCENES[kind](d, x, y, w, h)
    d.rectangle([x, y, x + w - 1, y + h - 1], outline=RULE, width=1)


def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- masthead -----------------------------------------------------------
    title_f = font(True, 56)
    tw = d.textlength("THE WORLD TODAY", font=title_f)
    d.text(((W - tw) / 2, 12), "THE WORLD TODAY", font=title_f, fill=INK)
    d.line([(28, 82), (996, 82)], fill=RULE, width=2)
    date_f = font(True, 24)
    dw = d.textlength(DATE_STR, font=date_f)
    d.text(((W - dw) / 2, 90), DATE_STR, font=date_f, fill=RED)
    d.line([(28, 124), (996, 124)], fill=RULE, width=3)

    # --- lead story ---------------------------------------------------------
    kind, headline, source = STORIES[0]
    draw_thumb(d, kind, 28, 136, 380, 210)
    tx = 428
    d.text((tx, 140), "TOP STORY", font=font(True, 16), fill=RED)
    lead_f = font(True, 31)
    lines = wrap(d, headline, lead_f, 568)
    ly = 168
    for ln in lines:
        d.text((tx, ly), ln, font=lead_f, fill=INK)
        ly += 39
    d.text((tx, ly + 8), "Source: " + source, font=font(False, 18), fill=MUTED)

    d.line([(28, 356), (996, 356)], fill=RULE, width=2)

    # --- grid: remaining 14 stories, two columns x seven rows ---------------
    head_f = font(True, 19)
    src_f = font(False, 14)
    row_h, top = 90, 364
    for i, (kind, headline, source) in enumerate(STORIES[1:]):
        col, row = i % 2, i // 2
        cx = 28 + col * 488
        cy = top + row * row_h
        draw_thumb(d, kind, cx, cy + 2, 148, 88)
        lines = wrap(d, headline, head_f, 322)
        ly = cy + 2
        for ln in lines[:3]:
            d.text((cx + 158, ly), ln, font=head_f, fill=INK)
            ly += 23
        d.text((cx + 158, ly + 4), "Source: " + source, font=src_f, fill=MUTED)

    # --- footer ---------------------------------------------------------------
    foot_f = font(False, 12)
    foot = "THE WORLD TODAY  ·  " + DATE_STR
    fw = d.textlength(foot, font=foot_f)
    d.text(((W - fw) / 2, 1006), foot, font=foot_f, fill=MUTED)

    return img


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, "entry.png")
    img = build()
    img.save(out, "JPEG", quality=90)
    print("wrote", out)


if __name__ == "__main__":
    main()
