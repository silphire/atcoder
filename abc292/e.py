from collections import defaultdict
from collections import deque

n, m = map(int, input().split())

g = defaultdict(set)
for _ in range(m):
    u, v = map(int, input().split())
    g[u - 1].add(v - 1)

reach = [None] * n
for x in range(n):
    q = deque([x])
    r = set()
    while q:
        a = q.popleft()
        for b in g[a]:
            if b not in r:
                r.add(b)
                q.append(b)
    reach[x] = r

ans = 0
for x in range(n):
    for y in reach[x]:
        if x == y:
            continue
        if y not in g[x]:
            ans += 1
            g[x].add(y)
print(ans)