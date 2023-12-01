import string
from itertools import chain

with open("input01") as f:
    lines = f.readlines()

# Part 1
digits = [ [ int(c) for c in line if c in string.digits ] for line in lines ]
print(sum([ d[0] * 10 + d[-1] for d in digits ]))

# Part 2
# replacement needs to be done "left-to-right", simply
# replacing all strings early on will not provide the
# desired output (eightwo => 82)
spelt = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits = [
    list(chain(*[
        [ int(line[i]) ] if line[i] in string.digits
        else [ j+1 for j in range(len(spelt)) if line[i:].startswith(spelt[j]) ]
        for i in range(len(line))
    ]))
    for line in lines
]
print(sum([ d[0] * 10 + d[-1] for d in digits ]))