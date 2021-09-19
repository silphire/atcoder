s = input().rstrip()
n = len(s)
MOD = 10 ** 9 + 7

dp = [[0] * 13 for _ in range(n + 1)]
dp[0][0] = 1

for i in range(n):
    for m in range(13):
        if s[i] == '?':
            for j in range(10):
                dp[i + 1][(m * 10 + j) % 13] += dp[i][m]
                dp[i + 1][(m * 10 + j) % 13] %= MOD
        else:
            dp[i + 1][(m * 10 + int(s[i])) % 13] += dp[i][m]
            dp[i + 1][(m * 10 + int(s[i])) % 13] %= MOD
            
print(dp[n][5])