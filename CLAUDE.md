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
git clone https://manishdiwaan:REDACTED — regenerate at github.com/settings/tokens if needed@github.com/manishdiwaan/mortgage-calculator.git repo
cd repo
# make changes
git config user.email "manishdiwaan@gmail.com"
git config user.name "manishdiwaan"
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
| Icons | Material Symbols Outlined |
| Charts | Chart.js 4.4.1 (calculator only) |
| PDF Export | jsPDF 2.5.2 + autoTable 3.8.4 (calculator only) |
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
│   │   ├── components/              ← Navbar, Footer, Breadcrumbs, TOC, CTABanner, AdSlot, CookieBanner
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
│       ├── calculator/index.html    ← Standalone calculator (DO NOT MODIFY structure)
│       ├── privacy/index.html
│       ├── terms/index.html
│       └── robots.txt               ← Points to sitemap-0.xml
├── docs/                            ← Architecture docs and handover files
└── tasks/                           ← backlog.md, todo.md, review.md, lessons.md
```

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
| Ad Placements | 700+ |
| Security Score | 9.0 / 10 |
| Internal Links | 13,597+ (validated) |

---

## 29 Countries

**Original 23:** Australia, India, United States, United Kingdom, UAE, Singapore, Canada, New Zealand, Germany, France, Spain, Italy, Netherlands, Ireland, Japan, South Korea, Hong Kong, Malaysia, Thailand, South Africa, Brazil, Mexico, Saudi Arabia

**Added July 2026:** Belgium, Switzerland, Denmark, Norway, Portugal, Sweden

**In countries.ts codes:** AU, IN, US, GB, AE, SG, CA, NZ, DE, FR, ES, IT, NL, IE, JP, KR, HK, MY, TH, ZA, BR, MX, SA, BE, CH, DK, NO, PT, SE

**Calculator CD object:** All 29 codes present — AU, BE, BR, CA, CH, DE, DK, ES, FR, GB, HK, IE, IN, IT, JP, KR, MX, MY, NL, NO, NZ, PT, SA, SE, SG, TH, US, ZA (+ region grouping G updated)

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
- Sitemap: sitemap-0.xml (submitted to GSC — 350 pages, resubmit after expansion)
- robots.txt: Allow all, Sitemap: https://urmortgage.online/sitemap-0.xml
- hreflang: NOT YET implemented (needed for multi-language P1)

---

## Security Implementation — 9.0/10

### Layers
1. **Cloudflare edge** — WAF rate limit (20 req/10s on /api/chat), custom rule (block empty User-Agent on /api/chat)
2. **Cloudflare Turnstile** — invisible bot challenge on /ask/ page before chat requests
3. **Pages Function** — in-memory rate limit (10 req/60s per IP), CORS restricted to urmortgage.online, HTML sanitisation, min(3)/max(500) char validation
4. **HTTP Headers** — HSTS, CSP (includes Turnstile + AdSense domains), X-Frame-Options: DENY, Permissions-Policy via src/public/_headers

### Chat API (functions/api/chat.js)
- CORS: allowed origins = urmortgage.online, www.urmortgage.online, mortgage-calculator-4ju.pages.dev
- Rate limiting: 10 req/60s per CF-Connecting-IP (in-memory)
- Turnstile: verifies token via challenges.cloudflare.com/turnstile/v0/siteverify if TURNSTILE_SECRET_KEY is set
- Input: strips HTML tags, control chars, trims whitespace, validates 3-500 chars
- System prompt: hardcoded server-side, covers all 29 countries, anti-jailbreak rules
- Fail-loud: console.error if CLAUDE_API_KEY missing

### Cloudflare WAF Rules (Security → Security rules)
| Type | Name | Rule | Status |
|------|------|------|--------|
| Rate Limiting | Chat API rate limit | URI Path = /api/chat → 20 req/10s → Block | Active |
| Custom | Block empty user agents | URI Path = /api/chat AND User-Agent = "" → Block | Active |

### Privacy
- Cookie consent banner on all pages (CookieBanner.astro)
- Privacy policy covers: AdSense, Turnstile (with Privacy Addendum reference), Anthropic Claude, Cloudflare CDN
- Last updated: July 11, 2026

---

## Google Search Console

- Property: urmortgage.online
- Sitemap submitted: sitemap-0.xml
- Discovered pages: 350 (as of July 11 2026 — needs resubmission after 29-country expansion adds ~70 more pages)
- Homepage live URL test: passes
- **TODO:** Resubmit sitemap-0.xml in GSC after expansion build deploys

---

## Content Pipeline (Ready, Not Yet Connected)

All components built, none activated:
- `scripts/prompts/` — brief generator, pillar guide, blog post, FAQ hub prompt templates
- `scripts/n8n/` — brief-generator.json and content-pipeline.json workflow files
- Airtable schema: documented in `docs/airtable-setup.md` (Content Queue table)
- n8n workflow: reads Airtable → Claude API → GitHub commit → auto-deploy

**To activate:** Connect n8n to Airtable, configure GitHub PAT in n8n, set ANTHROPIC_API_KEY in n8n workflow. See `docs/airtable-setup.md` and `docs/n8n-setup.md`.

---

## Monetisation

| Stream | Status | Notes |
|--------|--------|-------|
| Google AdSense | Active | 700+ placements, ca-pub-1263369613506494 |
| Affiliate Links | Planned P3 | On lender names in calculator |
| Lead Generation | Planned P3 | "Get a Quote" form |
| Rate Alert Emails | Planned P3 | Email capture for rate changes |

---

## Remaining Backlog

### P1 — Do Next
- [ ] Resubmit sitemap-0.xml to GSC (new pages from 29-country expansion)
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

**L002 — Read Docs Thoroughly:** When summarising structured documents, read every subsection and preserve original structure (priority tiers, numbering).

**L003 — FAQ Generation via API:** One country per API call. max_tokens=2500. Top up in multiple passes of 10-15. Always verify count after each call with `grep -c "question:"`.

**L004 — Work Autonomously:** With ANTHROPIC_API_KEY and GITHUB_TOKEN available — clone repo, generate, commit, push without asking Manish. Only interrupt for decisions, not execution.

**L005 — Security Defaults:** Always restrict CORS to known origins. static sites need _headers file for HTTP security headers — meta tags alone are insufficient.

**L006 — Platform vs Calculator Alignment:** When adding countries to SEO platform, always cross-check calculator CD object and region grouping G. Run: `python3 -c "import re; c=open('src/public/calculator/index.html').read(); print(sorted(set(re.findall(r'\b([A-Z]{2})\s*:\s*\{n:', c))))"` to verify.

**L007 — Check Before Building:** Always diff calculator countries vs platform countries.ts before expansion work to catch gaps in both directions.

**L008 — Shell Heredoc Quoting:** Bold markdown (`**text**`) and special chars break zsh heredocs. Use `echo` with single quotes or Python file writes for content with markdown formatting.

**L009 — Update CLAUDE.md Every Session:** This file is the project memory. Always update it before ending a session — backlog changes, lessons learned, new credentials, architectural decisions.

---

## Key Commands Reference

```bash
# Clone and work
git clone https://manishdiwaan:YOUR_GITHUB_TOKEN@github.com/manishdiwaan/mortgage-calculator.git repo

