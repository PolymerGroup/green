# -*- coding: utf-8 -*-
"""Generate brand, favicon and Open Graph images with Pillow."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

from data import PRODUCTS, BY_SLUG, CATEGORIES

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "public" / "assets" / "img"
OG = IMG / "og"

F_BOLD = r"C:\Windows\Fonts\segoeuib.ttf"
F_SEMI = r"C:\Windows\Fonts\segoeuisl.ttf"
F_REG = r"C:\Windows\Fonts\segoeui.ttf"
F_MONO = r"C:\Windows\Fonts\consola.ttf"
F_MONOB = r"C:\Windows\Fonts\consolab.ttf"

INK = (7, 34, 47)
DEEP = (10, 58, 82)
DEEP2 = (6, 28, 38)
TEAL = (22, 179, 173)
TEAL_DARK = (14, 143, 143)
MINT = (233, 248, 245)
WHITE = (255, 255, 255)
MUTED = (150, 185, 193)


def font(path, size):
    return ImageFont.truetype(path, size)


def text_size(draw, text, f):
    box = draw.textbbox((0, 0), text, font=f)
    return box[2] - box[0], box[3] - box[1]


def wrap(draw, text, f, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=f) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit_title(draw, text, max_w, max_lines=3, start=70, floor=40):
    for size in range(start, floor - 2, -4):
        f = font(F_BOLD, size)
        lines = wrap(draw, text, f, max_w)
        if len(lines) <= max_lines:
            return f, lines
    return font(F_BOLD, floor), wrap(draw, text, font(F_BOLD, floor), max_w)


def gradient(size, c1, c2, horizontal=False):
    w, h = size
    img = Image.new("RGB", (1, h if not horizontal else 1))
    if horizontal:
        img = Image.new("RGB", (w, 1))
        for x in range(w):
            t = x / max(1, w - 1)
            img.putpixel((x, 0), tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3)))
    else:
        for y in range(h):
            t = y / max(1, h - 1)
            img.putpixel((0, y), tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3)))
    return img.resize((w, h))


def rounded_gradient(size, c1, c2, radius, horizontal=False):
    w, h = size
    g = gradient((w, h), c1, c2, horizontal)
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, w - 1, h - 1], radius=radius, fill=255)
    out = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    out.paste(g, (0, 0), mask)
    return out


def tracked(draw, xy, text, f, fill, tracking=4):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=f, fill=fill)
        x += draw.textlength(ch, font=f) + tracking


def draw_logo(draw, x, y, s=54, dark=True, v_color=WHITE):
    # hexagon outline
    pts = []
    import math
    for i in range(6):
        a = math.radians(60 * i - 30)
        pts.append((x + s / 2 + (s / 2) * math.cos(a), y + s / 2 + (s / 2) * math.sin(a)))
    draw.polygon(pts, outline=TEAL, width=max(2, s // 14))
    # V chevron
    draw.line([(x + s * .29, y + s * .33), (x + s * .50, y + s * .78), (x + s * .71, y + s * .33)],
              fill=v_color, width=max(2, s // 12), joint="curve")
    r = max(2, s // 17)
    draw.ellipse([x + s * .50 - r, y + s * .24 - r, x + s * .50 + r, y + s * .24 + r], fill=TEAL)
    draw.ellipse([x + s * .29 - r, y + s * .33 - r, x + s * .29 + r, y + s * .33 + r], fill=TEAL)
    draw.ellipse([x + s * .71 - r, y + s * .33 - r, x + s * .71 + r, y + s * .33 + r], fill=TEAL)


def draw_vial(canvas, x, y, w, h, name, spec, powder=(207, 233, 228)):
    layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    # shadow
    d.ellipse([x + w * .16, y + h - 26, x + w * .84, y + h + 4], fill=(0, 0, 0, 120))
    layer = layer.filter(ImageFilter.GaussianBlur(12))
    canvas.alpha_composite(layer)

    # cap
    cap_w = w * .44
    cap_x = x + (w - cap_w) / 2
    cap = rounded_gradient((int(cap_w), 34), (160, 181, 190), (238, 246, 248), 5, horizontal=True)
    canvas.alpha_composite(cap, (int(cap_x), int(y + 8)))
    d = ImageDraw.Draw(canvas)
    d.rectangle([cap_x, y + 8, cap_x + cap_w, y + 42], outline=(120, 145, 153, 255), width=1)
    for i in range(6):
        gx = cap_x + 8 + i * (cap_w - 16) / 5
        d.line([(gx, y + 12), (gx, y + 38)], fill=(110, 135, 143, 130), width=1)
    d.rectangle([cap_x, y + 40, cap_x + cap_w, y + 43], fill=(120, 145, 153, 255))
    neck_w = cap_w * .58
    d.rectangle([x + (w - neck_w) / 2, y + 43, x + (w + neck_w) / 2, y + 58],
                fill=(210, 234, 238, 200), outline=(185, 211, 217, 255), width=1)

    # body glass
    bx0, bx1 = x + w * .16, x + w * .84
    by0, by1 = y + 58, y + h - 8
    body = rounded_gradient((int(bx1 - bx0), int(by1 - by0)), (248, 253, 254), (193, 219, 224), 34)
    canvas.alpha_composite(body, (int(bx0), int(by0)))
    d = ImageDraw.Draw(canvas)
    d.rounded_rectangle([bx0, by0, bx1, by1], radius=34, outline=(175, 205, 211, 255), width=2)

    # powder
    py = by0 + (by1 - by0) * .55
    mask = Image.new("L", canvas.size, 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle([bx0 + 3, py, bx1 - 3, by1 - 4], radius=30, fill=255)
    shade = Image.new("RGBA", canvas.size, powder + (235,))
    canvas.alpha_composite(Image.composite(shade, Image.new("RGBA", canvas.size, (0, 0, 0, 0)), mask))

    # highlight
    d = ImageDraw.Draw(canvas)
    d.rounded_rectangle([bx0 + 9, by0 + 22, bx0 + 19, by0 + (by1 - by0) * .6], radius=5, fill=(255, 255, 255, 150))
    d.rounded_rectangle([bx1 - 16, by0 + 36, bx1 - 10, by0 + (by1 - by0) * .5], radius=3, fill=(255, 255, 255, 95))

    # label
    lx0, lx1 = bx0 + 12, bx1 - 12
    ly0, ly1 = by0 + (by1 - by0) * .22, by0 + (by1 - by0) * .72
    d.rounded_rectangle([lx0, ly0, lx1, ly1], radius=5, fill=(255, 255, 255, 250), outline=(210, 226, 230, 255))
    d.rectangle([lx0, ly0, lx1, ly0 + 24], fill=DEEP)
    tracked(d, (lx0 + 12, ly0 + 7), "VIVALR", font(F_MONO, 10), (127, 224, 217), 2)
    # product name
    max_w = (lx1 - lx0) - 20
    nf = font(F_BOLD, 15)
    if d.textlength(name, font=nf) > max_w:
        nf = font(F_BOLD, 13)
    if d.textlength(name, font=nf) > max_w:
        nf = font(F_BOLD, 11)
    lines = wrap(d, name, nf, max_w)[:3]
    ty = ly0 + 40
    for line in lines:
        tw = d.textlength(line, font=nf)
        d.text((lx0 + (lx1 - lx0 - tw) / 2, ty), line, font=nf, fill=DEEP)
        ty += nf.size + 3
    # spec
    sf = font(F_MONO, 10)
    if d.textlength(spec, font=sf) > max_w:
        sf = font(F_MONO, 8)
    tw = d.textlength(spec, font=sf)
    d.text((lx0 + (lx1 - lx0 - tw) / 2, ly1 - 34), spec, font=sf, fill=(63, 101, 114))
    d.line([(lx0 + 12, ly1 - 20), (lx1 - 12, ly1 - 20)], fill=(219, 231, 234), width=1)
    rn = "RESEARCH USE ONLY"
    tw = d.textlength(rn, font=font(F_REG, 6))
    d.text((lx0 + (lx1 - lx0 - tw) / 2, ly1 - 15), rn, font=font(F_REG, 6), fill=(138, 162, 171))

    # measurement ticks
    d.line([(bx1 + 10, by0 + 40), (bx1 + 18, by0 + 40)], fill=(205, 228, 232, 180), width=1)
    d.line([(bx1 + 10, by0 + 120), (bx1 + 18, by0 + 120)], fill=(205, 228, 232, 180), width=1)


def og_base():
    canvas = Image.new("RGBA", (1200, 630), DEEP2 + (255,))
    g = gradient((1200, 630), (4, 20, 28), (10, 58, 82))
    canvas.paste(g, (0, 0))
    # glow
    glow = Image.new("RGBA", (1200, 630), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([720, -160, 1360, 470], fill=(22, 179, 173, 60))
    glow = glow.filter(ImageFilter.GaussianBlur(90))
    canvas.alpha_composite(glow)
    d = ImageDraw.Draw(canvas)
    # grid
    for x in range(780, 1200, 48):
        d.line([(x, 0), (x, 630)], fill=(255, 255, 255, 13), width=1)
    for y in range(0, 630, 48):
        d.line([(780, y), (1200, y)], fill=(255, 255, 255, 13), width=1)
    # frame accents
    d.line([(0, 0), (1200, 0)], fill=TEAL + (255,), width=3)
    return canvas


def brand_lockup(canvas):
    d = ImageDraw.Draw(canvas)
    draw_logo(d, 72, 46, 48)
    tracked(d, (136, 50), "VIVALR", font(F_BOLD, 22), WHITE, 6)
    tracked(d, (137, 80), "RESEARCH PEPTIDES", font(F_SEMI, 9), (143, 190, 197), 2)


def footer_line(canvas, pills):
    d = ImageDraw.Draw(canvas)
    d.line([(72, 566), (1128, 566)], fill=(255, 255, 255, 32), width=1)
    d.text((72, 585), "vivalr.com", font=font(F_BOLD, 15), fill=WHITE)
    d.text((190, 585), "info@vivalr.com", font=font(F_REG, 13), fill=(160, 195, 202))
    d.text((360, 585), "+86 15866781826", font=font(F_REG, 13), fill=(160, 195, 202))
    x = 1128
    for label in reversed(pills):
        f = font(F_MONO, 10)
        w = d.textlength(label, font=f)
        d.rounded_rectangle([x - w - 22, 578, x, 606], radius=14, outline=(110, 190, 190, 120), fill=(255, 255, 255, 12))
        d.text((x - w - 11, 585), label, font=f, fill=(170, 225, 222))
        x -= w + 30


def make_og(filename, eyebrow, title, subtitle, pills, vial=None, detail=None):
    canvas = og_base()
    brand_lockup(canvas)
    d = ImageDraw.Draw(canvas)
    d.text((72, 152), eyebrow.upper(), font=font(F_MONO, 12), fill=(110, 220, 212))
    d.line([(72, 174), (104, 174)], fill=TEAL, width=2)
    tf, lines = fit_title(d, title, 760, 2, 64, 40)
    y = 194
    for line in lines:
        d.text((72, y), line, font=tf, fill=WHITE)
        y += int(tf.size * 1.10) + 4
    y += 18
    if subtitle:
        sf = font(F_REG, 19)
        slines = wrap(d, subtitle, sf, 720)[:2]
        for line in slines:
            d.text((72, y), line, font=sf, fill=(174, 203, 209))
            y += 27
    if detail:
        y += 12
        d.text((72, y), detail, font=font(F_MONO, 13), fill=(127, 224, 217))
        d.text((72, y + 30), "COA + MS + SDS   ·   WORLDWIDE EXPRESS   ·   QUOTE IN 12 H",
               font=font(F_MONO, 10), fill=(112, 154, 164))
    if vial:
        name, spec, powder = vial
        draw_vial(canvas, 900, 120, 200, 400, name, spec, powder)
    footer_line(canvas, pills)
    canvas.convert("RGB").save(OG / filename, "PNG", optimize=True)


def make_home():
    canvas = og_base()
    brand_lockup(canvas)
    d = ImageDraw.Draw(canvas)
    d.text((72, 150), "B2B RESEARCH PEPTIDES  ·  JINAN, CHINA", font=font(F_MONO, 12), fill=(110, 220, 212))
    tf, lines = fit_title(d, "Research peptides, documented batch by batch.", 760, 2, 58, 40)
    y = 190
    for line in lines:
        d.text((72, y), line, font=tf, fill=WHITE)
        y += int(tf.size * 1.10) + 4
    y += 22
    d.text((72, y), "Cosmetic, repair, GLOW/KLOW blends and NAD+/NMN.", font=font(F_REG, 20), fill=(174, 203, 209))
    d.text((72, y + 30), "≥99% HPLC · MS verified · COA per batch · worldwide.", font=font(F_REG, 20), fill=(174, 203, 209))
    draw_vial(canvas, 900, 120, 200, 400, "GHK-Cu", "50 mg · 10 vials", (47, 111, 158))
    footer_line(canvas, ["34 MOLECULES", "COA + SDS", "MOQ 1 KIT"])
    canvas.convert("RGB").save(OG / "home.png", "PNG", optimize=True)


def make_generic(name, eyebrow, title, subtitle, pills, vial=None):
    make_og(name, eyebrow, title, subtitle, pills, vial=vial)


def make_favicon():
    # SVG
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="14" fill="#07222f"/>
<path d="M32 8 55 21v22L32 56 9 43V21Z" fill="none" stroke="#16b3ad" stroke-width="2.4" opacity=".55"/>
<path d="M19 22 32 46l13-24" fill="none" stroke="#16b3ad" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="32" cy="20" r="3.6" fill="#ffffff"/>
<circle cx="19" cy="22" r="2.3" fill="#16b3ad"/><circle cx="45" cy="22" r="2.3" fill="#16b3ad"/>
</svg>'''
    (IMG / "favicon.svg").write_text(svg, encoding="utf-8")

    # 512 transparent-ish deep tile
    for size, name in ((512, "favicon-512.png"), (192, "favicon-192.png"), (180, "apple-touch-icon.png"), (32, "favicon-32.png")):
        im = Image.new("RGBA", (size * 4, size * 4), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        s = size * 4
        d.rounded_rectangle([0, 0, s, s], radius=int(s * .22), fill=(7, 34, 47, 255))
        import math
        cx, cy, R = s / 2, s / 2, s * .40
        pts = []
        for i in range(6):
            a = math.radians(60 * i - 30)
            pts.append((cx + R * math.cos(a), cy + R * math.sin(a)))
        d.polygon(pts, outline=TEAL + (170,), width=max(2, s // 70))
        d.line([(s * .29, s * .34), (s * .50, s * .72), (s * .71, s * .34)],
               fill=TEAL, width=max(3, s // 26), joint="curve")
        r = s * .055
        d.ellipse([s * .5 - r, s * .28 - r, s * .5 + r, s * .28 + r], fill=WHITE)
        im = im.resize((size, size), Image.LANCZOS)
        im.save(IMG / name, "PNG", optimize=True)

    # logo-512 for schema: white tile with wordmark
    size = 512
    im = Image.new("RGBA", (size, size), (255, 255, 255, 255))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([36, 36, 476, 476], radius=90, fill=(247, 250, 251, 255), outline=(219, 231, 234, 255), width=2)
    draw_logo(d, 166, 96, 180, dark=True, v_color=INK)
    tracked(d, (108, 310), "VIVALR", font(F_BOLD, 54), INK, 8)
    tracked(d, (110, 378), "RESEARCH PEPTIDES", font(F_SEMI, 15), (91, 116, 128), 3)
    d.line([(150, 430), (362, 430)], fill=(219, 231, 234), width=2)
    im.convert("RGB").save(IMG / "logo-512.png", "PNG", optimize=True)


def main():
    IMG.mkdir(parents=True, exist_ok=True)
    OG.mkdir(parents=True, exist_ok=True)
    make_favicon()
    make_home()
    make_generic(
        "products.png",
        "THE CATALOGUE",
        "34 research molecules. One documentation standard.",
        "Cosmetic actives, repair peptides, GLOW & KLOW blends, and NAD+/NMN.",
        ["HPLC ≥99%", "MS VERIFIED", "COA PER BATCH"],
        vial=("BPC-157", "10 mg · 10 vials", (207, 233, 228)),
    )
    make_generic(
        "synthesis.png",
        "TECHNICAL FILE",
        "Synthesis, purity and stability.",
        "Fmoc SPPS, preparative HPLC, ESI-MS identity and stress-stability guidance.",
        ["SPPS", "HPLC ≥99%", "MS VERIFIED"],
        vial=("Epithalon", "10 mg · 10 vials", (207, 233, 228)),
    )
    make_generic(
        "about.png",
        "ABOUT VIVALR",
        "A Jinan-based supplier built for research buyers.",
        "Shandong Green International Trade Co., Ltd. — research peptides and coenzymes.",
        ["JINAN, CHINA", "WORLDWIDE", "RESEARCH USE ONLY"],
        vial=("GHK-Cu", "50 mg · 10 vials", (47, 111, 158)),
    )
    make_generic(
        "contact.png",
        "CONTACT",
        "Talk to a person who knows the chemistry.",
        "WhatsApp +86 15866781826 · info@vivalr.com · reply within 12 business hours.",
        ["WHATSAPP", "EMAIL", "RFQ"],
        vial=("GLOW", "70 mg blend", (207, 233, 228)),
    )
    for p in PRODUCTS:
        spec = p["variants"][0]["label"].split(" ×")[0]
        if p["cat"] == "blend":
            spec = p["variants"][0]["label"].split(" mg")[0] + " mg blend"
        powder = (47, 111, 158) if p["slug"] in ("ghk-cu", "ahk-cu") else (207, 233, 228)
        make_og(
            p["slug"] + ".png",
            p["cat_short"],
            p["name"],
            p["tagline"],
            ["HPLC ≥99%", "MS VERIFIED", "COA"],
            vial=(p["name"], spec, powder),
            detail="CAS " + p["cas"] + "  ·  " + p["spec_summary"],
        )
    print("images:", len(list(IMG.rglob("*.png"))), "png +", len(list(IMG.rglob("*.svg"))), "svg")


if __name__ == "__main__":
    main()
