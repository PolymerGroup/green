# -*- coding: utf-8 -*-
"""Build the Vivalr static site into ../public."""
import json
import os
import re
from pathlib import Path
from urllib.parse import quote

from data import (
    SITE, BRAND, COMPANY, ADDRESS, ADDRESS_SHORT, PHONE, PHONE_TEL, WHATSAPP,
    EMAIL, UPDATED, UPDATED_HUMAN, CATEGORIES, PRODUCTS, BY_SLUG, DEFAULT_MOQ,
)
from ui import (
    e, jsonld, icon, logo_svg, brand, head, header, footer, breadcrumb,
    faq_block, cta_band, product_card, generic_faqs, all_faqs, summary_card,
    product_visual_label, cite_box, disclaimer, vial_svg, molecule_svg, mini_vial,
    WA_TEXT,
)

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "public"


def write(path, content):
    target = OUT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    return target


def clamp_desc(text, limit=155):
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    cut = text[: limit - 1]
    cut = cut.rsplit(" ", 1)[0].rstrip(",;:")
    return cut + "."


def product_title(p):
    if p["slug"] == "thymalin":
        return "Thymalin | Thymic Peptide Complex | Vivalr"
    t = f'{p["title_name"]} Bulk Supplier | ≥99% HPLC | Vivalr'
    if len(t) > 60:
        t = f'{p["title_name"]} | Bulk Supplier | Vivalr'
    if len(t) > 60:
        t = f'{p["title_name"]} | Vivalr'
    return t


def short_spec(p):
    return p["variants"][0]["label"].split(" ×")[0]


def quote_text(p, variant, qty, unit="kit"):
    plural = "packs" if unit == "pack" else "kits"
    lines = [
        "Hello Vivalr, I would like a quotation for:",
        "Product: " + p["full_name"],
        "Specification: " + variant["label"],
        "Quantity: %d %s" % (qty, unit if qty == 1 else plural),
        "SKU: " + variant["sku"],
        "",
        "Please include bulk pricing, COA, lead time and shipping options to my country.",
    ]
    return "\n".join(lines)


def faq_schema(faqs, fid):
    return {
        "@type": "FAQPage",
        "@id": fid,
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in faqs
        ],
    }


def breadcrumb_schema(items):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i + 1,
                "name": label,
                "item": (SITE + href) if href else None,
            }
            for i, (label, href) in enumerate(items)
        ],
    }


def org_node():
    return {
        "@type": "Organization",
        "@id": SITE + "/#organization",
        "name": COMPANY,
        "alternateName": "Vivalr",
        "url": SITE + "/",
        "logo": {
            "@type": "ImageObject",
            "url": SITE + "/assets/img/logo-512.png",
            "width": 512,
            "height": 512,
        },
        "image": SITE + "/assets/img/og/home.png",
        "description": ("China-based B2B supplier of research-grade cosmetic peptides, repair and "
                        "bioregulator peptides, GLOW/KLOW blends and NAD+/NMN raw materials, based in "
                        "Jinan, Shandong."),
        "email": EMAIL,
        "telephone": PHONE_TEL,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Environmental Protection Science and Technology Park, High-Tech Zone",
            "addressLocality": "Jinan",
            "addressRegion": "Shandong",
            "postalCode": "250101",
            "addressCountry": "CN",
        },
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": PHONE_TEL,
                "contactType": "sales",
                "email": EMAIL,
                "availableLanguage": ["English", "Chinese"],
                "areaServed": "Worldwide",
            }
        ],
        "knowsAbout": [
            "research peptides", "cosmetic peptides", "copper peptides", "GHK-Cu", "BPC-157",
            "TB-500", "NAD+", "NMN", "peptide synthesis", "HPLC purity", "lyophilized peptides",
        ],
        "slogan": "Research-grade peptides, documented batch by batch.",
    }


def website_node():
    return {
        "@type": "WebSite",
        "@id": SITE + "/#website",
        "url": SITE + "/",
        "name": BRAND,
        "publisher": {"@id": SITE + "/#organization"},
        "inLanguage": "en",
        "description": ("Bulk research peptides, cosmetic actives and NAD+/NMN raw materials with "
                        "batch COA, HPLC and MS documentation."),
    }


def page(title, desc, path, body, schema, active="", og_type="website",
         og_image="/assets/img/og/home.png", keywords="", noindex=False):
    return (
        head(title, clamp_desc(desc), path, og_type=og_type, og_image=og_image,
             schema=schema, keywords=keywords, noindex=noindex)
        + header(active)
        + body
        + footer()
    )


# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------
HOME_FAQS = [
    ("Are Vivalr products intended for human use?",
     "No. Every product is supplied strictly for laboratory research and formulation evaluation, and is not for human or veterinary use. We do not provide dosage guidance, medical advice or retail-ready finished products."),
    ("Are you a manufacturer or a trading company?",
     "Vivalr is the research-peptide brand of Shandong Green International Trade Co., Ltd., a Jinan-based export company. We work with a qualified network of synthesis and fill-finish partners and take responsibility for the specification, batch documentation and export process."),
    ("Can I review a COA or request a sample before ordering?",
     "Yes. Send the molecule, pack size and intended application and we will share the current batch COA, MS spectrum and SDS. Paid samples are available for most catalogue items; sample freight is quoted separately."),
    ("What is the minimum order quantity?",
     "Most peptides ship as a 10-vial kit with an MOQ of one kit. Bulk powders such as NMN start at 10 g. Custom fill weights and larger pack sizes are quoted from 10 kits upward."),
    ("How do you ship temperature-sensitive peptides?",
     "Lyophilized peptides ship in sealed vials with desiccant, using insulated packaging and gel packs where the destination or season requires it. We use DHL, FedEx or UPS express with tracking, typically 3–7 business days after dispatch."),
    ("Do you offer OEM, private-label or custom fill/finish?",
     "Yes. We support custom vial fill, labelling, kit assembly and documentation packs from modest minimums. Share your target specification and artwork requirements for a feasibility review."),
]


