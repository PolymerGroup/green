# -*- coding: utf-8 -*-
"""Shared HTML components for the Vivalr static site."""
import html
import json
import re

from data import (
    SITE, BRAND, COMPANY, ADDRESS, ADDRESS_SHORT, PHONE, PHONE_TEL, WHATSAPP,
    EMAIL, UPDATED, UPDATED_HUMAN, CATEGORIES, PRODUCTS, BY_SLUG,
)

WA_TEXT = "Hello%20Vivalr%2C%20I%20would%20like%20a%20quotation%20for%20research%20peptides."


def e(value):
    return html.escape(str(value), quote=True)


def money(value):
    text = f"{float(value):,.2f}"
    if text.endswith(".00"):
        text = text[:-3]
    return "$" + text


def jsonld(graph):
    payload = {"@context": "https://schema.org", "@graph": graph}
    raw = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    raw = raw.replace("</", "<\\/")
    return '<script type="application/ld+json">' + raw + "</script>"


def icon(name, cls=""):
    paths = {
        "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 2 .7 2.9a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.2-1.2a2 2 0 0 1 2.1-.5c.9.3 1.9.6 2.9.7a2 2 0 0 1 1.7 2Z"/>',
        "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
        "whatsapp": '<path d="M20.5 11.6a8.5 8.5 0 0 1-12.6 7.5L3 20.5l1.4-4.7a8.5 8.5 0 1 1 16.1-4.2Z"/><path d="M8.4 7.8c.2-.4.4-.4.7-.4h.5c.2 0 .4 0 .6.5l.8 1.9c.1.2.1.4 0 .6l-.6.8c-.1.2-.2.3 0 .6.4.7 1 1.4 1.7 1.9.7.5 1.2.7 1.4.8.2.1.4.1.6-.1l.8-1c.2-.2.3-.2.6-.1l1.8.9c.2.1.4.2.4.3 0 .2 0 .9-.4 1.3-.4.4-1 1-1.8 1-.5 0-1.2 0-2.1-.4a9.3 9.3 0 0 1-3-2 9 9 0 0 1-1.9-3c-.2-.7-.2-1.2 0-1.7Z"/>',
        "pin": '<path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.6"/>',
        "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
        "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/>',
        "flask": '<path d="M9 3h6M10 3v6l-5.2 8.6A2 2 0 0 0 6.5 21h11a2 2 0 0 0 1.7-3.4L14 9V3"/><path d="M7.5 15h9"/>',
        "chart": '<path d="M3 3v18h18"/><path d="m7 14 3-4 3 3 5-7"/>',
        "snow": '<path d="M12 2v20M4.2 6.5l15.6 11M19.8 6.5l-15.6 11"/><path d="m9 4 3 3 3-3M9 20l3-3 3 3"/>',
        "box": '<path d="m21 8-9-5-9 5 9 5 9-5Z"/><path d="M3 8v8l9 5 9-5V8M12 13v10"/>',
        "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a15 15 0 0 1 0 18M12 3a15 15 0 0 0 0 18"/>',
        "search": '<circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/>',
        "copy": '<rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/>',
        "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
        "close": '<path d="m6 6 12 12M18 6 6 18"/>',
        "file": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>',
        "truck": '<path d="M1 3h15v13H1zM16 8h4l3 4v4h-7V8Z"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/>',
        "card": '<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/>',
        "spark": '<path d="m12 3 1.9 5.6L19.5 10l-5.6 1.9L12 17.5l-1.9-5.6L4.5 10l5.6-1.4Z"/><path d="M19 16v4M17 18h4"/>',
        "repair": '<path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.7 1.7"/><path d="M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.7-1.7"/>',
        "blend": '<circle cx="8" cy="8" r="4"/><circle cx="16" cy="16" r="4"/><circle cx="16" cy="7" r="2.5"/><circle cx="7" cy="17" r="2.5"/>',
        "nad": '<circle cx="12" cy="12" r="3"/><path d="M12 2v4M12 18v4M2 12h4M18 12h4M5 5l2.8 2.8M16.2 16.2 19 19M19 5l-2.8 2.8M7.8 16.2 5 19"/>',
        "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
        "arrow-up": '<path d="M7 17 17 7M7 7h10v10"/>',
        "check": '<path d="m5 12 4 4L19 6"/>',
        "chevron": '<path d="m9 18 6-6-6-6"/>',
        "quote": '<path d="M3 21c3 0 7-1 7-8V5c0-1.5-1-3-3-3S4 3 4 5s1 3 3 3c0 5-2 6-4 6v7Z"/><path d="M14 21c3 0 7-1 7-8V5c0-1.5-1-3-3-3s-3 1-3 3 1 3 3 3c0 5-2 6-4 6v7Z"/>',
        "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/>',
        "download": '<path d="M12 3v12M7 10l5 5 5-5M4 21h16"/>',
        "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
        "layers": '<path d="m12 2 9 5-9 5-9-5 9-5Z"/><path d="m3 12 9 5 9-5M3 17l9 5 9-5"/>',
        "lock": '<rect x="4" y="10" width="16" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>',
        "cart": '<circle cx="9" cy="20" r="1.6"/><circle cx="19" cy="20" r="1.6"/><path d="M2 3h3l2.4 11.4a2 2 0 0 0 2 1.6h8.9a2 2 0 0 0 2-1.6L22 7H6"/>',
        "trash": '<path d="M3 6h18M8 6V4h8v2M19 6l-1 14H6L5 6M10 11v5M14 11v5"/>',
    }
    body = paths.get(name, paths["info"])
    return ('<svg class="%s" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">%s</svg>'
            % (e(cls), body))


