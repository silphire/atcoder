import sys
from collections import defaultdict
sys.setrecursionlimit(2 * 10 ** 5)
n, m = map(int, input().split())
g = defaultdict(list)
f = [False] * n
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

def dfs(x, p):
    global g, f
    if f[x]:
        return
    f[x] = True
    for y in g[x]:
        if y != p:
            dfs(y, x)
dfs(0, None)
if all(f):
    print('The graph is connected.')
else:
    print('The graph is not connected.')