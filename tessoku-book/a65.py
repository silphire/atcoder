from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)

n = int(input())
aa = list(map(int, input().split()))

g = defaultdict(list)
for i, a in enumerate(aa):
    g[a - 1].append(i + 1)

ans = [0] * n
def dfs(x):
    ans[x] = len(g[x]) + sum([dfs(y) for y in g[x]])
    return ans[x]
dfs(0)
print(*ans)