def logo_svg(cls="brand-mark"):
    return (
        '<svg class="%s" viewBox="0 0 48 48" aria-hidden="true" focusable="false">'
        '<path d="M24 2.8 43 13.7v20.6L24 45.2 5 34.3V13.7Z" fill="#07222f"/>'
        '<path d="M24 5.7 40 15v18L24 42.3 8 33V15Z" fill="none" stroke="rgba(255,255,255,.16)" stroke-width="1"/>'
        '<path d="M14.6 15.2 24 37.2l9.4-22" fill="none" stroke="#16b3ad" stroke-width="3.4" '
        'stroke-linecap="round" stroke-linejoin="round"/>'
        '<circle cx="24" cy="14.2" r="2.9" fill="#fff"/>'
        '<circle cx="14.6" cy="15.2" r="2" fill="#16b3ad"/><circle cx="33.4" cy="15.2" r="2" fill="#16b3ad"/>'
        '</svg>' % e(cls)
    )


def brand(link="/"):
    return (
        '<a class="brand" href="%s" aria-label="Vivalr home">%s'
        '<span class="brand-word"><span class="brand-name">VIVALR</span>'
        '<span class="brand-sub">Research Peptides</span></span></a>'
    ) % (e(link), logo_svg())


def wrap_label(text, width=16, max_lines=2):
    words = str(text).split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if len(trial) <= width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
        if len(lines) == max_lines:
            break
    if cur and len(lines) < max_lines:
        lines.append(cur)
    if len(lines) == max_lines:
        used = " ".join(lines)
        if len(used.replace(" ", "")) < len(str(text).replace(" ", "")):
            lines[-1] = lines[-1][: max(0, width - 1)] + "…"
    return lines or [str(text)[:width]]


