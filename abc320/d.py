from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
d = defaultdict(list)
for _ in range(m):
    a, b, x, y = map(int, input().split())
    a -= 1
    b -= 1
    d[a].append((b, x, y))
    d[b].append((a, -x, -y))

px = [None] * n
py = [None] * n
px[0] = py[0] = 0

visited = [False] * n

def dfs(p):
    global visited, d

    if visited[p]:
        return
    visited[p] = True

    for i, x, y in d[p]:
        if not visited[i]:
            px[i] = px[p] + x
            py[i] = py[p] + y
            dfs(i)

dfs(0)
for i in range(n):
    if px[i] is None or py[i] is None:
        print("undecidable")
    else:
        print(*[px[i], py[i]])