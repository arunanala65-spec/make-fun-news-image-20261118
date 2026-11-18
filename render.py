#!/usr/bin/env python3
"""Render the 18 November 2026 world-news summary infographic (1024x1024 PNG).

Layout (baoyu-infographic): bento-grid -- six equal story tiles under one
date banner. Style: retro-pop-grid -- flat pop colours, thick ink outlines,
Swiss grid. All text is drawn by code with DejaVu fonts, so nothing is garbled.
Stories verified against >=2 sources each on 2026-11-18 (see README.md).
None of the 17 November stories are repeated.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
INK = (26, 26, 46)
CREAM = (255, 246, 229)
WHITE = (255, 255, 255)
MUTED = (70, 70, 90)
RED = (230, 57, 70)
TEAL = (42, 157, 143)
MUSTARD = (233, 196, 106)
BLUE = (69, 123, 157)
ORANGE = (244, 162, 97)
PURPLE = (123, 94, 167)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


F_TITLE = font(FB, 78)
F_SUB = font(FB, 26)
F_KICK = font(FB, 22)
F_HEAD = font(FB, 28)
F_BODY = font(FR, 20)
F_FOOT = font(FR, 19)
F_TAG = font(FB, 17)

STORIES = [
    dict(tag="MIDDLE EAST  •  GULF", colour=RED,
         head="Iran hits US bases in Gulf",
         body="Tehran strikes Ali Al Salem in Kuwait and sites in Bahrain after the US hit Qeshm.",
         icon="missile"),
    dict(tag="ASIA  •  SUMMIT", colour=ORANGE,
         head="Xi, Putin open APEC summit",
         body="Leaders denounce protectionism and sanctions in Shenzhen before meeting Trump.",
         icon="dome"),
    dict(tag="ISRAEL  •  POLITICS", colour=TEAL,
         head="Kahana elected Knesset speaker",
         body="A win for PM-elect Eisenkot's camp, and a setback for Netanyahu's candidate.",
         icon="gavel"),
    dict(tag="HEALTH  •  USA", colour=BLUE,
         head="US loses measles-free status",
         body="5,412 cases in 2026, the most since 1991, end 26 years of elimination status.",
         icon="virus"),
    dict(tag="HEALTH  •  AFRICA", colour=PURPLE,
         head="Ebola in Congo tops 11,000",
         body="Cases more than doubled in three months; three in four infected under-5s die.",
         icon="cross"),
    dict(tag="SPACE", colour=MUSTARD,
         head="Voyager 1: one light-day out",
         body="First human-made object 16 billion miles away; a signal now takes 24 hours.",
         icon="rocket"),
]


def wrap(text, fnt, width, draw):
    """Greedy word wrap to pixel width."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_icon(d, kind, cx, cy, colour):
    """Simple flat geometric icon, centred at (cx, cy), inside a 96px box."""
    s = 96
    x0, y0 = cx - s // 2, cy - s // 2
    if kind == "missile":
        # vertical missile with nose cone, fins and flame
        d.polygon([(x0 + 48, y0 + 6), (x0 + 62, y0 + 30), (x0 + 34, y0 + 30)],
                  fill=INK)
        d.rectangle([x0 + 34, y0 + 30, x0 + 62, y0 + 64], fill=INK)
        d.polygon([(x0 + 34, y0 + 52), (x0 + 18, y0 + 70), (x0 + 34, y0 + 66)],
                  fill=INK)
        d.polygon([(x0 + 62, y0 + 52), (x0 + 78, y0 + 70), (x0 + 62, y0 + 66)],
                  fill=INK)
        d.polygon([(x0 + 40, y0 + 64), (x0 + 56, y0 + 64), (x0 + 48, y0 + 90)],
                  fill=colour)
    elif kind == "dome":
        d.rectangle([x0 + 14, y0 + 58, x0 + 82, y0 + 82], fill=INK)
        d.pieslice([x0 + 28, y0 + 22, x0 + 68, y0 + 62], 180, 360, fill=INK)
        d.line([x0 + 48, y0 + 10, x0 + 48, y0 + 22], fill=INK, width=5)
        d.ellipse([x0 + 44, y0 + 6, x0 + 52, y0 + 14], fill=colour)
        for x in (x0 + 24, x0 + 44, x0 + 64):
            d.rectangle([x, y0 + 66, x + 8, y0 + 82], fill=CREAM)
        d.polygon([(x0 + 70, y0 + 82), (x0 + 92, y0 + 82), (x0 + 92, y0 + 60)],
                  fill=colour)
    elif kind == "gavel":
        d.line([x0 + 20, y0 + 76, x0 + 76, y0 + 20], fill=INK, width=8)
        d.rounded_rectangle([x0 + 52, y0 + 8, x0 + 90, y0 + 30], 6, fill=INK)
        d.rounded_rectangle([x0 + 6, y0 + 78, x0 + 44, y0 + 90], 4, fill=colour)
        d.ellipse([x0 + 8, y0 + 14, x0 + 34, y0 + 40], outline=colour, width=5)
    elif kind == "virus":
        # spiked ball: radiating spikes + core
        for ang in range(0, 360, 45):
            import math
            r = math.radians(ang)
            x1 = cx + int(22 * math.cos(r))
            y1 = cy + int(22 * math.sin(r))
            x2 = cx + int(40 * math.cos(r))
            y2 = cy + int(40 * math.sin(r))
            d.line([x1, y1, x2, y2], fill=INK, width=6)
            d.ellipse([x2 - 6, y2 - 6, x2 + 6, y2 + 6], fill=colour)
        d.ellipse([cx - 22, cy - 22, cx + 22, cy + 22], fill=INK)
        d.ellipse([cx - 8, cy - 12, cx + 2, cy - 2], fill=colour)
        d.ellipse([cx + 4, cy + 6, cx + 14, cy + 16], fill=colour)
    elif kind == "cross":
        d.rounded_rectangle([x0 + 10, y0 + 10, x0 + 86, y0 + 86], 12,
                            fill=INK)
        d.rectangle([x0 + 40, y0 + 22, x0 + 56, y0 + 74], fill=colour)
        d.rectangle([x0 + 22, y0 + 40, x0 + 74, y0 + 56], fill=colour)
    elif kind == "rocket":
        # ascending rocket with window and flame
        d.polygon([(x0 + 48, y0 + 4), (x0 + 64, y0 + 30), (x0 + 32, y0 + 30)],
                  fill=INK)
        d.rectangle([x0 + 32, y0 + 30, x0 + 64, y0 + 66], fill=INK)
        d.polygon([(x0 + 32, y0 + 54), (x0 + 16, y0 + 72), (x0 + 32, y0 + 68)],
                  fill=INK)
        d.polygon([(x0 + 64, y0 + 54), (x0 + 80, y0 + 72), (x0 + 64, y0 + 68)],
                  fill=INK)
        d.ellipse([x0 + 40, y0 + 36, x0 + 56, y0 + 52], fill=colour)
        d.polygon([(x0 + 40, y0 + 66), (x0 + 56, y0 + 66), (x0 + 48, y0 + 90)],
                  fill=colour)


