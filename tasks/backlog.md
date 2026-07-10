# URMortgage.online — Master Backlog

Generated: July 2026 | Source: Project Handover v2 + SEO Playbook v2

---

## CATEGORY 1: SEO PLATFORM BUILD (Playbook)

### 1.1 Site Architecture Expansion
- [ ] BL-001 — Astro SSG project scaffold with content collections
- [ ] BL-002 — Cloudflare Pages deployment pipeline (replace GitHub Pages)
- [ ] BL-003 — DNS migration from GoDaddy→GitHub Pages to GoDaddy→Cloudflare Pages
- [ ] BL-004 — Country Hub landing page template
- [ ] BL-005 — Pillar Guide page template (2,000–3,000 words, TOC, FAQs, schema, CTAs)
- [ ] BL-006 — Blog post page template (1,200–1,800 words, schema, CTAs)
- [ ] BL-007 — FAQ Hub page template (30–50 FAQs, featured snippet optimised)
- [ ] BL-008 — Market News section template
- [ ] BL-009 — Shared navbar with country selector + content navigation
- [ ] BL-010 — Shared footer with internal links, legal, sitemap
- [ ] BL-011 — Breadcrumb component with BreadcrumbList schema
- [ ] BL-012 — Migrate existing calculator (index.html) into Astro as interactive island
- [ ] BL-013 — Affordability calculator page per country
- [ ] BL-014 — Loan Products listing page per country

### 1.2 Content for Pilot Countries (AU, IN, US, UK, UAE, SG)
- [ ] BL-020 — Australia: landing page, 2 pillar guides, 10 blogs, FAQ hub
- [ ] BL-021 — India: landing page, 2 pillar guides, 10 blogs, FAQ hub
- [ ] BL-022 — United States: landing page, 2 pillar guides, 10 blogs, FAQ hub
- [ ] BL-023 — United Kingdom: landing page, 2 pillar guides, 10 blogs, FAQ hub
- [ ] BL-024 — UAE: landing page, 2 pillar guides, 10 blogs, FAQ hub
- [ ] BL-025 — Singapore: landing page, 2 pillar guides, 10 blogs, FAQ hub

### 1.3 SEO Technical Implementation
- [ ] BL-030 — URL structure per playbook: /country/, /country/property-buying-guide, etc.
- [ ] BL-031 — Metadata automation (SEO title, meta description, H1, H2s, ALT text)
- [ ] BL-032 — Article schema (JSON-LD) on all blog posts
- [ ] BL-033 — FAQ schema (JSON-LD) on all FAQ hubs + pillar guides
- [ ] BL-034 — BreadcrumbList schema on all pages
- [ ] BL-035 — Organization + WebSite schema (extend existing)
- [ ] BL-036 — Auto-generated sitemap.xml (Astro sitemap plugin) for all pages
- [ ] BL-037 — robots.txt update for expanded site
- [ ] BL-038 — Canonical URLs on all pages
- [ ] BL-039 — Open Graph + Twitter Card meta on all pages
- [ ] BL-040 — hreflang tags for multi-country (same language) disambiguation

### 1.4 Internal Linking Matrix
- [ ] BL-050 — Every blog → both pillar guides + FAQ + calculator + 2 related blogs
- [ ] BL-051 — Every pillar → all blogs + FAQ + calculators + products
- [ ] BL-052 — Country hub → everything in that country
- [ ] BL-053 — Internal linking automation script (validates and reports broken/missing links)

### 1.5 Backlink Strategy (Manual/Ongoing)
- [ ] BL-060 — Identify government portals, central banks, property regulators per country
- [ ] BL-061 — University outreach list
- [ ] BL-062 — Relocation blog outreach list
- [ ] BL-063 — Finance publication guest post targets
- [ ] BL-064 — HARO / digital PR signup
- [ ] BL-065 — Original data reports as linkable assets (e.g., "Mortgage Affordability Index")
- [ ] BL-066 — Calculator pages as linkable assets (submit to resource pages)

---

## CATEGORY 2: CONTENT AUTOMATION PIPELINE

