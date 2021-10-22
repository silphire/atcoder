import heapq
from collections import defaultdict

n, m = map(int, input().split())
c = [0] * (n + 1)
g = defaultdict(set)
for _ in range(m):
    a, b = map(int, input().split())
    if b not in g[a]:
        g[a].add(b)
        c[b] += 1

q = []
for i in range(1, n + 1):
    if c[i] == 0:
        heapq.heappush(q, i)

s = []
while q:
    x = heapq.heappop(q)
    s.append(x)
    for y in g[x]:
        if c[y] == 0:
            continue
        c[y] -= 1
        if c[y] == 0:
            heapq.heappush(q, y)

if sum(c) == 0:
    print(' '.join(map(str, s)))
else:
    print('-1')
