from collections import defaultdict
from collections import deque

MOD = 10 ** 9 + 7
n = int(input())
a, b = map(int, input().split())
m = int(input())
r = defaultdict(set)
for _ in range(m):
    x, y = map(int, input().split())
    r[x].add(y)
    r[y].add(x)
v = [False] * (n + 1)
c = [0] * (n + 1)

c[a] = 1
q = deque([a])
while q:
    nq = set()
    for x in q:
        if v[x]:
            continue
        for p in r[x]:
            if p not in q:
                c[p] += c[x]
                c[p] %= MOD
                if not v[p]:
                    nq.add(p)
        v[x] = True
    if c[b] > 0:
        print(c[b])
        exit()
    q = deque(nq)
print(c[b])