def main():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)

    # ---- Header banner ----
    d.rectangle([0, 0, W, 168], fill=INK)
    d.rectangle([0, 168, W, 176], fill=RED)
    d.text((40, 14), "THE WORLD IN ONE DAY", font=F_KICK, fill=MUSTARD)
    d.text((40, 44), "18 NOVEMBER 2026", font=F_TITLE, fill=WHITE)
    d.text((40, 128), "WEDNESDAY  •  SIX STORIES THAT LED THE DAY",
           font=F_SUB, fill=(255, 255, 255))

    # ---- Bento grid: 2 columns x 3 rows ----
    margin, gap = 24, 20
    cw = (W - 2 * margin - gap) // 2
    ch = 238
    top = 196
    for i, s in enumerate(STORIES):
        row, col = divmod(i, 2)
        x = margin + col * (cw + gap)
        y = top + row * (ch + gap)
        # card
        d.rounded_rectangle([x, y, x + cw, y + ch], 14, fill=WHITE,
                            outline=INK, width=4)
        # coloured tag chip
        tag = s["tag"]
        tw = d.textlength(tag, font=F_TAG) + 20
        d.rounded_rectangle([x + 16, y + 14, x + 16 + tw, y + 42], 8,
                            fill=s["colour"], outline=INK, width=3)
        d.text((x + 26, y + 18), tag, font=F_TAG, fill=INK)
        # icon badge
        ix, iy = x + 62, y + 118
        d.ellipse([ix - 56, iy - 56, ix + 56, iy + 56], fill=CREAM,
                  outline=INK, width=4)
        draw_icon(d, s["icon"], ix, iy, s["colour"])
        # headline + body
        tx = x + 132
        twidth = x + cw - 18 - tx
        lines = wrap(s["head"], F_HEAD, twidth, d)[:2]
        ly = y + 56
        for ln in lines:
            d.text((tx, ly), ln, font=F_HEAD, fill=INK)
            ly += 36
        for ln in wrap(s["body"], F_BODY, twidth, d)[:3]:
            d.text((tx, ly), ln, font=F_BODY, fill=MUTED)
            ly += 26

    # ---- Footer ----
    fy = top + 3 * ch + 2 * gap + 12
    d.text((40, fy), "All events first reported on 18 November 2026.",
           font=F_FOOT, fill=INK)
    d.text((40, fy + 26),
           "Sources: Reuters, Wall Street Journal, NASA, PAHO, UN, BBC.",
           font=F_FOOT, fill=MUTED)

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
