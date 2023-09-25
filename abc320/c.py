import itertools

m = int(input())
ss = [
    input()
    for _ in range(3)
]

ans = float('inf')
for i in range(10):
    si = str(i)

    f = False
    for s in ss:
        if si not in s:
            f = True
            break
    if f:
        continue

    for x in itertools.permutations(range(3), 3):
        p = 0
        t = -1
        while p < 3:
            t += 1
            if ss[x[p]][t % m] == si:
                p += 1
        ans = min(ans, t)

if ans == float('inf'):
    print(-1)
else:
    print(ans)