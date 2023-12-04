with open("day04.input") as f:
    cards = [ line.split(":")[1].strip().split("|") for line in f ]
cards = [ (set(win.strip().split()), set(played.strip().split())) for win, played in cards ]

print(sum( (1 << len(w & p)) // 2 for w, p in cards ))

cards = [ [c, 1] for c in cards ]

for i, ((w,p), cnt) in enumerate(cards):
    o = len(w & p)
    for j in range(i + 1, i + 1 + o):
        cards[j][1] += cnt

print(sum(c[1] for c in cards))