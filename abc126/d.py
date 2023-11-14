from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
c = [None] * n
g = defaultdict(list)
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append((v, w))
    g[v].append((u, w))

def dfs(x):
    for y, w in g[x]:
        if c[y] is None:
            if w % 2 == 0:
                c[y] = c[x]
            else:
                c[y] = 1 - c[x]
            dfs(y)
c[0] = 0
dfs(0)
for i in range(n):
    print(c[i])