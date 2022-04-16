n, m, k = map(int, input().split())
M = 998244353
dp = [[0] * (50 * 50 + 1) for _ in range(51)]
for i in range(1, m + 1):
    dp[0][i] = 1
for y in range(1, n):
    for x in range(1, m + 1):
        for i in range(2501):
            if i - x <= 0:
                continue
            dp[y][i] += dp[y - 1][i - x]
            dp[y][i] %= M

print(sum([dp[n - 1][i] for i in range(1, k + 1)]) % M)
