with open("day06.input") as f:
    time = list(map(int, f.readline().split()[1:]))
    dist = list(map(int, f.readline().split()[1:]))

from math import ceil, floor
eps = 1e-5
prod = 1
for t, d in zip(time, dist):
    t0 = ceil((t - (t ** 2 - 4 * d)**0.5)/ 2 + eps)
    t1 = floor((t + (t ** 2 - 4 * d)**0.5)/ 2 - eps)
    prod *= (t1 - t0 + 1)
print(prod)

t = int("".join(map(str, time)))
d = int("".join(map(str, dist)))
t0 = ceil((t - (t ** 2 - 4 * d)**0.5)/ 2 + eps)
t1 = floor((t + (t ** 2 - 4 * d)**0.5)/ 2 - eps)
print(t1 - t0 + 1)