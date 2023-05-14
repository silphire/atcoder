from collections import defaultdict
from collections import deque

n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
dist = [-1] * n
dist[0] = 0
q = deque([0])
while q:
    x = q.popleft()
    for y in g[x]:
        if dist[y] != -1:
            continue
        dist[y] = dist[x] + 1
        q.append(y)

for i in range(n):
    print(dist[i])
