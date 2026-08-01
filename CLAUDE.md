# URMortgage — Project Intelligence File
> This file is the single source of truth for AI assistants working on this project.
> Read this before doing anything. Update it at the end of every session.

---

## Project Identity

**Live URL:** https://urmortgage.online
**Preview URL:** https://mortgage-calculator-4ju.pages.dev
**GitHub:** manishdiwaan/mortgage-calculator
**Owner:** Manish Diwaan (manishdiwaan@gmail.com)
**Hosting:** Cloudflare Pages (auto-deploy from GitHub main branch)
**Domain:** GoDaddy registrar, DNS managed by Cloudflare

---

## What This Project Is

URMortgage.online is a mortgage and property knowledge platform serving **29 countries**. It combines:
- A standalone mortgage repayment calculator (29 countries, 250+ lenders, central bank rate tracking)
- Country-specific SEO content hubs (property buying guides, mortgage guides, blog posts, FAQ hubs)
- An AI-powered Q&A chat at /ask/ powered by Claude API via Cloudflare Pages Function

---

## Credentials (Keep Secure)

| Key | Value |
|-----|-------|
| Anthropic API Key | REDACTED — stored in Cloudflare Pages env as CLAUDE_API_KEY |
| GitHub Token | REDACTED — regenerate at github.com/settings/tokens if needed |
| Cloudflare Turnstile Site Key | 0x4AAAAAADzzRPXoqEJ1oLSB |
| Turnstile Secret Key | In Cloudflare Pages env as TURNSTILE_SECRET_KEY |
| AdSense Publisher ID | ca-pub-1263369613506494 |

**How to work autonomously:**
```bash
cd /home/claude
git clone https://manishdiwaan:YOUR_GITHUB_TOKEN@github.com/manishdiwaan/mortgage-calculator.git repo
cd repo
git pull origin main   # ALWAYS do this first — never work from stale clone
git config user.email "manishdiwaan@gmail.com"
git config user.name "manishdiwaan"
# make changes
git add -A && git commit -m "..." && git push origin main
# Cloudflare auto-deploys in ~15 seconds
```

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Framework | Astro v7 SSG with TypeScript |
| Styling | Tailwind CSS v3 (Precision Finance design tokens) |
| Font | Geist (Google Fonts) |
| Icons | Custom SVG Icon component (responds to text-xl/text-lg via 1em sizing) |
| Charts | Chart.js 4.4.1 (calculator only, via cdnjs.cloudflare.com) |
| PDF Export | jsPDF 2.5.2 + autoTable 3.8.4 (calculator only, via cdnjs) |
| Hosting | Cloudflare Pages |
| DNS/SSL | Cloudflare (full strict) |
| AI Chat | Claude Sonnet 4.6 via Cloudflare Pages Function |
| Bot Protection | Cloudflare Turnstile (invisible, on /ask/ page) |
| Ads | Google AdSense |

**Build command:** `cd src && npm install --legacy-peer-deps && npm run build`
**Build output:** `src/dist`
**Node version:** 22

---

## File Structure

```
repo/
├── CLAUDE.md                        ← YOU ARE HERE — read first every session
├── functions/api/chat.js            ← Cloudflare Pages Function for AI chat
├── src/
│   ├── astro.config.mjs
│   ├── src/
│   │   ├── components/              ← Navbar, Footer, Breadcrumbs, TOC, CTABanner, AdSlot, CookieBanner, Icon
│   │   ├── content/
│   │   │   ├── countries/           ← 29 .md files (one per country)
│   │   │   ├── pillar-guides/       ← 29 dirs × 2 guides = 58 pillar guides
│   │   │   ├── blogs/               ← 29 dirs × 10 posts = 290 blog posts
│   │   │   └── faqs/                ← 29 .md files × 50 FAQs = 1,450 FAQs
│   │   ├── data/countries.ts        ← 29 country definitions (source of truth)
│   │   ├── layouts/                 ← BaseLayout, BlogPost, PillarGuide, FAQHub, CountryHub
│   │   ├── pages/                   ← [country]/index, [country]/blog/[slug], ask, index
│   │   ├── styles/global.css
│   │   └── utils/                   ← schema.ts, seo.ts, links.ts
│   └── public/
│       ├── _headers                 ← Cloudflare security headers (HSTS, CSP, X-Frame)
│       ├── calculator/index.html    ← Standalone calculator — CRITICAL: has own deps, see notes below
│       ├── favicon.svg              ← UR favicon (blue square, white text)
│       ├── favicon.ico
│       ├── privacy/index.html
│       ├── terms/index.html
│       └── robots.txt               ← Points to sitemap-0.xml
├── docs/                            ← Architecture docs and handover files
└── tasks/                           ← backlog.md, todo.md, review.md, lessons.md
```

