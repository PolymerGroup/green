# -*- coding: utf-8 -*-
"""Final launch audit for the Vivalr build."""
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree as ET

from lxml import html as LH
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
SITE = "https://vivalr.com"
errors, warnings = [], []

pages = sorted(PUB.rglob("*.html"))
titles, descs = {}, {}
product_count = 0

for path in pages:
    r = str(path.relative_to(PUB)).replace("\\", "/")
    raw = path.read_text(encoding="utf-8")
    doc = LH.fromstring(raw)

    t = doc.xpath("//title/text()")[0].strip()
    d = doc.xpath('//meta[@name="description"]/@content')[0].strip()
    titles.setdefault(t, []).append(r)
    descs.setdefault(d, []).append(r)
    if len(t) > 60:
        errors.append(f"{r}: title {len(t)}")
    if len(d) > 155:
        errors.append(f"{r}: desc {len(d)}")

    canon = doc.xpath('//link[@rel="canonical"]/@href')[0]
    if r == "index.html":
        want = SITE + "/"
    elif r.endswith("/index.html"):
        want = SITE + "/" + r[: -len("index.html")]
    else:
        want = SITE + "/" + r[: -len(".html")]
    if canon != want:
        errors.append(f"{r}: canonical {canon} != {want}")

    if r.startswith("products/") and r != "products/index.html":
        product_count += 1
        if "wa.me/8615866781826" not in raw:
            errors.append(f"{r}: no WhatsApp link")
        if "Shandong Green International Trade Co., Ltd." not in raw:
            errors.append(f"{r}: supplier missing")
        if "Key Technical &amp; Supplier Summary" not in raw and "Key Technical & Supplier Summary" not in raw:
            errors.append(f"{r}: summary missing")
        blocks = doc.xpath('//script[@type="application/ld+json"]/text()')
        graph = json.loads(blocks[0])["@graph"]
        prod = [g for g in graph if g.get("@type") == "Product"][0]
        if prod["image"][0] != SITE + "/assets/img/og/" + r.split("/")[-1].replace(".html", ".png"):
            errors.append(f"{r}: schema image mismatch")
        if len(prod.get("additionalProperty", [])) < 8:
            errors.append(f"{r}: few product properties")
        if len([g for g in graph if g.get("@type") == "FAQPage"][0]["mainEntity"]) < 6:
            errors.append(f"{r}: FAQ schema count")
        if "Manufacturer" in raw:
            warnings.append(f"{r}: mentions Manufacturer")

for t, rs in titles.items():
    if len(rs) > 1:
        errors.append(f"duplicate title {t!r}: {rs}")
for d, rs in descs.items():
    if len(rs) > 1:
        errors.append(f"duplicate description {d!r}: {rs}")

# xml
sm = ET.parse(PUB / "sitemap.xml")
ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
locs = [x.text for x in sm.getroot().findall("s:url/s:loc", ns)]
if len(locs) != len(set(locs)):
    errors.append("duplicate sitemap URLs")
if len(locs) != len(pages) - 1:
    warnings.append(f"sitemap {len(locs)} vs pages-404 {len(pages)-1}")
if any(".pages.dev" in x for x in locs):
    errors.append("pages.dev in sitemap")

# robots
robots = (PUB / "robots.txt").read_text(encoding="utf-8")
for bot in ("GPTBot", "ClaudeBot", "PerplexityBot", "Google-Extended", "Sitemap: https://vivalr.com/sitemap.xml"):
    if bot not in robots:
        errors.append(f"robots missing {bot}")

# llms
llms = (PUB / "llms.txt").read_text(encoding="utf-8")
if llms.count("https://vivalr.com/products/") < 34:
    errors.append("llms.txt product links < 34")
if "Shandong Green International Trade Co., Ltd." not in llms:
    errors.append("llms missing company")
if "info@vivalr.com" not in llms:
    errors.append("llms missing email")

# images
for png in (PUB / "assets" / "img" / "og").glob("*.png"):
    im = Image.open(png)
    if im.size != (1200, 630):
        errors.append(f"{png.name}: {im.size}")
required_imgs = ["favicon.svg", "favicon-32.png", "favicon-192.png", "favicon-512.png",
                 "apple-touch-icon.png", "logo-512.png"]
for name in required_imgs:
    if not (PUB / "assets" / "img" / name).exists():
        errors.append(f"missing image {name}")

# global forbidden / required strings
for path in pages:
    raw = path.read_text(encoding="utf-8")
    r = str(path.relative_to(PUB)).replace("\\", "/")
    for bad in ("Fousi", ".pages.dev", "http://vivalr.com"):
        if bad in raw:
            errors.append(f"{r}: forbidden {bad}")
    if "For Laboratory Research and Formulation Evaluation Use Only. Not for Human or Veterinary Use." not in raw:
        errors.append(f"{r}: disclaimer")
    if "info@vivalr.com" not in raw:
        errors.append(f"{r}: email")

# JSON-LD parse all
for path in pages:
    doc = LH.fromstring(path.read_text(encoding="utf-8"))
    for b in doc.xpath('//script[@type="application/ld+json"]/text()'):
        try:
            obj = json.loads(b)
            if obj.get("@context") != "https://schema.org":
                errors.append(f"{path.name}: bad @context")
        except Exception as exc:
            errors.append(f"{path.name}: JSON-LD {exc}")

print(f"HTML pages: {len(pages)} | product pages: {product_count} | sitemap URLs: {len(locs)}")
print(f"OG images: {len(list((PUB/'assets/img/og').glob('*.png')))}")
print(f"errors: {len(errors)} | warnings: {len(warnings)}")
for x in errors:
    print("ERROR", x)
for x in warnings:
    print("WARN", x)
sys.exit(1 if errors else 0)
