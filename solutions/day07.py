import numpy as np
from collections import Counter

def eval(c):
    if len(c) > 1:
        (_, c1), (_, c2) = c.most_common(2)
    else:
        return 6 # 5 of a kind
    if c1 == 4:
        return 5
    elif c1 == 3 and c2 == 2:
        return 4
    elif c1 == 3:
        return 3
    elif c1 == 2 and c2 == 2:
        return 2
    elif c1 == 2:
        return 1
    return 0

def set_jokers(c): # jokers are always best played as the already highest
    cards = dict(c)
    if "J" not in c:
        return c
    if cards["J"] == 5:
        return Counter("22222")
    best = max( [(a,b) for a,b in cards.items() if a!="J"], key=lambda x: x[1])
    cards[best[0]] += cards["J"]
    del cards["J"]
    return Counter("".join([ a * b for a,b in cards.items() ]))
    
class Hand:
    def __init__(self, hand, jokers=False):
        self.hand = hand
        self.jokers = jokers
    
    def __lt__(self, oth):
        order = "23456789TJQKA" if not self.jokers else "J23456789TQKA"
        cs = Counter(self.hand)
        co = Counter(oth.hand)
        if self.jokers:
            cs, co = set_jokers(cs), set_jokers(co)

        e1 = eval(cs)
        e2 = eval(co)
        if e1 != e2:
            return e1 < e2
        
        for a,b in zip(self.hand, oth.hand):
            if a != b:
                return order.index(a) < order.index(b)
        return False

with open("day07.input") as f:
    hands_raw = [ (l[:5], int(l[6:-1])) for l in f ]

hands1 = [ (Hand(a), b) for a,b in hands_raw ]
hands2 = [ (Hand(a, True), b) for a,b in hands_raw ]

for hands in [ hands1, hands2 ]:
    h =np.array([ a for a,_ in hands ])
    rank = h.argsort().argsort() + 1
    bid = np.array([ b for _,b in hands ])
    print((rank * bid).sum())