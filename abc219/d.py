import math

n = int(input())
x, y = map(int, input().split())
ab = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [[[float('inf')] * (y + 1) for _ in range(x + 1)] for _ in range(n + 1)]
dp[0][0][0] = 0
for nn in range(1, n + 1):
    for xx in range(x + 1):
        for yy in range(y + 1):
            nx, ny = ab[nn - 1]
            dp[nn][min(x, xx + nx)][min(y, yy + ny)] = min(
                dp[nn][min(x, xx + nx)][min(y, yy + ny)],
                dp[nn - 1][xx][yy] + 1,
            )
            dp[nn][xx][yy] = min(dp[nn][xx][yy], dp[nn - 1][xx][yy])

ans = min([dp[i][x][y] for i in range(1, n + 1)])
if math.isinf(ans):
    print(-1)
else:
    print(ans)