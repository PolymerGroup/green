# -*- coding: utf-8 -*-
"""Page builders: about, contact, policies, 404, machine-readable files."""
import json
from pathlib import Path

from data import (
    SITE, BRAND, COMPANY, ADDRESS, ADDRESS_SHORT, PHONE, PHONE_TEL, WHATSAPP,
    EMAIL, UPDATED, UPDATED_HUMAN, CATEGORIES, PRODUCTS, BY_SLUG,
)
from ui import e, money, icon, breadcrumb, cta_band, faq_block
from build import (
    write, page, clamp_desc, org_node, breadcrumb_schema, faq_schema, OUT,
)


def build_about():
    body = f'''<section class="page-hero">
  <div class="wrap">
    {breadcrumb([("Home", "/"), ("About", None)])}
    <h1>A Shandong-based supplier built for research buyers.</h1>
    <p>Vivalr is the research-peptide brand of {COMPANY}. Based in Shandong, China, we supply cosmetic actives, repair and bioregulator peptides, fixed-ratio blends, and NAD+/NMN raw materials to laboratories, formulators, and ingredient buyers worldwide.</p>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="split-media">{molecule_visual()}</div>
    <div class="split-copy">
      <div class="section-head">
        <div class="eyebrow">Who we are</div>
        <h2 class="section-title">More than an export trader — a contract manufacturing partner.</h2>
      </div>
      <div class="prose">
        <p>We are not just an export-focused trading company. We are also a contract manufacturer. That distinction matters: we translate your specification into a qualified synthesis and fill-finish batch, verify the documentation, and get it to your laboratory without surprises.</p>
        <p>Our contract manufacturing team is based in Shandong, one of China's established chemical and biotechnology export clusters. We manage synthesis, purification, and lyophilization through a qualified production network, and we release every lot against a written specification before it is offered to a buyer.</p>
        <p>Our listed prices cover standard pack sizes in USD. Final pricing depends on pack size, counter-ion, documentation, and destination, and we confirm every detail in a written quotation before production.</p>
      </div>
      <div class="product-actions"><a class="btn btn-dark" href="/contact#rfq">Talk to our team {icon("arrow", "arrow")}</a></div>
    </div>
  </div>
</section>

<section class="section tight" style="background:#fff;border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="wrap">
    <div class="stat-row">
      <div class="stat-card"><b>{len(PRODUCTS)}</b><span>catalogue molecules</span></div>
      <div class="stat-card"><b>4</b><span>research directions</span></div>
      <div class="stat-card"><b>12 h</b><span>quote response target</span></div>
      <div class="stat-card"><b>3–7 d</b><span>express transit</span></div>
    </div>
    <div class="section-head center" style="margin-bottom:30px">
      <div class="eyebrow center">What we optimise for</div>
      <h2 class="section-title">Three commitments we can actually control.</h2>
    </div>
    <div class="value-grid">
      <div class="value-card"><div class="feature-icon">{icon("file")}</div><h3>Documentation first</h3><p>Every batch is released with a COA, HPLC chromatogram, MS spectrum and SDS. If a number is not on the certificate, ask — we would rather provide the data than defend a claim.</p></div>
      <div class="value-card"><div class="feature-icon">{icon("shield")}</div><h3>Research-use discipline</h3><p>We supply research material only. No dosage guidance, no medical claims, no finished retail products. Buyers receive a clear research-use statement with every order.</p></div>
      <div class="value-card"><div class="feature-icon">{icon("layers")}</div><h3>Low-MOQ access</h3><p>Start with one 10-vial kit and scale to 100+ kits on the same specification. Custom fill, labelling and kit assembly are available from modest minimums.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">Company details</div>
      <h2 class="section-title">The legal entity behind Vivalr.</h2>
      <p class="section-sub">Use these details for purchase orders, supplier onboarding and compliance checks. We are happy to complete your vendor questionnaire.</p>
    </div>
    <dl class="info-list">
      <div class="info-row"><dt>Legal name</dt><dd>{e(COMPANY)}</dd></div>
      <div class="info-row"><dt>Brand</dt><dd>Vivalr — research peptides &amp; coenzymes</dd></div>
      <div class="info-row"><dt>Business type</dt><dd>International trade and sourcing, research-grade chemical and peptide raw materials</dd></div>
      <div class="info-row"><dt>Office address</dt><dd>{e(ADDRESS)}</dd></div>
      <div class="info-row"><dt>Telephone / WhatsApp</dt><dd><a href="tel:{PHONE_TEL}">{PHONE}</a></dd></div>
      <div class="info-row"><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
      <div class="info-row"><dt>Markets</dt><dd>Worldwide — EU, UK, North America, Australia, Southeast Asia and the Middle East</dd></div>
      <div class="info-row"><dt>Minimum order</dt><dd>One 10-vial kit for most peptides; 10 g for bulk NMN</dd></div>
      <div class="info-row"><dt>Documentation</dt><dd>Batch COA, HPLC, ESI-MS, SDS; third-party testing on request</dd></div>
      <div class="info-row"><dt>Shipping</dt><dd>DHL, FedEx and UPS express with tracking</dd></div>
    </dl>
  </div>
</section>

<section class="section tight" style="background:#fff;border-top:1px solid var(--line)">
  <div class="wrap">
    <div class="section-head center">
      <div class="eyebrow center">How we work</div>
      <h2 class="section-title">No black boxes between the quote and the vial.</h2>
      <p class="section-sub">A named contact, a written specification and a dispatch date. That is the operating model.</p>
    </div>
    <div class="process">
      <div class="step"><div class="step-num">01</div><h3>Technical intake</h3><p>We confirm the molecule, counter-ion, pack size, destination and any analytical requirements before quoting.</p></div>
      <div class="step"><div class="step-num">02</div><h3>Written quotation</h3><p>Price, specification, lead time, shipping method and documentation are stated in one document.</p></div>
      <div class="step"><div class="step-num">03</div><h3>Batch release</h3><p>The lot is tested and the COA is reviewed against the agreed specification before packing.</p></div>
      <div class="step"><div class="step-num">04</div><h3>Dispatch &amp; aftercare</h3><p>Tracking, packing photos and documentation are sent. We stay available for technical follow-up.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="callout" style="max-width:860px;margin:0 auto">{icon("info")}<div><strong>Compliance position.</strong> Vivalr supplies raw materials for laboratory research and formulation evaluation only. We do not manufacture, market or sell finished pharmaceutical, cosmetic or veterinary products, and we do not provide medical or dosage advice. Buyers are responsible for ensuring that their use complies with the regulations of their jurisdiction.</div></div>
  </div>
</section>

{cta_band("Need a supplier you can put on a purchase order?", "Send your company details and the specification you need. We will reply with a quotation and the current batch documentation.")}
'''

    schema = [
        {
            "@type": "AboutPage",
            "@id": SITE + "/about#webpage",
            "url": SITE + "/about",
            "name": "About Vivalr — Research Peptide Supplier in Shandong",
            "description": clamp_desc("Vivalr is the research-peptide brand of Shandong Green International Trade Co., Ltd., based in Shandong, China. Contract manufacturing and global export."),
            "isPartOf": {"@id": SITE + "/#website"},
            "mainEntity": org_node(),
            "inLanguage": "en",
        },
        breadcrumb_schema([("Home", "/"), ("About", "/about")]),
    ]
    title = "About Vivalr — Research Peptide Supplier in Shandong"
    desc = "Vivalr is the research-peptide brand of Shandong Green International Trade Co., Ltd., based in Shandong, China. Contract manufacturing and global export."
    write("about.html", page(title, desc, "/about", body, schema, active="about",
                             og_image="/assets/img/og/about.png", keywords="Vivalr, Shandong Green International Trade, Shandong peptide supplier, research peptides"))


