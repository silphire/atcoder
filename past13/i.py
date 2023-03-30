from collections import defaultdict
from collections import deque

n, m = map(int, input().split())
g = defaultdict(list)
order = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    order[b] += 1

q = deque()
for i in range(n):
    if order[i] == 0:
        q.append(i)
r = []
while q:
    x = q.pop()
    r.append(x)
    for e in g[x]:
        order[e] -= 1
        if order[e] == 0:
            q.append(e)
if len(r) == n:
    print('Yes')
else:
    print('No')