def vial_svg(p, hero=False):
    slug = "hero" if hero else p["slug"]
    copper = p["cat"] == "cosmetic" and p["slug"] in ("ghk-cu", "ahk-cu")
    powder = "#2f6f9e" if copper else "#d9eee9"
    powder2 = "#173f5e" if copper else "#c2e3dd"
    if hero:
        name_lines = ["RESEARCH", "PEPTIDES"]
        spec = "≥99% HPLC"
        sub = "BATCH COA"
    else:
        name_lines = wrap_label(p["name"], 15, 2)
        first = p["variants"][0]["label"]
        spec = first.split(" ×")[0]
        if p["cat"] == "blend":
            spec = p["variants"][0]["label"].split(" mg")[0] + " mg blend"
        sub = "RESEARCH USE ONLY"
    name_size = 11 if max(len(x) for x in name_lines) <= 12 else 9.5
    name_el = "".join(
        '<text x="120" y="%d" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" '
        'font-size="%s" font-weight="700" fill="#0a3a52">%s</text>'
        % (178 + i * 12, name_size, e(line)) for i, line in enumerate(name_lines)
    )
    return f'''<svg class="vial-svg" viewBox="0 0 240 360" role="img" aria-label="{e(p['name'] if not hero else 'Vivalr research peptide vial')} — {e(spec)}">
<defs>
  <linearGradient id="glass-{slug}" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#ffffff" stop-opacity=".9"/><stop offset=".22" stop-color="#e9f6f8" stop-opacity=".55"/>
    <stop offset=".55" stop-color="#ffffff" stop-opacity=".18"/><stop offset=".8" stop-color="#cfe7ec" stop-opacity=".55"/>
    <stop offset="1" stop-color="#ffffff" stop-opacity=".8"/>
  </linearGradient>
  <linearGradient id="cap-{slug}" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#9fb4bb"/><stop offset=".25" stop-color="#eef5f6"/>
    <stop offset=".55" stop-color="#afc2c8"/><stop offset=".8" stop-color="#f7fbfc"/><stop offset="1" stop-color="#8ea3aa"/>
  </linearGradient>
  <linearGradient id="powder-{slug}" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{powder}"/><stop offset="1" stop-color="{powder2}"/>
  </linearGradient>
  <filter id="soft-{slug}" x="-30%" y="-30%" width="160%" height="160%">
    <feGaussianBlur stdDeviation="9"/>
  </filter>
</defs>
<ellipse cx="120" cy="336" rx="52" ry="9" fill="#062430" opacity=".22" filter="url(#soft-{slug})"/>
<g>
  <rect x="98" y="27" width="44" height="9" rx="3" fill="#78939b"/>
  <rect x="96" y="34" width="48" height="30" rx="5" fill="url(#cap-{slug})"/>
  <g stroke="#6d868e" stroke-width="1" opacity=".55">
    <path d="M100 39v20M105 39v20M110 39v20M115 39v20M120 39v20M125 39v20M130 39v20M135 39v20M140 39v20"/>
  </g>
  <path d="M106 64h28v14h-28z" fill="url(#glass-{slug})" stroke="#b9d3d9" stroke-width="1"/>
  <path d="M82 86c0-6 8-8 12-8h52c4 0 12 2 12 8v210c0 19-13 31-38 31s-38-12-38-31Z"
        fill="url(#glass-{slug})" stroke="#b7d2d8" stroke-width="2"/>
  <path d="M89 250h62v46c0 13-9 23-31 23s-31-10-31-23Z" fill="url(#powder-{slug})" opacity=".92"/>
  <path d="M89 250h62v10H89Z" fill="#ffffff" opacity=".28"/>
  <rect x="95" y="101" width="7" height="132" rx="3.5" fill="#ffffff" opacity=".55"/>
  <rect x="144" y="106" width="4" height="118" rx="2" fill="#ffffff" opacity=".4"/>
  <rect x="88" y="143" width="64" height="98" rx="4" fill="#ffffff" stroke="#d3e2e6" stroke-width="1"/>
  <rect x="88" y="143" width="64" height="17" rx="4" fill="#0a3a52"/>
  <text x="120" y="155" text-anchor="middle" font-family="Cascadia Mono,Consolas,monospace" font-size="6.2"
        letter-spacing="1.4" fill="#7fe0d9">VIVALR</text>
  {name_el}
  <text id="vial-spec" x="120" y="212" text-anchor="middle" font-family="Cascadia Mono,Consolas,monospace" font-size="7.6"
        fill="#3f6572">{e(spec)}</text>
  <line x1="99" y1="219" x2="141" y2="219" stroke="#dbe7ea" stroke-width="1"/>
  <text x="120" y="230" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="5.6"
        letter-spacing=".7" fill="#8aa2ab">{e(sub)}</text>
  <text id="vial-sku" x="120" y="260" text-anchor="middle" font-family="Cascadia Mono,Consolas,monospace"
        font-size="5.4" fill="#7d939c">{e(p['variants'][0]['sku'] if not hero else 'VVR-RP')}</text>
  <g opacity=".8">
    <path d="M157 120h8M161 116v8M157 172h8" stroke="#b7d2d8" stroke-width="1"/>
  </g>
</g>
</svg>'''


def mini_vial():
    return ('<svg class="pcard-mini-vial" viewBox="0 0 34 86" aria-hidden="true">'
            '<rect x="12" y="1" width="10" height="3" rx="1" fill="#7d939c"/>'
            '<rect x="11" y="4" width="12" height="8" rx="2" fill="#b9ccd1"/>'
            '<path d="M10 12h14v60c0 6-3 9-7 9s-7-3-7-9Z" fill="#ffffff" fill-opacity=".55" stroke="#9fbcc5"/>'
            '<path d="M10 50h14v22c0 6-3 9-7 9s-7-3-7-9Z" fill="#cfe9e4"/>'
            '<rect x="11" y="30" width="12" height="18" rx="1" fill="#fff" stroke="#dbe7ea"/>'
            '<rect x="11" y="30" width="12" height="4" fill="#0a3a52"/>'
            '<path d="M13 37h8M13 40h8M13 43h6" stroke="#9fb4bb" stroke-width=".8"/>'
            '</svg>')


