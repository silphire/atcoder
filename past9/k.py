from collections import defaultdict
from collections import deque

n, m, q, k = map(int, input().split())
aa = list(map(int, input().split()))
sa = set(aa)

g = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

inf = float('inf')
d = [[inf] * (n + 1) for _ in range(k)]
for i, a in enumerate(aa):
    d[i][a] = 0
    que = deque([(a, 0)])
    while que:
        x, c = que.popleft()
        for b in g[x]:
            if d[i][b] == inf:
                d[i][b] = c + 1
                que.append((b, c + 1))

for _ in range(q):
    s, t = map(int, input().split())
    ans = float('inf')
    for i in range(k):
        ans = min(ans, d[i][s] + d[i][t])
    print(ans)