### CRITICAL — Calculator Standalone File Notes
`src/public/calculator/index.html` is a fully self-contained HTML file. It:
- Has its own nav (Countries/Calculator/Ask URMortgage + Dashboard/Scenarios/Amortisation tabs)
- Loads Material Symbols from `fonts.googleapis.com` + `fonts.gstatic.com`
- Loads Chart.js + jsPDF from `cdnjs.cloudflare.com`
- Loads Tailwind from `cdn.tailwindcss.com`
- Has its own favicon link
- Reads `?country=XX` URL param to pre-select country on load
- ALL these domains must be in `_headers` CSP or the calculator breaks silently

---

## Platform Stats (Current)

| Metric | Count |
|--------|-------|
| Countries | 29 |
| Total Pages (est.) | 420+ |
| Pillar Guides | 58 (2 per country) |
| Blog Posts | 290 (10 per country) |
| FAQ Hubs | 29 × 50 FAQs = 1,450 total |
| Calculator Lenders | 250+ |
| Security Score | 9.0 / 10 |

---

## 29 Countries

**Original 23:** Australia, India, United States, United Kingdom, UAE, Singapore, Canada, New Zealand, Germany, France, Spain, Italy, Netherlands, Ireland, Japan, South Korea, Hong Kong, Malaysia, Thailand, South Africa, Brazil, Mexico, Saudi Arabia

**Added July 2026:** Belgium, Switzerland, Denmark, Norway, Portugal, Sweden

**In countries.ts codes:** AU, IN, US, GB, AE, SG, CA, NZ, DE, FR, ES, IT, NL, IE, JP, KR, HK, MY, TH, ZA, BR, MX, SA, BE, CH, DK, NO, PT, SE

**Calculator CD object:** All 29 codes present — AU, BE, BR, CA, CH, DE, DK, ES, FR, GB, HK, IE, IN, IT, JP, KR, MX, MY, NL, NO, NZ, PT, SA, SE, SG, TH, US, ZA

**Calculator region grouping G:**
- Asia-Pacific: AU, NZ, JP, SG, HK, KR, IN, MY, TH
- North America: US, CA, MX
- Europe: GB, DE, FR, NL, ES, IT, SE, NO, DK, CH, IE, BE, PT
- Middle East & Africa: AE, SA, ZA
- South America: BR

---

## Design System — Precision Finance

| Token | Value | Usage |
|-------|-------|-------|
| Primary | #004ac6 | Action Blue — buttons, links, active states |
| Secondary | #006c49 | Growth Green — positive metrics |
| Surface | #f8f9ff | Light background |
| Dark BG | #0F172A | Dark mode |
| Border | #c3c6d7 | Card borders |
| Font | Geist | All text |
| Card Radius | 16px | Cards, containers |
| Button Radius | 10px | Buttons, CTAs |
| Max Content Width | 720px | Blog/guide body |
| Max Page Width | 1200px | Page container |

---

## SEO Implementation

- Title tags: unique, 50-60 chars, includes country + year
- Meta descriptions: unique, 150-160 chars
- Canonical URLs: absolute https://urmortgage.online/...
- Schema: Article, FAQPage, BreadcrumbList, Organization, WebSite, SoftwareApplication
- Breadcrumb @id: absolute URLs (fixed July 2026)
- Sitemap: sitemap-0.xml (submitted to GSC — needs resubmission after 29-country expansion)
- robots.txt: Allow all, Sitemap: https://urmortgage.online/sitemap-0.xml
- hreflang: NOT YET implemented (needed for multi-language P1)

---

## Security Implementation — 9.0/10

