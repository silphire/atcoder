from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)

n = int(input())
g = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

def dfs(x, p):
    m = 1
    for a in g[x]:
        if a != p:
            m += dfs(a, x)
    return m

ans = []
for a in g[1]:
    x = dfs(a, 1)
    ans.append(x)
print(sum(sorted(ans)[:-1]) + 1)