def build_home():
    counts = {k: sum(1 for p in PRODUCTS if p["cat"] == k) for k in CATEGORIES}
    cat_cards = ""
    for key, cat in CATEGORIES.items():
        cat_cards += f'''<a class="cat-card" href="/products/?category={key}">
  <span class="cat-num">0{list(CATEGORIES).index(key) + 1}</span>
  <span class="cat-icon">{icon(cat["icon"])}</span>
  <h3>{e(cat["label"])}</h3>
  <p>{e(cat["desc"])}</p>
  <span class="cat-link">{counts[key]} molecules <span>Explore {icon("arrow", "arrow")}</span></span>
</a>'''

    featured = [p for p in PRODUCTS if p["featured_rank"]][:9]
    featured_cards = "".join(product_card(p) for p in featured)
    faqs = HOME_FAQS

    body = f'''<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <div class="hero-kicker">
        <span class="pill"><span class="dot"></span> B2B research supplier</span>
        <span class="pill">Jinan, China · worldwide</span>
      </div>
      <h1 class="hero-title">Research peptides and NAD<sup>+</sup>, <span class="accent">documented batch by batch.</span></h1>
      <p class="hero-sub">Vivalr supplies ≥99% HPLC-purified cosmetic, repair and longevity peptides to laboratories, formulators and ingredient buyers. COA and MS data with every batch. Quote-only B2B pricing, low minimums, English-language support.</p>
      <div class="hero-actions">
        <a class="btn btn-primary btn-lg" href="/products/">Browse the catalogue {icon("arrow", "arrow")}</a>
        <a class="btn btn-ghost btn-lg" href="/contact#rfq">Request a quote</a>
      </div>
      <div class="hero-stats">
        <div class="hero-stat"><b>{len(PRODUCTS)}</b><span>molecules</span></div>
        <div class="hero-stat"><b>≥99%</b><span>HPLC purity</span></div>
        <div class="hero-stat"><b>10</b><span>vials per kit</span></div>
        <div class="hero-stat"><b>2–3 d</b><span>stock dispatch</span></div>
      </div>
    </div>
    <div class="hero-visual">
      <div class="lab-card">
        <div class="lab-card-head"><span>VVR / QC RELEASE</span><span class="lab-dots"><i></i><i></i><i></i></span></div>
        <div class="vial-stage">{vial_svg(BY_SLUG["ghk-cu"], hero=True)}</div>
        <div class="lab-caption"><span><b>GHK-Cu</b> · 50 mg × 10 vials</span><span>HPLC 99.2%</span></div>
      </div>
      <div class="float-chip chip-a">{icon("chart")}<span>HPLC ≥99%<small>area purity</small></span></div>
      <div class="float-chip chip-b">{icon("flask")}<span>MS verified<small>ESI-MS identity</small></span></div>
      <div class="float-chip chip-c">{icon("file")}<span>COA + SDS<small>every batch</small></span></div>
    </div>
  </div>
</section>

<section class="trustbar" aria-label="Quality commitments">
  <div class="wrap">
    <div class="trust-item">{icon("chart")}<span>HPLC ≥99%<small>every batch</small></span></div>
    <div class="trust-item">{icon("flask")}<span>MS identity<small>ESI-MS confirmed</small></span></div>
    <div class="trust-item">{icon("file")}<span>COA + SDS<small>documentation pack</small></span></div>
    <div class="trust-item">{icon("snow")}<span>Cold chain<small>gel-pack shipping</small></span></div>
    <div class="trust-item">{icon("globe")}<span>Worldwide<small>DHL · FedEx · UPS</small></span></div>
  </div>
</section>

<section class="section" id="categories">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">Four research directions</div>
      <h2 class="section-title">One supplier for the molecules your project actually needs.</h2>
      <p class="section-sub">Cosmetic actives, tissue-repair peptides, fixed-ratio blends and NAD+ precursors — each with a dedicated technical page, aggregated pack sizes and a batch-level documentation standard.</p>
    </div>
    <div class="cat-grid">{cat_cards}</div>
  </div>
</section>

<section class="section tight" style="background:#fff;border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="wrap">
    <div class="section-head" style="display:flex;align-items:flex-end;justify-content:space-between;gap:24px;max-width:none;flex-wrap:wrap">
      <div style="max-width:700px">
        <div class="eyebrow">Selected molecules</div>
        <h2 class="section-title">The peptides buyers ask for first.</h2>
        <p class="section-sub">Every size of a molecule lives on one page, so you can compare packs without chasing duplicate listings.</p>
      </div>
      <a class="text-link" href="/products/">View all {len(PRODUCTS)} products {icon("arrow", "arrow")}</a>
    </div>
    <div class="product-grid">{featured_cards}</div>
  </div>
</section>

<section class="section dark-band" id="quality">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">Quality control</div>
      <h2 class="section-title">The specification is the product.</h2>
      <p class="section-sub">Every lot is released against a written specification. Request the current COA, MS spectrum and SDS before you commit — we would rather answer a technical question than replace a batch.</p>
    </div>
    <div class="qc-grid">
      <div class="qc-item"><div class="qc-num">≥99<small>%</small></div><div class="qc-label">HPLC purity</div><p>RP-HPLC area purity at 214/220 nm, reported per batch.</p></div>
      <div class="qc-item"><div class="qc-num">±1<small> Da</small></div><div class="qc-label">MS identity</div><p>ESI-MS confirms the expected molecular ion for each sequence.</p></div>
      <div class="qc-item"><div class="qc-num">≤5<small>%</small></div><div class="qc-label">Water content</div><p>Karl Fischer control protects fill weight and long-term stability.</p></div>
      <div class="qc-item"><div class="qc-num">100<small>%</small></div><div class="qc-label">Batch COA</div><p>No lot leaves without a batch-specific certificate and SDS.</p></div>
    </div>
    <div class="table-wrap">
      <table class="data-table">
        <thead><tr><th>Test</th><th>Method</th><th>Typical specification</th><th>Reported on COA</th></tr></thead>
        <tbody>
          <tr><td><strong>Appearance</strong></td><td>Visual</td><td>White / off-white; blue for Cu peptides</td><td>Yes</td></tr>
          <tr><td><strong>Purity</strong></td><td>RP-HPLC, 214/220 nm</td><td>≥99% area</td><td>Yes</td></tr>
          <tr><td><strong>Identity</strong></td><td>ESI-MS</td><td>Matches calculated mass</td><td>Yes</td></tr>
          <tr><td><strong>Water content</strong></td><td>Karl Fischer</td><td>≤5%</td><td>Yes</td></tr>
          <tr><td><strong>Counter-ion</strong></td><td>Ion chromatography / titration</td><td>Acetate or TFA, reported</td><td>Yes</td></tr>
          <tr><td><strong>Heavy metals</strong></td><td>ICP-MS</td><td>≤10 ppm</td><td>On request</td></tr>
          <tr><td><strong>Microbial limits</strong></td><td>USP &lt;61&gt; / &lt;62&gt;</td><td>Specification on request</td><td>On request</td></tr>
          <tr><td><strong>Endotoxin</strong></td><td>LAL</td><td>Specification on request</td><td>On request</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small" style="color:#a9c6cc;margin-top:14px">Methods and limits are adapted by product format. Bulk powders such as NAD+, NMN and glutathione follow the same release philosophy with format-appropriate assays. <a href="/synthesis-stability" style="color:#7fe0d9;font-weight:700">Read the synthesis &amp; stability file →</a></p>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="split-media">{molecule_svg()}</div>
    <div class="split-copy">
      <div class="section-head">
        <div class="eyebrow">Why Vivalr</div>
        <h2 class="section-title">Built around the way research buyers actually purchase.</h2>
        <p class="section-sub">Not a marketplace listing. A documentation-first supplier with a named contact, a written spec and a dispatch date.</p>
      </div>
      <ul class="check-list">
        <li><strong>One page per molecule.</strong> Every pack size is aggregated on a single technical page, with SKUs and a variant selector.</li>
        <li><strong>Documentation before dispatch.</strong> COA, MS spectrum and SDS travel with the batch; third-party testing is available on request.</li>
        <li><strong>Low minimums, scalable supply.</strong> Start with one 10-vial kit; scale to 100+ kits with the same specification and lot traceability.</li>
        <li><strong>English-language technical support.</strong> A real person answers specification, compatibility and shipping questions — usually within 12 business hours.</li>
      </ul>
      <div class="product-actions"><a class="btn btn-dark" href="/about">How we work {icon("arrow", "arrow")}</a></div>
    </div>
  </div>
</section>

<section class="section tight" style="background:#fff;border-top:1px solid var(--line)">
  <div class="wrap">
    <div class="section-head center">
      <div class="eyebrow center">From enquiry to delivery</div>
      <h2 class="section-title">A short, predictable purchasing path.</h2>
    </div>
    <div class="process">
      <div class="step"><div class="step-num">01</div><h3>Send your specification</h3><p>Molecule, pack size, quantity and destination country. A target COA or application note helps us quote precisely.</p></div>
      <div class="step"><div class="step-num">02</div><h3>Receive quote + COA</h3><p>We reply within 12 business hours with pricing, current batch data, lead time and shipping options.</p></div>
      <div class="step"><div class="step-num">03</div><h3>Approve and pay</h3><p>Proforma invoice by bank transfer, T/T or Wise. Production or allocation is confirmed on receipt.</p></div>
      <div class="step"><div class="step-num">04</div><h3>Dispatch and track</h3><p>Stock items leave in 2–3 business days. Cold-chain packing and tracking are confirmed before pickup.</p></div>
    </div>
  </div>
</section>

{faq_block(faqs, heading="Questions buyers ask before the first order", eyebrow="B2B buyer FAQ", intro="Direct answers on use restrictions, documentation, minimums and shipping. If your question is not here, WhatsApp us — a technical reply is usually faster than a form.")}

{cta_band()}
'''

    schema = [
        org_node(),
        website_node(),
        {
            "@type": "WebPage",
            "@id": SITE + "/#webpage",
            "url": SITE + "/",
            "name": "Research Peptides & NAD+ Bulk Supplier | Vivalr",
            "description": clamp_desc("Bulk research peptides and NAD+ precursors from Jinan, China. ≥99% HPLC, MS verified, COA per batch, low MOQ, worldwide shipping. Request a quote."),
            "isPartOf": {"@id": SITE + "/#website"},
            "about": {"@id": SITE + "/#organization"},
            "primaryImageOfPage": SITE + "/assets/img/og/home.png",
            "inLanguage": "en",
        },
        faq_schema(faqs, SITE + "/#faq"),
    ]
    title = "Research Peptides & NAD+ Bulk Supplier | Vivalr"
    desc = "Bulk research peptides and NAD+ precursors from Jinan, China. ≥99% HPLC, MS verified, COA per batch, low MOQ, worldwide shipping. Request a quote."
    html = page(title, desc, "/", body, schema, active="home", og_image="/assets/img/og/home.png")
    write("index.html", html)


