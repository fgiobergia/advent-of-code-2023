
with open("day03.input") as f:
    lines = [ list(l.strip()) for l in f ]

for i in range(len(lines)):
    c = []
    cstart = None
    j = 0
    while j < len(lines[i]):
        if lines[i][j].isdigit():
            if not c:
                cstart = j
            c.append(lines[i][j])
        elif c:
            # some number loaded, replace!
            num = int("".join(c))
            lines[i][cstart:j] = [num] * len(c)
            c = []
            cstart = None
        j += 1
    if c:
        num = int("".join(c))
        lines[i][cstart:j] = [num] * len(c)

# Part 1
csum = 0
for i in range(len(lines)):
    j = 0
    while j < len(lines[i]):
        if isinstance(lines[i][j], int):
            # a number, check neighbors
            found = False
            for y in [-1,0,+1]:
                for x in [-1,0,+1]:
                    if i+y < 0 or i+y >= len(lines) or j+x < 0 or j+x >= len(lines[i]): # should be lines[i+y] but let's assume it's consistent
                        continue # can't go there
                    if not isinstance(lines[i+y][j+x], int) and lines[i+y][j+x] != ".":
                        # part! (no "breaking" to avoid extra if's... the input is small enough
                        # for this not to be very computationally expensive)
                        found = True
            if found:
                csum += lines[i][j]
                # skip the rest of the number
                while j < len(lines[i]) and isinstance(lines[i][j], int):
                    j += 1
                j -= 1 # one step back, 
        j += 1
print(csum)

# Part 2
ratios = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] != "*":
            continue
        parts = []
        skip = []
        for y in [-1,0,+1]:
            for x in [-1,0,+1]:
                if (y,x) in skip or i+y < 0 or i+y >= len(lines) or j+x < 0 or j+x >= len(lines[i]):
                    continue
                if isinstance(lines[i+y][j+x], int):
                    # number!
                    parts.append(lines[i+y][j+x])

                    # Turns out, there is no gear for which the same
                    # number appears twice , so we could have just
                    # removed all gears with parts[0] == parts[1] -
                    # however, this way should me more robust
                    x0 = x
                    while x < 2:
                        if j+x < len(lines[i+y]) and lines[i+y][j+x] == lines[i+y][j+x0]:
                            skip.append((y,x))
                        x += 1
        if len(parts) == 2:
            ratios += parts[0] * parts[1]

print(ratios)