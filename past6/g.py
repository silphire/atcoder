import heapq
from collections import defaultdict

n, m, q = map(int, input().split())

w = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    w[a].append((c, b))
    w[b].append((c, a))
x = list(map(int, input().split()))

p = [False] * n
p[0] = True
ans = 1

s = [pt for pt in w[0]]
heapq.heapify(s)

for i in range(q):
    nx = []
    while s:
        c, t = heapq.heappop(s)
        if c > x[i]:
            heapq.heappush(s, (c, t))
            break
        if p[t]:
            continue
        p[t] = True
        ans += 1
        for cc, tt in w[t]:
            if not p[tt]:
                nx.append((cc, tt))
    for a in nx:
        heapq.heappush(s, a)
    print(ans)
