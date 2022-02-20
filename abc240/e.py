from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)

n = int(input())
g = defaultdict(list)

for _ in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

ans = [None] * n
m = 0

def dfs(x, p):
    global m, n, g
    mi = float('inf')
    ma = float('-inf')

    for y in g[x]:
        if y == p:
            continue
        a, b = dfs(y, x)
        mi = min(mi, a)
        ma = max(ma, b)

    if ma < 0:
        m += 1
        mi = m
        ma = m

    ans[x - 1] = (mi, ma)
    return (mi, ma)

dfs(1, 0)
for a in ans:
    print(*a)