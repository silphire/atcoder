h, w = map(int, input().split())
n = h * w
a = [
    list(map(int, input().split()))
    for _ in range(h)
]

dp = [[[0] * (h + w) for _ in range(w + 1)] for _ in range(h + 1)]

ans = 0
for k in range(1, h + w):
    for y in range(1, h + 1):
        for x in range(1, w + 1):
            dp[y][x][k] = max(
                dp[y][x - 1][k],
                dp[y - 1][x][k],
                dp[y][x - 1][k - 1] + a[y - 1][x - 1],
                dp[y - 1][x][k - 1] + a[y - 1][x - 1],
            )
    print(dp[h][w][k])
