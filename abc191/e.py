import heapq
from collections import defaultdict

INF = float('inf')

n, m = map(int, input().split())

cost = defaultdict(list)
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    cost[a].append((c, b))

d = [[INF] * n for _ in range(n)]

for v in range(n):
    visited = [False] * n
    q = [(0, v)]
    while q:
        _, a = heapq.heappop(q)
        
        if visited[a]:
            continue
        visited[a] = True

        for c, b in cost[a]:
            d[v][b] = min(d[v][b], (0 if v == a else d[v][a]) + c)
            heapq.heappush(q, (d[v][b], b))

for a in range(n):
    ans = d[a][a]
    for b in range(n):
        if a == b:
            continue
        if d[a][b] != INF and d[b][a] != INF:
            ans = min(ans, d[a][b] + d[b][a])
    if ans == INF:
        print(-1)
    else:
        print(ans)