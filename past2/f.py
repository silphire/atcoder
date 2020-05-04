from collections import defaultdict
import heapq

n = int(input())

t = defaultdict(list)
for _ in range(n):
    a, b = map(int, input().split())
    t[a].append(-b)

p = 0
d = 1
q = []
for d in range(1, n + 1):
    if d in t:
        for w in t[d]:
            heapq.heappush(q, w)
    if len(q) > 0:
        p += -heapq.heappop(q)
    print(p)
