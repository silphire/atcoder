from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)

n, q = map(int, input().split())
xx = list(map(int, input().split()))

g = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

ans = [None] * (n + 1)
def dfs(x, p):
    ans[x] = [xx[x - 1]]
    for y in g[x]:
        if y == p:
            continue
        ans[x].extend(dfs(y, x))
    ans[x] = sorted(ans[x], reverse=True)[:20]
    return ans[x]
dfs(1, 0)

for _ in range(q):
    v, k = map(int, input().split())
    print(ans[v][k - 1])