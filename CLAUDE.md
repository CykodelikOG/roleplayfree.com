# CLAUDE.md — roleplayfree.com Project Brief
# Read this file at the start of every session before doing anything else.
# This is the single source of truth for this project.

---

## SESSION ZERO — DO THIS FIRST

Before writing a single line of code, run through this checklist with Peter:

1. Confirm project folder path on local machine
2. Confirm GitHub repository name: `roleplayfree.com`
3. Confirm GitHub Pages is enabled on the repo (Settings → Pages → Deploy from main branch)
4. Walk Peter through pointing GoDaddy domain to GitHub Pages:
   - In GoDaddy DNS settings, add four A records pointing to GitHub's IPs:
     185.199.108.153 / 185.199.109.153 / 185.199.110.153 / 185.199.111.153
   - Add a CNAME record: www → [username].github.io
   - Create a file called `CNAME` in the repo root containing: roleplayfree.com
   - HTTPS is automatic once DNS propagates (up to 48hrs)
5. Confirm affiliate placeholder IDs are ready (see Affiliate section below)
6. Ask Peter to review the site structure summary below before proceeding
7. Only begin scaffolding once Peter says "go ahead"

---

## PROJECT OVERVIEW

**Site:** roleplayfree.com
**Purpose:** Free TTRPG resource hub. Helps newcomers find a system, understand the basics, find a group, and start playing — as fast as possible and for free where possible.
**Secondary purpose:** Placeholder and anchor for SHIFT RPG (coming soon).
**Stack:** Astro static site generator, deployed to GitHub Pages, custom domain via GoDaddy.
**No backend.** No database. No user accounts. No server-side code. Static only.

---

## PRIORITIES AND RULES

- Peter has ADHD. Do one task at a time. Never do more than asked.
- No scope creep. If a change would affect more than one component file, list every file that will be touched and get approval before proceeding.
- No silent changes. If something breaks while fixing something else, say so immediately.
- Warn before any irreversible action.
- Flag anything that could affect security or HTTPS.
- After every session, commit to GitHub with a version tag (v1.0, v1.1 etc.) and update CHANGELOG.md.

---

## FILE STRUCTURE — MANDATORY

Every part of the site is isolated. One file per component. Never put everything in one file.

```
roleplayfree.com/
├── CLAUDE.md                  ← this file, always in root
├── CHANGELOG.md               ← updated every session
├── CNAME                      ← contains: roleplayfree.com
├── src/
│   ├── content/
│   │   └── site-content.json  ← ALL copy, ALL links, ALL card data lives here
│   ├── components/
│   │   ├── Nav.astro
│   │   ├── ShiftBanner.astro
│   │   ├── Hero.astro
│   │   ├── HowToSteps.astro
│   │   ├── QuizTeaser.astro
│   │   ├── Terminology.astro
│   │   ├── SystemCards.astro
│   │   ├── SystemCard.astro   ← single card component, reused
│   │   ├── DiscordSection.astro
│   │   ├── LFGGuide.astro
│   │   ├── FreeRules.astro
│   │   ├── Tools.astro
│   │   ├── AIGameMasters.astro
│   │   ├── GameMasterSection.astro
│   │   └── Footer.astro
│   ├── pages/
│   │   ├── index.astro        ← main scrolling page, imports all components including Quiz.astro
│   │   ├── quiz.astro         ← quiz standalone at /quiz, imports Quiz.astro
│   │   └── start.astro        ← "Start Your Own Game" page at /start
│   └── styles/
│       └── global.css
└── public/
    └── downloads/             ← hosted free PDFs go here
```

**Rule:** To change copy, open site-content.json only. To change layout, open the relevant component only. Never edit index.astro except to add or remove a component import.

---

## VERSIONING — MANDATORY

After every session:
1. `git add .`
2. `git commit -m "v[X.X] — [one line description of what changed]"`
3. `git push origin main`
4. Update CHANGELOG.md with: version number, date, files touched, what changed

If Peter asks to revert: `git checkout v[X.X]` — show Peter the command, do not run it without confirmation.

---

## DESIGN SYSTEM

**Background:** Warm off-white / vellum paper texture. Not bright white. Hex approx #F5F0E8 or similar warm parchment tone.
**Body text:** Charcoal. Not black. Hex approx #2C2C2C.
**Max-width container:** 1200px, centred. Never let content stretch full width on large screens.
**Mobile responsive:** From day one. Single column on mobile, grid on desktop.
**No splash screen.**
**No sidebar.**
**Fixed nav bar** at top. Collapses to hamburger menu on mobile.