def molecule_svg():
    return '''<svg viewBox="0 0 420 360" role="img" aria-label="Schematic of a peptide chain with batch analytics">
<defs>
  <linearGradient id="mol-a" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0e8f8f"/><stop offset="1" stop-color="#16b3ad"/></linearGradient>
  <radialGradient id="mol-glow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#16b3ad" stop-opacity=".22"/><stop offset="1" stop-color="#16b3ad" stop-opacity="0"/></radialGradient>
</defs>
<circle cx="210" cy="180" r="168" fill="url(#mol-glow)"/>
<g fill="none" stroke="#0a3a52" stroke-opacity=".14">
  <circle cx="210" cy="180" r="120"/><circle cx="210" cy="180" r="86"/><circle cx="210" cy="180" r="52"/>
  <path d="M210 20v320M30 180h360M83 53l254 254M337 53 83 307"/>
</g>
<g stroke="url(#mol-a)" stroke-width="3" stroke-linecap="round" fill="none">
  <path d="M96 232 141 201 189 221 232 186 280 205 324 166"/>
</g>
<g fill="#fff" stroke="#0a3a52" stroke-width="2">
  <circle cx="96" cy="232" r="10"/><circle cx="141" cy="201" r="7"/><circle cx="189" cy="221" r="10"/>
  <circle cx="232" cy="186" r="7"/><circle cx="280" cy="205" r="10"/><circle cx="324" cy="166" r="7"/>
</g>
<g fill="#0e8f8f"><circle cx="96" cy="232" r="4"/><circle cx="189" cy="221" r="4"/><circle cx="280" cy="205" r="4"/></g>
<g font-family="Cascadia Mono,Consolas,monospace" font-size="9" fill="#3f6572">
  <text x="62" y="212">Gly</text><text x="162" y="198">His</text><text x="252" y="182">Lys</text><text x="304" y="148">Cu²⁺</text>
</g>
<g font-family="Segoe UI,Arial,sans-serif" font-size="10" font-weight="700" fill="#0a3a52">
  <rect x="42" y="286" width="150" height="46" rx="8" fill="#fff" stroke="#dbe7ea"/>
  <text x="56" y="305">RP-HPLC 214 nm</text><text x="56" y="321" font-family="Cascadia Mono,monospace" font-size="11" fill="#0e8f8f">99.2% area</text>
  <rect x="228" y="286" width="150" height="46" rx="8" fill="#fff" stroke="#dbe7ea"/>
  <text x="242" y="305">ESI-MS identity</text><text x="242" y="321" font-family="Cascadia Mono,monospace" font-size="11" fill="#0e8f8f">403.94 Da</text>
</g>
</svg>'''


def head(title, desc, path, og_type="website", og_image="/assets/img/og/home.png",
         schema=None, keywords="", noindex=False):
    canonical = SITE + path
    image = SITE + og_image
    robots = "noindex,follow" if noindex else "index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1"
    kw = f'<meta name="keywords" content="{e(keywords)}">' if keywords else ""
    schema_html = jsonld(schema) if schema else ""
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{kw}
<link rel="canonical" href="{e(canonical)}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#0a3a52">
<meta name="format-detection" content="telephone=no">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/assets/img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="manifest" href="/manifest.webmanifest">
<link rel="stylesheet" href="/assets/css/style.css">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{e(canonical)}">
<meta property="og:image" content="{e(image)}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(title)}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{e(image)}">
<meta name="twitter:image:alt" content="{e(title)}">
{schema_html}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>'''


def header(active=""):
    links = [
        ("/", "Home", "home"),
        ("/products/", "Products", "products"),
        ("/synthesis-stability", "Synthesis & QC", "synthesis"),
        ("/about", "About", "about"),
        ("/contact", "Contact", "contact"),
    ]
    nav = "".join(
        '<li><a href="%s"%s>%s</a></li>' % (href, ' aria-current="page"' if key == active else "", label)
        for href, label, key in links
    )
    return f'''