### Layers
1. **Cloudflare edge** — WAF rate limit (20 req/10s on /api/chat), custom rule (block empty User-Agent on /api/chat)
2. **Cloudflare Turnstile** — invisible bot challenge on /ask/ page before chat requests
3. **Pages Function** — in-memory rate limit (10 req/60s per IP), CORS restricted to urmortgage.online, HTML sanitisation, min(3)/max(500) char validation
4. **HTTP Headers** — HSTS, CSP, X-Frame-Options: DENY, Permissions-Policy via src/public/_headers

### CSP Domains (src/public/_headers)
- script-src: self, unsafe-inline, pagead2.googlesyndication.com, partner.googleadservices.com, tpc.googlesyndication.com, googletagmanager.com, google-analytics.com, adservice.google.com, fundingchoicesmessages.google.com, challenges.cloudflare.com, static.cloudflareinsights.com, **cdnjs.cloudflare.com, cdn.tailwindcss.com, ep2.adtrafficquality.google**
- style-src: self, unsafe-inline, **fonts.googleapis.com**
- font-src: self, **fonts.gstatic.com**
- frame-src: googleads.g.doubleclick.net, tpc.googlesyndication.com, fundingchoicesmessages.google.com, challenges.cloudflare.com, **ep2.adtrafficquality.google, www.google.com**

### Chat API (functions/api/chat.js)
- CORS: allowed origins = urmortgage.online, www.urmortgage.online, mortgage-calculator-4ju.pages.dev
- Rate limiting: 10 req/60s per CF-Connecting-IP (in-memory)
- Turnstile: verifies token server-side if TURNSTILE_SECRET_KEY is set
- Input: strips HTML tags, control chars, validates 3-500 chars
- System prompt: covers all 29 countries, anti-jailbreak rules

### Cloudflare WAF Rules
| Type | Name | Rule | Status |
|------|------|------|--------|
| Rate Limiting | Chat API rate limit | URI Path = /api/chat → 20 req/10s → Block | Active |
| Custom | Block empty user agents | URI Path = /api/chat AND User-Agent = "" → Block | Active |

---

## Google Search Console

- Property: urmortgage.online
- Sitemap submitted: sitemap-0.xml
- Discovered pages: 350 (needs resubmission — 29-country expansion added ~70 more pages)
- **TODO:** Resubmit sitemap-0.xml in GSC

---

## Content Pipeline (Ready, Not Yet Connected)

- `scripts/prompts/` — brief generator, pillar guide, blog post, FAQ hub prompt templates
- `scripts/n8n/` — brief-generator.json and content-pipeline.json workflow files
- Airtable schema: documented in `docs/airtable-setup.md`
- n8n workflow: reads Airtable → Claude API → GitHub commit → auto-deploy
- **To activate:** Connect n8n to Airtable, configure GitHub PAT in n8n, set ANTHROPIC_API_KEY in n8n workflow

---

## Monetisation

| Stream | Status | Notes |
|--------|--------|-------|
| Google AdSense | Active | 700+ placements, ca-pub-1263369613506494 |
| Affiliate Links | Planned P3 | On lender names in calculator |
| Lead Generation | Planned P3 | "Get a Quote" form |
| Rate Alert Emails | Planned P3 | Email capture for rate changes |

---

## Backlog

### P1 — Do Next
- [ ] Resubmit sitemap-0.xml to GSC (29-country expansion)
- [ ] Airtable + n8n pipeline activation
- [ ] Multi-language support for non-English countries

### P2 — Track
- [ ] Content refresh automation (flag pages older than 6 months)
- [ ] Competitor benchmarking
- [ ] KPI dashboard (organic traffic, rankings, CTR, backlinks)

### P3 — Future
- [ ] Affiliate links on lender names in calculator
- [ ] Lead generation form ("Get a Quote")
- [ ] Email list for rate alerts
- [ ] Lender comparison view
- [ ] Stamp duty calculator
- [ ] Live rate API integration

### P4 — Long Term
- [ ] User accounts with login
- [ ] Saved comparisons
- [ ] Personalised rate tracking

---

## Lessons Learned (Apply Every Session)

**L001 — GSC Sitemap:** Always submit `sitemap-0.xml` directly to GSC for Astro sites. robots.txt must reference it too.

