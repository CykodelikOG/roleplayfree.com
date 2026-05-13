with open('src/content/site-content.json', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    ('SHIFT RPG — a system built for modern play.', 'SHIFT RPG: a system built for modern play.'),
    ('No screen, no controller — just you', 'No screen, no controller. Just you'),
    ('All links labelled — you\'ll know before you click', 'All links labelled. You\'ll know before you click'),
    ('that actually gets accepted — also below.', 'that actually gets accepted. Both are below.'),
    ('Free — registration required', 'Free, registration required'),
    ('Free — downloads instantly', 'Free, downloads instantly'),
    ('Free — no registration', 'Free, no registration'),
    ('Free tier — registration required', 'Free tier, registration required'),
    ('StartPlaying.games — skip the queue, get a professional GM this week', 'StartPlaying.games: skip the queue, get a professional GM this week'),
    ('Free rules on D&D Beyond — no purchase required to start.', 'Free rules on D&D Beyond. No purchase required to start.'),
    ('Yes — playable in one session', 'Yes. Playable in one session.'),
    ('Rarely — D&D is forgiving by default', 'Rarely. D&D is forgiving by default.'),
    ('Now you run the city — or you\'re trying to.', 'Now you run the city, or you\'re trying to.'),
    ('"I want to be that" — this is your game.', '"I want to be that"? This is your game.'),
    ('Medium — the rules serve the story, not the other way around', 'Medium. The rules serve the story, not the other way around.'),
    ('Yes — and it\'ll mean something when it happens', 'Yes, and it\'ll mean something when it happens'),
    ('Medium to long — political intrigue needs time to breathe', 'Medium to long. Political intrigue needs time to breathe.'),
    ('a separate game — different lore, different clans, different world.', 'a separate game. Different lore, different clans, different world.'),
    ('Hard — but worth it. The crunch is part of the flavour.', 'Hard, but worth it. The crunch is part of the flavour.'),
    ('Frequently — this world is not on your side.', 'Frequently. This world is not on your side.'),
    ('Flexible — single runs or full campaigns', 'Flexible. Single runs or full campaigns.'),
    ('There\'s no GM — players share the storytelling between them.', 'There\'s no GM. Players share the storytelling between them.'),
    ('Yes — designed specifically for fast pickup', 'Yes, designed for fast pickup'),
    ('Yes — the world is still hostile, the rules are just kinder', 'Yes. The world is still hostile, the rules are just kinder.'),
    ('Short to medium — fast and loose by design', 'Short to medium. Fast and loose by design.'),
    ('Cthulhu is everywhere — the memes, the plushies, the references.', 'Cthulhu is everywhere: the memes, the plushies, the references.'),
    ('Yes — one of the simplest systems on this list', 'Yes, one of the simplest systems on this list'),
    ('Yes — or worse, go mad. Probably both.', 'Yes. Or worse, go mad. Probably both.'),
    ('Short to medium — most scenarios are self-contained', 'Short to medium. Most scenarios are self-contained.'),
    ('want more depth — this is where you go next.', 'want more depth. This is where you go next.'),
    ('Full free rules at Archives of Nethys — no purchase required, ever.', 'Full free rules at Archives of Nethys. No purchase required, ever.'),
    ('Medium to hard — more options than D&D, well documented', 'Medium to hard. More options than D&D, well documented.'),
    ('Sometimes — more dangerous than D&D, less brutal than OSR systems', 'Sometimes. More dangerous than D&D, less brutal than OSR systems.'),
    ('Long — built for epic progression', 'Long. Built for epic progression.'),
    ('FATE is a storytelling engine — you bring the world, it handles the rest.', 'FATE is a storytelling engine. You bring the world, it handles the rest.'),
    ('Completely free — pay what you want directly from the publisher.', 'Completely free. Pay what you want directly from the publisher.'),
    ('Medium — simple rules, but thinking in aspects takes adjustment', 'Medium. Simple rules, but thinking in aspects takes adjustment.'),
    ('Rarely — FATE is built for protagonists, not casualties', 'Rarely. FATE is built for protagonists, not casualties.'),
    ('Yes — deliberately stripped back', 'Yes, deliberately stripped back'),
    ('Short — horror works best in concentrated doses', 'Short. Horror works best in concentrated doses.'),
    ('Yes — brutally simple by design', 'Yes, brutally simple by design'),
    ('Short — characters rarely survive long enough for campaigns', 'Short. Characters rarely survive long enough for campaigns.'),
    ('Yes — one of the fastest to learn on this list', 'Yes, one of the fastest to learn on this list'),
    ('Yes — the forest doesn\'t care about your backstory', 'Yes. The forest doesn\'t care about your backstory.'),
    ('Short to medium — moves fast', 'Short to medium. Moves fast.'),
    ('unlike anything else at the table — rolling and reading them is half the experience.', 'unlike anything else at the table. Rolling and reading them is half the experience.'),
    ('Medium to hard — the dice pool takes an hour to get comfortable with', 'Medium to hard. The dice pool takes an hour to get comfortable with'),
    ('Yes — and honour demands you face it with dignity', 'Yes, and honour demands you face it with dignity'),
    ('Medium to long — the political web needs time to tangle', 'Medium to long. The political web needs time to tangle.'),
    ('One recommendation — plus your runner-up.', 'One recommendation, plus your runner-up.'),
    ('find your system — share it with your group so everyone finds theirs.', 'find your system. Share it with your group so everyone finds theirs.'),
    ('Swords, magic, dragons — classic high fantasy', 'Swords, magic, dragons. Classic high fantasy.'),
    ('Gothic horror — old mansions, political intrigue, things that go bump', 'Gothic horror: old mansions, political intrigue, things that go bump'),
    ('Gritty survival — post-apocalypse, no heroes, just people trying to live', 'Gritty survival: post-apocalypse, no heroes, just people trying to live'),
    ('Feudal honour — samurai, courtiers, a world where one wrong word ends you', 'Feudal honour: samurai, courtiers, a world where one wrong word ends you'),
    ('Fight — tactical combat, knowing my build cold', 'Fight: tactical combat, knowing my build cold'),
    ('Talk — negotiate, manipulate, charm, deceive', 'Talk: negotiate, manipulate, charm, deceive'),
    ('Investigate — uncover mysteries and secrets', 'Investigate: uncover mysteries and secrets'),
    ('Become someone — deep character, personal story arc', 'Become someone: deep character, personal story arc'),
    ('Build and acquire — resources, territory, power', 'Build and acquire: resources, territory, power'),
    ('Cause chaos — unpredictable, impulsive, consequences be damned', 'Cause chaos: unpredictable, impulsive, consequences be damned'),
    ('I want deep mechanics — I like knowing exactly how everything works', 'I want deep mechanics. I like knowing exactly how everything works.'),
    ('Get out of my way — I want to roleplay, not do maths', 'Get out of my way. I want to roleplay, not do maths.'),
    ("I've never played before — I need something that teaches me as I go", "I've never played before. I need something that teaches me as I go."),
]

for old, new in replacements:
    content = content.replace(old, new)

remaining = [line.strip()[:120] for i, line in enumerate(content.split('\n'), 1) if '—' in line]
print(f'Remaining em dashes: {len(remaining)}')
for r in remaining:
    print(f'  {r}')

with open('src/content/site-content.json', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
