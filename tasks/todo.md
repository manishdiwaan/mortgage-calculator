# URMortgage — Todo

## Completed

### ✅ P0 — GSC Sitemap Submission — COMPLETE
- [x] Submit sitemap-0.xml (350 pages discovered)
- [x] Update robots.txt to reference sitemap-0.xml
- [ ] Monitor indexing — check July 13

### ✅ P1 — Content Enrichment (FAQ equalisation) — COMPLETE
- [x] India: 24 → 50 FAQs
- [x] United States: 24 → 50 FAQs
- [x] United Kingdom: 24 → 50 FAQs
- [x] UAE: 24 → 50 FAQs
- [x] Singapore: 24 → 50 FAQs
- [x] Canada: 15 → 50 FAQs
- [x] New Zealand: 15 → 50 FAQs
- [x] Germany: 15 → 50 FAQs
- [x] France: 15 → 50 FAQs
- [x] Spain: 15 → 50 FAQs
- [x] Italy: 15 → 50 FAQs
- [x] Netherlands: 15 → 50 FAQs
- [x] Ireland: 15 → 50 FAQs
- [x] Japan: 15 → 50 FAQs
- [x] South Korea: 15 → 50 FAQs
- [x] Hong Kong: 15 → 50 FAQs
- [x] Malaysia: 15 → 50 FAQs
- [x] Thailand: 15 → 50 FAQs
- [x] South Africa: 15 → 50 FAQs
- [x] Brazil: 15 → 50 FAQs
- [x] Mexico: 15 → 50 FAQs
- [x] Saudi Arabia: 15 → 50 FAQs
- [x] Australia: already at 50 ✓

## Next Up
- [ ] P1 — Mobile responsive final tweaks
- [ ] P1 — Airtable + n8n pipeline activation
- [ ] P1 — Multi-language support (12 non-English countries)

### ✅ P1 — Mobile Responsive Tweaks — COMPLETE
- [x] Breadcrumbs — truncate long titles, smaller text on xs screens
- [x] TOC — collapsible on mobile via details/summary
- [x] CTABanner — responsive padding and text sizes
- [x] BlogPost — px-4 sm:px-6, smaller h1 on mobile
- [x] PillarGuide — px-4 sm:px-6, smaller h1, larger FAQ touch targets
- [x] FAQHub — px-4 sm:px-6, smaller h1, larger accordion touch targets
- [x] CountryHub — px-4 sm:px-6
- [x] Country hub page — smaller flag, gap, h1, body text on mobile
- [x] Homepage — smaller country card padding, emoji, CTA button, features gap
- [x] BaseLayout pre-footer ad — px-4 sm:px-6

### ✅ Security Hardening — COMPLETE
- [x] CORS restricted to urmortgage.online on chat API (was wildcard *)
- [x] Rate limiting: 10 req/60s per IP on chat endpoint
- [x] Security headers via _headers file: X-Frame-Options, CSP, Permissions-Policy
- [x] Breadcrumb schema @id now uses absolute URLs (fixes GSC non-critical warning)
- [x] System prompt hardened — prompt injection resistance added
- [x] Chat system prompt updated to cover all 23 countries (was 6)

### Remaining Security (future)
- [ ] Cloudflare WAF custom rule — block non-browser UAs on /api/chat
- [ ] Cloudflare Rate Limiting rule at edge level (upgrade from in-memory)
- [ ] Quarterly security review scheduled

### ✅ Cloudflare WAF Edge Rate Limiting — COMPLETE
- [x] Rate limiting rule: 20 req/10s per IP on /api/chat — Active
- [x] Custom rule: block empty User-Agent on /api/chat — Active
- [x] Both rules verified Active in Cloudflare Security rules dashboard
