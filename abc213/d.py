from collections import defaultdict
from collections import deque
import sys
sys.setrecursionlimit(10 ** 5)

n = int(input())
r = defaultdict(set)
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    r[a].add(b)
    r[b].add(a)

rr = defaultdict(list)
for k, v in r.items():
    rr[k] = deque(sorted(v))
r = rr

ans = []
v = [False] * n
v[0] = True
p = 0
ans.append(1)
pr = {}
while True:
    f = True
    while r[p]:
        x = r[p].popleft()
        if not v[x]:
            v[x] = True
            ans.append(x + 1)
            pr[x] = p
            p = x
            f = False
            break
    if f:
        if p == 0:
            break
        ans.append(pr[p] + 1)
        p = pr[p]
print(' '.join(map(str, ans)))