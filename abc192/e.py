import sys
import heapq
from collections import defaultdict

sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7
input = sys.stdin.readline

n, m, x, y = map(int, input().split())

r = defaultdict(list)
for i in range(m):
    a, b, t, k = map(int, input().split())
    r[a].append((b, t, k))
    r[b].append((a, t, k))

visited = [False] * (n + 1)
q = [(0, x)]
while q:
    p = heapq.heappop(q)
    if visited[p[1]]:
        continue
    if p[1] == y:
        print(p[0])
        exit()
    visited[p[1]] = True
    for a in r[p[1]]:
        town, t, k = a
        if p[0] % k == 0:
            nt = p[0] + t
        else:
            nt = p[0] + k - p[0] % k + t
        heapq.heappush(q, (nt, a[0]))
print(-1)