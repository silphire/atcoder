from collections import defaultdict

n = int(input())
f = defaultdict(int)
for x in range(2, n + 1):
    xx = x
    for y in range(2, x + 1):
        while xx % y == 0:
            f[y] += 1
            xx //= y

ans = 0

ns = list(f)
nns = len(ns)
for a in range(nns):
    if f[ns[a]] >= 74:
        ans += 1
for a in range(nns):
    for b in range(nns):
        if a == b:
            continue
        if f[ns[a]] >= 2 and f[ns[b]] >= 24:
            ans += 1
for a in range(nns):
    for b in range(nns):
        if a == b:
            continue
        if f[ns[a]] >= 4 and f[ns[b]] >= 14:
            ans += 1
for a in range(nns):
    for b in range(nns):
        if a == b:
            continue
        for c in range(b + 1, nns):
            if a == b or a == c:
                continue
            if f[ns[a]] >= 2 and f[ns[b]] >= 4 and f[ns[c]] >= 4:
                ans += 1

print(ans)
