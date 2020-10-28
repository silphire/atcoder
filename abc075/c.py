import sys

sys.setrecursionlimit(100000)

n, m = map(int, input().split())
v = [[False] * n for _ in range(n)]
e = [None] * m
for i in range(m):
    e[i] = list(map(int, input().split()))
    e[i][0] -= 1
    e[i][1] -= 1
    v[e[i][0]][e[i][1]] = True
    v[e[i][1]][e[i][0]] = True

ans = 0
for i in range(m):
    v[e[i][0]][e[i][1]] = False
    v[e[i][1]][e[i][0]] = False
    f = [False] * n

    def dfs(x):
        global f
        if f[x]:
            return
        f[x] = True
        for i in range(n):
            if v[x][i]:
                dfs(i)
    
    dfs(0)

    v[e[i][0]][e[i][1]] = True
    v[e[i][1]][e[i][0]] = True

    if not all(f):
        ans += 1
print(ans)