# ---------------------------------------------------------------------------
# PRODUCTS INDEX
# ---------------------------------------------------------------------------
def build_products_index():
    cards = "".join(product_card(p) for p in PRODUCTS)
    counts = {k: sum(1 for p in PRODUCTS if p["cat"] == k) for k in CATEGORIES}
    filters = '<button class="filter-btn" data-filter="all" aria-pressed="true">All <span style="opacity:.6">%d</span></button>' % len(PRODUCTS)
    for key, cat in CATEGORIES.items():
        filters += '<button class="filter-btn" data-filter="%s" aria-pressed="false">%s <span style="opacity:.6">%d</span></button>' % (key, e(cat["short"]), counts[key])

    body = f'''<section class="page-hero">
  <div class="wrap">
    {breadcrumb([("Home", "/"), ("Products", None)])}
    <h1>Bulk research peptides, organised by what you are formulating.</h1>
    <p>{len(PRODUCTS)} molecules across cosmetic and anti-aging actives, tissue-repair and bioregulator peptides, GLOW/KLOW blends, and NAD+/NMN raw materials. Every size of a molecule is aggregated on one page, with SKUs, MOQ and a batch COA.</p>
  </div>
</section>

<section class="section tight">
  <div class="wrap">
    <div class="catalog-toolbar">
      <div class="filter-group" role="group" aria-label="Filter by research direction">{filters}</div>
      <div class="search-box">{icon("search")}<input id="catalog-search" type="search" placeholder="Search name, CAS or application…" aria-label="Search products"></div>
      <div class="catalog-count" id="catalog-count"><b>{len(PRODUCTS)}</b> of {len(PRODUCTS)} products</div>
    </div>
    <div class="product-grid catalog-grid" id="catalog-grid">{cards}</div>
    <div class="empty-state" id="catalog-empty">
      <h3 style="font-size:18px;color:var(--ink);margin-bottom:6px">No molecules match that filter.</h3>
      <p style="font-size:13px">Try a different keyword, or <a href="/contact#rfq">send us the CAS number</a> — we source beyond the catalogue.</p>
    </div>
    <div class="callout" style="margin-top:26px">{icon("info")}<div><strong>Every product is for laboratory research and formulation evaluation only.</strong> Not for human or veterinary use. Bulk pricing is quoted per specification, pack size and destination; list prices are not published.</div></div>
  </div>
</section>

<section class="section tight" style="background:#fff;border-top:1px solid var(--line)">
  <div class="wrap">
    <div class="section-head center" style="margin-bottom:24px">
      <div class="eyebrow center">Sourcing beyond the catalogue</div>
      <h2 class="section-title">Need a molecule that is not listed?</h2>
      <p class="section-sub">Send the name, CAS number or sequence. We will confirm availability, counter-ion options, minimum batch size and documentation.</p>
    </div>
    <div style="display:flex;justify-content:center;gap:10px;flex-wrap:wrap">
      <a class="btn btn-primary" href="/contact#rfq">Send a sourcing request {icon("arrow", "arrow")}</a>
      <a class="btn btn-ghost" href="{WHATSAPP}?text={WA_TEXT}" target="_blank" rel="noopener">{icon("whatsapp")} WhatsApp</a>
    </div>
  </div>
</section>

{cta_band("Ready to compare specifications?", "Tell us the molecule and pack size. We will send the current COA, MS data and a quote — usually within 12 business hours.")}
'''

    schema = [
        {
            "@type": "CollectionPage",
            "@id": SITE + "/products/#webpage",
            "url": SITE + "/products/",
            "name": "Research Peptide Catalog — Bulk Supplier | Vivalr",
            "description": clamp_desc("Browse 34 bulk research peptides: GHK-Cu, AHK-Cu, Snap-8, Matrixyl, BPC-157, TB-500, GLOW, KLOW, Epithalon, Pinealon, NAD+ and NMN."),
            "isPartOf": {"@id": SITE + "/#website"},
            "inLanguage": "en",
        },
        {
            "@type": "ItemList",
            "@id": SITE + "/products/#list",
            "name": "Vivalr research peptide catalogue",
            "numberOfItems": len(PRODUCTS),
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "url": p["url"], "name": p["full_name"]}
                for i, p in enumerate(PRODUCTS)
            ],
        },
        breadcrumb_schema([("Home", "/"), ("Products", "/products/")]),
    ]
    title = "Research Peptide Catalog — Bulk Supplier | Vivalr"
    desc = "Browse 34 bulk research peptides: GHK-Cu, AHK-Cu, Snap-8, Matrixyl, BPC-157, TB-500, GLOW, KLOW, Epithalon, Pinealon, NAD+ and NMN."
    write("products/index.html", page(title, desc, "/products/", body, schema, active="products",
                                     og_image="/assets/img/og/products.png", keywords="bulk research peptides, peptide catalog, cosmetic peptides, BPC-157, GHK-Cu, NAD+, NMN"))


