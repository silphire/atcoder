import math
from collections import defaultdict
from collections import deque

def dist2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

n = int(input())
sx, sy ,tx, ty = map(int, input().split())
xx = [0] * n
yy = [0] * n
rr = [0] * n
r2 = [0] * n
for i in range(n):
    xx[i], yy[i], rr[i] = map(int, input().split())

g = defaultdict(list)
for i in range(n):
    for j in range(i + 1, n):
        d = dist2((xx[i], yy[i]), (xx[j], yy[j]))
        if d > (rr[i] + rr[j]) ** 2:
            continue
        if d < abs(rr[i] - rr[j]) ** 2:
            continue
        g[i].append(j)
        g[j].append(i)

sp = None
tp = None
for i in range(n):
    if dist2((sx, sy), (xx[i], yy[i])) == rr[i] ** 2:
        sp = i
    if dist2((tx, ty), (xx[i], yy[i])) == rr[i] ** 2:
        tp = i

visited = [False] * n
q = deque([sp])
while q:
    p = q.popleft()
    if visited[p]:
        continue
    visited[p] = True
    if p == tp:
        print('Yes')
        exit()
    for x in g[p]:
        q.append(x)
print('No')