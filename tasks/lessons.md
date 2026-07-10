# Lessons Learned — URMortgage.online

---

## Lesson 1: Tailwind v4 PostCSS Integration
- **Mistake:** Used `@astrojs/tailwind` integration which expects Tailwind v3 API
- **Cause:** Tailwind v4 moved PostCSS plugin to `@tailwindcss/postcss` package
- **Correct Rule:** For Tailwind v4 + Astro v7, use `@tailwindcss/postcss` in postcss.config.mjs, NOT `@astrojs/tailwind`. Import with `@import "tailwindcss/preflight"` and `@import "tailwindcss/utilities"`, NOT `@import "tailwindcss"`.
- **Example:** postcss.config.mjs with `{ '@tailwindcss/postcss': {} }` + global.css with layer imports

## Lesson 2: Astro v7 Content Layer API
- **Mistake:** Used old `entry.render()` method and old `src/content/config.ts` location
- **Cause:** Astro v7 replaced the Content Collections API with the Content Layer API
- **Correct Rule:** In Astro v7: (1) config goes in `src/content.config.ts` (root of src), (2) use `glob()` loader, (3) use `import { render } from 'astro:content'` and call `render(entry)` instead of `entry.render()`
- **Example:** `const { Content, headings } = await render(guide);`

## Lesson 3: Bash Brace Expansion
- **Mistake:** Used `mkdir -p dir/{a,b,c}` inside heredoc/script which doesn't expand braces
- **Cause:** Brace expansion doesn't work in all shell contexts (e.g., inside heredocs or when sh is used instead of bash)
- **Correct Rule:** Write each mkdir path explicitly or use multiple mkdir commands
- **Example:** `mkdir -p content/countries content/pillar-guides content/blogs content/faqs`

## Lesson 4: Tailwind v4 Source Detection with Astro
- **Mistake:** Used Tailwind v4 with @tailwindcss/postcss — @source directives failed to detect .astro files, resulting in missing utility classes
- **Cause:** Tailwind v4's auto-detection and @source glob patterns don't reliably scan .astro files in the Astro build pipeline
- **Correct Rule:** Use Tailwind v3 (@astrojs/tailwind@5 + tailwindcss@3) with explicit content paths in tailwind.config.mjs. Tailwind v3 is battle-tested with Astro. Don't chase v4 compatibility until the Astro integration officially supports it.
- **Example:** `content: ['./src/**/*.{astro,html,js,jsx,md,mdx,ts,tsx}']` in tailwind.config.mjs

## Lesson 5: Astro v7 Glob Loader Duplicate IDs
- **Mistake:** Content files with same filename in flat directory got same ID, causing overwrites (only last country's content survived)
- **Cause:** Astro v7's glob loader derives ID from filename by default, ignoring parent directory
- **Correct Rule:** Use country subdirectories (`blogs/australia/`, `blogs/india/`) AND add `generateId: ({ entry }) => entry.replace(/\.mdx?$/, '')` to the glob config. The `entry` param includes the relative path, making IDs like `australia/first-home-buyer-guide` unique.
- **Example:** `loader: glob({ pattern: '**/*.md', base: './src/content/blogs', generateId: ({ entry }) => entry.replace(/\.mdx?$/, '') })`