<div class="topbar">
  <div class="wrap">
    <div class="topbar-note"><span class="topbar-dot"></span> For laboratory research use only — not for human or veterinary use</div>
    <div class="topbar-links">
      <a class="topbar-item" href="mailto:{EMAIL}">{icon("mail")} {EMAIL}</a>
      <a class="topbar-item" href="tel:{PHONE_TEL}">{icon("phone")} {PHONE}</a>
    </div>
  </div>
</div>
<header class="site-header">
  <div class="wrap">
    {brand("/")}
    <nav class="nav" aria-label="Primary">
      <ul class="nav-links">{nav}</ul>
      <div class="nav-cta">
        <a class="btn btn-ghost btn-sm" href="/contact">Talk to sales</a>
        <a class="btn btn-primary btn-sm" href="/contact#rfq">Request a quote {icon("arrow", "arrow")}</a>
      </div>
      <button class="cart-toggle" id="cart-toggle" type="button" aria-haspopup="dialog" aria-controls="cart-drawer" aria-label="Open inquiry cart">
        {icon("cart")}<span class="cart-toggle-label">Cart</span><span class="cart-count" id="cart-count">0</span>
      </button>
      <button class="nav-toggle" id="nav-toggle" aria-expanded="false" aria-controls="mobile-nav" aria-label="Open menu">
        {icon("menu")}
      </button>
    </nav>
  </div>
</header>
<nav class="mobile-nav" id="mobile-nav" aria-label="Mobile" aria-hidden="true">
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/products/">Products</a></li>
    <li><a href="/products/?category=cosmetic">Cosmetic &amp; Anti-Aging</a></li>
    <li><a href="/products/?category=repair">Repair &amp; Bioregulator</a></li>
    <li><a href="/products/?category=blend">Blend Kits</a></li>
    <li><a href="/products/?category=nad">NAD+ &amp; NMN</a></li>
    <li><a href="/synthesis-stability">Synthesis &amp; Stability</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
  <a class="btn btn-primary" href="/contact#rfq">Request a quote {icon("arrow", "arrow")}</a>
  <a class="btn btn-wa" href="{WHATSAPP}?text={WA_TEXT}" target="_blank" rel="noopener">{icon("whatsapp")} WhatsApp us</a>
</nav>
<main id="main">'''


def cart_drawer():
    return f'''<div class="cart-overlay" id="cart-overlay" aria-hidden="true"></div>
<aside class="cart-drawer" id="cart-drawer" role="dialog" aria-modal="true" aria-labelledby="cart-title" aria-hidden="true">
  <div class="cart-head">
    <div>
      <div class="eyebrow">Inquiry cart</div>
      <h2 id="cart-title">Your selection</h2>
      <p id="cart-summary">0 items</p>
    </div>
    <button class="cart-close" id="cart-close" type="button" aria-label="Close cart">{icon("close")}</button>
  </div>
  <div class="cart-body">
    <div class="cart-empty" id="cart-empty">
      <span class="cart-empty-icon">{icon("cart")}</span>
      <strong>Your cart is empty.</strong>
      <p>Add a pack size from any product page. The cart will build a complete inquiry for you.</p>
      <a class="btn btn-primary btn-sm" href="/products/">Browse products {icon("arrow", "arrow")}</a>
    </div>
    <div id="cart-items"></div>
  </div>
  <div class="cart-foot">
    <div class="cart-total"><span>Estimated total</span><strong id="cart-total">$0</strong></div>
    <p class="cart-note">Prices are in USD per kit. Shipping, taxes and any testing are quoted separately. No payment is taken online.</p>
    <a class="btn btn-wa" id="cart-wa" href="#" target="_blank" rel="noopener">{icon("whatsapp")} Send inquiry on WhatsApp</a>
    <a class="btn btn-dark" id="cart-email" href="mailto:{EMAIL}">{icon("mail")} Email the inquiry</a>
    <button class="btn btn-ghost" id="cart-clear" type="button">{icon("trash")} Clear cart</button>
    <p class="cart-foot-note">The message is written for you — product, pack size, quantity and total are included.</p>
  </div>
</aside>'''


def footer():
    cats = "".join(
        '<li><a href="/products/?category=%s">%s</a></li>' % (k, e(v["short"]))
        for k, v in CATEGORIES.items()
    )
    return f'''</main>
