import sys
sys.setrecursionlimit(10 ** 9)

h, w, a, b = map(int, input().split())

tile = [[0] * w for _ in range(h)]

def dfs(x, y, r, a, b):
    if r < 0 or a < 0 or b < 0:
        return 0
    if r == 0:
        return 1

    if tile[y][x] == 1:
        nx = x + 1
        ny = y
        if nx >= w:
            nx = 0
            ny += 1
        return dfs(nx, ny, r, a, b)

    n = 0
    tile[y][x] = 1
    n += dfs(x, y, r - 1, a, b - 1)
    tile[y][x] = 0
    if y + 1 < h and tile[y][x] == 0 and tile[y + 1][x] == 0:
        tile[y][x] = tile[y + 1][x] = 1
        n += dfs(x, y, r - 2, a - 1, b)
        tile[y][x] = tile[y + 1][x] = 0
    if x + 1 < w and tile[y][x] == 0 and tile[y][x + 1] == 0:
        tile[y][x] = tile[y][x + 1] = 1
        n += dfs(x, y, r - 2, a - 1, b)
        tile[y][x] = tile[y][x + 1] = 0
    return n

print(dfs(0, 0, h * w, a, b))