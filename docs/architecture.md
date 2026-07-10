# URMortgage.online — Technical Architecture

Version: 2.0 | July 2026

---

## 1. System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                     CONTENT PIPELINE                            │
│                                                                 │
│  Airtable ──→ Claude/ChatGPT API ──→ Markdown (.md) files      │
│  (Briefs)     (Generate content)      (Astro content collections)│
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                     BUILD & DEPLOY                              │
│                                                                 │
│  GitHub Repo ──→ Cloudflare Pages ──→ urmortgage.online         │
│  (Push to main)  (Auto-build Astro)   (CDN edge delivery)      │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                     TRACKING                                    │
│                                                                 │
│  Google Search Console ◄──► Cloudflare Analytics ──→ Airtable   │
│  (Rankings, indexing)       (Traffic, Core Web Vitals)  (KPIs)  │
└─────────────────────────────────────────────────────────────────┘
```

## 2. Current State (v1)

| Aspect | Detail |
|--------|--------|
| App | Single index.html (~900 lines), Tailwind + Chart.js + jsPDF |
| Hosting | GitHub Pages (manishdiwaan/mortgage-calculator) |
| Domain | GoDaddy DNS → GitHub Pages A records |
| SSL | Let's Encrypt via GitHub Pages |
| Pages | 3 total (index.html, privacy.html, terms.html) |
| SEO | Basic meta tags, JSON-LD, sitemap with 3 URLs |

## 3. Target State (v2)

| Aspect | Detail |
|--------|--------|
| Framework | Astro SSG with TypeScript |
| Hosting | Cloudflare Pages (auto-build from GitHub) |
| Domain | GoDaddy DNS → Cloudflare Pages (CNAME) |
| SSL | Cloudflare (automatic) |
| Pages | 300+ (23 countries × 13 pages each + shared pages) |
| Content | Markdown in Astro content collections with Zod schemas |
| SEO | Full schema markup, auto-sitemap, internal linking, hreflang |

## 4. Site Information Architecture

```
urmortgage.online/
├── (home)                              ← Global landing page
├── calculator/                         ← Existing calculator (Astro island)
├── privacy/
├── terms/
│
├── australia/                          ← Country Hub landing page
│   ├── property-buying-guide/          ← Pillar Guide 1
│   ├── mortgage-guide/                 ← Pillar Guide 2
│   ├── blog/
│   │   ├── first-home-buyer-guide/     ← Blog post
│   │   ├── stamp-duty-explained/
│   │   ├── ...                         ← (10 blogs per country)
│   ├── faqs/                           ← FAQ Hub
│   ├── loan-products/                  ← Loan Products listing
│   └── market-news/                    ← Market News
│
├── india/                              ← Same structure
├── united-states/
├── united-kingdom/
├── uae/
├── singapore/
└── ... (17 more countries later)
```

## 5. Astro Project Structure

```
urmortgage/
├── astro.config.mjs                    ← Astro config + integrations
├── tailwind.config.mjs                 ← Precision Finance design tokens
├── tsconfig.json
├── package.json
│
├── public/
│   ├── robots.txt
│   ├── llms.txt
│   ├── favicon.ico
│   └── images/
│       ├── countries/                  ← Country hero images
│       └── blog/                       ← Blog post images
│
├── src/
│   ├── content/
│   │   ├── config.ts                   ← Collection schemas (Zod)
│   │   ├── countries/
│   │   │   ├── australia.md
│   │   │   ├── india.md
│   │   │   └── ...
│   │   ├── pillar-guides/
│   │   │   ├── australia-property-buying-guide.md
│   │   │   ├── australia-mortgage-guide.md
│   │   │   └── ...
│   │   ├── blogs/
│   │   │   ├── australia-first-home-buyer-guide.md
│   │   │   └── ...
│   │   └── faqs/
│   │       ├── australia.md            ← 50 FAQs per file
│   │       └── ...
│   │
│   ├── layouts/
│   │   ├── BaseLayout.astro            ← HTML head, nav, footer, schema
│   │   ├── CountryHub.astro
│   │   ├── PillarGuide.astro
│   │   ├── BlogPost.astro
│   │   └── FAQHub.astro
│   │
│   ├── components/
│   │   ├── Navbar.astro                ← Shared nav with country selector
│   │   ├── Footer.astro
│   │   ├── Breadcrumbs.astro           ← Auto breadcrumb + schema
│   │   ├── TOC.astro                   ← Table of contents for pillar guides
│   │   ├── FAQAccordion.astro          ← FAQ with FAQ schema
│   │   ├── CTABanner.astro             ← Reusable call-to-action
│   │   ├── RelatedPosts.astro          ← Internal linking component
│   │   ├── SchemaOrg.astro             ← JSON-LD renderer
│   │   ├── AdSlot.astro                ← AdSense component
│   │   └── Calculator.astro            ← Island: existing calculator
│   │
│   ├── pages/
│   │   ├── index.astro                 ← Home page
│   │   ├── calculator.astro            ← Calculator page
│   │   ├── privacy.astro
│   │   ├── terms.astro
│   │   └── [country]/
│   │       ├── index.astro             ← Country hub (dynamic)
│   │       ├── property-buying-guide.astro
│   │       ├── mortgage-guide.astro
│   │       ├── faqs.astro
│   │       ├── loan-products.astro
│   │       ├── market-news.astro
│   │       └── blog/
│   │           └── [slug].astro        ← Blog post (dynamic)
│   │
│   ├── data/
│   │   ├── countries.ts                ← Country metadata (code, name, currency, flag)
│   │   ├── lenders.ts                  ← Lender data (from existing calculator)
│   │   └── rates.ts                    ← Central bank rates (from existing calculator)
│   │
│   └── utils/
│       ├── schema.ts                   ← JSON-LD generators
│       ├── links.ts                    ← Internal linking matrix logic
│       └── seo.ts                      ← Meta tag helpers
│
└── scripts/
    ├── generate-briefs.ts              ← AI content brief generator
    ├── generate-content.ts             ← AI content generator (Claude/ChatGPT)
    ├── validate-links.ts              ← Internal link matrix validator
    └── publish.sh                      ← Batch publish + git push
