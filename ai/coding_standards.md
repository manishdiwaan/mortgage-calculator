# Coding Standards — URMortgage.online

---

## 1. Astro Components

- File naming: PascalCase for components (`Navbar.astro`, `SchemaOrg.astro`)
- File naming: kebab-case for pages and content (`property-buying-guide.astro`)
- Props: define with TypeScript interface in component frontmatter
- Layouts: extend BaseLayout for all pages — never skip it
- Slots: use named slots for layout injection (e.g., `<slot name="sidebar" />`)
- Styles: use Tailwind utility classes; scoped `<style>` only for component-specific CSS

```astro
---
// Good: typed props
interface Props {
  title: string;
  description: string;
  country?: string;
}
const { title, description, country } = Astro.props;
---
```

## 2. Content Collections (Markdown)

### Frontmatter Template — Blog Post
```yaml
---
title: "First Home Buyer Guide in Australia"
country: "australia"
slug: "first-home-buyer-guide"
category: "first-home"
metaTitle: "First Home Buyer Guide Australia 2026 | URMortgage"
metaDescription: "Complete guide to buying your first home in Australia. Learn about grants, stamp duty, deposit requirements, and the step-by-step buying process."
primaryKeyword: "first home buyer australia"
secondaryKeywords:
  - "first home buyer grant"
  - "buying first home australia"
  - "first home deposit australia"
publishDate: 2026-07-15
lastUpdated: 2026-07-15
wordCount: 1500
heroImage: "/images/blog/au-first-home-buyer.webp"
imageAlt: "Young couple receiving keys to their first home in Australia"
relatedPosts:
  - "stamp-duty-explained"
  - "property-inspection-checklist"
---
```

### Frontmatter Template — Pillar Guide
```yaml
---
title: "Complete Property Buying Guide — Australia"
country: "australia"
slug: "property-buying-guide"
type: "property-buying"
metaTitle: "How to Buy Property in Australia 2026 | Complete Guide"
metaDescription: "Step-by-step guide to buying property in Australia. Covers budgeting, pre-approval, searching, offers, conveyancing, settlement and more."
primaryKeyword: "buying property australia"
secondaryKeywords:
  - "how to buy a house in australia"
  - "property buying process australia"
publishDate: 2026-07-10
lastUpdated: 2026-07-10
wordCount: 2800
faqs:
  - question: "How much deposit do I need to buy a house in Australia?"
    answer: "Most Australian lenders require a minimum 5-20% deposit..."
relatedBlogs:
  - "first-home-buyer-guide"
  - "stamp-duty-explained"
  - "property-inspection-checklist"
---
```

## 3. TypeScript

- Strict mode enabled in tsconfig.json
- No `any` types — use proper interfaces
- Utility functions in `src/utils/` — pure functions, well-typed
- Data files in `src/data/` — typed with `as const` where applicable
- Enums: prefer string unions over TypeScript enums

## 4. JSON-LD Schema

- Render via `<SchemaOrg>` component in BaseLayout
- Pass schema data as typed props
- Always include @context and @type
- Article schema must include: headline, datePublished, dateModified, author, publisher, image
- FAQ schema: array of Question entities with acceptedAnswer

```typescript
// src/utils/schema.ts
export function articleSchema(data: ArticleData): object {
  return {
    "@context": "https://schema.org",
    "@type": "Article",
    headline: data.title,
    datePublished: data.publishDate,
    dateModified: data.lastUpdated,
    author: {
      "@type": "Organization",
      name: "URMortgage"
    },
    publisher: {
      "@type": "Organization",
      name: "URMortgage",
      url: "https://urmortgage.online"
    },
    description: data.metaDescription,
    mainEntityOfPage: {
      "@type": "WebPage",
      "@id": `https://urmortgage.online/${data.country}/${data.slug}`
    }
  };
}
```

## 5. File Organization

- One component per file
- Group by function, not by type:
  - `src/components/` — reusable UI components
  - `src/layouts/` — page layouts (extend BaseLayout)
  - `src/pages/` — routes (minimal logic, delegate to layouts)
  - `src/content/` — Markdown content collections
  - `src/data/` — static data (countries, lenders, rates)
  - `src/utils/` — pure utility functions
  - `scripts/` — CLI scripts (content generation, link validation)

## 6. Git Conventions

- Branch: `main` for production (auto-deploys via Cloudflare Pages)
- Branch: `dev` for work in progress
- Commit messages: `type: description`
  - `feat: add australia blog posts`
  - `fix: correct schema on FAQ pages`
  - `content: publish uk pillar guides`
  - `seo: update internal links for india hub`
  - `chore: update dependencies`

## 7. Image Standards

- Format: WebP preferred, PNG fallback
- Naming: `{country}-{topic}.webp` (e.g., `au-first-home-buyer.webp`)
- Location: `public/images/{type}/` (blog/, countries/, etc.)
- Always include descriptive ALT text with keyword
- Use Astro `<Image>` component for automatic optimization
- Hero images: 1200×630px (doubles as OG image)
- Thumbnails: 400×300px

## 8. Testing / Validation

Before every deploy, verify:
- [ ] `npm run build` succeeds with zero errors
- [ ] All pages have unique metaTitle and metaDescription
- [ ] All pages have canonical URL
- [ ] All blog posts link to both pillar guides
- [ ] Schema validates (Google Rich Results Test)
- [ ] No broken internal links (run validate-links script)
- [ ] Images have ALT text
- [ ] Lighthouse audit: Performance 95+, SEO 100
