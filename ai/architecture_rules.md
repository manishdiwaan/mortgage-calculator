# Architecture Rules — URMortgage.online

These rules are binding. All code, content, and configuration must comply.

---

## 1. URL Rules

- All URLs lowercase, hyphenated, no trailing slashes in code (Astro handles trailing slash config)
- Country slugs are full names: `/australia/`, `/united-states/`, `/united-kingdom/`, `/uae/`, `/singapore/`, `/india/`
- Pillar guides: `/{country}/property-buying-guide`, `/{country}/mortgage-guide`
- Blog posts: `/{country}/blog/{topic-slug}`
- FAQ hubs: `/{country}/faqs`
- Calculator: `/calculator` (global) — country preselected via query param `?country=au`
- No date-based URLs for blogs (evergreen content, updated regularly)
- Canonical URL on every page, always the absolute https://urmortgage.online/... path

## 2. Design System — Precision Finance

### Colors
| Token | Value | Usage |
|-------|-------|-------|
| --color-primary | #004ac6 | Action Blue — buttons, links, active states |
| --color-secondary | #006c49 | Growth Green — positive metrics, savings |
| --color-surface | #f8f9ff | Light background |
| --color-bg-dark | #0F172A | Dark mode background |
| --color-border | #c3c6d7 | Card borders, dividers |
| --color-text | #1e293b | Body text (light mode) |
| --color-text-dark | #e2e8f0 | Body text (dark mode) |

### Typography
- Font: Geist (Google Fonts) — all text
- H1: 2rem/2.5rem, font-weight 700
- H2: 1.5rem, font-weight 600
- H3: 1.25rem, font-weight 600
- Body: 1rem/1.125rem, line-height 1.75
- Blog content: max-width 720px, centered

### Components
- Cards: white bg, 16px radius, 1px border --color-border, shadow-sm
- Inputs: 48px height, 12px radius, 1px border, 16px padding
- Buttons: primary = --color-primary fill, white text, 10px radius
- Dark mode: Tailwind `dark:` classes, toggle persists to localStorage

### Breakpoints
- Desktop: > 900px
- Tablet: 600–900px
- Mobile: < 600px
- Touch targets: minimum 48px

## 3. Content Rules

### Pillar Guides
- 2,000–3,000 words
- Must include: TOC (auto-generated), 5–8 H2 sections, 3–5 FAQs inline, CTA at end
- Must link to: all 10 blogs, FAQ hub, calculator, loan products, other pillar guide
- Schema: Article + FAQPage

### Blog Posts
- 1,200–1,800 words
- Must include: hero image with ALT text, 3–5 H2 sections, 1 CTA, key takeaway box
- Must link to: both pillar guides, FAQ hub, calculator, 2 related blogs
- Schema: Article

### FAQ Hub
- 30–50 FAQs per country
- Grouped by category (buying process, financing, costs, legal, investment)
- Each answer 50–150 words, targeting featured snippets
- Schema: FAQPage

### All Content
- Metadata required: metaTitle (50–60 chars), metaDescription (150–160 chars), primaryKeyword, secondaryKeywords
- H1 must match or closely reflect metaTitle
- Image ALT text must be descriptive and include keyword naturally
- No keyword stuffing — write for humans, optimise for search
- Country-specific: use local terminology (e.g., "stamp duty" in AU/UK, "closing costs" in US)
- Currency: always use local currency symbol and formatting

## 4. Schema Rules

- Every page: BreadcrumbList
- Home: Organization + WebSite + SoftwareApplication
- Pillar guides: Article + FAQPage
- Blog posts: Article
- FAQ hubs: FAQPage
- Calculator: SoftwareApplication
- All schema as JSON-LD in <script type="application/ld+json">
- Validate with Google Rich Results Test before publishing

## 5. Internal Linking Rules

- Minimum links per page type enforced (see architecture.md Section 8)
- Links must be contextual (within body text), not just sidebar/footer lists
- Anchor text must be descriptive (not "click here")
- No orphan pages — every page must have at least 3 inbound links
- Run link validation script before every deploy

## 6. Performance Rules

- Blog/FAQ pages: zero client-side JavaScript (pure static HTML + CSS)
- Calculator: loaded as Astro island (client:visible) — JS only loads when scrolled into view
- Images: use Astro Image component for automatic optimisation (WebP, lazy loading, srcset)
- Fonts: preload Geist, use font-display: swap
- No render-blocking resources
- Target: Lighthouse Performance 95+, SEO 100

## 7. AdSense Rules

- Maximum 5 ad slots per page (follow existing slot layout)
- No ads above the fold on content pages (first ad after first H2)
- All slots use data-full-width-responsive="true"
- Publisher ID: ca-pub-1263369613506494
- Ad slots implemented as reusable <AdSlot /> component

## 8. Security Rules

- HTML entity encoding on all dynamic content (esc function)
- Referrer-policy: strict-origin-when-cross-origin
- X-Content-Type-Options: nosniff
- X-Frame-Options: DENY
- SRI hashes on CDN scripts (when implemented)
- CSP headers via Cloudflare (future)
