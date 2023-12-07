with open("day05.input") as f:
    seeds = list(map(int,f.readline().split()[1:]))

    maps = []
    curr_map = []
    for line in f:
        line = line.strip()
        if not line:
            continue
        if line[0].isalpha():
            # new map
            if curr_map:
                maps.append(curr_map)
            curr_map = []
            continue
        dst, src, rng = map(int, line.split())
        curr_map.append((src, src+rng, dst, dst+rng))
    if curr_map:
        maps.append(curr_map)
    
def seed_to_location(seed, maps):
    for m in maps:
        for ss, se, ds, _ in m:
            if ss <= seed < se:
                # found the range
                seed = ds + (seed - ss)
                break
        # default: keep same seed
    return seed

print(min(seed_to_location(seed, maps) for seed in seeds))

def seed_range_to_location(seed, rng, maps):
    seeds = [[seed, seed+rng-1, 0]]
    ref = rng
    for m in maps:
        new_seeds = []
        i = 0
        while i < len(seeds):
            seed_start, seed_end, _ = seeds[i]
            for ss, se, ds, de in m:
                #   v---------v
                #      v---v
                if ss <= seed_start < seed_end <= se:
                    new_seeds.append([ds + seed_start - ss, ds + seed_end - ss, 0])
                    seeds[i][2] = 1 # processed
                    break
                #     v-----v
                #   v----v seed
                elif seed_start <= ss < seed_end <= se:
                    new_seeds.append([ds, ds + seed_end - ss, 0])
                    seeds.append([seed_start, ss-1, 0])
                    seeds[i][2] = 1
                    break
                #     v-----v
                #   v----------v seed
                elif seed_start < ss < se < seed_end: 
                    new_seeds.append([ds, de, 0])
                    seeds.append([seed_start, ss-1, 0])
                    seeds.append([se+1, seed_end, 0])
                    seeds[i][2] = 1
                    break
                #      v----v
                #        v-----v seed
                elif ss <= seed_start < se <= seed_end:
                    new_seeds.append([seed_start - ss + ds, de, 0])
                    seeds.append([se+1, seed_end, 0])
                    seeds[i][2] = 1
                    break
                    
            i += 1
        seeds = new_seeds + [ [s, e, 0] for s, e, p in seeds if not p ]

    return [ w[0] for w in seeds ]

# keep maps sorted
maps = [ sorted(m, key=lambda x: x[0]) for m in maps ]
maps = [ [ [a, b-1, c, d-1] for a,b,c,d in map ] for map in maps ]

from itertools import chain
mins = [ seed_range_to_location(seeds[i], seeds[i+1], maps) for i in range(0, len(seeds), 2) ]
print(min(chain(*mins)))