**L002 — Read Docs Thoroughly:** Read every subsection, preserve original structure (priority tiers, numbering).

**L003 — FAQ Generation via API:** One country per API call. max_tokens=2500. Top up in multiple passes. Always verify count: `grep -c "question:"`.

**L004 — Work Autonomously:** With API key and GitHub token — clone repo, generate, commit, push. Only interrupt Manish for decisions, not execution.

**L005 — Security Defaults:** Always restrict CORS to known origins. Static sites need _headers for HTTP security headers.

**L006 — Platform vs Calculator Alignment:** When adding countries, cross-check calculator CD object and region grouping G.
```bash
python3 -c "import re; c=open('src/public/calculator/index.html').read(); print(sorted(set(re.findall(r'\b([A-Z]{2})\s*:\s*\{n:', c))))"
```

**L007 — Check Before Building:** Always diff calculator countries vs platform countries.ts before expansion.

**L008 — Shell Heredoc Quoting:** Bold markdown and special chars break zsh heredocs. Use Python file writes instead.

**L009 — Update CLAUDE.md Every Session:** This file is the project memory. Always update before ending.

**L010 — ALWAYS git pull first:** `git pull origin main` before ANY changes. Never work from a stale clone. Stale push overwrote 3 commits and broke the entire site in Session 2.

**L011 — Calculator is a Standalone File:** `src/public/calculator/index.html` has its own external dependencies (Material Symbols, Chart.js, jsPDF, Tailwind CDN). All must be in CSP _headers or calculator breaks silently. Never assume Astro build settings apply to it.

**L012 — Screenshot Before Next Change:** Never push a fix and immediately push another. Get screenshot confirmation the fix worked first.

**L013 — Icon Component Sizing:** The custom Icon.astro SVG component uses `width="1em" height="1em"` so it responds to Tailwind text-xl/text-lg classes. Never use w-/h- classes on Icon — use text-xl, text-lg etc.

---

## Key Commands Reference

```bash
# Start of every session — clone fresh and pull
cd /home/claude
git clone https://manishdiwaan:YOUR_GITHUB_TOKEN@github.com/manishdiwaan/mortgage-calculator.git repo
cd repo
git pull origin main

# Check FAQ counts
for f in src/src/content/faqs/*.md; do echo "$(basename $f .md): $(grep -c 'question:' $f)"; done

# Check calculator countries (should be 29)
python3 -c "import re; c=open('src/public/calculator/index.html').read(); keys=set(re.findall(r'\b([A-Z]{2})\s*:\s*\{n:', c)); print(len(keys), sorted(keys))"

# Check platform country count (should be 29)
ls src/src/content/countries/ | wc -l

# Trigger redeploy without changes
git commit --allow-empty -m "chore: trigger redeploy" && git push origin main

# Run build locally to check for errors
cd src && npm install --legacy-peer-deps && npm run build
```

---

## Session History

### Session 1 — July 11, 2026
- P0: GSC sitemap — submitted sitemap-0.xml, 350 pages discovered
- P1: FAQ equalisation — all 29 countries at 50 FAQs (1,450 total)
- P1: Mobile responsive tweaks — 10 files updated
- Security hardening — CORS, WAF, Turnstile, HSTS, CSP, cookie consent (9.0/10)
- Platform expansion — Belgium, Switzerland, Denmark, Norway, Portugal, Sweden (23→29)
- Calculator fixed — TH, MX, SA added; all 29 aligned
- Chat knowledge base expanded to all 29 countries

### Session 2 — August 2026
- Fixed Icon SVG sizing — `width="1em" height="1em"` so text-xl/text-lg works
- Standardised calculator nav — Countries/Calculator/Ask URMortgage + Dashboard/Scenarios/Amortisation tabs
- Fixed CSP — added Google Fonts, cdnjs, Tailwind CDN, adtrafficquality to correct directives
- Added favicon to calculator page
- Added URL param country pre-selection to calculator (?country=XX)
- Added Export CSV/PDF to Scenarios tab
- Removed ad gap in Dashboard — Calculate button moved under Apply All Rates
- Fixed Dashboard tab not highlighted on load
- **Key mistakes:** Worked from stale clone, overwrote 3 commits, broke site. Never again — L010.
