import math
import sys
sys.setrecursionlimit(10 ** 6)

h, w = map(int, input().split())
s = [
    input().rstrip()
    for _ in range(h)
]
c = [[0] * w for _ in range(h)]
nc = 1

def dfs(x, y, z):
    global s, c, nc
    if not (0 <= x < w and 0 <= y < h):
        return
    if s[y][x] == z:
        return
    if c[y][x] != 0:
        return
    c[y][x] = nc
    
    dfs(x - 1, y, s[y][x])
    dfs(x + 1, y, s[y][x])
    dfs(x, y - 1, s[y][x])
    dfs(x, y + 1, s[y][x])

for y in range(h):
    for x in range(w):
        if c[y][x] == 0:
            dfs(x, y, None)
            nc += 1
bn = [0] * nc
wn = [0] * nc
for y in range(h):
    for x in range(w):
        if s[y][x] == '#':
            bn[c[y][x]] += 1
        else:
            wn[c[y][x]] += 1

def comb(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n - r)

ans = 0
for i in range(nc):
    ans += bn[i] * wn[i]
print(ans)