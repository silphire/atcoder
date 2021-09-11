n = int(input())
ss = [
    list(input().rstrip())
    for _ in range(n)
]
tt = [
    list(input().rstrip())
    for _ in range(n)
]

sx = 0
sy = 0
sex = 0
sey = 0
for y in range(n):
    sy = y
    f = False
    for x in range(n):
        if ss[y][x] == '#':
            f = True
            break
    if f:
        break
for x in range(n):
    sx = x
    f = False
    for y in range(n):
        if ss[y][x] == '#':
            f = True
            break
    if f:
        break
for y in range(n - 1, -1, -1):
    sey = y
    f = False
    for x in range(n):
        if ss[y][x] == '#':
            f = True
            break
    if f:
        break
for x in range(n - 1, -1, -1):
    sex = x
    f = False
    for y in range(n):
        if ss[y][x] == '#':
            f = True
            break
    if f:
        break

for _ in range(4):
    t2 = [[None] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            t2[n - 1 - x][y] = tt[y][x]

    tx = 0
    ty = 0
    tex = 0
    tey = 0
    for y in range(n):
        ty = y
        f = False
        for x in range(n):
            if tt[y][x] == '#':
                f = True
                break
        if f:
            break
    for x in range(n):
        tx = x
        f = False
        for y in range(n):
            if tt[y][x] == '#':
                f = True
                break
        if f:
            break
    for y in range(n - 1, -1, -1):
        tey = y
        f = False
        for x in range(n):
            if tt[y][x] == '#':
                f = True
                break
        if f:
            break
    for x in range(n - 1, -1, -1):
        tex = x
        f = False
        for y in range(n):
            if tt[y][x] == '#':
                f = True
                break
        if f:
            break

    if tex - tx != sex - sx or tey - ty != sey - sy:
        tt = t2
        continue

    f = False
    nx = n - max(sx, tx)
    ny = n - max(sy, ty)
    for y in range(ny):
        for x in range(nx):
            if ss[sy + y][sx + x] != tt[ty + y][tx + x]:
                f = True
                break
        if f:
            break
    if not f:
        print('Yes')
        exit(0)

    tt = t2

print('No')