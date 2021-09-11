from collections import defaultdict

n = int(input())
xx = set()
yy = set()
xy = [None] * n
for i in range(n):
    x, y = map(int, input().split())
    xx.add(x)
    yy.add(y)
    xy[i] = (x, y)

dx = {}
for i, x in enumerate(sorted(xx)):
    dx[x] = i
dy = {}
for i, y in enumerate(sorted(yy)):
    dy[y] = i
for i in range(n):
    xy[i] = (dx[xy[i][0]], dy[xy[i][1]])

ff = [[False] * n for _ in range(n)]
for x, y in xy:
    ff[y][x] = True

ans = 0
for ax, ay in xy:
    for bx, by in xy:
        if ax < bx and ay < by and ff[ay][bx] and ff[by][ax]:
            ans += 1
print(ans)
