#!/usr/bin/env python3
"""Compose the 18 November 2026 news front page (1024x1024) from panel artwork.

Layout: masthead, black date banner, 3x2 panel grid with kicker strips,
headlines and one-line explainers, source footer. Output: ../entry.png
"""
from PIL import Image, ImageDraw, ImageFont
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ASSETS = os.path.join(ROOT, "assets")

W = 1024
PAPER = (246, 241, 231)
INK = (20, 22, 26)
RED = (179, 40, 45)
GREY = (92, 92, 88)
WHITE = (255, 255, 255)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def fit_font(draw, text, path, max_width, start):
    size = start
    while size > 8:
        f = font(path, size)
        if draw.textlength(text, font=f) <= max_width:
            return f
        size -= 1
    return font(path, 8)


def wrap(draw, text, f, max_width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=f) <= max_width:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def crop_to(im, tw, th):
    """Center-crop image to cover tw x th, then resize."""
    sw, sh = im.size
    scale = max(tw / sw, th / sh)
    im = im.resize((round(sw * scale), round(sh * scale)), Image.LANCZOS)
    x = (im.size[0] - tw) // 2
    y = (im.size[1] - th) // 2
    return im.crop((x, y, x + tw, y + th))


PANELS = [
    dict(img="apec.png", color=(146, 32, 38), kicker="DIPLOMACY · SHENZHEN",
         head="APEC SUMMIT OPENS IN SHENZHEN",
         sub="Xi urges AI partnership and free trade; Trump meets Quad leaders in Manila."),
    dict(img="qeshm.png", color=(196, 96, 20), kicker="CONFLICT · PERSIAN GULF",
         head="U.S. STRIKES IRAN MISSILE SITE",
         sub="Jets hit the Qeshm Island base; Iran answers with drones on Bahrain and Kuwait."),
    dict(img="bridge.png", color=(52, 84, 128), kicker="WAR · CRIMEA",
         head="UKRAINE HITS CRIMEA BRIDGE AGAIN",
         sub="Second day of strikes: a Kerch road span falls into the strait."),
    dict(img="measles.png", color=(178, 44, 52), kicker="HEALTH · UNITED STATES",
         head="U.S. MEASLES-FREE STATUS ENDS",
         sub="Elimination status ends after 26 years; 5,400+ cases so far in 2026."),
    dict(img="cyclone.png", color=(24, 108, 118), kicker="WEATHER · SOUTH PACIFIC",
         head="CATEGORY 5 CYCLONE XAVIER",
         sub="Gusts up to 315 km/h batter the Northern Cook Islands."),
    dict(img="ebola.png", color=(58, 110, 52), kicker="HEALTH · DR CONGO",
         head="EBOLA PASSES 11,000 CASES",
         sub="WHO: the outbreak has more than doubled in three months; 5,400 dead."),
]


def main():
    page = Image.new("RGB", (W, W), PAPER)
    d = ImageDraw.Draw(page)

    # --- masthead ---
    d.rectangle([10, 10, W - 11, W - 11], outline=INK, width=3)
    title = "THE WORLD IN ONE IMAGE"
    f = fit_font(d, title, SERIF_B, 940, 66)
    tw = d.textlength(title, font=f)
    d.text(((W - tw) / 2, 26), title, font=f, fill=INK)
    tag = "THE DAY'S BIGGEST STORIES, ON ONE PAGE"
    ftag = font(SANS_B, 17)
    tw = d.textlength(tag, font=ftag)
    d.text(((W - tw) / 2, 104), tag, font=ftag, fill=GREY)
    d.line([28, 132, W - 28, 132], fill=INK, width=2)

    # --- date banner ---
    by0, by1 = 144, 204
    d.rectangle([24, by0, W - 24, by1], fill=INK)
    d.rectangle([24, by0, 36, by1], fill=RED)
    d.rectangle([W - 36, by0, W - 24, by1], fill=RED)
    date = "WEDNESDAY · 18 NOVEMBER 2026"
    f = fit_font(d, date, SANS_B, 880, 44)
    tw = d.textlength(date, font=f)
    bb = d.textbbox((0, 0), date, font=f)
    d.text(((W - tw) / 2, by0 + (by1 - by0 - (bb[3] - bb[1])) / 2 - bb[1]), date, font=f, fill=WHITE)

    # --- panel grid ---
    gx, gy = 24, 220
    gutter = 14
    pw = (W - 2 * gx - 2 * gutter) // 3          # 314
    img_h = 196
    kick_h = 26
    ph = 366
    f_kick = font(SANS_B, 15)
    f_head = font(SANS_B, 24)
    f_sub = font(SANS, 16)
    for i, p in enumerate(PANELS):
        cx = gx + (i % 3) * (pw + gutter)
        cy = gy + (i // 3) * (ph + gutter)
        # kicker strip
        d.rectangle([cx, cy, cx + pw, cy + kick_h], fill=p["color"])
        kw = d.textlength(p["kicker"], font=f_kick)
        d.text((cx + (pw - kw) / 2, cy + 5), p["kicker"], font=f_kick, fill=WHITE)
        # image
        im = Image.open(os.path.join(ASSETS, p["img"])).convert("RGB")
        page.paste(crop_to(im, pw, img_h), (cx, cy + kick_h))
        # headline: one fixed size for every panel, wrapped over two lines
        lines = wrap(d, p["head"], f_head, pw - 6)
        assert len(lines) <= 2, f"headline wraps to {len(lines)} lines: {p['head']!r} -> {lines}"
        assert len(wrap(d, p["sub"], f_sub, pw - 6)) <= 3, f"sub too long: {p['sub']!r}"
        hy = cy + kick_h + img_h + 9
        for ln in lines[:2]:
            lw = d.textlength(ln, font=f_head)
            d.text((cx + (pw - lw) / 2, hy), ln, font=f_head, fill=INK)
            hy += 30
        hy = cy + kick_h + img_h + 9 + 60  # sub-lines start at a fixed offset
        # sub-line
        for ln in wrap(d, p["sub"], f_sub, pw - 6)[:3]:
            lw = d.textlength(ln, font=f_sub)
            d.text((cx + (pw - lw) / 2, hy + 2), ln, font=f_sub, fill=(52, 52, 50))
            hy += 21
        # panel border
        d.rectangle([cx, cy, cx + pw, cy + ph], outline=(190, 184, 170), width=1)

    # --- footer ---
    fy = gy + 2 * ph + gutter + 8
    d.line([28, fy, W - 28, fy], fill=INK, width=2)
    foot = "Sources: Reuters · CBS News · UN News (WHO) · RNZ · FeedCast · One Turn"
    ffoot = font(SANS, 15)
    tw = d.textlength(foot, font=ffoot)
    d.text(((W - tw) / 2, fy + 8), foot, font=ffoot, fill=GREY)

    out = os.path.join(ROOT, "entry.png")
    page.save(out, optimize=True)
    size = os.path.getsize(out)
    print("saved", out, page.size, size, "bytes")
    if size > 1048576:
        q = page.quantize(colors=256, method=Image.MEDIANCUT)
        q.save(out, optimize=True)
        print("quantized ->", os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
