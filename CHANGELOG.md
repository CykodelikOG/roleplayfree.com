# Changelog

## v2.2 - 2026-10-06
Play Now block at the top of the homepage. Three honest routes into a game.
Files: src/components/PlayNow.astro (new), src/components/Analytics.astro, src/content/site-content.json, src/pages/index.astro.
- **Why:** GA4 lifetime shows 77% bounce, an 18 second average visit, every session landing on `/` and not one ever reaching a second page. The homepage was asking a newcomer to read eleven system cards and choose. This gives them one action instead.
- PlayNow.astro: new block placed above the Hero, after ShiftBanner. All copy and links live in site-content.json under `playNow`, per the project file-structure rule.
- Three options, ordered on Peter's call: **Roll20 Pick Up Games first** ("if a game is running, a game is running"), then Friends and Fables, then Perchance AI RPG.
- Each option states **what you get and what the catch is at equal visual weight**, plus badges for cost, whether an account is needed, and where it runs out. Nobody should hit a turn limit or a paywall by surprise, which was Peter's stated qualifier after being burned by AI GMs that give ten replies then ask for money.
- Perchance carries an explicit honesty panel: not vetted, not ours, sits on a community platform that hosts adult material elsewhere and is often network-blocked. Listed because it is the only option that asks nothing of the visitor at all.
- Roll20 carries its own panel: Pick Up Games are the fast lane, ordinary Roll20 LFG means waiting weeks.
- CTA: "Play now for free" with a per-option subtitle, full width, forest green #2D5016 with a gold #C9A84C outline. Both colours are existing system card accents, so the button is loud without introducing a new colour.
- **No third-party logos, deliberately.** Roll20's terms forbid use of their marks without prior written consent; Friends and Fables and Perchance publish no brand assets; and a Perchance logo would imply an endorsement that is explicitly withheld. Icons are inline SVG in site accents, honouring the no-emoji design rule.
- Analytics.astro: AI game masters split out of the VTT bucket into a new `ai_gm` class. Previously Roll20 and both AI options all reported as `vtt_tool`, which would have made this block's reports unreadable.
- site-content.json: **LoreKeeper factual fix.** The site claimed "the host's plan covers a session, guests don't need their own subscription". Their site states each player needs their own free account and uses their own daily turn cap. Corrected.

**Verification:** build clean at 14 pages; 3 CTAs render in the block in the intended order; all three tracked as `outbound_click` with `section="play-now"` and the correct `link_class`; existing affiliate and system-link tracking unaffected; 15 of 15 jsdom checks passing.

**Resolved same day:** the DriveThruRPG affiliate ID does **not** cover Roll20. Matt McElroy's approval email of 2026-05-15 lists the covered sites as DriveThruRPG, DMsGuild, DriveThruComics, DriveThruFiction, DriveThruCards, Storytellers Vault and WarGameVault, with Roll20 absent. Those are product storefronts; Roll20 is the parent platform selling subscriptions. Shipping the Roll20 link with no affiliate parameter was therefore correct. Moot in any case, since Pick Up Games is a free LFG listing rather than a purchase page.

**Also open:** Questwright remains the lead entry in the AI Game Masters section despite being a waitlist. Peter's call, on the basis that a short waitlist is acceptable for a free alpha. It is not in the Play Now block, so nothing here depends on it.

## v2.1 - 2026-10-06
Custom event tracking. The site can finally measure behaviour, not just page views.
Files: src/components/Analytics.astro (new), src/layouts/Layout.astro, src/pages/systems/[id].astro.
- **Why:** five months of GA4 data contained exactly four event types (first_visit, page_view, session_start, user_engagement). Nothing recorded whether a visitor had ever clicked an affiliate link, opened a free rulebook, or finished the quiz. With the Amazon Associates requirement of 3 qualifying sales, "does anyone click the money links" was unanswerable.
- Analytics.astro: new component holding the GA4 tag plus custom tracking. One delegated click listener on `document`, so no other component needs editing and links added later are covered automatically.
- Events added: `outbound_click`, `affiliate_click`, `discord_click`, `system_link_click`, `system_page_view`, `scroll_depth` (25/50/75/90), `quiz_start`, `quiz_answer`, `quiz_complete`, `quiz_retake`, `quiz_share`.
- Parameters captured: link_domain, link_url, link_text, link_class, price_label (read off the existing `link-label--*` badge classes), section, system, quiz_result, depth.
- `affiliate_click` and `discord_click` are deliberately separate EVENT NAMES rather than parameters, because GA4 reports event counts with no configuration but will not break down by a parameter until it is registered as a custom dimension. The two questions that matter most stay readable with zero GA4 setup.
- Layout.astro: inline GA4 block replaced with `<Analytics />`. One GA4 install per page, verified.
- systems/[id].astro: added ids `where-to-start` and `find-players` so the `section` parameter resolves on system pages instead of reporting "none".

**Two bugs caught before deploy, both by testing rather than reading:**
- `define:vars` makes Astro wrap an inline script in an IIFE, which scopes `gtag` locally and leaves `window.gtag` undefined. That would have silently killed every event on the site. **This is the same fault as commit 9bff2cb (2026-05-25).** Fixed by writing the measurement ID literally and assigning `window.gtag` explicitly. A comment in the file warns against reintroducing define:vars.
- The script sits in `<head>`, so `getElementById` ran before `<body>` was parsed and the quiz-completion observer never attached. Click tracking was unaffected because it delegates off `document`. Fixed with a DOM-ready wrapper, plus an immediate check on attach so a result restored from localStorage by a returning visitor is not missed.

**Verification:** 18 automated checks against the real built HTML in jsdom, all passing. Build clean at 14 pages, GA4 tag present on all 14, exactly one gtag config per page.

**Still manual, Peter's call:** register the custom dimensions in GA4 (Admin > Custom definitions) to break reports down by parameter, and switch on Enhanced Measurement in the data stream settings, which is currently OFF and is why no `scroll` or `click` events exist historically.

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
