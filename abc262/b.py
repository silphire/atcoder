from collections import defaultdict

n, m = map(int, input().split())
g = defaultdict(set)
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].add(v)
    g[v].add(u)
ans = 0
for a in range(n):
    for b in range(a + 1, n):
        if b not in g[a]:
            continue
        for c in range(b + 1, n):
            if c in g[b] and a in g[c]:
                ans += 1
print(ans)