MOD = 998244353
n = int(input())
dp = [[0] * 10 for _ in range(n + 1)]
for i in range(10):
    dp[0][i] = 1
for i in range(1, n):
    for j in range(1, 10):
        if j - 1 >= 1:
            dp[i][j] += dp[i - 1][j - 1]
        dp[i][j] += dp[i - 1][j]
        if j + 1 < 10:
            dp[i][j] += dp[i - 1][j + 1]
        dp[i][j] %= MOD
print(sum(dp[n - 1]) % MOD)