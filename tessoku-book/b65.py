from collections import defaultdict
from collections import deque
import sys
sys.setrecursionlimit(10 ** 7)

n, t = map(int, input().split())
t -= 1
g = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

h = defaultdict(list)
ff = [True] * n
ff[t] = False
q = deque([t])
while q:
    m = q.popleft()
    for a in g[m]:
        if ff[a]:
            ff[a] = False
            h[m].append(a)
            q.append(a)

ss = [0] * n
def dfs(x):
    global ss, h
    for a in h[x]:
        ss[x] = max(ss[x], dfs(a) + 1)
    return ss[x]
dfs(t)
print(*ss)