**System card accent colours (one per system):**
- D&D 5e: Gold (#C9A84C)
- Vampire: The Masquerade: Deep crimson (#8B0000)
- Shadowrun 5e: Chrome silver with neon green edge (#A8A9AD / #39FF14)
- Shadowrun Anarchy: Neon orange / dark grey (#FF6B00 / #2D2D2D)
- Call of Cthulhu: Deep ocean green / black (#1B4332 / #0A0A0A)
- Pathfinder 2e: Forest green / bronze (#2D5016 / #8B6914)
- FATE Core: Deep purple / silver (#4A0E8F / #C0C0C0)
- Mothership: Cold grey / deep black (#708090 / #0D0D0D)
- Mörk Borg: Sickly yellow / black (#C8B400 / #0A0A0A)
- Cairn: Mossy green / stone grey (#4A7C59 / #6B7280)
- Legend of the Five Rings: Deep red / black / gold (#8B0000 / #0A0A0A / #C9A84C)

**Image slots:** Each system card has an image slot. For v1, fill with a solid colour block matching the card accent. Slot is designed to accept a Freepik image later — dimensions 400x200px, object-fit cover.

**Fonts:** One serif for headings (suggest Playfair Display or similar), one sans-serif for body (suggest Inter or similar). Both available via Google Fonts free.

**No emojis in any UI element.**

---

## COPY RULES — MANDATORY

All text on the site must pass these rules before going live:

NEVER use:
- Em dashes (—) in copy
- Oxford-style three-part parallel lists ("fast, reliable, and seamless")
- "Dive into" / "delve into" / "it's worth noting" / "in today's world" / "seamlessly" / "robust" / "leverage" / "at the end of the day"
- Sentences starting with "Whether you're..."
- Bullet points in player-facing prose
- Passive voice where active works
- Any sentence that feels like it was written to cover all bases

ALWAYS write like a human who knows the subject. Short sentences. Direct. Occasional incomplete sentences for rhythm. Personality over coverage.

**After scaffolding:** Present every block of copy as plain text for Peter to review and rewrite before going live. Section by section. Do not consider copy final until Peter approves it.

---

## AFFILIATE SYSTEM

All paid links use variables defined at the top of site-content.json:

```json
{
  "affiliates": {
    "drivethrurpg_id": "PLACEHOLDER",
    "amazon_tag": "PLACEHOLDER",
    "startplaying_referral": "PLACEHOLDER"
  }
}
```

All DriveThruRPG links format as:
`https://www.drivethrurpg.com/product/[ID]?affiliate_id={{affiliates.drivethrurpg_id}}`

All Amazon links format as:
`https://www.amazon.com/[product]?tag={{affiliates.amazon_tag}}`

StartPlaying link uses:
`{{affiliates.startplaying_referral}}`

**Peter's affiliate setup to-do list — Claude Code should remind Peter of these at Session Zero:**

1. **DriveThruRPG** — Free to join.
   - Create account at drivethrurpg.com if not already done
   - Email matt@roll20.net with: your account email + roleplayfree.com as your website
   - Wait 2-4 business days for approval
   - Once approved, find your affiliate ID in your account dashboard
   - Replace PLACEHOLDER in site-content.json

2. **Amazon Associates** — Free to join.
   - Go to associates.amazon.com
   - Sign up with existing Amazon account
   - Add roleplayfree.com as your website
   - Get your tracking tag (format: yourname-20)
   - Replace PLACEHOLDER in site-content.json

3. **StartPlaying.games** — Free.
   - Create account at startplaying.games
   - Go to Account Settings → Refer a Friend
   - Copy your unique referral URL
   - Replace PLACEHOLDER in site-content.json
   - Note: this earns site credit not cash ($10 per referral who plays)

**Roll20 and Foundry VTT:** No affiliate programme. Plain links only.

---

## LINK LABELLING — EVERY LINK ON THE SITE

Every link must carry one of three visible labels immediately after it:

- **[Free — downloads instantly]** — hosted on GitHub, PDF starts downloading on click
- **[Free — registration required]** — external free resource requiring an account
- **[Paid]** — affiliate link, opens new tab

No exceptions. Users always know what they're clicking before they click it.

---

## PAGE STRUCTURE — INDEX.ASTRO

In this exact order, top to bottom:

1. Fixed Nav Bar
2. SHIFT RPG Banner Strip
3. Hero Section
4. How-To Steps (5 steps + optional step 6)
5. Quiz Teaser
6. Terminology
7. System Cards Grid
8. Discord Section
9. LFG Guide
10. Free Rules Index
11. Tools Links
12. AI Game Masters Section
13. Game Master Section
14. Footer

---

## NAV BAR

Fixed at top. Logo/site name left. Links right. Hamburger on mobile.

Links:
- Systems (dropdown — D&D 5e, Vampire, Shadowrun, Call of Cthulhu)
- Resources (dropdown — Free Rules, Tools, AI GMs)
- Discord
- Quiz (anchor jump to quiz section on homepage)
- Start Your Own Game (links to /start page)
- Game Master (anchor jump to GM section on homepage)

Note: Most nav links are anchor jumps within index. Only Quiz (/quiz) and Start Your Own Game (/start) are separate pages. All external links and affiliate links open in new tabs.

---

## SHIFT RPG BANNER STRIP

Full width. Dark accent bar. Minimal.
Copy: "Something new is coming. SHIFT RPG — a system built for modern play."
Email signup field placeholder (no backend — mailto link for now, or omit until ready).
[PLACEHOLDER — Peter to supply final copy and graphics when ready]

---

## HERO SECTION

Three sentences. No heading. Centred text.

Copy (locked — do not rewrite without Peter's approval):
"Tabletop RPGs are the best games you've never played. No screen, no controller — just you, some friends, or soon-to-be friends, a pile of dice, and a story no one's told before. Here is where we'll get you started."

Below hero: one button — "Skip straight to the games ↓" — anchor links to System Cards section.

---

## HOW-TO STEPS

Five numbered steps. Scannable. No walls of text.

**Step 1 — Find your system**
Not sure what to play? Take the quiz below. Already know? Skip ahead to the cards.

**Step 2 — Get the free rules**
Most systems have free starter rules. All links labelled — you'll know before you click whether it's free, needs registration, or costs money.

**Step 3 — Know what you need**
At minimum: the rules, a character sheet, and somewhere to play (a VTT if online). Most of this is free.

**Step 4 — Find your group**
Discord servers with active LFG channels below. How to write an LFG post that actually gets accepted — also below.

**Step 5 — Find a GM and start playing**
Links to Discord LFG servers. Roll20 free account [Free — registration required].
Paid option: StartPlaying.games — skip the queue, get a professional GM this week. We're not pushing this. A free game is just as good. But if you want guaranteed play tonight: [StartPlaying referral link] [Paid].
Note: framing must make clear this is optional and unbiased.

**Step 6 — AI options exist**
It's not the same as playing with real people. No banter, no shared memory, no chaos. But if you need to roll dice this second, they're out there. [Scroll link to AI Game Masters section below]

---

## QUIZ — Embedded + Standalone

The quiz component is built once and used in two places:
1. Embedded directly into index.astro as a full working section — not a teaser, not a button, the actual quiz
2. Available as a standalone page at /quiz for shareability and SEO

Same component, two places. No duplicated code.

Title: "What tabletop RPG should you play?"
Subtitle: "Eight questions. Honest answers. One recommendation — plus your runner-up."

Result displays TWO systems side by side — never just one. Format:

Left card: "Your game is [PRIMARY SYSTEM]" — full system name, colour accent, one sentence why it fits their answers, button linking to that system's card on the homepage.

Right card: "Your runner-up is [SECOND SYSTEM]" — same format. Framed as: "Not feeling [PRIMARY]? This one fits you almost as well — and for different reasons."

Both cards equal size. Neither presented as more correct than the other. The runner-up exists because someone might see their primary result and reject it — it's their exit ramp, not a consolation prize.

### SHARE BUTTONS

Two sets of share buttons:

SET 1 — Before quiz starts, above the first question:
Static share text: "Not sure what RPG to play? Take this quiz and find your system — share it with your group so everyone finds theirs."
Platforms: Facebook, Twitter/X, WhatsApp, Copy Link

SET 2 — After result is displayed, below the result cards:
Dynamic share text — pre-filled with their actual result:
"I got [SYSTEM NAME] — what tabletop RPG are you? Find out: roleplayfree.com/quiz"
Platforms: Facebook, Twitter/X, WhatsApp, Copy Link

The after share is the important one. Pre-filling with their result is what makes it travel. Build the share URL to include the result as a parameter so when someone clicks a shared link they see the quiz with a prompt saying "Your friend got Vampire: The Masquerade — what will you get?"

### QUESTION 1 — Single choice
**Setting**
"When you imagine your ideal story, what's the setting?"

A) Swords, magic, dragons — classic high fantasy
B) Dark city streets, rain on neon, corporate dystopia, cybernetic augmentation, guns and vehicles
C) Gothic horror — old mansions, political intrigue, things that go bump
D) Deep space, alien worlds, the unknown frontier
E) Gritty survival — post-apocalypse, no heroes, just people trying to live
F) Feudal honour — samurai, courtiers, a world where one wrong word ends you

Weights:
- A: D&D(3), Pathfinder(3), Cairn(2), Mörk Borg(1)
- B: Shadowrun(3), Shadowrun Anarchy(3), Cyberpunk RED(2)
- C: Vampire(3), Call of Cthulhu(2), Mörk Borg(1)
- D: Mothership(3), FATE(2)
- E: Mörk Borg(3), Cairn(3), Mothership(2), Call of Cthulhu(1)
- F: L5R(3)

### QUESTION 2 — Multi-select, pick up to four
**Playstyle**
"When you sit down at the table, what do you actually want to do?"

☐ Fight — tactical combat, knowing my build cold
☐ Talk — negotiate, manipulate, charm, deceive
☐ Investigate — uncover mysteries and secrets
☐ Become someone — deep character, personal story arc
☐ Build and acquire — resources, territory, power
☐ Cause chaos — unpredictable, impulsive, consequences be damned
☐ All of this sounds good

Weights per selection:
- Fight: D&D(3), Pathfinder(3), Shadowrun(2), Mothership(1)
- Talk: Vampire(3), Shadowrun(2), L5R(2), FATE(1)
- Investigate: Call of Cthulhu(3), Vampire(2), FATE(1)
- Become someone: Vampire(3), L5R(3), FATE(2), D&D(1)
- Build and acquire: Shadowrun(3), Vampire(2), L5R(2)
- Cause chaos: D&D(2), Shadowrun Anarchy(2), Mörk Borg(2)
- All of this: D&D(2), Pathfinder(2), Shadowrun(2), FATE(2)

### QUESTION 3 — Single choice
**Rules appetite**
"How do you feel about rules and mechanics?"

A) I want deep mechanics — I like knowing exactly how everything works
B) I want enough rules to feel fair but I don't want homework
C) Get out of my way — I want to roleplay, not do maths
D) I've never played before — I need something that teaches me as I go

Weights:
- A: Pathfinder(3), Shadowrun(3), L5R(2), D&D(1)
- B: D&D(3), Vampire(3), Shadowrun(2), Call of Cthulhu(2)
- C: FATE(3), Shadowrun Anarchy(3), Cairn(2), Mörk Borg(2)
- D: D&D(3), Call of Cthulhu(2), Cairn(2)

### QUESTION 4 — Single choice
**Character identity**
"Who do you want to be at the table?"

A) A hero — maybe flawed, but fundamentally trying to do good
B) A survivor — morality is a luxury, staying alive isn't
C) A monster — powerful, dangerous, wrestling with what that means
D) An operator — professional, skilled, the job comes first
E) A wildcard — I genuinely don't know what my character will do next
F) The joker — comic relief, chaos merchant, the one who makes the table laugh
G) A builder — networks, influence, power, politics. I want to own the throne or build a better world trying

