# Content Brief Generator Prompt

Use this prompt with Claude or ChatGPT to generate a structured content brief.
n8n injects the {{variables}} automatically from Airtable.

---

## PROMPT

```
You are an SEO content strategist for urmortgage.online, a global mortgage and property knowledge platform.

Generate a detailed content brief for the following:

COUNTRY: {{country_name}}
CONTENT TYPE: {{content_type}} (pillar-guide | blog | faq-hub)
TOPIC: {{topic}}
CATEGORY: {{category}}

Research and produce the following brief in JSON format:

{
  "title": "SEO-optimised title",
  "metaTitle": "50-60 character title tag with country and year",
  "metaDescription": "150-160 character meta description with primary keyword",
  "primaryKeyword": "main target keyword",
  "secondaryKeywords": ["4-6 related keywords"],
  "searchIntent": "informational | transactional | navigational",
  "targetAudience": "who this content is for",
  "outline": [
    {
      "h2": "Section heading",
      "keyPoints": ["point 1", "point 2", "point 3"],
      "wordCount": 300
    }
  ],
  "faqs": [
    {
      "question": "Question targeting featured snippet",
      "answerGuidance": "Key points to cover in 50-150 words"
    }
  ],
  "internalLinks": {
    "pillarGuides": [
      "{{country_slug}}/property-buying-guide/",
      "{{country_slug}}/mortgage-guide/"
    ],
    "faqHub": "{{country_slug}}/faqs/",
    "calculator": "/calculator/?country={{country_iso_lower}}",
    "relatedBlogs": ["{{country_slug}}/blog/related-slug-1/", "{{country_slug}}/blog/related-slug-2/"]
  },
  "cta": "Call to action text",
  "references": ["Government or authority URLs to fact-check against"],
  "localTerminology": {
    "depositTerm": "local term for deposit",
    "taxTerm": "local term for property tax (e.g., stamp duty, closing costs)",
    "currencyFormat": "e.g., $1,000 or ₹1,00,000"
  },
  "wordCount": 2500,
  "estimatedReadTime": "10 min"
}

RULES:
- Use country-specific terminology (stamp duty vs closing costs, conveyancing vs settlement agent)
- Use local currency formatting
- Reference country-specific government bodies, regulations, and schemes
- Keywords must be locally relevant (people search "buying property in {{country_name}}", not generic terms)
- FAQs must target featured snippet format (direct, concise answers)
- All internal links must follow the URL structure: /{{country_slug}}/blog/topic-slug/
- Include 3-5 FAQs for blog posts, 5-8 for pillar guides, 30-50 for FAQ hubs

Respond ONLY with the JSON. No commentary.
```
