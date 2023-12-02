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

    def prod(x):
        return reduce(lambda a,b: a * b, x)
    
    def lower_bounds(drafts):
        return reduce(lambda a,b: { i: max(a.get(i,0), b.get(i,0)) for i in a.keys() | b.keys() }, drafts)

    bounds = { game: lower_bounds(drafts) for game, drafts in games.items() }

    # part 1 -- check games for validity
    print(sum([ g for g, b in bounds.items() if all([ limits[k] >= b.get(k,0) for k in limits ])]))

    # part 2 -- get lower bound on dice
    print(sum(prod(lower_bounds(drafts).values()) for drafts in games.values()))