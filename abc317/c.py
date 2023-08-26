from collections import defaultdict

g = defaultdict(list)    
n, m = map(int, input().split())
ee = [None] * m
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append((b, c))
    g[b].append((a, c))

visited = [False] * n
def dfs(x, xc):
    global g
    a = 0
    if visited[x]:
        return 0
    visited[x] = True
    for (v, c) in g[x]:
        a = max(a, xc + dfs(v, c))
    visited[x] = False
    return a

ans = 0
for i in range(n):
    ans = max(ans, dfs(i, 0))
print(ans)