Weights:
- A: D&D(3), Pathfinder(2), Call of Cthulhu(1)
- B: Mörk Borg(3), Cairn(3), Mothership(2)
- C: Vampire(3), Call of Cthulhu(1)
- D: Shadowrun(3), Shadowrun Anarchy(2)
- E: FATE(3), Shadowrun Anarchy(2), D&D(1)
- F: D&D(2), Pathfinder(2), FATE(1)
- G: Vampire(3), Shadowrun(2), L5R(3)

### QUESTION 5 — Single choice
**Crisis response**
"When things go wrong — and they will — how does your character handle it?"

A) Fight through it — aggression, power, direct confrontation
B) Talk your way out — lies, charm, negotiation
C) Disappear — disengage, regroup, come back smarter
D) Sacrifice something — relationships, morality, resources
E) Adapt and improvise — no plan survives contact with the enemy
F) Rally others — my strength is in who I know and who trusts me

Weights:
- A: D&D(3), Pathfinder(2), Mörk Borg(2)
- B: Vampire(3), Shadowrun(2), L5R(2)
- C: Shadowrun(3), Cairn(2)
- D: Vampire(2), Mothership(2), Call of Cthulhu(2)
- E: Shadowrun Anarchy(3), Shadowrun(2), FATE(2)
- F: Vampire(3), L5R(3), Shadowrun(1)

