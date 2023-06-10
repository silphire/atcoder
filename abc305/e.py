from collections import defaultdict
from collections import deque

n, m, k = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

defend = set()
mind = [-1] * (n + 1)
ph = [None] * k
for i in range(k):
    ph[i] = tuple(map(int, input().split()))
ph = sorted(ph, key=lambda x: -x[1])

for (p, h) in ph:
    q = deque([(p, h)])
    while q:
        x, d = q.popleft()
        if d <= mind[x]:
            continue
        mind[x] = d
        defend.add(x)
        for y in g[x]:
            q.append((y, d - 1))

print(len(defend))
print(*sorted(defend))