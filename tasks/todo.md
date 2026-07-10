# URMortgage.online — Current Sprint TODO

Sprint: 1 — Platform Scaffold
Started: July 2026

---

## Phase 1: Project OS & Documentation ✅ IN PROGRESS

- [x] Create project directory structure (ai/, tasks/, agents/, docs/)
- [x] Populate tasks/backlog.md from handover + SEO playbook
- [ ] Create tasks/todo.md (this file)
- [ ] Create docs/architecture.md — full technical architecture
- [ ] Create ai/architecture_rules.md — URL conventions, design system, content rules
- [ ] Create ai/coding_standards.md — Astro/Markdown/schema standards
- [ ] Create tasks/lessons.md — initialise learning log
- [ ] Create tasks/review.md — initialise verification log

## Phase 2: Astro Project Scaffold

- [ ] Initialise Astro project with TypeScript
- [ ] Install integrations: @astrojs/cloudflare, @astrojs/sitemap, @astrojs/mdx
- [ ] Configure Tailwind CSS with Precision Finance design tokens
- [ ] Define content collections: countries, pillar-guides, blogs, faqs
- [ ] Create collection schemas with Zod validation
- [ ] Create base layout (BaseLayout.astro) with shared head, nav, footer
- [ ] Create country hub layout
- [ ] Create pillar guide layout with TOC auto-generation
- [ ] Create blog post layout
- [ ] Create FAQ hub layout
- [ ] Implement BreadcrumbList component
- [ ] Implement JSON-LD schema components (Article, FAQ, Breadcrumb)
- [ ] Configure URL routing: /country/, /country/slug, /country/blog/slug, /country/faqs

## Phase 3: Content Pipeline Design

- [ ] Design Airtable base schema (tables, fields, views, relationships)
- [ ] Write content brief generator prompt
- [ ] Write pillar guide generator prompt
- [ ] Write blog post generator prompt
- [ ] Write FAQ generator prompt
- [ ] Write metadata/schema generator prompt
- [ ] Create Markdown frontmatter template for each content type
- [ ] Build internal link injection logic

## Phase 4: Pilot Content (6 Countries)

- [ ] Generate content briefs for Australia (2 pillars + 10 blogs + 50 FAQs)
- [ ] Generate content briefs for India
- [ ] Generate content briefs for United States
- [ ] Generate content briefs for United Kingdom
- [ ] Generate content briefs for UAE
- [ ] Generate content briefs for Singapore
- [ ] Generate draft content (AI pipeline)
- [ ] Review and fact-check pass
- [ ] Publish to Astro content collections
- [ ] Validate internal linking matrix
- [ ] Verify schema markup (Google Rich Results Test)

## Phase 5: Deploy & Track

- [ ] Configure Cloudflare Pages project
- [ ] Repoint DNS (GoDaddy → Cloudflare Pages)
- [ ] Submit expanded sitemap to Google Search Console
- [ ] Verify all pages indexed
- [ ] Set up Cloudflare Web Analytics
- [ ] Baseline KPIs in Airtable

---

## Current Focus

**RIGHT NOW: Phase 1 — Completing documentation before any code.**

## Definition of Done

- [ ] All 84 pilot pages live on urmortgage.online
- [ ] All pages pass Google Rich Results Test
- [ ] Internal linking matrix 100% complete
- [ ] Sitemap reflects all pages
- [ ] GSC shows pages indexed
- [ ] KPI baseline recorded
