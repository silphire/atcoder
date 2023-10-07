from collections import defaultdict
import heapq

d = defaultdict(int)

n = int(input())
q = []
for i in range(n):
    s, c = map(int, input().split())
    d[s] = c
    heapq.heappush(q, s)

ans = 0
while q:
    s = heapq.heappop(q)
    c = d[s]
    d[s] = 0

    if c & 1 == 1:
        ans += 1
    
    s <<= 1
    c >>= 1
    if c > 0:
        if s not in d:
            heapq.heappush(q, s)
        d[s] += c

print(ans)