# ---------------------------------------------------------------------------
# PRODUCT PAGE
# ---------------------------------------------------------------------------
def faq_details(faqs):
    items = "".join(
        '<details class="faq-item"%s><summary><span>%s</span><span class="faq-icon" aria-hidden="true"></span></summary>'
        '<div class="faq-a"><p>%s</p></div></details>' % (" open" if i == 0 else "", e(q), e(a))
        for i, (q, a) in enumerate(faqs)
    )
    return '<div class="faq">' + items + '</div>'


def build_product(p):
    faqs = all_faqs(p)
    v0 = p["variants"][0]
    unit = "pack" if p["slug"] == "nmn" else "kit"
    unit_plural = "packs" if unit == "pack" else "kits"
    quote0 = quote_text(p, v0, 1, unit)
    wa0 = WHATSAPP + "?text=" + quote(quote0)
    mail0 = ("mailto:" + EMAIL + "?subject=" + quote("Quote request — " + p["name"] + " — " + v0["label"]) +
             "&body=" + quote(quote0))

    options = ""
    for i, v in enumerate(p["variants"]):
        short = v["label"].split(" ×")[0]
        if p["cat"] == "blend":
            short = v["label"].split(" mg")[0] + " mg blend"
        options += ('<option value="%s" data-label="%s" data-sku="%s" data-short="%s"%s>%s — %s</option>'
                    % (e(v["sku"]), e(v["label"]), e(v["sku"]), e(short),
                       " selected" if i == 0 else "", e(v["label"]), e(v["sku"])))

    spec_rows = "".join(
        '<tr><td><strong>%s</strong></td><td class="mono">%s</td><td>%s</td><td>%s</td><td>Quote</td></tr>'
        % (e(v["label"]), e(v["sku"]),
           "10 vials / kit" if "× 10 vials" in v["label"] else "Bulk container",
           e(p["moq"]))
        for v in p["variants"]
    )

    research_cards = "".join(
        '<div class="research-item"><h3>%s</h3><p>%s</p></div>' % (e(t), e(d))
        for t, d in p["research"]
    )
    risk_rows = "".join(
        '<div class="risk-row"><dt>%s <span class="severity sev-%s">%s</span></dt><dd>%s</dd></div>'
        % (e(name), e(sev), e(sev), e(detail))
        for name, sev, detail in p["risks"]
    )
    apps = "".join('<span class="chip">%s</span>' % e(a) for a in p["applications"])
    related = "".join(
        f'''<a class="related-card" href="/products/{r}">
  <span class="rc-cat">{e(BY_SLUG[r]["cat_short"])}</span>
  <strong>{e(BY_SLUG[r]["name"])}</strong>
  <span>View spec {icon("arrow", "arrow")}</span>
</a>''' for r in p["related"] if r in BY_SLUG
    )

    glance = (f'{p["name"]} is supplied by Vivalr ({COMPANY}) as a {p["purity"]} {p["form"].lower()} '
              f'in {p["spec_summary"]} packs, CAS {p["cas"]}. Each batch ships with a certificate of analysis '
              f'and MS identity data. MOQ: {p["moq"]}; worldwide express shipping from Jinan, China.')

    if p["cat"] == "blend":
        glance = (f'{p["name"]} is a fixed-ratio research blend supplied by Vivalr ({COMPANY}): '
                  f'{p["seq"]}. It is prepared from independently synthesized and purified components and '
                  f'ships with a component-level COA and MS data. MOQ: {p["moq"]}.')

    synthetic = p["cat"] != "nad" and p["slug"] not in ("glutathione", "thymalin")
    synthesis_label = "SPPS route & purification" if synthetic else "Production route & purification"

    body = f'''<section class="product-hero">
  <div class="wrap">
    {breadcrumb([("Home", "/"), ("Products", "/products/"), (p["name"], None)])}
    <div class="product-hero-grid">
      {product_visual_label(p)}
      <div class="product-intro">
        <div class="eyebrow">{e(p["cat_label"])}</div>
        <h1>{e(p["full_name"])}</h1>
        <p class="product-sub">{e(p["tagline"])}</p>
        <div class="badge-row">
          <span class="badge teal">{icon("check")} {e(p["purity"])}</span>
          <span class="badge">{icon("flask")} MS verified</span>
          <span class="badge">{icon("file")} COA per batch</span>
          <span class="badge warn">Research use only</span>
        </div>
        <div class="product-actions">
          <a class="btn btn-primary" href="#quote">Request a quote {icon("arrow", "arrow")}</a>
          <a class="btn btn-ghost" href="#synthesis">Synthesis &amp; stability</a>
        </div>
        <div class="product-meta">
          <div>CAS number<b class="mono">{e(p["cas"])}</b></div>
          <div>Form<b>{e(p["form"])}</b></div>
          <div>MOQ<b>{e(p["moq"])}</b></div>
        </div>
      </div>
    </div>
    {summary_card(p)}
  </div>
</section>

<section class="wrap">
  <div class="product-layout">
    <div class="product-main">
      <div class="at-a-glance"><div class="label">At a glance · quotable summary</div><p>{e(glance)}</p></div>
      <div class="prose">
        <h2 id="overview">Research overview</h2>
        {''.join('<p>' + e(x) + '</p>' for x in p["overview"])}

        <h2 id="research">Research focus</h2>
        <p>Published work on {e(p["name"])} spans several complementary lines of investigation. The summaries below describe research areas, not therapeutic claims or recommended uses.</p>
        <div class="research-grid">{research_cards}</div>

        <h2 id="synthesis">Synthesis &amp; Stability Profile</h2>
        <p>This section summarises the production route, the analytical release criteria and the degradation risks that matter when handling {e(p["name"])} in the laboratory or in formulation.</p>
        <div class="tech-panel">
          <div class="tech-panel-head"><h3>{e(synthesis_label)}</h3><span>Batch-released</span></div>
          <div class="tech-panel-body"><p>{e(p["synthesis"])}</p></div>
        </div>
        <h3>Degradation risks &amp; mitigation</h3>
        <dl class="risk-list">{risk_rows}</dl>
        <h3>Recommended storage &amp; handling</h3>
        <div class="table-wrap">
          <table class="data-table">
            <thead><tr><th>Condition</th><th>Typical guidance</th><th>Notes</th></tr></thead>
            <tbody>
              <tr><td><strong>Sealed powder, -20 °C</strong></td><td>{e(p["shelf"])}</td><td>Desiccated, protected from light. Retest after the stated period.</td></tr>
              <tr><td><strong>Short-term, 2–8 °C</strong></td><td>Up to 6 months</td><td>Use for bench aliquots; avoid repeated warming.</td></tr>
              <tr><td><strong>Ambient, 25 °C</strong></td><td>Up to 4 weeks</td><td>Transit only. Not a long-term storage condition.</td></tr>
              <tr><td><strong>Reconstituted (lab)</strong></td><td>7 days at 2–8 °C</td><td>Filter sterilise, aliquot and avoid repeated freeze–thaw.</td></tr>
              <tr><td><strong>Express shipping</strong></td><td>3–7 business days</td><td>Insulated pack with gel packs where required by destination or season.</td></tr>
            </tbody>
          </table>
        </div>
        <p class="small muted" style="margin-top:10px">Typical handling guidance for research material, not a batch-specific stability study. Formal stability protocols and data packages can be provided under NDA.</p>
        <p>{e(p["handling"])}</p>

        <h2 id="specifications">Specifications &amp; pack sizes</h2>
        <div class="table-wrap">
          <table class="data-table">
            <thead><tr><th>Pack size</th><th>SKU</th><th>Format</th><th>MOQ</th><th>Price</th></tr></thead>
            <tbody>{spec_rows}</tbody>
          </table>
        </div>
        <p class="small muted" style="margin-top:10px">Custom fill weights, salt forms, labelling and kit assembly are available from 10 kits. Prices are quote-based and depend on pack size, destination and documentation requirements.</p>

        <h2 id="qc">Quality control &amp; documentation</h2>
        <p>Each batch is released against the specification below. The COA reports the actual measured values for the lot, not catalogue targets. Third-party HPLC/MS testing and custom analytical panels can be arranged before shipment.</p>
        <div class="table-wrap">
          <table class="data-table">
            <thead><tr><th>Test</th><th>Method</th><th>Specification</th></tr></thead>
            <tbody>
              <tr><td><strong>Appearance</strong></td><td>Visual</td><td>{e(p["appearance"])}</td></tr>
              <tr><td><strong>Purity</strong></td><td>RP-HPLC, 214/220 nm</td><td>{e(p["purity"])}</td></tr>
              <tr><td><strong>Identity</strong></td><td>ESI-MS</td><td>Matches calculated mass</td></tr>
              <tr><td><strong>Water content</strong></td><td>Karl Fischer</td><td>≤5% (typical)</td></tr>
              <tr><td><strong>Counter-ion</strong></td><td>Ion chromatography / titration</td><td>Reported per batch</td></tr>
              <tr><td><strong>Heavy metals</strong></td><td>ICP-MS</td><td>≤10 ppm (on request)</td></tr>
            </tbody>
          </table>
        </div>

        <h2 id="formulation">Formulation &amp; handling notes</h2>
        <p>{e(p["formulation"])}</p>
        <div class="callout">{icon("snow")}<div><strong>Handling summary.</strong> {e(p["handling"])}</div></div>

        <h2 id="applications">Research applications</h2>
        <div class="spec-chips" style="gap:6px">{apps}</div>
        <p class="small muted" style="margin-top:10px">Application labels describe research areas only. They are not claims of efficacy, safety or regulatory approval.</p>

        <h2 id="faq">Frequently asked questions</h2>
        {faq_details(faqs)}
      </div>

      <div style="margin-top:38px">
        <h2 style="font-size:1.4rem;letter-spacing:-.02em;margin-bottom:6px">Related molecules</h2>
        <p class="small muted" style="margin:0">Compare specifications across adjacent research directions.</p>
        <div class="related-grid">{related}</div>
      </div>

      {disclaimer()}
      {cite_box(p["full_name"] + " — Bulk Research Supplier", p["path"])}
    </div>

    <aside class="product-aside" data-quote-root data-product-name="{e(p["full_name"])}" data-product-short="{e(p["name"])}" data-unit="{unit}">
      <div class="inquiry-card" id="quote">
        <div class="inquiry-head">
          <div class="eyebrow">Quick inquiry</div>
          <h2>Request a quote</h2>
          <p>Current COA + MS + bulk pricing</p>
        </div>
        <div class="inquiry-body">
          <div class="field">
            <label for="variant-select">Pack size</label>
            <select id="variant-select">{options}</select>
          </div>
          <div class="variant-meta"><span>SKU <b id="selected-sku">{e(v0["sku"])}</b></span><span>{e(p["purity"])}</span></div>
          <div class="field">
            <label for="qty">Quantity ({unit_plural})</label>
            <div class="qty">
              <button type="button" data-step="-1" aria-label="Decrease quantity">−</button>
              <input id="qty" type="number" min="1" max="999" step="1" value="1" inputmode="numeric" aria-label="Quantity in kits">
              <button type="button" data-step="1" aria-label="Increase quantity">+</button>
            </div>
          </div>
          <div class="quote-preview" id="quote-preview"><strong>{e(p["name"])}</strong> · {e(v0["label"])}<br>1 {unit} · batch COA &amp; MS included</div>
          <div class="quote-actions">
            <a class="btn btn-wa" id="wa-quote" href="{e(wa0)}" target="_blank" rel="noopener">{icon("whatsapp")} Send on WhatsApp</a>
            <a class="btn btn-dark" id="email-quote" href="{e(mail0)}">{icon("mail")} Email the inquiry</a>
            <button class="btn btn-ghost" id="copy-quote" type="button">{icon("copy")} Copy inquiry summary</button>
          </div>
          <div class="copy-status" id="copy-status" role="status" aria-live="polite"></div>
          <p class="quote-note">{icon("lock")}<span>Opens WhatsApp or your email app with the product and pack size prefilled. No form data is stored on this site.</span></p>
        </div>
        <div class="inquiry-foot"><span>{icon("clock")} Reply within 12 business hours</span><a href="mailto:{EMAIL}">{EMAIL}</a></div>
      </div>
    </aside>
  </div>
</section>

{cta_band("Need a different pack size or a custom blend?", "We support custom fill weights, salt forms, labelling and kit assembly from 10 kits. Send the specification and destination for a feasibility quote.")}
'''

    schema = [
        {
            "@type": "Product",
            "@id": p["url"] + "#product",
            "name": p["full_name"],
            "sku": v0["sku"],
            "mpn": v0["sku"],
            "description": p["intro"],
            "image": [p["og_image"]],
            "url": p["url"],
            "brand": {"@type": "Brand", "name": BRAND},
            "category": p["cat_label"],
            "audience": {
                "@type": "BusinessAudience",
                "audienceType": "Research laboratories, cosmetic formulators and ingredient buyers",
            },
            "countryOfOrigin": "CN",
            "additionalProperty": [
                {"@type": "PropertyValue", "name": "CAS Number", "value": p["cas"]},
                {"@type": "PropertyValue", "name": "Sequence / Formula / MW", "value": p["seq_mw"]},
                {"@type": "PropertyValue", "name": "Purity", "value": p["purity"]},
                {"@type": "PropertyValue", "name": "Form", "value": p["form"]},
                {"@type": "PropertyValue", "name": "Storage", "value": p["storage"]},
                {"@type": "PropertyValue", "name": "Available pack sizes", "value": p["spec_summary"]},
                {"@type": "PropertyValue", "name": "MOQ", "value": p["moq"]},
                {"@type": "PropertyValue", "name": "Supplier", "value": COMPANY},
            ],
            "offers": {
                "@type": "Offer",
                "url": p["url"],
                "availability": "https://schema.org/InStock",
                "seller": {
                    "@type": "Organization",
                    "name": COMPANY,
                    "url": SITE + "/",
                    "email": EMAIL,
                    "telephone": PHONE_TEL,
                },
                "areaServed": "Worldwide",
                "businessFunction": "http://purl.org/goodrelations/v1#Sell",
                "description": "Bulk pricing is quoted per specification, pack size and destination.",
            },
            "isRelatedTo": [{"@type": "Product", "name": BY_SLUG[r]["full_name"], "url": BY_SLUG[r]["url"]}
                            for r in p["related"] if r in BY_SLUG],
        },
        faq_schema(faqs, p["url"] + "#faq"),
        breadcrumb_schema([("Home", "/"), ("Products", "/products/"), (p["name"], p["path"])]),
    ]

    write("products/" + p["slug"] + ".html",
          page(product_title(p), p["meta_desc"], p["path"], body, schema,
               active="products", og_type="product", og_image="/assets/img/og/" + p["slug"] + ".png",
               keywords=", ".join([p["name"], p["full_name"], "CAS " + p["cas"]] + p["tags"] + ["bulk supplier", "research peptide"])))