def molecule_visual():
    from ui import molecule_svg
    return molecule_svg()


def build_contact():
    body = f'''<section class="page-hero">
  <div class="wrap">
    <div class="eyebrow">Contact us</div>
    <h1>Talk to a person who knows the chemistry.</h1>
    <p>Send the products, pack size and destination. We reply with pricing, COA and lead time — usually within 12 business hours. WhatsApp is fastest for urgent technical questions.</p>
  </div>
</section>

<section class="section tight">
  <div class="wrap contact-grid">
    <div>
      <div class="eyebrow">Direct channels</div>
      <h2 class="section-title" style="font-size:1.7rem;margin-top:12px">Reach us without a ticket queue.</h2>
      <div class="contact-methods">
        <a class="contact-method" href="{WHATSAPP}?text={quote_text()}" target="_blank" rel="noopener">
          <span class="cm-icon">{icon("whatsapp")}</span>
          <div><h3>WhatsApp</h3><p>{PHONE}</p><small>Fastest for quotes and technical questions</small></div>
        </a>
        <a class="contact-method" href="mailto:{EMAIL}?subject=Quotation%20request%20—%20Vivalr">
          <span class="cm-icon">{icon("mail")}</span>
          <div><h3>Email</h3><p>{EMAIL}</p><small>For purchase orders, COAs and vendor forms</small></div>
        </a>
        <a class="contact-method" href="tel:{PHONE_TEL}">
          <span class="cm-icon">{icon("phone")}</span>
          <div><h3>Telephone</h3><p>{PHONE}</p><small>Mon–Sat, 09:00–18:00 UTC+8</small></div>
        </a>
        <div class="contact-method">
          <span class="cm-icon">{icon("pin")}</span>
          <div><h3>Office</h3><p>{e(ADDRESS)}</p><small>Visits by prior appointment</small></div>
        </div>
      </div>

      <div class="callout" style="margin-top:24px">{icon("file")}<div><strong>What to include for a fast quote.</strong> Product name or CAS, pack size, quantity, destination country and any required tests (for example heavy metals or endotoxin). If you need a specific counter-ion or custom fill, say so up front.</div></div>

      <div class="info-list" style="margin-top:8px">
        <div class="info-row"><dt>Quote response</dt><dd>Within 12 business hours, Monday–Saturday</dd></div>
        <div class="info-row"><dt>Sample policy</dt><dd>Paid samples available; freight quoted separately</dd></div>
        <div class="info-row"><dt>Payment</dt><dd>Bank transfer, T/T, Wise; proforma invoice issued first</dd></div>
        <div class="info-row"><dt>Shipping</dt><dd>DHL, FedEx, UPS express with tracking</dd></div>
      </div>
    </div>

    <div class="form-card" id="rfq">
      <h2>Request a quotation</h2>
      <p class="form-sub">This form composes an email or WhatsApp message in your own app. No data is stored on this website.</p>
      <form id="rfq-form" action="mailto:{EMAIL}" method="get">
        <div class="form-row">
          <div class="field"><label for="f-name">Name *</label><input id="f-name" name="name" type="text" autocomplete="name" required placeholder="Dr Jane Smith"></div>
          <div class="field"><label for="f-company">Company / institution</label><input id="f-company" name="company" type="text" autocomplete="organization" placeholder="Lab or brand name"></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="f-email">Email *</label><input id="f-email" name="email" type="email" autocomplete="email" required placeholder="you@company.com"></div>
          <div class="field"><label for="f-country">Country</label><input id="f-country" name="country" type="text" autocomplete="country-name" placeholder="Germany"></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="f-interest">Product / CAS</label><input id="f-interest" name="interest" type="text" placeholder="GHK-Cu, CAS 89030-95-5"></div>
          <div class="field"><label for="f-qty">Estimated quantity</label><input id="f-qty" name="quantity" type="text" placeholder="10 kits / 100 g"></div>
        </div>
        <div class="field"><label for="f-message">Requirements *</label><textarea id="f-message" name="message" required placeholder="Application, target specification, required tests, delivery timeline…"></textarea></div>
        <div class="form-actions">
          <button class="btn btn-dark" type="submit">{icon("mail")} Open email draft</button>
          <button class="btn btn-wa" id="wa-form" type="button">{icon("whatsapp")} Send via WhatsApp</button>
          <button class="btn btn-ghost" id="copy-form" type="button">{icon("copy")} Copy</button>
        </div>
        <div class="form-status" id="form-status" role="status" aria-live="polite"></div>
        <p class="form-note">By sending an inquiry you confirm that you are requesting material for laboratory research or formulation evaluation, not for human or veterinary use. See our <a href="/privacy">privacy policy</a> and <a href="/terms">research-use terms</a>.</p>
      </form>
    </div>
  </div>
</section>

<section class="section tight" style="background:#fff;border-top:1px solid var(--line)">
  <div class="wrap">
    <div class="section-head center" style="margin-bottom:24px">
      <div class="eyebrow center">Before you write</div>
      <h2 class="section-title">Three things that speed up a technical quote.</h2>
    </div>
    <div class="value-grid">
      <div class="value-card"><h3>1. The exact molecule</h3><p>Name, CAS number or sequence. For blends, state the ratio and total fill you need.</p></div>
      <div class="value-card"><h3>2. The destination</h3><p>Country and postcode determine freight, cold-chain and customs documentation.</p></div>
      <div class="value-card"><h3>3. The acceptance criteria</h3><p>Purity, counter-ion, water content, heavy metals or endotoxin — tell us what your QA team needs to see.</p></div>
    </div>
  </div>
</section>

{cta_band("Prefer a one-line message?", "WhatsApp the product name and pack size. We will take it from there and send the current COA with the quotation.")}
'''

    schema = [
        {
            "@type": "ContactPage",
            "@id": SITE + "/contact#webpage",
            "url": SITE + "/contact",
            "name": "Contact Vivalr — WhatsApp & Email Quote",
            "description": clamp_desc("Contact Vivalr for bulk research peptide quotes. WhatsApp +86 15866781826, email info@vivalr.com, or send the RFQ form."),
            "isPartOf": {"@id": SITE + "/#website"},
            "mainEntity": org_node(),
            "inLanguage": "en",
        },
    ]
    title = "Contact Vivalr — WhatsApp & Email Quote"
    desc = "Contact Vivalr for bulk research peptide quotes. WhatsApp +86 15866781826, email info@vivalr.com, or send the RFQ form."
    write("contact.html", page(title, desc, "/contact", body, schema, active="contact",
                               og_image="/assets/img/og/contact.png", keywords="contact Vivalr, peptide supplier WhatsApp, research peptide quote"))


