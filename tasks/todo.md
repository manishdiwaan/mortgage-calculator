# URMortgage — Todo

## Completed This Session

### ✅ P0 — GSC Sitemap Submission
- [x] Submitted sitemap-0.xml (350 pages discovered)
- [x] Updated robots.txt to reference sitemap-0.xml
- [ ] Resubmit sitemap after 29-country expansion

### ✅ P1 — Content Enrichment (FAQ equalisation)
- [x] All 29 countries expanded to 50 FAQs each (1,450 total)

### ✅ P1 — Mobile Responsive Tweaks
- [x] Breadcrumbs, TOC, CTABanner, BlogPost, PillarGuide, FAQHub
- [x] Country hub page, Homepage, BaseLayout pre-footer

### ✅ Security Hardening
- [x] CORS restricted to urmortgage.online
- [x] Rate limiting: 3 layers (Cloudflare edge + in-memory + Turnstile)
- [x] Cloudflare WAF: rate limit rule + empty user-agent block rule
- [x] Turnstile invisible bot challenge on /ask/ page
- [x] Security headers via _headers: HSTS, CSP, X-Frame, Permissions-Policy
- [x] HTML sanitisation + min/max length validation on chat endpoint
- [x] Cookie consent banner (GDPR/APPs compliance)
- [x] Privacy policy updated: Turnstile, Anthropic, Cloudflare disclosures
- [x] Breadcrumb schema absolute URLs (fixes GSC non-critical warning)

### ✅ Platform Expansion — 29 Countries
- [x] Added Belgium, Switzerland, Denmark, Norway, Portugal, Sweden
- [x] Added Thailand, Mexico, Saudi Arabia to calculator (were missing)
- [x] Calculator updated to 29 countries with lenders and rate history
- [x] All count references updated: "29 countries" everywhere
- [x] Chat knowledge base covers all 29 countries
- [x] Calculator region grouping updated with correct categories

## Next Up
- [ ] Resubmit sitemap to GSC (new pages from expansion)
- [ ] Airtable + n8n pipeline activation
- [ ] Multi-language support
