from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)

n = int(input())
g = defaultdict(set)
for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].add(v)
    g[v].add(u)

d = [0] * n
sz = [1] * n
def dfs(x, n):
    if d[x] > 0:
        return

    nv = []
    d[x] = n
    for v in g[x]:
        if d[v] == 0 and v != 0:
            nv.append(v)
    for v in nv:
        dfs(v, n + 1)
        sz[x] += sz[v]
dfs(0, 0)

ans = [0] * n
ans[0] = sum(d)

def dfs2(x):
    for v in g[x]:
        if ans[v] > 0:
            continue
        ans[v] = ans[x] + n - 2 * sz[v]
        dfs2(v)
dfs2(0)

for a in ans:
    print(a)
