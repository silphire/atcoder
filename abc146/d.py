from collections import defaultdict
from collections import deque

n = int(input())
edge = [-1] * (n - 1)
maxc = 0
g = defaultdict(list)
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a].append((b, i))
    g[b].append((a, i))

q = deque([1])
while q:
    vc = q.popleft()
    paint = []
    exist = set()
    for v, e in g[vc]:
        if edge[e] == -1:
            paint.append((v, e))
        else:
            exist.add(edge[e])
    c = 1
    for v, e in paint:
        while c in exist:
            c += 1
        edge[e] = c
        exist.add(c)
        q.append(v)
    maxc = max(maxc, c)
print(maxc)
for c in edge:
    print(c)