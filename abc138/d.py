from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)

n, q = map(int, input().split())

ctr = [0] * n
g = defaultdict(set)
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].add(b)
    g[b].add(a)

for i in range(q):
    p, x = map(int, input().split())
    p -= 1
    ctr[p] += x

visited = [False] * n
ans = [0] * n
def dfs(p, x):
    global visited, g, ctr, ans
    visited[p] = True
    ans[p] += x
    for pp in g[p]:
        if not visited[pp]:
            dfs(pp, x + ctr[pp])
    visited[p] = False

dfs(0, ctr[0])
print(' '.join(map(str, ans)))