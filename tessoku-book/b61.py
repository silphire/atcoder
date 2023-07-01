from collections import defaultdict

n, m = map(int, input().split())
g = defaultdict(int)
for _ in range(m):
    a, b = map(int, input().split())
    g[a] += 1
    g[b] += 1

print(sorted(g.items(), key=lambda x: -x[1])[0][0])