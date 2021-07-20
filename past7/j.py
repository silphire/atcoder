from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
d = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    d[u - 1].append(v - 1)

visited = [0] * n
ans = False
r = []
s = list(d)
for v in s:
    def dfs(x):
        global visited
        global ans

        if visited[x] == 1:
            ans = True
        elif visited[x] == 0:
            visited[x] = 1
            for y in d[x]:
                dfs(y)
            visited[x] = 2
            r.append(x)
    dfs(v)
    if ans:
        print('Yes')
        exit()
print('No')