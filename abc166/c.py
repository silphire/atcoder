from collections import defaultdict

n, m = map(int, input().split())
h = list(map(int, input().split()))

to = defaultdict(set)
for i in range(m):
    aa, bb = map(int, input().split())
    aa -= 1
    bb -= 1
    to[aa].add(bb)
    to[bb].add(aa)

ans = 0
for i in range(n):
    f = True
    for t in to[i]:
        if h[i] <= h[t]:
            f = False
            break
    if f:
        ans += 1
print(ans)