def build_products():
    for p in PRODUCTS:
        build_product(p)


# ---------------------------------------------------------------------------
# SYNTHESIS & STABILITY
# ---------------------------------------------------------------------------
SYNTH_FAQS = [
    ("What does ≥99% HPLC purity actually mean?",
     "It means the target peptide accounts for at least 99% of the UV-absorbing area in the release chromatogram, excluding counter-ion and water. The COA also reports the actual retention time, column method and integrated purity for the batch."),
    ("Can I review a batch-specific COA before ordering?",
     "Yes. Send the product and pack size and we will share the current lot's COA, MS spectrum and SDS. If you need a specific specification or third-party laboratory, tell us before the order is confirmed."),
    ("Do you perform third-party testing?",
     "Yes, on request and at the buyer's cost. Common third-party panels include HPLC purity, ESI-MS identity, water content, heavy metals, microbial limits and endotoxin. We can also send samples to a laboratory you nominate."),
    ("How do you control the cold chain?",
     "Lyophilized peptides are packed with desiccant in sealed vials, then insulated with gel packs when the destination or season requires it. We use express carriers with tracking and share the dispatch photos and tracking number."),
    ("Can you customise salt form, fill weight or labelling?",
     "Yes. Acetate, TFA, arginine and other counter-ion forms can be quoted, along with custom fill weights, vial sizes, labels and kit assembly. Custom work typically starts at 10 kits, subject to technical review."),
    ("Why does a batch sometimes differ slightly in colour?",
     "Colour can vary with moisture, pH and — for copper peptides — the state of the Cu(II) complex. Colour alone is not a purity measure. Release decisions are based on HPLC, MS and the specified tests, not visual shade."),
]