### QUESTION 6 — Single choice
**Story type**
"What kind of story do you actually want to tell?"

A) Me against the world — personal struggle, internal demons, who am I becoming
B) Us against the world — crew dynamics, loyalty, pulling off the impossible together
C) Uncovering the truth — conspiracies, mysteries, nothing is what it seems
D) Climbing the ladder — reputation, power, becoming untouchable
E) Surviving the world — it's hostile, it's brutal, just getting through is enough
F) Changing the world — my character will leave a mark, for better or worse

Weights:
- A: Vampire(3), Call of Cthulhu(2), Mothership(1)
- B: Shadowrun(3), D&D(2), Pathfinder(1)
- C: Call of Cthulhu(3), Vampire(2), L5R(1)
- D: Vampire(2), Shadowrun(2), L5R(3)
- E: Mörk Borg(3), Cairn(3), Mothership(2)
- F: Vampire(3), Shadowrun(2), Pathfinder(1)

### QUESTION 7 — Single choice
**Dice relationship**
"Let's talk about dice. How do you feel about them?"

A) Give me ALL of them — d4 d6 d8 d10 d12 d20 the weird ones the pretty ones I want a bag that rattles
B) I need dice at the table — rolling a handful and counting successes is half the fun
C) One type of die is fine — keep it simple, same die every time
D) Dice are fine but I could take or leave them
E) Please don't make me do dice maths