# Check FAQ counts
for f in repo/src/src/content/faqs/*.md; do echo "$(basename $f .md): $(grep -c 'question:' $f)"; done

# Check calculator countries
python3 -c "import re; c=open('repo/src/public/calculator/index.html').read(); keys=set(re.findall(r'\b([A-Z]{2})\s*:\s*\{n:', c)); print(len(keys), sorted(keys))"

# Check country count in platform
ls repo/src/src/content/countries/ | wc -l

# Trigger redeploy without changes
git commit --allow-empty -m "chore: trigger redeploy" && git push origin main
```

---

## Session History

### Session 1 — July 11, 2026
**What was done:**
- P0: GSC sitemap — submitted sitemap-0.xml, 350 pages discovered, robots.txt updated
- P1: FAQ equalisation — all 29 countries at 50 FAQs (1,450 total)
- P1: Mobile responsive tweaks — 10 files updated across all layouts and components
- Security hardening — CORS, WAF, Turnstile, HSTS, CSP, cookie consent, privacy policy (9.0/10)
- Platform expansion — added Belgium, Switzerland, Denmark, Norway, Portugal, Sweden (23→29 countries)
- Calculator fixed — TH, MX, SA added to calculator; all 29 now aligned across platform + calculator
- Chat knowledge base — expanded to all 29 countries with country-specific rules and terminology
- Handover v4.0 created

**Commits this session:**
- `9861794` — fix: robots.txt sitemap ref + project OS
- `e79516d` — feat: expand all 22 country FAQs to 50 questions
- `7bbfd9a` — fix: mobile responsive tweaks
- `b5a7276` — security: CORS, rate limiting, security headers, breadcrumb schema
- `4aeade1` — security: Turnstile, HTML sanitisation, HSTS, cookie consent
- `ef5808d` — legal: privacy policy updated for Turnstile invisible mode
- `b0e8a5c` — feat: chat knowledge base expanded to 29 countries
- `b09bf08` — feat: expand platform to 29 countries
- `60e8bb0` — chore: update full project OS
- `e6f1b1d` — docs: handover v4.0

**Pending from this session:**
- Resubmit sitemap-0.xml to GSC (new pages from expansion not yet crawled)