<footer class="site-footer">
  <div class="footer-main">
    <div class="wrap">
      <div class="footer-grid">
        <div class="footer-brand">
          {brand("/")}
          <p>Research-grade peptides, cosmetic actives and NAD+ precursors from Jinan, China. Documented batch by batch for laboratories, formulators and ingredient buyers worldwide.</p>
          <div class="research-notice"><strong>For Laboratory Research and Formulation Evaluation Use Only. Not for Human or Veterinary Use.</strong></div>
        </div>
        <div class="footer-col">
          <h4>Products</h4>
          <ul>
            {cats}
            <li><a href="/products/">All products</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Company</h4>
          <ul>
            <li><a href="/about">About Vivalr</a></li>
            <li><a href="/synthesis-stability">Synthesis &amp; stability</a></li>
            <li><a href="/contact">Contact</a></li>
            <li><a href="/privacy">Privacy policy</a></li>
            <li><a href="/terms">Terms &amp; research-use policy</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Contact</h4>
          <ul class="footer-contact">
            <li>{icon("pin")}<span>{e(ADDRESS)}</span></li>
            <li>{icon("phone")}<a href="tel:{PHONE_TEL}">{PHONE}</a></li>
            <li>{icon("mail")}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li>{icon("whatsapp")}<a href="{WHATSAPP}?text={WA_TEXT}" target="_blank" rel="noopener">WhatsApp: {PHONE}</a></li>
            <li>{icon("clock")}<span>Mon–Sat, 09:00–18:00 China Standard Time (UTC+8)</span></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="wrap">
      <span>&copy; <span data-year>2026</span> {e(COMPANY)}. All rights reserved.</span>
      <div class="legal">
        <a href="/privacy">Privacy</a><a href="/terms">Terms</a>
        <a href="/sitemap.xml">Sitemap</a><a href="/llms.txt">llms.txt</a>
      </div>
    </div>
  </div>
</footer>
{cart_drawer()}
<script src="/assets/js/main.js" defer></script>
</body>
</html>'''


def breadcrumb(items):
    parts = []
    for i, (label, href) in enumerate(items):
        if i:
            parts.append('<span class="sep">/</span>')
        if href:
            parts.append('<a href="%s">%s</a>' % (href, e(label)))
        else:
            parts.append('<span aria-current="page">%s</span>' % e(label))
    return '<nav class="breadcrumb" aria-label="Breadcrumb">' + "".join(parts) + "</nav>"


def faq_block(faqs, heading="Frequently asked questions", eyebrow="B2B buyer FAQ", intro=""):
    items = []
    for i, (q, a) in enumerate(faqs):
        items.append(
            '<details class="faq-item"%s><summary><span>%s</span><span class="faq-icon" aria-hidden="true"></span></summary>'
            '<div class="faq-a"><p>%s</p></div></details>' % (" open" if i == 0 else "", e(q), e(a))
        )
    sub = '<p class="section-sub">%s</p>' % e(intro) if intro else ""
    return f'''<section class="section" id="faq">
  <div class="wrap">
    <div class="section-head center">
      <div class="eyebrow center">{e(eyebrow)}</div>
      <h2 class="section-title">{e(heading)}</h2>
      {sub}
    </div>
    <div class="faq">{''.join(items)}</div>
  </div>
</section>'''


def cta_band(title="Need a specification sheet or a bulk quote?",
             text="Send the molecule, pack size and destination. We reply with pricing, COA and lead time within one business day.",
             primary=("Request a quote", "/contact#rfq"),
             secondary=("WhatsApp us", WHATSAPP + "?text=" + WA_TEXT)):
    return f'''<section class="cta-band">
  <div class="wrap">
    <div>
      <h2>{e(title)}</h2>
      <p>{e(text)}</p>
    </div>
    <div class="cta-actions">
      <a class="btn btn-light btn-lg" href="{e(primary[1])}">{e(primary[0])} {icon("arrow", "arrow")}</a>
      <a class="btn btn-outline-light btn-lg" href="{e(secondary[1])}" target="_blank" rel="noopener">{icon("whatsapp")} {e(secondary[0])}</a>
    </div>
  </div>