Weights:
- A: D&D(3), Pathfinder(3), Call of Cthulhu(2), Mörk Borg(2), Cairn(2)
- B: Shadowrun(3), L5R(3), Vampire(2)
- C: Shadowrun Anarchy(2), FATE(2), Cairn(2)
- D: Vampire(2), FATE(2), Mothership(1)
- E: FATE(3), Shadowrun Anarchy(2)

### QUESTION 8 — Single choice
**PvP tolerance**
"One last thing. How do you feel about conflict with other players?"

A) Love it — I want to scheme against, betray, and outmanoeuvre the people I'm sitting with
B) Occasionally fine — if it emerges naturally from the story, great
C) I'd rather not — we're a team working against the world
D) Hard no — if my character gets stabbed in the back by another player I'm going home

Weights:
- A: Vampire(3), L5R(3), Shadowrun(1)
- B: Vampire(2), Shadowrun(2), Call of Cthulhu(1)
- C: Shadowrun(3), D&D(3), Pathfinder(2), Mothership(2)
- D: D&D(3), Pathfinder(2), Cairn(2), FATE(2)

### SCORING
Tally points per system across all eight questions.
Display top two systems as results.
Result card format:
"Your game is [SYSTEM]. Your runner-up is [SYSTEM]."
Brief one-paragraph description of why. Link to each system's card on main page.

---

## TERMINOLOGY SECTION

Displayed as a two-column grid. Term left, plain English right. No paragraphs.

Gender neutral throughout. Never he/she. Always they/them/this person.

Terms:
- **PC** — Player Character. That's you. The person you play in the game world.
- **NPC** — Non-Player Character. Everyone else. The bartender, the crime boss, the dragon. The GM plays all of them.
- **GM** — Game Master. Also called Dungeon Master in D&D, Storyteller in Vampire, Keeper in Call of Cthulhu. This person builds and runs the world for everyone else. They fill in all the blanks so you can enjoy the story without building it. You might want to become one someday. Right now you're probably just looking for one.
- **XP / Karma / Advancement** — Every system has its own name for this. It's how your character grows and gets better. D&D calls it Experience Points. Shadowrun calls it Karma. Some systems skip it entirely.
- **Session** — One sitting of play. Usually two to four hours. A campaign is many sessions. A one-shot is a complete story in one session.
- **Session Zero** — The meeting before the campaign starts. No dice. Everyone agrees on the kind of story they want, what's off limits, and who their characters are. [VIDEO EMBED — Peter to replace with own YouTube link or recommended video]
- **VTT** — Virtual Tabletop. Software your group uses to play online. Roll20, Foundry, Owlbear Rodeo. You'll need an account before most online groups accept you.
- **One-Shot** — A complete game in a single session. No commitment. Great for beginners.

---

## SYSTEM CARDS

Displayed as a responsive grid. 3 per row on desktop, 2 on tablet, 1 on mobile.

Each card structure (built from site-content.json data):
1. Colour accent bar (top)
2. System name (large)
3. Tagline (one paragraph — see content below)
4. Social proof line (where applicable)
5. Image slot (400x200px, colour block for v1, Freepik image slot for v2)
6. Quick stats (plain English labels):
   - Vibe
   - Easy to learn?
   - Will my character die?
   - Campaign length
7. Dice icons (small, inline)
8. Free rules link (with label) — where available
9. Paid rulebook link (DriveThruRPG affiliate) — where applicable
10. Find a Discord button

---

## SYSTEM CARD CONTENT

### D&D 5e
Colour: Gold
Tagline: The one everyone's heard of. Be an edgy rogue, a righteous paladin, a monster-slaying barbarian. Fight things. Loot dungeons. Laugh it off in a tavern.
Social proof: As seen on Critical Role and Dimension 20. Free rules on D&D Beyond — no purchase required to start.
Vibe: Heroic fantasy
Easy to learn: Yes — playable in one session
Will my character die: Rarely — D&D is forgiving by default
Campaign length: One-shot to lifetime — completely open ended
Dice: d4 d6 d8 d10 d12 d20
Free rules: D&D Beyond [Free — registration required]
Paid: DriveThruRPG affiliate link [Paid]