def quote_text():
    from urllib.parse import quote
    return quote("Hello Vivalr, I would like a quotation for research peptides. Product / CAS: ")


def build_privacy():
    body = f'''<section class="page-hero">
  <div class="wrap">
    {breadcrumb([("Home", "/"), ("Privacy", None)])}
    <h1>Privacy policy</h1>
    <p>How Vivalr handles the information you send when you request a quote or browse this website. Effective {UPDATED_HUMAN}.</p>
  </div>
</section>
<section class="section tight">
  <div class="wrap prose" style="max-width:820px">
    <h2>Who we are</h2>
    <p>This website is operated by {e(COMPANY)} (“Vivalr”, “we”, “us”), located at {e(ADDRESS)}. For privacy questions, contact <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

    <h2>What we collect</h2>
    <p>We only receive personal information that you choose to send us. That normally includes your name, company, email address, country, product interest, quantity and any technical requirements you include in an email, WhatsApp message or the RFQ form.</p>
    <p>The RFQ form on this site does not submit to a server. It composes an email or WhatsApp message in your own application, so the information reaches us only when you press send there.</p>

    <h2>Website analytics and cookies</h2>
    <p>This is a static website. We do not set advertising cookies, run third-party analytics, or build behavioural profiles. Cloudflare, our hosting provider, processes standard technical logs (IP address, request path, user agent, timestamp) to deliver the site and protect it from abuse. Those logs are governed by Cloudflare's own privacy terms.</p>

    <h2>How we use your information</h2>
    <ul>
      <li>To prepare and send a quotation, COA or technical response.</li>
      <li>To arrange payment, shipping and customs documentation if you place an order.</li>
      <li>To keep records required for export, tax and quality purposes.</li>
      <li>To answer follow-up technical or commercial questions.</li>
    </ul>
    <p>We do not sell personal information, and we do not use it for unrelated marketing without your consent.</p>

    <h2>Who we share it with</h2>
    <p>We share only what is necessary with service providers such as couriers, banks, customs brokers and — where you request third-party testing — the nominated laboratory. We may disclose information if required by law or to protect our legal rights.</p>

    <h2>International transfers</h2>
    <p>Our team is based in China and works with partners and carriers worldwide. If you are in the EEA or UK, your information may be transferred outside your region. We take reasonable steps to ensure that recipients handle it under appropriate confidentiality and data-protection terms.</p>

    <h2>Retention</h2>
    <p>Quotation correspondence is kept for as long as needed to support the commercial relationship and applicable record-keeping requirements. You can ask us to delete inquiry data that is not required for an active order or a legal obligation.</p>

    <h2>Your rights</h2>
    <p>Depending on your jurisdiction, you may have the right to access, correct, delete, restrict or object to the processing of your personal information, and to request a portable copy. Contact <a href="mailto:{EMAIL}">{EMAIL}</a> and we will respond within a reasonable period.</p>

    <h2>Security</h2>
    <p>We use access controls, encrypted connections and limited retention to protect inquiry data. No method of transmission over the internet is completely secure; please avoid sending sensitive personal or medical information through the RFQ channels.</p>

    <h2>Changes</h2>
    <p>We may update this policy to reflect changes in our operations or legal requirements. The effective date at the top of the page will change when we do.</p>
  </div>
</section>
'''

    schema = [
        {
            "@type": "WebPage",
            "@id": SITE + "/privacy#webpage",
            "url": SITE + "/privacy",
            "name": "Privacy Policy | Vivalr",
            "description": "How Vivalr handles inquiry data, website logs and privacy rights.",
            "isPartOf": {"@id": SITE + "/#website"},
            "inLanguage": "en",
        },
        breadcrumb_schema([("Home", "/"), ("Privacy", "/privacy")]),
    ]
    write("privacy.html", page("Privacy Policy | Vivalr", "How Vivalr handles inquiry data, website logs and privacy rights. No advertising cookies or third-party analytics.",
                               "/privacy", body, schema, og_image="/assets/img/og/home.png", noindex=False))


