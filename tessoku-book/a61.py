from collections import defaultdict

n, m = map(int, input().split())
g = defaultdict(set)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].add(b)
    g[b].add(a)
for x in range(1, n + 1):
    if g[x]:
        print(f'{x}: {g[x]}')
    else:
        print(f'{x}: {{}}')
