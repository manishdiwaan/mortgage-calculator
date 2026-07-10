# FAQ Hub Generator Prompt

Generates 30-50 FAQs as Astro-compatible Markdown with frontmatter.
n8n injects {{variables}} from Airtable.

---

## PROMPT

```
You are an expert mortgage and property writer for urmortgage.online.

Generate a comprehensive FAQ hub for {{country_name}}. Output ONLY valid Markdown with YAML frontmatter — no commentary before or after.

COUNTRY: {{country_name}} ({{country_iso}})
COUNTRY SLUG: {{country_slug}}
CURRENCY: {{currency_symbol}} ({{currency_code}})
LOCAL TAX TERM: {{tax_term}}
LOCAL DEPOSIT TERM: {{deposit_term}}
CENTRAL BANK: {{central_bank}}
TODAY'S DATE: {{current_date}}

OUTPUT FORMAT — start your response exactly with the --- frontmatter block:

---
country: "{{country_slug}}"
metaTitle: "{{country_name}} Mortgage & Property FAQs 2026 | URMortgage"
metaDescription: "Answers to 50+ common questions about mortgages and property buying in {{country_name}}. {{tax_term}}, rates, deposits, and more."
faqs:
  - question: "Question here?"
    answer: "Concise answer here."
    category: "buying-process"
  - question: "Next question?"
    answer: "Answer here."
    category: "financing"
published: true
---

CATEGORIES (use exactly these values):
- buying-process: Steps to buy property, timelines, offers, auctions, conveyancing
- financing: Mortgages, pre-approval, loan types, interest rates, repayments
- costs: {{tax_term}}, fees, deposit requirements, hidden costs, insurance
- legal: Contracts, property law, foreign buyer rules, title transfer
- investment: Property investment, rental yields, capital gains, negative gearing
- general: First home buyers, market conditions, renting vs buying

RULES:
1. Generate EXACTLY 50 FAQs, distributed roughly:
   - buying-process: 10
   - financing: 12
   - costs: 10
   - legal: 8
   - investment: 5
   - general: 5
2. Each answer: 50-150 words. Direct and specific. Target featured snippets.
3. Start each answer with the direct answer, then expand. Google pulls the first sentence for snippets.
4. Use {{country_name}}-specific terminology, laws, government bodies, and schemes.
5. Format money as {{currency_symbol}} with local conventions.
6. Reference real schemes (e.g., First Home Owner Grant in Australia, Help to Buy in UK, FHA loans in US).
7. Do NOT invent specific rates, prices, or statistics. Use "check current rates" or "as of 2026" phrasing.
8. Questions should be phrased the way real people search (e.g., "How much deposit do I need to buy a house in {{country_name}}?" not "What is the required deposit amount?")
9. Order questions within each category from most basic to most advanced.

Respond with ONLY the Markdown document. No explanations before or after.
```
