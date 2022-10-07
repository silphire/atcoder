from collections import deque
from collections import defaultdict

n = int(input())
g = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

f = [False] * n
q = deque([(0, None)])
while q:
    x, p = q.popleft()
    if f[x]:
        print('No')
        exit()
    f[x] = True
    for e in g[x]:
        if e != p:
            q.append((e, x))
if all(f):
    print('Yes')
else:
    print('No')