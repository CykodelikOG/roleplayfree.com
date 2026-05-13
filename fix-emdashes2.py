with open('src/content/site-content.json', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Vampire social proof (escaped quotes in JSON source)
    (r'\"I want to be that\" — this is your game.', r'\"I want to be that\"? This is your game.'),
    # Q4 options
    ('A hero — maybe flawed, but fundamentally trying to do good', 'A hero, maybe flawed, but fundamentally trying to do good'),
    ('A survivor — morality is a luxury, staying alive isn\'t', 'A survivor: morality is a luxury, staying alive isn\'t'),
    ('A monster — powerful, dangerous, wrestling with what that means', 'A monster: powerful, dangerous, wrestling with what that means'),
    ('An operator — professional, skilled, the job comes first', 'An operator: professional, skilled, the job comes first'),
    ('A wildcard — I genuinely don\'t know what my character will do next', 'A wildcard. I genuinely don\'t know what my character will do next.'),
    ('The joker — comic relief, chaos merchant, the one who makes the table laugh', 'The joker: comic relief, chaos merchant, the one who makes the table laugh'),
    ('A builder — networks, influence, power, politics. I want to own the throne or build a better world trying', 'A builder: networks, influence, power, politics. I want to own the throne, or build a better world trying.'),
    # Q5 question text
    ('When things go wrong — and they will — how does your character handle it?', 'When things go wrong, and they will, how does your character handle it?'),
    # Q5 options
    ('Fight through it — aggression, power, direct confrontation', 'Fight through it: aggression, power, direct confrontation'),
    ('Talk your way out — lies, charm, negotiation', 'Talk your way out: lies, charm, negotiation'),
    ('Disappear — disengage, regroup, come back smarter', 'Disappear: disengage, regroup, come back smarter'),
    ('Sacrifice something — relationships, morality, resources', 'Sacrifice something: relationships, morality, resources'),
    ('Adapt and improvise — no plan survives contact with the enemy', 'Adapt and improvise. No plan survives contact with the enemy.'),
    ('Rally others — my strength is in who I know and who trusts me', 'Rally others: my strength is in who I know and who trusts me'),
    # Q6 options
    ('Me against the world — personal struggle, internal demons, who am I becoming', 'Me against the world: personal struggle, internal demons, who am I becoming'),
    ('Us against the world — crew dynamics, loyalty, pulling off the impossible together', 'Us against the world: crew dynamics, loyalty, pulling off the impossible together'),
    ('Uncovering the truth — conspiracies, mysteries, nothing is what it seems', 'Uncovering the truth: conspiracies, mysteries, nothing is what it seems'),
    ('Climbing the ladder — reputation, power, becoming untouchable', 'Climbing the ladder: reputation, power, becoming untouchable'),
    ('Surviving the world — it\'s hostile, it\'s brutal, just getting through is enough', 'Surviving the world: it\'s hostile, it\'s brutal, just getting through is enough'),
    ('Changing the world — my character will leave a mark, for better or worse', 'Changing the world: my character will leave a mark, for better or worse'),
    # Q7 options
    ('Give me ALL of them — d4 d6 d8 d10 d12 d20 the weird ones the pretty ones I want a bag that rattles', 'Give me ALL of them: d4 d6 d8 d10 d12 d20, the weird ones, the pretty ones. I want a bag that rattles.'),
    ('I need dice at the table — rolling a handful and counting successes is half the fun', 'I need dice at the table: rolling a handful and counting successes is half the fun'),
    ('One type of die is fine — keep it simple, same die every time', 'One type of die is fine: keep it simple, same die every time'),
    # Q8 options
    ('Love it — I want to scheme against, betray, and outmanoeuvre the people I\'m sitting with', 'Love it: I want to scheme against, betray, and outmanoeuvre the people I\'m sitting with'),
    ('Occasionally fine — if it emerges naturally from the story, great', 'Occasionally fine. If it emerges naturally from the story, great.'),
    ("I'd rather not — we're a team working against the world", "I'd rather not. We're a team working against the world."),
    ('Hard no — if my character gets stabbed in the back by another player I\'m going home', 'Hard no. If my character gets stabbed in the back by another player, I\'m going home.'),
    # Character sheet names
    ('Pathfinder 2e — Archives of Nethys', 'Pathfinder 2e: Archives of Nethys'),
    ('Progeny — Vampire V5 character creator', 'Progeny: Vampire V5 character creator'),
    ('Renegade Game Studios — Vampire V5 fillable PDF', 'Renegade Game Studios: Vampire V5 fillable PDF'),
    ('Chaosium — Call of Cthulhu sheets', 'Chaosium: Call of Cthulhu sheets'),
    ('Evil Hat — FATE Core sheet', 'Evil Hat: FATE Core sheet'),
    ('Tuesday Knight Games — Mothership sheets', 'Tuesday Knight Games: Mothership sheets'),
    # Pricing notes
    ('private beta — free while in beta.', 'private beta. Free while in beta.'),
    ('covers a session — guests don\'t need their own subscription.', 'covers a session. Guests don\'t need their own subscription.'),
]

for old, new in replacements:
    content = content.replace(old, new)

remaining = [(i+1, line.strip()[:120]) for i, line in enumerate(content.split('\n')) if '—' in line]
print(f'Remaining em dashes: {len(remaining)}')
for lineno, r in remaining:
    print(f'  Line {lineno}: {r}')

with open('src/content/site-content.json', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
