# System Prompt — URMortgage.online AI Project

## Project Identity
- **Name:** URMortgage.online
- **Owner:** Manish Diwaan
- **GitHub:** manishdiwaan/mortgage-calculator
- **Domain:** urmortgage.online
- **Purpose:** Global mortgage and property knowledge platform

## What This Project Is
A mortgage repayment calculator (25 countries, 250+ lenders) being expanded into a full SEO content platform with country-specific hubs, pillar guides, blogs, FAQs, and automated content pipeline.

## Tech Stack
- **Framework:** Astro SSG (TypeScript)
- **Styling:** Tailwind CSS (Precision Finance design system)
- **Hosting:** Cloudflare Pages
- **Content:** Markdown in Astro content collections
- **Pipeline:** Airtable (inventory) → Claude/ChatGPT (generation) → Markdown → Git → Deploy
- **Analytics:** Google Search Console + Cloudflare Web Analytics
- **Ads:** Google AdSense (ca-pub-1263369613506494)

## Key Documents
- `docs/architecture.md` — Full technical architecture
- `ai/architecture_rules.md` — Binding rules for URLs, design, content, schema
- `ai/coding_standards.md` — Code conventions
- `tasks/backlog.md` — Complete backlog
- `tasks/todo.md` — Current sprint
- `tasks/lessons.md` — Learning log (mistakes to avoid)

## Pilot Countries
Australia, India, United States, United Kingdom, UAE, Singapore

## Non-Negotiable Rules
1. Never break the existing calculator functionality
2. All content pages must have full schema markup
3. Internal linking matrix must be 100% complete
4. Zero client-side JS on content pages (calculator is an island)
5. All URLs follow the defined structure — no exceptions
6. Country-specific terminology and currency always