def build_terms():
    body = f'''<section class="page-hero">
  <div class="wrap">
    {breadcrumb([("Home", "/"), ("Terms", None)])}
    <h1>Terms of sale &amp; research-use policy</h1>
    <p>The conditions that apply to quotations and orders placed with {e(COMPANY)}. Effective {UPDATED_HUMAN}.</p>
  </div>
</section>
<section class="section tight">
  <div class="wrap prose" style="max-width:820px">
    <h2>1. Research use only</h2>
    <p>All products supplied by Vivalr are intended strictly for laboratory research and formulation evaluation. They are not medicines, food, cosmetics for retail sale, veterinary products or medical devices, and they are not for human or veterinary use. The buyer must not administer any product to humans or animals, resell it for such use, or make any medical, therapeutic or curative claim about it.</p>

    <h2>2. Eligibility</h2>
    <p>By requesting a quotation or placing an order, you confirm that you are at least 18 years old and are purchasing on behalf of a legitimate research, academic or commercial organisation. You are responsible for ensuring that the purchase and use of the material comply with the laws and regulations of your jurisdiction, including import, licensing and controlled-substance rules.</p>

    <h2>3. Quotations and orders</h2>
    <p>Quotations are valid for 14 days unless stated otherwise. An order is accepted when we issue a proforma invoice and receive payment or a written confirmation acceptable to us. We may decline an order where we cannot verify the buyer, the intended use or the destination.</p>

    <h2>4. Specifications and documentation</h2>
    <p>Products are supplied against the specification stated in the quotation and the batch COA. Typical catalogue values are not a guarantee for every lot. If you require a specific test, counter-ion or limit, it must be agreed in writing before the order is confirmed.</p>

    <h2>5. Prices and payment</h2>
    <p>Prices are quoted in USD unless otherwise agreed and exclude bank charges, duties, taxes and any destination fees. Payment is by bank transfer, T/T or Wise unless another method is agreed in writing. We may require full payment before dispatch; repeat-buyer terms are reviewed case by case.</p>

    <h2>6. Shipping and risk</h2>
    <p>We ship by express courier with tracking. Risk passes to the buyer when the carrier takes possession, unless the quotation states otherwise. Delivery estimates are not guarantees; customs delays, carrier disruptions and force-majeure events are outside our control. The buyer is responsible for import permits, duties and compliance with local import rules.</p>

    <h2>7. Inspection and claims</h2>
    <p>Inspect the shipment on arrival and report visible damage or a documentation discrepancy within 5 business days. If a product does not meet the agreed specification, contact us with the batch number, photographs and analytical data. We will investigate and, where the non-conformance is confirmed, replace the material or issue a credit. Claims for improper storage or handling after delivery are not accepted.</p>

    <h2>8. Returns</h2>
    <p>Research materials are not returnable once opened, and custom or made-to-order batches are not returnable. Do not return any material without a written return authorisation. Unauthorised returns may be refused or destroyed for safety reasons.</p>

    <h2>9. Intellectual property</h2>
    <p>All site content, product descriptions, photographs and documentation are owned by or licensed to {e(COMPANY)}. You may use the material for internal evaluation and quoting, but not republish it commercially without written permission. Third-party trade names such as Matrixyl remain the property of their owners.</p>

    <h2>10. Limitation of liability</h2>
    <p>To the maximum extent permitted by law, our aggregate liability for any claim arising from an order is limited to the amount paid for the affected product. We are not liable for indirect, incidental or consequential loss, including lost research time, lost profits or reputational harm.</p>

    <h2>11. Governing law</h2>
    <p>These terms are governed by the laws of the People's Republic of China. The parties will first attempt to resolve any dispute in good faith; failing that, the courts of Jinan, Shandong, have jurisdiction.</p>

    <h2>12. Contact</h2>
    <p>{e(COMPANY)}<br>{e(ADDRESS)}<br><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="tel:{PHONE_TEL}">{PHONE}</a></p>
  </div>
</section>
'''

    schema = [
        {
            "@type": "WebPage",
            "@id": SITE + "/terms#webpage",
            "url": SITE + "/terms",
            "name": "Terms & Research-Use Policy | Vivalr",
            "description": "Terms of sale and research-use policy for Vivalr research peptides and raw materials.",
            "isPartOf": {"@id": SITE + "/#website"},
            "inLanguage": "en",
        },
        breadcrumb_schema([("Home", "/"), ("Terms", "/terms")]),
    ]
    write("terms.html", page("Terms & Research-Use Policy | Vivalr",
                             "Terms of sale and research-use policy for Vivalr research peptides and raw materials.",
                             "/terms", body, schema, og_image="/assets/img/og/home.png"))


