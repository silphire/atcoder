h, w = map(int, input().split())
xx = [
    list(map(int, input().split()))
    for _ in range(h)
]

yy = [[0] * w for _ in range(h)]
for y in range(h):
    for x in range(w):
        yy[y][x] = xx[y][x]
        if y > 0:
            yy[y][x] += yy[y - 1][x]
        if x > 0:
            yy[y][x] += yy[y][x - 1]
        if x > 0 and y > 0:
            yy[y][x] -= yy[y - 1][x - 1]

q = int(input())
for _ in range(q):
    a, b, c, d = map(lambda x: int(x) - 1, input().split())
    ans = yy[c][d]
    if a > 0:
        ans -= yy[a - 1][d]
    if b > 0:
        ans -= yy[c][b - 1]
    if a > 0 and b > 0:
        ans += yy[a - 1][b - 1]
    print(ans)