def build_synthesis():
    body = f'''<section class="page-hero">
  <div class="wrap">
    {breadcrumb([("Home", "/"), ("Synthesis & Stability", None)])}
    <h1>Peptide synthesis, purification and stability — the technical file.</h1>
    <p>How Vivalr peptides are made, what ≥99% HPLC means in practice, and how to store, formulate and ship them without losing the specification you paid for.</p>
  </div>
</section>

<section class="section tight">
  <div class="wrap">
    <div class="anchor-list" aria-label="On this page">
      <a href="#route">Synthesis route</a><a href="#purity">Purity &amp; identity</a><a href="#stress">Stress stability</a>
      <a href="#compatibility">Formulation compatibility</a><a href="#shipping">Storage &amp; shipping</a><a href="#documents">Documentation</a><a href="#faq">FAQ</a>
    </div>

    <div class="prose" style="max-width:860px">
      <h2 id="route">The synthesis route: Fmoc SPPS, then purification</h2>
      <p>Most of the peptides in the catalogue are produced by Fmoc solid-phase peptide synthesis (SPPS). The sequence is assembled on a resin support, one protected amino acid at a time, then cleaved and purified. The exceptions are the biological complex Thymalin, fermentation-derived glutathione and the small molecules NAD+, NMN, AICAR and 5-Amino-1MQ, which follow separate production routes.</p>
      <div class="process" style="margin:22px 0 26px">
        <div class="step"><div class="step-num">01</div><h3>Resin &amp; coupling</h3><p>Fmoc-amino acids are coupled with HBTU/HATU or DIC/Oxyma. Each coupling and deprotection step is monitored to limit deletions.</p></div>
        <div class="step"><div class="step-num">02</div><h3>Cleavage</h3><p>TFA/TIS/water cleavage releases the peptide and removes side-chain protecting groups. The crude peptide is precipitated in cold ether.</p></div>
        <div class="step"><div class="step-num">03</div><h3>Purification</h3><p>Preparative C18 HPLC removes deletion, truncation and oxidation impurities. Fractions are pooled only when they meet the purity window.</p></div>
        <div class="step"><div class="step-num">04</div><h3>Salt &amp; drying</h3><p>Ion exchange sets the counter-ion (usually acetate), and controlled lyophilization gives a stable, low-moisture powder.</p></div>
      </div>
      <p>For copper peptides such as GHK-Cu and AHK-Cu, the purified tripeptide is complexed with copper(II) acetate under controlled pH, then isolated and lyophilized. Copper content is verified by ICP-OES and reported alongside peptide purity. This is a separate process step from peptide synthesis and is a common source of batch-to-batch variation in the market.</p>

      <h2 id="purity">Purity and identity: what the numbers mean</h2>
      <p>“≥99%” is a release specification, not a marketing phrase. The number is generated by reverse-phase HPLC, usually at 214 or 220 nm, and is reported as area percentage against the total integrated peak area. It says nothing on its own about counter-ion, water content or peptide content by mass — which is why the COA reports those separately.</p>
      <div class="table-wrap">
        <table class="data-table">
          <thead><tr><th>Measurement</th><th>Method</th><th>Why it matters</th></tr></thead>
          <tbody>
            <tr><td><strong>Purity</strong></td><td>RP-HPLC, 214/220 nm</td><td>Detects deletion, truncation and many oxidation products; the primary release criterion.</td></tr>
            <tr><td><strong>Identity</strong></td><td>ESI-MS</td><td>Confirms the molecular ion matches the intended sequence; a purity peak can still be the wrong peptide.</td></tr>
            <tr><td><strong>Water content</strong></td><td>Karl Fischer</td><td>Affects fill weight, stability and the accuracy of mass-based dosing in formulation.</td></tr>
            <tr><td><strong>Counter-ion</strong></td><td>Ion chromatography / titration</td><td>Acetate and TFA have different mass and pH effects; the salt form must be known.</td></tr>
            <tr><td><strong>Peptide content</strong></td><td>Nitrogen / amino-acid analysis</td><td>Converts gross powder weight into actual peptide mass for accurate formulation.</td></tr>
          </tbody>
        </table>
      </div>
      <div class="callout">{icon("info")}<div><strong>A 99% HPLC result does not mean 99% peptide by mass.</strong> Water, counter-ion and residual salts are part of the powder. For formulation work, use the peptide-content value on the COA, not the vial fill weight, when calculating active concentration.</div></div>

      <h2 id="stress">Stress stability: what degrades, and how fast</h2>
      <p>The table below summarises the degradation behaviour we design around across the catalogue. It is a handling framework, not a substitute for a formal stability study on your specific batch and matrix.</p>
      <div class="table-wrap">
        <table class="data-table">
          <thead><tr><th>Condition</th><th>Typical observation</th><th>Recommended handling</th></tr></thead>
          <tbody>
            <tr><td><strong>Sealed powder, -20 °C</strong></td><td>No significant change over 24 months for most lyophilized peptides</td><td>Desiccant, dark, airtight; retest after the stated period.</td></tr>
            <tr><td><strong>2–8 °C</strong></td><td>Stable short term; moisture ingress is the main risk</td><td>Use for bench aliquots, not multi-year storage.</td></tr>
            <tr><td><strong>25 °C / ambient</strong></td><td>Gradual hydrolysis and oxidation; colour shift in Cu peptides</td><td>Limit to transit and short experiments; avoid repeat warming.</td></tr>
            <tr><td><strong>40 °C / 75% RH</strong></td><td>Moisture uptake, aggregation and measurable purity loss</td><td>Not a storage condition; use only as an accelerated stress test.</td></tr>
            <tr><td><strong>Light</strong></td><td>Oxidation of Met, Trp and Cys; discolouration</td><td>Amber glass, opaque secondary packaging.</td></tr>
            <tr><td><strong>pH &lt;3 or &gt;9</strong></td><td>Hydrolysis, deamidation and salt-form shifts</td><td>Formulate at pH 4–7 unless the molecule-specific note says otherwise.</td></tr>
            <tr><td><strong>Reconstituted solution</strong></td><td>Hydrolysis and microbial growth</td><td>2–8 °C for up to 7 days; aliquot and freeze at -20 °C for longer work.</td></tr>
            <tr><td><strong>Repeated freeze–thaw</strong></td><td>Aggregation, especially for large peptides</td><td>Single-use aliquots; avoid foaming and high shear.</td></tr>
          </tbody>
        </table>
      </div>

      <h2 id="compatibility">Formulation compatibility matrix</h2>
      <p>Compatibility depends on the full formula, not just the peptide. The guidance below flags the interactions that most often cause a formulation to fail during scale-up.</p>
      <div class="table-wrap">
        <table class="data-table">
          <thead><tr><th>System or excipient</th><th>Watch-out</th><th>Practical guidance</th></tr></thead>
          <tbody>
            <tr><td><strong>Copper peptides + ascorbic acid</strong></td><td>Redox cycling, colour change, complex destabilisation</td><td>Separate phases or use a non-reducing vitamin C derivative; validate colour over 4 weeks.</td></tr>
            <tr><td><strong>Copper peptides + EDTA / chelators</strong></td><td>Copper stripping and loss of the complex</td><td>Keep chelators out of the same phase; check the full INCI list.</td></tr>
            <tr><td><strong>Anionic emulsifiers / surfactants</strong></td><td>Electrostatic interaction, haze or precipitation</td><td>Pre-test the specific surfactant pair at the intended use level.</td></tr>
            <tr><td><strong>High shear / homogenisation</strong></td><td>Foaming and aggregation of large peptides</td><td>Add at low shear and cool-down; avoid over-mixing.</td></tr>
            <tr><td><strong>Phenoxyethanol / common preservatives</strong></td><td>Generally compatible, but pH-dependent</td><td>Confirm at the final pH and run a challenge test on the finished base.</td></tr>
            <tr><td><strong>Ethanol / glycols</strong></td><td>Solubility limits for large or lipophilic peptides</td><td>Screen solubility before selecting the vehicle; avoid abrupt solvent shifts.</td></tr>
          </tbody>
        </table>
      </div>

      <h2 id="shipping">Storage and shipping, by format</h2>
      <div class="table-wrap">
        <table class="data-table">
          <thead><tr><th>Format</th><th>Storage</th><th>Shipping</th></tr></thead>
          <tbody>
            <tr><td><strong>Lyophilized peptide vials</strong></td><td>-20 °C, desiccated, dark</td><td>Insulated pack; gel packs when required by route or season.</td></tr>
            <tr><td><strong>Bulk peptide powder</strong></td><td>-20 °C under dry, dark conditions</td><td>Sealed double container with desiccant; express courier.</td></tr>
            <tr><td><strong>NAD+ / NMN / AICAR</strong></td><td>-20 °C, desiccated, dark; minimise open time</td><td>Moisture-barrier bag; avoid prolonged transit heat.</td></tr>
            <tr><td><strong>Glutathione</strong></td><td>-20 °C under inert gas if possible</td><td>Opaque, moisture-barrier packaging; avoid metal contact.</td></tr>
          </tbody>
        </table>
      </div>
      <p>Shipments are sent by DHL, FedEx or UPS express with tracking. For destinations with complex customs requirements we prepare the commercial invoice, packing list, COA and SDS before dispatch. Buyers are responsible for import permits and local regulatory compliance.</p>

      <h2 id="documents">The documentation pack</h2>
      <div class="feature-grid" style="margin:20px 0 8px">
        <div class="feature"><div class="feature-icon">{icon("file")}</div><h3>Batch COA</h3><p>Appearance, assay, water, counter-ion and identity for the exact lot.</p></div>
        <div class="feature"><div class="feature-icon">{icon("chart")}</div><h3>HPLC chromatogram</h3><p>Method, retention time and integrated purity.</p></div>
        <div class="feature"><div class="feature-icon">{icon("flask")}</div><h3>MS spectrum</h3><p>ESI-MS with the observed and calculated molecular ion.</p></div>
        <div class="feature"><div class="feature-icon">{icon("shield")}</div><h3>SDS</h3><p>Handling, storage and transport classification.</p></div>
      </div>
      <p>Third-party testing, custom analytical panels, stability protocols and batch reservation can be arranged under NDA. Ask for the current documentation package for the molecule you are evaluating.</p>
    </div>
  </div>
</section>

{faq_block(SYNTH_FAQS, heading="Technical questions, answered directly", eyebrow="Synthesis & QC FAQ", intro="The questions that come up most often in technical due diligence. Ask us for the underlying data rather than taking a summary on trust.")}

{cta_band("Need the technical file for a specific molecule?", "Tell us the product and the specification you need to meet. We will send the COA, MS data, SDS and a stability statement for the current batch.")}
'''

    schema = [
        {
            "@type": "TechArticle",
            "@id": SITE + "/synthesis-stability#article",
            "headline": "Peptide Synthesis, HPLC Purity and Stability — Technical File",
            "description": clamp_desc("How Vivalr peptides are synthesized by Fmoc SPPS, purified to ≥99% by HPLC, verified by MS, and stored and shipped for stability."),
            "url": SITE + "/synthesis-stability",
            "mainEntityOfPage": SITE + "/synthesis-stability",
            "image": SITE + "/assets/img/og/synthesis.png",
            "datePublished": UPDATED,
            "dateModified": UPDATED,
            "inLanguage": "en",
            "author": {"@type": "Organization", "name": COMPANY, "url": SITE + "/"},
            "publisher": {"@type": "Organization", "name": COMPANY, "url": SITE + "/"},
            "about": ["Peptide synthesis", "Solid-phase peptide synthesis", "HPLC purity", "Peptide stability", "Lyophilization"],
        },
        faq_schema(SYNTH_FAQS, SITE + "/synthesis-stability#faq"),
        breadcrumb_schema([("Home", "/"), ("Synthesis & Stability", "/synthesis-stability")]),
    ]
    title = "Peptide Synthesis, HPLC & Stability | Vivalr"
    desc = "How Vivalr peptides are made: Fmoc SPPS, ≥99% HPLC purification, MS identity, stress-stability data and storage/shipping guidance for research buyers."
    write("synthesis-stability.html", page(title, desc, "/synthesis-stability", body, schema,
                                          active="synthesis", og_image="/assets/img/og/synthesis.png",
                                          keywords="peptide synthesis, SPPS, HPLC purity, peptide stability, lyophilization, QC"))