```

## 6. Content Collection Schemas

### Country Hub
```typescript
{
  country: string           // "Australia"
  code: string              // "australia" (URL slug)
  iso: string               // "AU"
  currency: string          // "AUD"
  currencySymbol: string    // "$"
  flag: string              // "🇦🇺"
  language: string          // "en"
  metaTitle: string
  metaDescription: string
  heroImage: string
  region: string            // "Asia-Pacific"
}
```

### Pillar Guide
```typescript
{
  title: string
  country: string           // reference to country code
  slug: string
  type: "property-buying" | "mortgage"
  metaTitle: string
  metaDescription: string
  primaryKeyword: string
  secondaryKeywords: string[]
  publishDate: Date
  lastUpdated: Date
  wordCount: number
  faqs: { question: string, answer: string }[]
  relatedBlogs: string[]    // slug references
}
```

### Blog Post
```typescript
{
  title: string
  country: string
  slug: string
  category: string          // "first-home" | "costs" | "taxes" | etc.
  metaTitle: string
  metaDescription: string
  primaryKeyword: string
  secondaryKeywords: string[]
  publishDate: Date
  lastUpdated: Date
  wordCount: number
  heroImage: string
  imageAlt: string
  relatedPosts: string[]
}
```

### FAQ
```typescript
{
  country: string
  faqs: {
    question: string
    answer: string
    category: string
  }[]
}
```

## 7. Schema Markup Strategy

| Page Type | Schema Types |
|-----------|-------------|
| Home | Organization, WebSite, SoftwareApplication |
| Country Hub | WebPage, BreadcrumbList |
| Pillar Guide | Article, FAQPage, BreadcrumbList |
| Blog Post | Article, BreadcrumbList |
| FAQ Hub | FAQPage, BreadcrumbList |
| Calculator | SoftwareApplication, BreadcrumbList |

## 8. Internal Linking Matrix

| From | Links To |
|------|----------|
| Country Hub | Both pillars, all 10 blogs, FAQ hub, calculator, loan products, market news |
| Pillar Guide | All 10 blogs, FAQ hub, calculator, loan products, other pillar |
| Blog Post | Both pillars, FAQ hub, calculator, loan products, 2 related blogs |
| FAQ Hub | Both pillars, calculator, loan products |
| Calculator | Country hub, both pillars |

## 9. Airtable Base Design

### Tables

**Content Inventory** (primary tracking table)
- Country (single select)
- URL (formula from slug)
- Title (text)
- Content Type (single select: hub/pillar/blog/faq)
- Primary Keyword (text)
- Search Intent (single select: informational/transactional/navigational)
- Status (single select: Brief/Draft/Review/Published/Refresh)
- Word Count (number)
- Publish Date (date)
- Last Updated (date)
- Links In (number)
- Links Out (number)
- Backlinks (number)
- Priority (single select: P0/P1/P2/P3)

**Content Briefs** (linked to Content Inventory)
- Linked Content (link to Content Inventory)
- Target Audience (text)
- Outline / H2s (long text)
- FAQs to Include (long text)
- CTA (text)
- Reference URLs (long text)
- Internal Links Required (long text)
- Schema Type (single select)

**Editorial Calendar** (calendar view of Content Inventory)
- Grouped by Country, filtered by Status

**KPI Tracking** (weekly snapshots)
- Country (single select)
- Week (date)
- Organic Traffic (number)
- Impressions (number)
- Clicks (number)
- Avg Position (number)
- Indexed Pages (number)
- Backlinks (number)

**Competitor Benchmark**
- Country (single select)
- Competitor (text)
- Structure Score (number 1-10)
- Content Depth Score (number 1-10)
- FAQs (checkbox)
- Calculator (checkbox)
- Schema (checkbox)
- Notes (long text)

## 10. Deployment Pipeline

```
Developer / AI generates .md content
        ↓
Content placed in src/content/{collection}/
        ↓
Git commit + push to main branch
        ↓
Cloudflare Pages detects push
        ↓
Astro build runs (SSG — generates static HTML)
        ↓
Built files deployed to Cloudflare CDN edge
        ↓
Live at urmortgage.online within 1-2 minutes
```

## 11. Migration Plan (GitHub Pages → Cloudflare Pages)

1. Create Cloudflare Pages project linked to manishdiwaan/mortgage-calculator
2. Configure build: Framework = Astro, Build command = `npm run build`, Output = `dist/`
3. Add custom domain urmortgage.online in Cloudflare Pages
4. Update GoDaddy DNS:
   - Remove A records (185.199.108-111.153)
   - Add CNAME @ → urmortgage-online.pages.dev
   - Keep CNAME www → urmortgage-online.pages.dev
5. Verify SSL auto-provisions on Cloudflare
6. Test existing calculator still works
7. Remove CNAME file from repo
8. Update GitHub repo settings (disable Pages)

## 12. Performance Targets

| Metric | Target |
|--------|--------|
| Lighthouse Performance | 95+ |
| Lighthouse SEO | 100 |
| First Contentful Paint | < 1.0s |
| Largest Contentful Paint | < 1.5s |
| Cumulative Layout Shift | < 0.05 |
| Time to Interactive | < 1.5s |
| Page Size (blog) | < 100KB |
| Page Size (calculator) | < 500KB (JS-heavy island) |