### Vampire: The Masquerade
Colour: Deep crimson
Tagline: You're dead. You've been dead for three hundred years. Now you run the city — or you're trying to. Politics, betrayal, and the monster you're slowly becoming.
Social proof: If you've ever watched anything gothic and thought "I want to be that" — this is your game. Note: No free full rulebook. Free supplements and character sheets at paradoxinteractive.com [Free — downloads instantly]
Vibe: Gothic horror / Political intrigue
Easy to learn: Medium — the rules serve the story, not the other way around
Will my character die: Yes — and it'll mean something when it happens
Campaign length: Medium to long — political intrigue needs time to breathe
Dice: d10 pool
Free rules: Free supplements at Paradox [Free — downloads instantly]
Paid: DriveThruRPG affiliate link [Paid]
Note on editions: V5 is current. V20 is still widely played. Vampire: The Requiem is a separate game — different lore, different clans, different world. Check which edition your group is running before buying.

### Shadowrun 5e
Colour: Chrome silver / neon green
Tagline: Corporate dystopia. Cybernetic implants. Magic came back and nobody asked for it. You're a criminal for hire in a world that would rather you didn't exist. Run fast. Shoot straight. Never deal with a dragon.
Social proof: If Cyberpunk and fantasy had a baby and that baby had a shotgun.
Vibe: Cyberpunk fantasy / Crew dynamics
Easy to learn: Hard — but worth it. The crunch is part of the flavour.
Will my character die: Frequently — this world is not on your side. But you might have a soft-hearted GM. (Rare in Shadowrun.)
Campaign length: Flexible — single runs work as one-shots, campaigns build loyalty over time
Dice: d6 pool
Free rules: Official quickstart on DriveThruRPG [Free — registration required]
Paid: DriveThruRPG affiliate link [Paid]

### Shadowrun Anarchy
Colour: Neon orange / dark grey
Tagline: Same world as Shadowrun. Same neon-drenched corporate nightmare. Half the rulebook. There's no GM — players share the storytelling between them. If you want the flavour without the spreadsheet, start here.
Vibe: Cyberpunk fantasy / Rules light
Easy to learn: Yes — designed specifically for fast pickup
Will my character die: Yes — the world is still hostile, the rules are just kinder
Campaign length: Short to medium — fast and loose by design
Dice: d6 pool
Paid: DriveThruRPG affiliate link [Paid]

### Call of Cthulhu
Colour: Deep ocean green / black
Tagline: You're not the hero. You're an accountant from Ohio who just found something in the library that cannot be unread. You will investigate. You will probably regret it.
Social proof: Cthulhu is everywhere — the memes, the plushies, the references. The game is better than all of them.
Vibe: Cosmic horror / Investigation
Easy to learn: Yes — one of the simplest systems on this list
Will my character die: Yes — or worse, go mad. Probably both.
Campaign length: Short to medium — most scenarios are self-contained
Dice: d100 d6
Free rules: Official quickstart including The Haunting adventure + solo adventure Alone Against the Flames — both free from Chaosium [Free — downloads instantly once hosted, or Free — registration required via Chaosium site]
Paid: DriveThruRPG affiliate link [Paid]

### Pathfinder 2e
Colour: Forest green / bronze
Tagline: D&D's more tactical sibling. Every choice matters, every build is deliberate, every combat is a puzzle. If you've outgrown 5e and want more depth — this is where you go next.
Social proof: Full free rules at Archives of Nethys — no purchase required, ever.
Vibe: Heroic fantasy / Tactical depth
Easy to learn: Medium to hard — more options than D&D, well documented
Will my character die: Sometimes — more dangerous than D&D, less brutal than OSR systems
Campaign length: Long — built for epic progression
Dice: d4 d6 d8 d10 d12 d20
Free rules: Archives of Nethys [Free — no registration]
Paid: DriveThruRPG affiliate link [Paid]

### FATE Core
Colour: Deep purple / silver
Tagline: No setting. No genre. No limits. FATE is a storytelling engine — you bring the world, it handles the rest. If you've got a concept that doesn't fit anything else, it fits here.
Social proof: Completely free — pay what you want directly from the publisher.
Vibe: Genre agnostic / Narrative first
Easy to learn: Medium — simple rules, but thinking in aspects takes adjustment
Will my character die: Rarely — FATE is built for protagonists, not casualties
Campaign length: Completely variable
Dice: FATE dice — four custom d6s with plus minus and blank faces
Free rules: Evil Hat pay-what-you-want [Free — registration required]
Paid: DriveThruRPG affiliate link [Paid]

