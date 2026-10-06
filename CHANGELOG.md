# Changelog

## v2.0 - 2026-10-06
Per-system landing pages. 11 new indexable pages, one per game system.
Files: src/pages/systems/[id].astro (new), src/components/SystemCard.astro, src/content/site-content.json, public/sitemap.xml, .gitignore, rf-analytics.py (new), rf-report.txt (new).
- src/pages/systems/[id].astro: new dynamic route. getStaticPaths maps the route param to each system's slug, so URLs are /systems/<slug>/. Each page carries its own title ("How to start playing X"), meta description, canonical URL and BreadcrumbList JSON-LD, plus that system's free rules, paid rulebook, character sheets and Discord links pulled from site-content.json.
- site-content.json: added slug + metaDescription to all 11 systems; added systemIds to all 8 character sheets so pages can filter them; repointed 4 nav dropdown links from #systems to the new pages.
- site-content.json: fixed mojibake that was live on the site. "MÃ¶rk Borg" to "Mork Borg" (correct umlaut), "â†“" to the down arrow in the hero CTA, "â€“" to an en dash in the AI GM pricing note. Cause was a UTF-8 file previously saved as Latin-1.
- SystemCard.astro: card title becomes a link to the system page when a slug exists, plain text when it does not.
- sitemap.xml: 11 new URLs at priority 0.7. Also dropped the file's UTF-8 BOM (harmless for XML).
- rf-analytics.py: GA4 reporting script (was untracked since 2026-05-24). Reuses the claude-youtube-488012 OAuth project; credentials live outside the repo in ClaudeAssets, nothing secret is committed.
- .gitignore: added .astro/ so the Astro build cache timestamp stops appearing in every diff. .astro/settings.json untracked.
- Verified before push: build clean, 14 pages, all 11 slugs match the sitemap exactly, GA4 tag G-TRZLDRM1GF present on all 14 built pages with the inline config block intact.

**Version note:** this entry resolves the v1.9 vs v2.0 discrepancy flagged on 2026-08-09. CHANGELOG had no v2.0 while MEMORY.md recorded the site as live v2.0. The likely cause is the 2026-05-24 GA4 measurement-ID fix and the og:url/is:inline commits, which shipped to the live site after v1.9 without a CHANGELOG entry, breaching the VERSIONING rule. Those changes are live and are treated here as part of v2.0 rather than back-dated into a version that was never written.

## v1.7 — 2026-05-20
SEO fundamentals pass 1.
Files: astro.config.mjs, public/robots.txt, public/sitemap.xml (new), src/layouts/Layout.astro, package.json, package-lock.json.
- public/sitemap.xml created as static file covering /, /quiz/, /start/.
- robots.txt: added Sitemap directive pointing to /sitemap.xml.
- Layout.astro: added canonical link tag, reordered default title keyword-first ("Free Tabletop RPG Guide for Beginners | roleplayfree.com").
- Astro sitemap integration installed but unused (Windows path bug in underlying sitemap lib). Static file is the working approach.

## v1.8 — 2026-05-20
JSON-LD structured data on all pages.
Files: src/layouts/Layout.astro, src/pages/index.astro, src/pages/quiz.astro, src/pages/start.astro.
- Layout.astro: added jsonLd prop that renders application/ld+json script tag.
- index.astro: WebSite schema (name, url, description).
- quiz.astro + start.astro: BreadcrumbList schemas pointing back to home.
- start.astro: ogUrl canonical added.

## v1.9 — 2026-05-20
og:url trailing slash fix.
Files: src/pages/quiz.astro, src/pages/start.astro.
- ogUrl on /quiz and /start now ends with trailing slash to match GitHub Pages 301 redirect target and canonical URL.
- Fixes Facebook Sharing Debugger canonical mismatch.

---

## v0.1 — 2026-05-13
Session Zero complete. Project scaffolded.
Files: all 27 project files created. No deploy yet.
Status: local dev only. GitHub repo not yet created.

---
