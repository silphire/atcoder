h, w, n = map(int, input().split())
aa = [[0] * w for _ in range(h)]

x = y = 0
d = 0
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

for _ in range(n):
    if aa[y][x] == 0:
        aa[y][x] = 1
        d += 1
    else:
        aa[y][x] = 0
        d -= 1

    while d < 0:
        d += 4
    d %= 4

    x += dx[d]
    while x < 0:
        x += w
    x %= w

    y += dy[d]
    while y < 0:
        y += h
    y %= h

ss = ''
for y in range(h):
    s = ''
    for x in range(w):
        s += '.#'[aa[y][x]]
    ss += s + '\n'
print(ss)