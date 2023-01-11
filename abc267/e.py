from collections import defaultdict
import heapq

n, m = map(int, input().split())
aa = list(map(int, input().split()))

cc = [0] * n
g = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)
    cc[u] += aa[v]
    cc[v] += aa[u]

removed = [False] * n
pq = []

for x in range(n):
    heapq.heappush(pq, (cc[x], x))

ans = 0
while n > 0:
    s, x = heapq.heappop(pq)
    if removed[x]:
        continue
    removed[x] = True
    
    ans = max(ans, s)

    for y in g[x]:
        cc[y] -= aa[x]
        heapq.heappush(pq, (cc[y], y))

    n -= 1

print(ans)