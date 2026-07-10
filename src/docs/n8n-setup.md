# n8n Setup Guide — URMortgage Content Pipeline

## Overview

Two workflows automate the entire content lifecycle:

1. **Brief Generator** — Run once per country. Creates 13 Airtable rows (2 pillars + 10 blogs + 1 FAQ hub) with AI-generated briefs and prompts.
2. **Content Pipeline** — Runs on schedule (every 8 hours). Picks up "Ready" rows, generates content via Claude, commits to GitHub, updates Airtable.

## Prerequisites

- n8n instance (cloud or self-hosted)
- Anthropic API key (for Claude)
- GitHub personal access token (repo scope)
- Airtable personal access token
- Airtable base created (see airtable-setup.md)

## Step 1: Set Up n8n Credentials

### Claude API Key
1. In n8n → Settings → Credentials → Add Credential
2. Type: Header Auth
3. Name: `x-api-key`
4. Value: your Anthropic API key (sk-ant-...)

### GitHub
1. Add Credential → GitHub API
2. Access Token: your GitHub personal access token
3. Needs `repo` scope

### Airtable
1. Add Credential → Airtable Personal Access Token
2. Token: your Airtable token

## Step 2: Import Workflows

### Brief Generator
1. In n8n → Workflows → Import from File
2. Select `scripts/n8n/brief-generator.json`
3. Replace placeholder credentials:
   - `{{AIRTABLE_BASE_ID}}` → your base ID (appXXXXXX)
   - `{{AIRTABLE_CREDENTIAL_ID}}` → select your Airtable credential
   - `{{CLAUDE_CREDENTIAL_ID}}` → select your Claude credential
4. Update "Set Country Variables" node with the first country

### Content Pipeline
1. Import `scripts/n8n/content-pipeline.json`
2. Replace same placeholders
3. Also replace `{{GITHUB_CREDENTIAL_ID}}` → select your GitHub credential

## Step 3: Run Brief Generator

1. Open Brief Generator workflow
2. In "Set Country Variables" node, set:
   - country_name: Australia
   - country_slug: australia
   - country_iso: AU
   - currency_symbol: $
   - currency_code: AUD
   - tax_term: stamp duty
   - deposit_term: deposit
   - central_bank: Reserve Bank of Australia
3. Click "Execute Workflow"
4. Check Airtable — you should see 13 new rows with Status = "Ready"

Repeat for each country, changing the variables:

| Country | Slug | ISO | Currency | Tax Term | Deposit Term |
|---------|------|-----|----------|----------|-------------|
| Australia | australia | AU | $ AUD | stamp duty | deposit |
| India | india | IN | ₹ INR | stamp duty | down payment |
| United States | united-states | US | $ USD | closing costs | down payment |
| United Kingdom | united-kingdom | GB | £ GBP | stamp duty | deposit |
| UAE | uae | AE | د.إ AED | transfer fee | down payment |
| Singapore | singapore | SG | $ SGD | stamp duty | down payment |

## Step 4: Activate Content Pipeline

1. Open Content Pipeline workflow
2. Toggle "Active" to ON
3. It will run every 8 hours, generating one content piece per run
4. At this pace: 13 items per country × 6 countries = 78 items = ~26 days to publish everything

To go faster, change the schedule interval in the trigger node (e.g., every 4 hours = ~13 days).

## Step 5: Monitor

- Check Airtable "Published" view — rows update as content goes live
- Check GitHub commits — each content piece creates a commit
- Check Cloudflare Pages — auto-deploys within 1-2 minutes of each commit
- Check urmortgage.online — pages appear automatically

## Workflow Diagram

```
BRIEF GENERATOR (manual, once per country):
  Manual Trigger
    → Set Country Variables
    → Build Content Plan (13 items)
    → Generate Brief (Claude API)
    → Build Generation Prompt
    → Create Airtable Row (Status = Ready)

CONTENT PIPELINE (scheduled, every 8 hours):
  Schedule Trigger
    → Read Next "Ready" Row from Airtable
    → If row exists:
      → Generate Content (Claude API)
      → Parse Content & Build File Path
      → Commit .md File to GitHub
      → Update Airtable (Status = Published)
    → If no rows: Stop
```

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Claude returns error | Check API key, check you have credits |
| GitHub commit fails | Check token has `repo` scope, check file path doesn't exist (use update instead of create) |
| Airtable empty | Run Brief Generator first |
| Content malformed | Check Prompt field in Airtable — the prompt may need tweaking |
| Wrong file path | Check Parse Content node — verify switch/case logic |

## Cost Per Country

~$5-10 in Claude API calls per country (13 items × ~$0.50 each) = ~$30-60 for all 6 countries.
