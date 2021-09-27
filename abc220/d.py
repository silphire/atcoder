n = int(input())
aa = list(map(int, input().split()))
MOD = 998244353

dp = [[0] * 10 for _ in range(n)]
dp[0][aa[0]] = 1
for i in range(1, n):
    for k in range(10):
        nk = (k + aa[i]) % 10
        dp[i][nk] += dp[i - 1][k]
        dp[i][nk] %= MOD

        nk = (k * aa[i]) % 10
        dp[i][nk] += dp[i - 1][k]
        dp[i][nk] %= MOD

for k in range(10):
    print(dp[-1][k])