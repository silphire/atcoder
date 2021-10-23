from collections import deque
from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)

m = int(input())
g = defaultdict(set)
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].add(v)
    g[v].add(u)
pp = tuple(map(int, input().split()))
pos = [-1] * 9
for i, p in enumerate(pp):
    pos[p - 1] = i
v = 0
for i in range(9):
    if pos[i] == -1:
        v = i
        break
pos = tuple(pos)
if v == 8 and pos == (0, 1, 2, 3, 4, 5, 6, 7, -1):
    print(0)
    exit()

ex = set()
q = deque([(0, v, pos)])
while q:
    x, v, pp = q.popleft()
    for nv in g[v]:
        npp = list(pp)
        npp[v] = npp[nv]
        npp[nv] = -1
        npp = tuple(npp)
        if nv == 8 and npp == (0, 1, 2, 3, 4, 5, 6, 7, -1):
            print(x + 1)
            exit()
        if npp in ex:
            continue
        ex.add(npp)
        q.append((x + 1, nv, npp))
print(-1)