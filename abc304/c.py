from collections import defaultdict
from collections import deque

n, d = map(int, input().split())
d = d * d
xx = [0] * n
yy = [0] * n
for i in range(n):
    xx[i], yy[i] = map(int, input().split())
g = defaultdict(list)
for i in range(n):
    for j in range(i + 1, n):
        if (xx[i] - xx[j]) ** 2 + (yy[i] - yy[j]) ** 2 <= d:
            g[i].append(j)
            g[j].append(i)

vv = [False] * n
q = deque([0])
while q:
    p = q.popleft()
    if vv[p]:
        continue
    vv[p] = True
    for np in g[p]:
        q.append(np)

for i in range(n):
    if vv[i]:
        print('Yes')
    else:
        print('No')
