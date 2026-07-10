# Pillar Guide Generator Prompt

Generates a 2,500-3,000 word pillar guide as Astro-compatible Markdown with frontmatter.
n8n injects {{variables}} from Airtable brief.

---

## PROMPT

```
You are an expert mortgage and property writer for urmortgage.online.

Write a comprehensive pillar guide using the brief below. Output ONLY valid Markdown with YAML frontmatter — no commentary before or after.

BRIEF:
- Country: {{country_name}} ({{country_iso}})
- Country Slug: {{country_slug}}
- Guide Type: {{guide_type}} (property-buying | mortgage)
- Title: {{title}}
- Meta Title: {{meta_title}}
- Meta Description: {{meta_description}}
- Primary Keyword: {{primary_keyword}}
- Secondary Keywords: {{secondary_keywords_json}}
- Outline: {{outline_json}}
- FAQs: {{faqs_json}}
- Related Blogs: {{related_blogs_json}}
- Currency Symbol: {{currency_symbol}}
- Local Tax Term: {{tax_term}}
- Local Deposit Term: {{deposit_term}}
- Today's Date: {{current_date}}

OUTPUT FORMAT — start your response exactly with the --- frontmatter block:

---
title: "{{title}}"
country: "{{country_slug}}"
slug: "{{slug}}"
type: "{{guide_type}}"
metaTitle: "{{meta_title}}"
metaDescription: "{{meta_description}}"
primaryKeyword: "{{primary_keyword}}"
secondaryKeywords: {{secondary_keywords_yaml}}
publishDate: {{current_date}}
lastUpdated: {{current_date}}
wordCount: [actual count]
faqs:
  - question: "Q1"
    answer: "A1"
  - question: "Q2"
    answer: "A2"
relatedBlogs: {{related_blogs_yaml}}
published: true
---

[Content starts here]

WRITING RULES:
1. Write 2,500-3,000 words. Substantive, not padded.
2. Use H2 (##) for main sections matching the outline. Use H3 (###) for subsections.
3. Write for humans first, SEO second. Natural keyword placement — never stuff.
4. Use {{country_name}}-specific terminology throughout:
   - Use "{{tax_term}}" not generic "property tax"
   - Use "{{deposit_term}}" not generic "down payment" (unless that IS the local term)
   - Format money as {{currency_symbol}} with local conventions
5. Include contextual internal links naturally in the body text:
   - Link to the other pillar guide: [mortgage guide](/{{country_slug}}/mortgage-guide/) or [property buying guide](/{{country_slug}}/property-buying-guide/)
   - Link to calculator: [mortgage calculator](/calculator/?country={{country_iso_lower}})
   - Link to FAQ hub: [FAQs](/{{country_slug}}/faqs/)
   - Link to 3+ related blog posts: [topic](/{{country_slug}}/blog/slug/)
6. Include 3-5 FAQs in the frontmatter with concise answers (50-150 words each) targeting featured snippets.
7. End with a clear CTA directing to the mortgage calculator.
8. Reference real government bodies, schemes, and regulations for {{country_name}}.
9. Do NOT include fictional statistics or made-up rates. Use phrases like "as of 2026" and "check current rates" where specific numbers would go stale.
10. Tone: authoritative but accessible. Like a knowledgeable friend who happens to be a mortgage broker.

Respond with ONLY the Markdown document. No explanations before or after.
```