</section>'''


def product_card(p):
    chips = "".join('<span class="chip">%s</span>' % e(v["label"].replace(" × 10 vials", "")) for v in p["variants"][:3])
    if len(p["variants"]) > 3:
        chips += '<span class="chip">+%d sizes</span>' % (len(p["variants"]) - 3)
    search_blob = " ".join([p["name"], p["full_name"], p["cas"], p["cat_short"], p["spec_summary"], " ".join(p["tags"])]).lower()
    return f'''<article class="pcard" data-cat="{p['cat']}" data-search="{e(search_blob)}">
  <div class="pcard-visual">
    <span class="pcard-cat">{e(p['cat_short'])}</span>
    {mini_vial()}
  </div>
  <div class="pcard-body">
    <h3 class="pcard-title"><a href="{p['path']}">{e(p['name'])}</a></h3>
    <div class="pcard-cas">CAS {e(p['cas'])}</div>
    <div class="spec-chips">{chips}</div>
    <div class="pcard-price"><span>{'From' if len(p['variants']) > 1 else 'Price'}</span> <strong>{money(p['price_from'])}</strong> <small>/ {p['unit']}</small></div>
    <div class="pcard-foot"><span>MOQ {e(p['moq'])}</span><span>View specs {icon("arrow", "arrow")}</span></div>
  </div>
</article>'''


def generic_faqs(p):
    return [
        ("What purity and documentation come with %s?" % p["name"],
         "%s is released against the specification stated on its batch COA, with ESI-MS identity confirmation, "
         "and ships with a batch-specific COA and SDS. The COA reports appearance, assay, water content and "
         "identity; third-party HPLC/MS testing can be arranged on request." % p["name"]),
        ("What is the MOQ and how does bulk pricing work?" % (),
         "The minimum order is %s. Listed prices cover standard pack sizes in USD; pricing steps down at "
         "10+ kits and 100+ kits. The final quotation confirms the pack size, freight and any documentation "
         "or testing you require." % p["moq"]),
        ("How is %s packaged and shipped?" % p["name"],
         "Material ships in sealed, tamper-evident vials or bulk containers with desiccant and appropriate "
         "temperature control. We use DHL, FedEx or UPS express with tracking, typically 3–7 business days "
         "door to door after dispatch."),
        ("What are the lead time and payment terms?" % (),
         "Stock items usually dispatch in 2–3 business days; bulk or custom fill/finish takes 10–15 business "
         "days. We issue a proforma invoice and accept bank transfer, T/T and Wise, with terms for repeat "
         "buyers reviewed case by case."),
    ]


def all_faqs(p):
    return generic_faqs(p)[:4] + list(p["faqs"])[:2]


def summary_card(p):
    synth = p["form"]
    if p["cat"] != "nad" and p["slug"] not in ("glutathione", "thymalin"):
        synth = "SPPS; " + p["form"]
    rows = [
        ("Product name", p["full_name"]),
        ("CAS number", p["cas"]),
        ("Sequence / formula / MW", p["seq_mw"]),
        ("Purity", p["purity"]),
        ("Synthesis / form", synth),
        ("Stability & storage", p["storage"] + "; " + p["shelf"]),
        ("Supplier", COMPANY),
        ("MOQ", p["moq"]),
    ]
    items = "".join(
        '<div class="summary-item"><div class="summary-label">%s</div><div class="summary-value%s">%s</div></div>'
        % (e(k), " mono" if k in ("CAS number", "Sequence / formula / MW") else "", e(v))
        for k, v in rows
    )
    return f'''<section class="summary-card" aria-labelledby="tech-summary">
  <div class="summary-head"><h2 id="tech-summary">Key Technical &amp; Supplier Summary</h2><span>Reviewed {UPDATED}</span></div>
  <div class="summary-grid">{items}</div>
</section>'''


def product_visual_label(p):
    return f'''<div class="product-visual">{vial_svg(p)}<span class="pv-tag">Vial render · not to scale</span></div>'''


def cite_box(title, path):
    return f'''<div class="cite-box"><strong>Cite this page</strong>
Vivalr. “{e(title)}.” {SITE}{path} (accessed {UPDATED_HUMAN}).</div>'''


def disclaimer():
    return '''<div class="disclaimer"><strong>Research-use disclaimer</strong>
All products on this page are supplied for laboratory research and formulation evaluation only. They are not medicines, food, cosmetics for retail sale, or veterinary products, and are not intended for human or veterinary use. Nothing on this page is a medical claim, dosage recommendation or statement of efficacy. Buyers are responsible for compliance with the laws and regulations of their own jurisdiction.</div>'''
