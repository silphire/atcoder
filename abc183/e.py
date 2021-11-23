h, w = map(int, input().split())
ss = [
    input().rstrip()
    for _ in range(h)
]

MOD = 10 ** 9 + 7

dp = [[0] * 2001 for _ in range(2001)]
xx = [[0] * 2001 for _ in range(2001)]
yy = [[0] * 2001 for _ in range(2001)]
zz = [[0] * 2001 for _ in range(2001)]

dp[0][0] = 1
for y in range(h):
    for x in range(w):
        if x == 0 and y == 0:
            continue
        if x > 0 and ss[y][x - 1] == '.':
            xx[y][x] = xx[y][x - 1] + dp[y][x - 1]
            xx[y][x] %= MOD
        if y > 0 and ss[y - 1][x] == '.':
            yy[y][x] = yy[y - 1][x] + dp[y - 1][x]
            yy[y][x] %= MOD
        if x > 0 and y > 0 and ss[y - 1][x - 1] == '.':
            zz[y][x] = zz[y - 1][x - 1] + dp[y - 1][x - 1]
            zz[y][x] %= MOD
        dp[y][x] = xx[y][x] + yy[y][x] + zz[y][x]
        dp[y][x] %= MOD
print(dp[h - 1][w - 1])