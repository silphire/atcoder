from collections import defaultdict

n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

q = int(input())
for _ in range(q):
    x, k = map(int, input().split())

    vs = {x}
    def dfs(v, d, p):
        if d <= 0:
            return 0
        for nv in g[v]:
            if nv != p:
                vs.add(nv)
                dfs(nv, d - 1, v)
    dfs(x, k, -1)
    print(sum(vs))