### Mothership
Colour: Cold grey / deep black
Tagline: Deep space. No heroes. Your ship's life support is failing, something got into the cargo hold, and the corporation doesn't care if you make it back. Survive if you can.
Social proof: Indie darling of the OSR (Old School Renaissance — games that embrace old-school lethality and player-driven creativity) scene. The best sci-fi horror RPG running right now.
Vibe: Sci-fi horror / Survival
Easy to learn: Yes — deliberately stripped back
Will my character die: Absolutely and graphically
Campaign length: Short — horror works best in concentrated doses
Dice: d10 d100 d6
Paid: DriveThruRPG affiliate link [Paid]

### Mörk Borg
Colour: Sickly yellow / black
Tagline: The world is ending. It has been ending for a while. You are not special. Go find something worth dying for.
Social proof: Won every indie RPG award going. Also looks incredible on a table.
Vibe: Doom metal / Grimdark fantasy
Easy to learn: Yes — brutally simple by design
Will my character die: Yes. Repeatedly. That's the game.
Campaign length: Short — characters rarely survive long enough for campaigns
Dice: d4 d6 d8 d10 d12 d20
Free rules: Free SRD at morkborg.com [Free — no registration]
Paid: DriveThruRPG affiliate link [Paid]

### Cairn
Colour: Mossy green / stone grey
Tagline: Dark forests. Ancient ruins. No classes, no levels, just what you carry and how clever you are. Old school survival fantasy stripped to its bones.
Social proof: Free. Completely free. Always will be.
Vibe: Old school fantasy / Exploration
Easy to learn: Yes — one of the fastest to learn on this list
Will my character die: Yes — the forest doesn't care about your backstory
Campaign length: Short to medium — moves fast
Dice: d4 d6 d8 d10 d12 d20
Free rules: cairnrpg.com [Free — no registration]

### Legend of the Five Rings
Colour: Deep red / black / gold
Tagline: Feudal Japan. Samurai, courtiers, and monks in a world where honour is currency and a single wrong word ends your life faster than any blade.
Social proof: A dice system unlike anything else at the table — rolling and reading them is half the experience.
Vibe: Political drama / Feudal fantasy
Easy to learn: Medium to hard — the d10 dice pool takes an hour to get comfortable with, and you'll want to read up on the lore and factions before your first session or you'll be lost
Will my character die: Yes — and honour demands you face it with dignity
Campaign length: Medium to long — the political web needs time to tangle
Dice: Custom d10 ring and skill dice unique to L5R
Paid: DriveThruRPG affiliate link [Paid]

---

## DISCORD SECTION

Your own Discord server widget first (placeholder until Peter creates server).
Discord server setup note for Peter: create one server, one general channel, pin links mirroring the site. Takes 20 minutes. Widget embed code goes here once created.

Followed by: curated external Discord servers, grouped by system.

---

## LFG GUIDE

Title: How to Actually Get Into a Discord Game

Step 1 — Before you join anything, have these ready:
- Your timezone written out properly. Not "I'm in Europe" — "GMT+1, available weekday evenings and Sunday afternoons"
- Your experience level. Be honest. GMs prefer honest beginners over people who fake experience and slow the table.
- Your system preferences (the quiz just gave you these)
- A VTT account — Roll20 is free and runs in the browser [Free — registration required]

Step 2 — The wall you'll hit:
Most servers make you complete onboarding before you can see anything useful. Read the rules post, react with the emoji, go to the roles channel, select your systems and availability. Don't skip this. It's a filter. Servers use it to remove people who can't follow basic instructions. Many servers also have their own specific application format pinned in the LFG channel. It won't look like any generic template. Read it. Follow it exactly, to the letter. Not following their format is a soft rejection even if nobody tells you that.

Step 3 — Writing an LFG post that gets responses:
```
System: [system name]
Experience: [honest assessment]
Timezone: [specific]
Availability: [specific days and times]
Looking for: [campaign / one-shot / open to either]
VTT: [which one, account ready or needs setup]
About me: [two sentences, be a human being]
```
What kills your application: vague availability, no timezone, writing an essay, saying "I'm flexible."

Step 4 — Paid GMing:
We're not pushing this. A free game found above is just as good. But if you want a guaranteed seat at a table this week without waitlists or applications, paid GMing exists and it works. [StartPlaying referral link] [Paid]

