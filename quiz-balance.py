import json

with open('src/content/site-content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

questions = data['quiz']['questions']
systems = [s['id'] for s in data['systems']]

max_scores = {s: 0 for s in systems}

for q in questions:
    if q['type'] == 'single':
        # Best single option per system
        best = {s: 0 for s in systems}
        for opt in q['options']:
            for sys, pts in opt['weights'].items():
                best[sys] = max(best[sys], pts)
        for s in systems:
            max_scores[s] += best[s]

    elif q['type'] == 'multi':
        # Best 4 options per system
        for s in systems:
            opts_with_pts = sorted(
                [opt['weights'].get(s, 0) for opt in q['options']],
                reverse=True
            )
            max_scores[s] += sum(opts_with_pts[:4])

print("Maximum possible score per system:\n")
ranked = sorted(max_scores.items(), key=lambda x: x[1], reverse=True)
for sys, score in ranked:
    name = next(s['name'] for s in data['systems'] if s['id'] == sys)
    bar = '█' * score
    print(f"  {name:<32} {score:>3}  {bar}")

print(f"\nHighest: {ranked[0][1]}  Lowest: {ranked[-1][1]}")
print(f"Range: {ranked[0][1] - ranked[-1][1]} points")
