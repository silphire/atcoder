import math
n = int(input())
xx = [0] * n
yy = [0] * n
pp = [0] * n
for i in range(n):
    xx[i], yy[i], pp[i] = map(int, input().split())

inf = float('inf')
g = [[inf] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        g[i][j] = (abs(xx[i] - xx[j]) + abs(yy[i] - yy[j])) / pp[i]
for k in range(n):
    for i in range(n):
        for j in range(n):
            g[i][j] = min(g[i][j], max(g[i][k], g[k][j]))
x = float('inf')
for k in range(n):
    x = min(x, max(g[k]))
print(math.ceil(x))