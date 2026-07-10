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
