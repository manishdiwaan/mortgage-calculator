# Airtable Base Setup — URMortgage Content Pipeline

## Create the Base

1. Go to airtable.com → Create new base → Name it "URMortgage Content"

## Table: Content Queue

This is the only table you need. It drives the entire n8n pipeline.

### Fields to Create

| Field Name | Type | Options |
|-----------|------|---------|
| Country | Single select | Australia, India, United States, United Kingdom, UAE, Singapore |
| Country Slug | Single line text | e.g., australia, india, united-states |
| Title | Single line text | Content title |
| Slug | Single line text | URL slug (e.g., first-home-buyer-guide) |
| Content Type | Single select | pillar-guide, blog, faq-hub |
| Category | Single select | first-home, costs, taxes, grants, inspections, loan-types, rent-vs-buy, investment, refinancing, mistakes, property-buying, mortgage, general |
| URL | Single line text | Relative URL path |
| Status | Single select | Ready, Generating, Published, Refresh |
| Priority | Single select | P0, P1, P2, P3 |
| Brief | Long text | AI-generated content brief (JSON) |
| Prompt | Long text | Full generation prompt for Claude/ChatGPT |
| Content | Long text | Generated markdown content (filled by n8n) |
| Publish Date | Date | Auto-filled when published |
| Last Updated | Date | Track content freshness |
| Word Count | Number | Actual word count |
| Primary Keyword | Single line text | |
| Meta Title | Single line text | |
| Meta Description | Single line text | |
| Notes | Long text | Manual notes |

### Views to Create

1. **Content Queue** (Grid) — Filter: Status = "Ready". Sort by Priority ASC. This is what n8n reads.
2. **Published** (Grid) — Filter: Status = "Published". Group by Country.
3. **Editorial Calendar** (Calendar) — Date field: Publish Date. Color by Country.
4. **By Country** (Grid) — Group by Country, then by Content Type.
5. **Needs Refresh** (Grid) — Filter: Last Updated is before 6 months ago.

## How It Connects to n8n

```
Brief Generator workflow (manual, once per country)
    → Fills 13 rows per country (2 pillars + 10 blogs + 1 FAQ hub)
    → Each row has Status = "Ready" and a Prompt field

Content Pipeline workflow (scheduled, every 8 hours)
    → Reads next "Ready" row
    → Sends Prompt to Claude API
    → Commits generated .md to GitHub
    → Updates Status to "Published"
```

## Getting Your API Key

1. Go to airtable.com/create/tokens
2. Create a personal access token
3. Scopes: data.records:read, data.records:write
4. Add to n8n as "Airtable" credential

## Base ID

After creating the base, get the base ID from the URL:
`https://airtable.com/appXXXXXXXXXXXX/...`
The `appXXXXXXXXXXXX` part is your base ID. Put this in the n8n workflow.