### 2.1 Airtable Master Inventory
- [ ] BL-100 — Airtable base: Content Inventory table (Country, URL, Title, Keyword, Intent, Status, Author, Publish Date, Last Updated, Links In, Links Out, Backlinks, Priority)
- [ ] BL-101 — Airtable base: Editorial Calendar view (phased rollout, pillar first)
- [ ] BL-102 — Airtable base: Content Brief table (Audience, Intent, Keywords, Outline, FAQs, References, CTA, Internal/External Links, Schema, Word Count)
- [ ] BL-103 — Airtable base: Competitor Benchmark table
- [ ] BL-104 — Airtable base: KPI Tracking table

### 2.2 AI Content Generation Pipeline
- [ ] BL-110 — Content brief generator prompt (Claude/ChatGPT)
- [ ] BL-111 — Pillar guide generator prompt with TOC, FAQs, schema, CTAs
- [ ] BL-112 — Blog post generator prompt with metadata, internal links, schema
- [ ] BL-113 — FAQ generator prompt targeting featured snippets + voice search
- [ ] BL-114 — Metadata/schema generator prompt (title, description, JSON-LD)
- [ ] BL-115 — Fact-checking pass prompt (verify rates, regulations, lender info)
- [ ] BL-116 — Internal link injection prompt (add contextual links per matrix)
- [ ] BL-117 — Content optimization prompt (readability, keyword density, headings)

### 2.3 Publishing Automation
- [ ] BL-120 — Markdown file generator (AI output → Astro-compatible .md with frontmatter)
- [ ] BL-121 — Git auto-commit + push script (new content → deploy)
- [ ] BL-122 — Image sourcing/generation pipeline (hero images, infographics)
- [ ] BL-123 — Bulk publishing script (batch process briefs → drafts → markdown → deploy)

---

## CATEGORY 3: TRACKING & ANALYTICS

- [ ] BL-200 — Google Search Console setup for expanded site
- [ ] BL-201 — Cloudflare Web Analytics integration
- [ ] BL-202 — KPI dashboard: organic traffic, rankings, CTR, backlinks, indexed pages
- [ ] BL-203 — Core Web Vitals monitoring
- [ ] BL-204 — Content refresh tracking (flag pages older than 6 months)
- [ ] BL-205 — Competitor benchmark tracking (structure, depth, FAQs, calculators, schema)

---

## CATEGORY 4: EXISTING BACKLOG (from Handover Doc)

### 4.1 Revenue
- [ ] BL-300 — Affiliate links on lender names
- [ ] BL-301 — Lead generation ("Get a Quote" form)
- [ ] BL-302 — Email list for rate change alerts

### 4.2 Features
- [ ] BL-310 — Side-by-side lender comparison view
- [ ] BL-311 — Loan comparison (compare 2-3 scenarios)
- [ ] BL-312 — Live rate API integration
- [ ] BL-313 — SRI hashes on CDN scripts
- [ ] BL-314 — Stamp duty / transfer tax calculator
- [ ] BL-315 — Multi-language support
- [ ] BL-316 — User accounts with login

### 4.3 Growth
- [ ] BL-320 — Google Search Console sitemap submission
- [ ] BL-321 — AdSense scaling across new pages

---

## CATEGORY 5: REMAINING COUNTRIES (Post-Pilot)

- [ ] BL-400 — Scale to remaining 17 countries (from 23-country list)
- [ ] BL-401 — 34 additional pillar guides
- [ ] BL-402 — 170 additional blog posts
- [ ] BL-403 — 17 additional FAQ hubs
- [ ] BL-404 — Country-specific calculators and loan products

---

## PRIORITY MATRIX

| Priority | Items | Rationale |
|----------|-------|-----------|
| P0 — Now | BL-001 to BL-012, BL-030 to BL-040 | Platform scaffold must exist before content |
| P1 — Next | BL-100 to BL-117, BL-020 to BL-025 | Pipeline + pilot content |
| P2 — Soon | BL-050 to BL-053, BL-120 to BL-123 | Linking + publishing automation |
| P3 — Track | BL-200 to BL-205, BL-300 to BL-321 | Analytics + revenue + features |
| P4 — Scale | BL-400 to BL-404 | Remaining countries after pilot proves model |
