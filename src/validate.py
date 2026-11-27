# -*- coding: utf-8 -*-
"""Static-site QA: SEO, schema, links, IDs, required claims."""
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

from lxml import html as LH

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
SITE = "https://vivalr.com"
errors = []
warnings = []


def rel(p):
    return str(p.relative_to(PUB)).replace("\\", "/")


pages = sorted(PUB.rglob("*.html"))
if not pages:
    sys.exit("no html files")

for path in pages:
    r = rel(path)
    raw = path.read_text(encoding="utf-8")
    doc = LH.fromstring(raw)

    titles = doc.xpath("//title/text()")
    if len(titles) != 1:
        errors.append(f"{r}: expected 1 title, got {len(titles)}")
    else:
        t = titles[0].strip()
        if len(t) > 60:
            errors.append(f"{r}: title {len(t)} chars: {t}")
        if "Vivalr" not in t and r != "404.html":
            warnings.append(f"{r}: title lacks Vivalr: {t}")

    descs = doc.xpath('//meta[@name="description"]/@content')
    if len(descs) != 1:
        errors.append(f"{r}: expected 1 meta description, got {len(descs)}")
    else:
        d = descs[0].strip()
        if len(d) > 155:
            errors.append(f"{r}: description {len(d)} chars: {d}")
        if len(d) < 70:
            warnings.append(f"{r}: short description {len(d)} chars")

    h1s = doc.xpath("//h1")
    if len(h1s) != 1:
        errors.append(f"{r}: expected 1 h1, got {len(h1s)}")

    canons = doc.xpath('//link[@rel="canonical"]/@href')
    if len(canons) != 1:
        errors.append(f"{r}: canonical count {len(canons)}")
    else:
        c = canons[0]
        if not c.startswith(SITE + "/"):
            errors.append(f"{r}: bad canonical {c}")
        if ".pages.dev" in c:
            errors.append(f"{r}: pages.dev in canonical")

    if doc.xpath('//html/@lang') != ["en"]:
        errors.append(f"{r}: html lang is not en")

    if ".pages.dev" in raw:
        errors.append(f"{r}: .pages.dev appears in page")

    if "For Laboratory Research and Formulation Evaluation Use Only" not in raw:
        errors.append(f"{r}: research-use disclaimer missing")

    # duplicate ids
    ids = doc.xpath("//*[@id]/@id")
    dup = [k for k, v in Counter(ids).items() if v > 1]
    if dup:
        errors.append(f"{r}: duplicate ids {dup}")

    # JSON-LD
    blocks = doc.xpath('//script[@type="application/ld+json"]/text()')
    if not blocks and r not in ("404.html",):
        errors.append(f"{r}: no JSON-LD")
    for b in blocks:
        try:
            obj = json.loads(b)
        except Exception as exc:
            errors.append(f"{r}: invalid JSON-LD: {exc}")
            continue
        graph = obj.get("@graph", [])
        types = [g.get("@type") for g in graph]
        if r.startswith("products/") and r != "products/index.html":
            if "Product" not in types:
                errors.append(f"{r}: no Product schema")
            if "FAQPage" not in types:
                errors.append(f"{r}: no FAQPage schema")
            for g in graph:
                if g.get("@type") == "Product":
                    if not g.get("name") or not g.get("offers"):
                        errors.append(f"{r}: incomplete Product")
                    props = [x.get("name") for x in g.get("additionalProperty", [])]
                    for need in ("CAS Number", "Purity", "Supplier", "MOQ"):
                        if need not in props:
                            errors.append(f"{r}: Product missing {need}")
                if g.get("@type") == "FAQPage":
                    if len(g.get("mainEntity", [])) < 5:
                        errors.append(f"{r}: fewer than 5 FAQs in schema")
        if r == "index.html":
            for need in ("Organization", "WebSite"):
                if need not in types:
                    errors.append(f"{r}: missing {need} schema")

    # internal links
    for href in doc.xpath("//a/@href"):
        h = href.strip()
        if not h or h.startswith("#") or h.startswith("mailto:") or h.startswith("tel:"):
            continue
        if h.startswith("http"):
            if "vivalr.com" in h and ".pages.dev" not in h:
                p = urlparse(h).path
            else:
                continue
        elif h.startswith("/"):
            p = h.split("#")[0].split("?")[0]
        else:
            warnings.append(f"{r}: relative link {h}")
            continue
        if p in ("", "/"):
            target = PUB / "index.html"
        elif p.endswith("/"):
            target = PUB / p.strip("/") / "index.html"
        elif "." in p.rsplit("/", 1)[-1]:
            target = PUB / p.strip("/")
        else:
            target = PUB / (p.strip("/") + ".html")
        if not target.exists():
            errors.append(f"{r}: broken link {h} -> {target}")

    # og + icon assets exist
    for og in doc.xpath('//meta[@property="og:image"]/@content'):
        if og.startswith(SITE + "/"):
            target = PUB / og[len(SITE) + 1:]
            if not target.exists():
                errors.append(f"{r}: missing og:image {og}")
    for ico in doc.xpath('//link[contains(@rel,"icon") or @rel="apple-touch-icon"]/@href'):
        if ico.startswith("/"):
            if not (PUB / ico.strip("/")).exists():
                errors.append(f"{r}: missing icon {ico}")

    if r.startswith("products/") and r != "products/index.html":
        if "Synthesis &amp; Stability Profile" not in raw and "Synthesis & Stability Profile" not in raw:
            errors.append(f"{r}: missing synthesis profile")
        faq_items = doc.xpath('//details[contains(@class,"faq-item")]')
        if len(faq_items) < 6:
            errors.append(f"{r}: only {len(faq_items)} visible FAQs")

# sitemap coverage
sm = (PUB / "sitemap.xml").read_text(encoding="utf-8")
locs = re.findall(r"<loc>(.*?)</loc>", sm)
for path in pages:
    r = rel(path)
    if r in ("404.html",):
        continue
    if r == "index.html":
        want = SITE + "/"
    elif r.endswith("/index.html"):
        want = SITE + "/" + r[: -len("index.html")]
    else:
        want = SITE + "/" + r[: -len(".html")]
    if want not in locs:
        errors.append(f"sitemap missing {want}")
if any(".pages.dev" in x for x in locs):
    errors.append("sitemap contains pages.dev")

# required contact facts
idx = (PUB / "index.html").read_text(encoding="utf-8")
for needle in (
    "Shandong Green International Trade Co., Ltd.",
    "+86 15866781826",
    "info@vivalr.com",
    "https://wa.me/8615866781826",
    "Environmental Protection Science and Technology Park",
):
    if needle not in idx:
        errors.append(f"index missing required fact: {needle}")

print(f"pages checked: {len(pages)}")
print(f"errors: {len(errors)}")
for x in errors:
    print("  ERROR", x)
print(f"warnings: {len(warnings)}")
for x in warnings[:80]:
    print("  WARN", x)
sys.exit(1 if errors else 0)
