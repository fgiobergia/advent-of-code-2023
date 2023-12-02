from functools import reduce

def strip_split(s,ch=","):
    return s.strip().split(ch)

if __name__ == "__main__":
    with open("day02.input") as f:
        games = { i+1: list(map(strip_split, strip_split(strip_split(l,":")[1],";"))) for i, l in enumerate(f.readlines()) }
    
    # preparing the data structure
    games = {
        k: [
            {
                el.strip().split(" ")[1]: int(el.strip().split(" ")[0])
                for el in draft
            }
            for draft in v
        ]
        for k, v in games.items()
    }

    limits = {"red": 12, "green": 13, "blue": 14}

    # part 1 -- check games for validity
    sum_id = 0
    for game_id, drafts in games.items():
        valid = True
        for draft in drafts:
            valid &= all([ limits[k] >= draft.get(k, 0) for k in limits.keys() ])
        sum_id += valid * game_id
    print(sum_id)

    # part 2 -- get lower bound on dice
    def prod(x):
        return reduce(lambda a,b: a * b, x)
    
    def lower_bounds(drafts):
        return reduce(lambda a,b: { i: max(a.get(i,0), b.get(i,0)) for i in a.keys() | b.keys() }, drafts)

    print(sum(prod(lower_bounds(drafts).values()) for drafts in games.values()))