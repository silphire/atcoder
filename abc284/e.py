from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 9)

n, m = map(int, input().split())
g = defaultdict(list)
vis = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

ans = 0
def dfs(x, p):
    global g, vis, ans
    if ans >= 10 ** 6:
        return
    vis[x] = True
    ans += 1
    for y in g[x]:
        if y == p:
            continue
        if vis[y]:
            continue
        dfs(y, x)
    vis[x] = False
dfs(1, -1)
print(min(10 ** 6, ans))