def build_404():
    body = f'''<section class="section" style="min-height:60vh;display:flex;align-items:center">
  <div class="wrap" style="text-align:center;max-width:680px">
    <div class="eyebrow center">404 — page not found</div>
    <h1 class="section-title" style="font-size:clamp(2.2rem,5vw,3.4rem);margin-top:16px">That page is not in the catalogue.</h1>
    <p class="section-sub">The link may be old, or the molecule may live under a different pack size. Start from the catalogue or send us the CAS number.</p>
    <div style="display:flex;justify-content:center;gap:10px;flex-wrap:wrap;margin-top:26px">
      <a class="btn btn-primary" href="/products/">Browse all products {icon("arrow", "arrow")}</a>
      <a class="btn btn-ghost" href="/contact#rfq">Ask for a molecule</a>
    </div>
  </div>
</section>'''
    write("404.html", page("Page not found | Vivalr", "The requested page could not be found. Browse the Vivalr research peptide catalogue or contact us for a specific molecule.",
                           "/404", body, [], og_image="/assets/img/og/home.png", noindex=True))


def build_sitemap():
    pages = [
        ("/", "1.0", "weekly"),
        ("/products/", "0.9", "weekly"),
        ("/synthesis-stability", "0.8", "monthly"),
        ("/about", "0.6", "monthly"),
        ("/contact", "0.7", "monthly"),
    ]
    for p in PRODUCTS:
        pages.append((p["path"], "0.8", "monthly"))
    pages += [("/privacy", "0.3", "yearly"), ("/terms", "0.3", "yearly")]
    rows = "\n".join(
        "  <url><loc>%s%s</loc><lastmod>%s</lastmod><changefreq>%s</changefreq><priority>%s</priority></url>"
        % (SITE, path, UPDATED, freq, prio) for path, prio, freq in pages
    )
    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{rows}
