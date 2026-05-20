# Changelog

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
