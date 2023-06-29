from collections import defaultdict
from collections import deque
import sys
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

v = [False] * (n + 1)
r = deque()
def dfs(x):
    v[x] = True
    r.append(x)
    if x == n:
        return True
    for y in g[x]:
        if not v[y]:
            if dfs(y):
                return True
    v[x] = False
    r.pop()
    return False

dfs(1)
print(*r)