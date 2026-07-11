# URMortgage — Lessons Learned

## Lesson 001 — GSC Sitemap Submission
- Date: 2026-07-11
- Mistake: Submitted sitemap.xml instead of sitemap-0.xml
- Cause: Astro generates sitemap-index.xml pointing to sitemap-0.xml. GSC failed to process the index.
- Rule: For Astro sites, submit sitemap-0.xml directly. Update robots.txt accordingly.

## Lesson 002 — Read Handover Docs Thoroughly
- Date: 2026-07-11
- Mistake: First backlog summary missed priority tiers P0-P4.
- Cause: Skimmed section 11 instead of reading all subsections.
- Rule: Preserve original structure when summarising structured documents.

## Lesson 003 — Autonomous FAQ Generation
- **Date:** 2026-07-11
- **Mistake:** Generating too many FAQs per API call caused timeouts. Batching 3+ countries in one call also hit limits.
- **Cause:** Large max_tokens + long prompts = slow responses exceeding execution timeout.
- **Correct Rule:** Generate one country per API call. Use max_tokens=2500. Top up in multiple passes rather than one giant call. Always verify count after each call.

## Lesson 004 — Don't Ask Manish What Claude Can Do Autonomously
- **Date:** 2026-07-11
- **Mistake:** Asked Manish to manually copy/paste files and run commands when API key and GitHub token were available.
- **Correct Rule:** With ANTHROPIC_API_KEY and GITHUB_TOKEN available — clone repo, generate, commit, push autonomously. Only interrupt Manish for decisions, not execution.

## Lesson 005 — Security Review Against posst.app Framework
- **Date:** 2026-07-11
- **Finding:** CORS wildcard * on chat.js allowed any domain to call the Claude API endpoint — potential credit drain attack.
- **Correct Rule:** Always restrict CORS to known origins. For Cloudflare Pages Functions, use CF-Connecting-IP for rate limiting. Static sites still need _headers file for HTTP security headers.
