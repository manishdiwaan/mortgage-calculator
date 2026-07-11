# URMortgage — Lessons Learned

## Lesson 001 — GSC Sitemap Submission
- Date: 2026-07-11
- Mistake: Submitted sitemap.xml instead of sitemap-0.xml
- Cause: Astro generates sitemap-index.xml pointing to sitemap-0.xml. GSC failed to process the index layer.
- Rule: For Astro sites, always submit sitemap-0.xml directly. Update robots.txt accordingly.

## Lesson 002 — Read Handover Docs Thoroughly
- Date: 2026-07-11
- Mistake: First backlog summary missed priority tiers P0-P4.
- Cause: Skimmed section 11 instead of reading all subsections.
- Rule: Preserve original structure when summarising structured documents.

## Lesson 003 — Autonomous FAQ Generation
- Date: 2026-07-11
- Mistake: Generating too many FAQs per API call caused timeouts.
- Cause: Large max_tokens + long prompts = slow responses exceeding execution timeout.
- Rule: One country per API call. max_tokens=2500. Top up in multiple passes. Always verify count after each call.

## Lesson 004 — Don't Ask Manish What Claude Can Do Autonomously
- Date: 2026-07-11
- Mistake: Asked Manish to manually copy/paste files when API key and GitHub token were available.
- Rule: With ANTHROPIC_API_KEY and GITHUB_TOKEN available — clone repo, generate, commit, push autonomously. Only interrupt for decisions.

## Lesson 005 — Security Review Process
- Date: 2026-07-11
- Mistake: CORS wildcard * on chat.js allowed any domain to call the Claude API.
- Rule: Always restrict CORS to known origins. Use CF-Connecting-IP for rate limiting. Static sites still need _headers for HTTP security headers.

## Lesson 006 — Verify Platform vs Calculator Alignment
- Date: 2026-07-11
- Mistake: Calculator had 26 countries, platform had 23, both advertised different numbers (25 vs 23).
- Cause: Calculator was built independently as a standalone HTML file and was never synced with platform expansion.
- Rule: When adding countries to the SEO platform, always cross-check calculator CD object and region grouping G to keep both in sync.

## Lesson 007 — Check Existing Before Building
- Date: 2026-07-11
- Mistake: Assumed 6 countries were missing. Actually 6 were missing from SEO platform but 3 others (TH, MX, SA) were missing from calculator.
- Cause: Did not cross-reference calculator CD keys against platform countries.ts before planning expansion.
- Rule: Always diff calculator countries vs platform countries before any expansion work.
