# Vivalr — research peptides & NAD+/NMN

Static B2B catalogue for **https://vivalr.com**, built for GitHub + Cloudflare Pages.

- 34 molecules, 69 aggregated pack sizes
- Pure HTML5 + one CSS file + one vanilla JS file (no framework, no build step at deploy time)
- Product, FAQ, Breadcrumb, Organization and WebSite JSON-LD
- `sitemap.xml`, `robots.txt` (AI crawlers allowed), `llms.txt` and `llms-full.txt`
- Quote flow: WhatsApp, `mailto:info@vivalr.com`, copy-to-clipboard — no backend

> **Research use only.** All products are for laboratory research and formulation evaluation. Not for human or veterinary use.

## Repository layout

```text
green/                        # GitHub repository root
├── public/                     # Cloudflare Pages output directory
│   ├── index.html
│   ├── products/
│   │   ├── index.html
│   │   └── [34 product pages].html
│   ├── synthesis-stability.html
│   ├── about.html
│   ├── contact.html
│   ├── privacy.html
│   ├── terms.html
│   ├── 404.html
│   ├── sitemap.xml
│   ├── robots.txt
│   ├── llms.txt
│   ├── llms-full.txt
│   ├── manifest.webmanifest
│   ├── _headers
│   ├── _redirects
│   └── assets/
│       ├── css/style.css
│       ├── js/main.js
│       └── img/                # favicon, logo, 39 OG images
├── src/
│   ├── data.py                 # product single source of truth
│   ├── ui.py                   # shared HTML components + SVG vial
│   ├── build.py                # home, catalogue, product, synthesis pages
│   ├── pages.py                # about, contact, policies, 404, sitemap, llms
│   ├── images.py               # favicons, logo, OG/product cards (Pillow)
│   ├── validate.py             # SEO/link/schema checks
│   └── audit.py                # launch audit
├── PRODUCT-SELECTION.md        # filtering + SKU aggregation decisions
├── requirements.txt
└── README.md
```

## Rebuild locally

Requires Python 3.11+ with Pillow and lxml.

```powershell
pip install -r requirements.txt
python src/pages.py      # regenerate all HTML + sitemap + robots + llms
python src/images.py     # regenerate favicons/logo/OG images
python src/validate.py   # structural SEO checks
python src/audit.py      # launch audit
```

Preview:

```powershell
python -m http.server 8080 --directory public
# open http://127.0.0.1:8080/
```

Cloudflare Pages serves clean URLs (`/products/ghk-cu` from `ghk-cu.html`). The plain Python server does not, so open `/products/ghk-cu.html` directly during local review, or use `npx wrangler pages dev public`.

## Deploy to Cloudflare Pages

1. Push this folder to a GitHub repository (do **not** commit the `public/_preview*.html` debug files — they are deleted).
2. Cloudflare dashboard → **Workers & Pages** → **Create** → **Pages** → **Connect to Git**.
3. Select the repository and configure:
   - **Project name:** `vivalr`
   - **Production branch:** `main`
   - **Framework preset:** `None`
   - **Build command:** leave empty
   - **Build output directory:** `public`
4. Deploy. The `*.pages.dev` preview is only for QA; it is never used in canonical tags, sitemaps or schema.
5. Every push to `main` redeploys automatically. Pull requests get preview URLs.

## Bind `vivalr.com`

> The domain currently points to an existing WordPress installation. Back up the site and database before changing DNS, and lower the TTL on the old records at least an hour in advance.

1. Add the domain to Cloudflare (or use the existing Cloudflare zone).
2. In the Pages project → **Custom domains** → **Set up a domain**:
   - `vivalr.com` (apex)
   - `www.vivalr.com`
3. If the zone is on Cloudflare, Pages creates/verifies the required CNAME automatically. If DNS is external:
   - `CNAME @ → <project>.pages.dev`
   - `CNAME www → <project>.pages.dev`
   - Use CNAME flattening at the apex, or move the nameservers to Cloudflare.
4. Remove the old WordPress `A`/`CNAME` records for `@` and `www` only after the Pages domain shows **Active**.
5. SSL/TLS → **Full (strict)**; enable **Always Use HTTPS**.
6. Add a Redirect Rule: `www.vivalr.com/*` → `https://vivalr.com/$1` (301).
7. Purge Cloudflare cache and verify `https://vivalr.com/`, `/products/ghk-cu`, `/sitemap.xml`, `/robots.txt`, `/llms.txt`.

`_redirects` already handles the old WordPress paths:

```text
/about-us  → /about   301
/contact-us → /contact 301
```

Add more legacy paths there if the old site has indexed blog or product URLs.

## Search & AI discovery checklist

1. **Google Search Console** — add a Domain property for `vivalr.com`, verify by DNS TXT, submit `https://vivalr.com/sitemap.xml`.
2. **Bing Webmaster Tools** — add the site (or import from GSC), submit the sitemap, enable IndexNow.
3. **Yandex Webmaster** — optional, submit the sitemap if you sell into that market.
4. **Rich Results Test** — check the home page and 3 product pages for Product + FAQ validity. The Product offer is quote-based (no public price), so merchant-listing rich results are not expected; the markup remains valid.
5. **Schema Markup Validator** — confirm `Organization`, `WebSite`, `Product`, `FAQPage`, `BreadcrumbList`, `TechArticle`.
6. **PageSpeed Insights** — mobile and desktop; the site ships no web fonts, no analytics and no frameworks.
7. **AI crawlers** — `robots.txt` explicitly allows `GPTBot`, `OAI-SearchBot`, `ChatGPT-User`, `ClaudeBot`, `Claude-Web`, `anthropic-ai`, `PerplexityBot`, `Google-Extended`, `Applebot-Extended`, `CCBot` and `cohere-ai`. `llms.txt` gives a curated index; `llms-full.txt` gives the full product reference.
8. **Request indexing** for the home page, catalogue, synthesis page and the 10 highest-value product pages (GHK-Cu, BPC-157, TB-500, GLOW, KLOW, Snap-8, Matrixyl, Epithalon, NAD+, NMN).
9. **Post-launch QA** — click every WhatsApp and email CTA on mobile, submit the RFQ form with a real mailbox, and verify the 301s from the old WordPress URLs.

## Product data & pricing

`src/data.py` is the single source of truth. Prices from the source workbook are intentionally not published: the site is quote-based, and internal cost bands should never appear in the public HTML.

See `PRODUCT-SELECTION.md` for the filtering rules, duplicate aggregation (GLOW/KLOW/BPC-TB blends/glutathione), the Pancragen 116-vial typo, and the NMN addition (NMN is not in the source workbook and is quote-based from 10 g).