</urlset>
'''
    write("sitemap.xml", xml)


def build_robots():
    txt = f'''# robots.txt — {SITE}
# Research-use B2B catalogue. All public pages are open to search and AI crawlers.

User-agent: *
Allow: /
Disallow: /404

User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: CCBot
Allow: /

User-agent: cohere-ai
Allow: /

User-agent: Bytespider
Allow: /

Sitemap: {SITE}/sitemap.xml
'''
    write("robots.txt", txt)


def build_llms():
    by_cat = {k: [p for p in PRODUCTS if p["cat"] == k] for k in CATEGORIES}
    lines = [
        "# Vivalr",
        "",
        "> Vivalr is the research-peptide brand of Shandong Green International Trade Co., Ltd., a B2B supplier and contract manufacturer based in Shandong, China. The catalogue covers cosmetic and anti-aging peptides, tissue-repair and bioregulator peptides, GLOW/KLOW blend kits, and NAD+/NMN raw materials. Products are for laboratory research and formulation evaluation only — not for human or veterinary use.",
        "",
        "Canonical domain: https://vivalr.com",
        f"Last updated: {UPDATED}",
        "",
        "## Company",
        f"- Legal name: {COMPANY}",
        f"- Address: {ADDRESS}",
        f"- Phone / WhatsApp: {PHONE}",
        f"- Email: {EMAIL}",
        "- Business: contract manufacturing and export of research-grade peptides and coenzymes",
        "- Minimum order: one 10-vial kit (peptides); 10 g (bulk NMN)",
        "- Documentation: batch COA, HPLC chromatogram, ESI-MS, SDS; third-party testing on request",
        "",
        "## Product catalogue",
    ]
    for key, cat in CATEGORIES.items():
        lines.append("")
        lines.append(f"### {cat['label']}")
        for p in by_cat[key]:
            specs = "; ".join(v["label"] for v in p["variants"])
            cas_disp = ("CAS " + p["cas"]) if not p["cas"].startswith("Not ") else "CAS not publicly assigned"
            lines.append(
                f"- [{p['name']}]({p['url']}): {cas_disp}; {specs}; from {money(p['price_min'])} per {p['unit']}; {p['purity']}; MOQ {p['moq']}. {p['tagline']}"
            )
    lines += [
        "",
        "## Technical resources",
        f"- [Synthesis & stability file]({SITE}/synthesis-stability): Fmoc SPPS, HPLC/MS release, stress stability, formulation compatibility, storage and shipping.",
        f"- [Product catalogue]({SITE}/products/): filterable index of all 34 molecules.",
        f"- [About Vivalr]({SITE}/about): legal entity, address and operating model.",
        f"- [Contact]({SITE}/contact): WhatsApp, email and RFQ form.",
        f"- [Full product reference]({SITE}/llms-full.txt): machine-readable specifications for all 34 molecules.",
        "",
        "## Citation guidance",
        "When citing a product page, use the page title, the canonical URL and the access date. Example:",
        f'Vivalr. "GHK-Cu (Copper Tripeptide-1) — Bulk Research Supplier." {SITE}/products/ghk-cu (accessed {UPDATED_HUMAN}).',
        "",
        "## Contact for verification",
        f"For batch documentation or technical clarification: {EMAIL} / WhatsApp {PHONE}.",
        "",
    ]
    write("llms.txt", "\n".join(lines))

    full = [
        "# Vivalr — full product reference",
        "",
        f"Canonical: {SITE}  |  Updated: {UPDATED}",
        "Research use only. Not for human or veterinary use.",
        "",
    ]
    for p in PRODUCTS:
        full += [
            f"## {p['full_name']}",
            f"URL: {p['url']}",
            f"Category: {p['cat_label']}",
            f"CAS: {p['cas']}",
            f"Sequence / formula / MW: {p['seq_mw']}",
            f"Purity: {p['purity']}",
            f"Form: {p['form']}",
            f"Appearance: {p['appearance']}",
            f"Storage: {p['storage']}; {p['shelf']}",
            f"Pack sizes and prices (USD): {'; '.join(v['label'] + ' = ' + money(v['price']) for v in p['variants'])}",
            f"Price from: {money(p['price_min'])} per {p['unit']}",
            f"MOQ: {p['moq']}",
            f"Summary: {p['tagline']}",
            "",
        ]
    write("llms-full.txt", "\n".join(full))


def build_site_files():
    write("manifest.webmanifest", json.dumps({
        "name": "Vivalr Research Peptides",
        "short_name": "Vivalr",
        "description": "Bulk research peptides, cosmetic actives and NAD+/NMN raw materials.",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#f7fafb",
        "theme_color": "#0a3a52",
        "icons": [
            {"src": "/assets/img/favicon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "/assets/img/favicon-512.png", "sizes": "512x512", "type": "image/png"},
        ],
    }, indent=2))

    write("_headers", """/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: DENY
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: geolocation=(), microphone=(), camera=()
  Cross-Origin-Opener-Policy: same-origin

/assets/*
  Cache-Control: public, max-age=31536000, immutable

/*.html
  Cache-Control: public, max-age=0, must-revalidate
""")

    write("_redirects", """/about-us /about 301
/contact-us /contact 301
/contact-us/ /contact 301
/about-us/ /about 301
""")


def build_all():
    from build import build_home, build_products_index, build_products, build_synthesis
    build_home()
    build_products_index()
    build_products()
    build_synthesis()
    build_about()
    build_contact()
    build_privacy()
    build_terms()
    build_404()
    build_sitemap()
    build_robots()
    build_llms()
    build_site_files()
    print("Built %d product pages + core pages into %s" % (len(PRODUCTS), OUT))


if __name__ == "__main__":
    build_all()