Step 5 — Session Zero:
Most serious campaigns start with a Session Zero. A no-dice meeting to agree on safety tools, what content is off limits, and character concepts. It sounds formal. It's what separates campaigns that run for two years from ones that collapse after three sessions.
[VIDEO EMBED — Peter to replace with own YouTube link or link to recommended video. Claude Code: ask Peter for this URL before finalising]

---

## FREE RULES INDEX

Separate section. Lists all freely available rules with download links.

Host directly on GitHub (public/downloads/) where license permits:
- Call of Cthulhu Quickstart (Creative Commons / free distribution permitted by Chaosium)
- Cairn full rules (completely free, always)
- Mörk Borg SRD

Link externally (do not host):
- D&D 5e Free Rules — D&D Beyond [Free — registration required]
- Pathfinder 2e — Archives of Nethys [Free — no registration]
- FATE Core — Evil Hat [Free — registration required]
- Shadowrun 5e Quickstart — DriveThruRPG [Free — registration required]

All links labelled with appropriate tag.

---

## TOOLS SECTION

Subsectioned. Plain links. Labelled.

VTTs:
- Roll20 [Free — registration required]
- Owlbear Rodeo [Free — registration required]
- Foundry VTT [Paid]
- Alchemy VTT [Free tier — registration required]
- FreeVTT [Free — no registration]

Character Sheets:
- D&D Beyond [Free — registration required]
- Archives of Nethys for Pathfinder [Free — no registration]

Dice Rollers:
- Dice.Codes [Free — no registration]

---

## AI GAME MASTERS SECTION

Intro copy (locked — do not rewrite without approval):
"Don't have a group yet and can't wait? AI Game Masters exist — and some of them are genuinely impressive. This isn't the same as playing with real people. You won't have the table banter, the shared memory, or the chaos of four humans making terrible decisions together. But if you need to roll dice this second, these platforms come closest to the real thing."

Platforms (plain links — no affiliate programmes confirmed):

**Questwright** — Purpose-built TTRPG platform with persistent character sheets, real dice mechanics, proper game state tracking, procedural world generation, tactical battle maps, NPC memory, and a rules engine that enforces actual game rules. D&D 5e and Pathfinder supported. Solo or multiplayer. The closest thing to a real TTRPG with an AI GM that currently exists.

**Friends & Fables** — AI GM called Franz. Tracks character sheets, inventory, locations, and health automatically. D&D 5e mechanics. Built for both veterans with scheduling problems and complete newcomers.

**LoreKeeper** — AI GM with persistent campaigns and multiplayer up to six players.

**MasterAI** — Mobile app. 12 classes, 8 races, levels 1-20, automatic character progression, 3D dice. Free to play with token rewards.

---

## START YOUR OWN GAME PAGE — /start

Audience: people who have friends willing to play but don't know how to begin. Completely different from the LFG audience. Tone shifts from "here's how to find your way in" to "here's how to lead your friends through the door."

Page structure:
1. One line intro — "You've got people. Here's how to turn that into a game."
2. How many people you need — three to five is ideal. Two players and a GM works. One GM, two players minimum.
3. Who runs it — one person needs to be GM. Honest one-paragraph description of what that involves. Link to GM section on homepage.
4. What you need on the night — character sheets (free), dice or a dice app (free), somewhere to sit, the free rules. Nothing else required for session one.
5. Session Zero — what it is, why it matters. Video embed placeholder (same as homepage).
6. System quick-start guides — one short section per system Peter knows well: D&D 5e, Shadowrun, Vampire, Call of Cthulhu. Three most important things to know before your first session. Peter writes these in his own voice — not AI copy.

[Peter: this page content is largely yours to write. Claude Code should scaffold the layout and leave clearly marked placeholder sections for your text.]

[TO BE PLANNED — Peter and Claude to discuss in a future session]
Placeholder: "Thinking about running your own game? This section is coming. Check back soon."
Link in nav pointing to this section so it's not a dead link.

---

## FOOTER

Simple. Links repeated from nav. Attribution line:
"Images from Freepik" (add once images are added in v2)
"Built with Astro. Hosted on GitHub Pages."
No copyright date (causes maintenance overhead — omit).

---

## CHANGELOG

### v0.1 — Planning complete
Date: [date Claude Code starts]
Status: CLAUDE.md written. No code yet. Awaiting Session Zero.

---

## WHAT CLAUDE CODE MUST NOT DO

- Do not add features not listed in this document without asking first
- Do not rewrite copy without presenting it to Peter for approval
- Do not change more than one component at a time without listing every affected file first
- Do not use em dashes, bullet points in prose, or any of the banned phrases listed above
- Do not commit without a version tag and CHANGELOG entry
- Do not proceed past Session Zero checklist without Peter's explicit approval
- Do not assume. If something is unclear, ask one specific question before proceeding.
