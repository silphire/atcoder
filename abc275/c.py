import itertools

def dist2(p, q):
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2

ss = [
    input().rstrip()
    for _ in range(9)
]
pp = {(x, y) for y in range(9) for x in range(9) if ss[y][x] == '#'}

ans = 0
for ps in itertools.combinations(pp, 4):
    s = set(dist2(a, b) for (a, b) in itertools.combinations(ps, 2))
    if len(s) == 2:
        ans += 1
print(ans)