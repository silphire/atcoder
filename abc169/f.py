from collections import defaultdict

n, s = map(int, input().split())
aa = tuple(sorted(map(int, input().split())))

MOD = 998244353
dp = [[0 for i in range(s + 1)] for j in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for j in range(s + 1):
        # 選ばない場合
        dp[i + 1][j] += 2 * dp[i][j]
        dp[i + 1][j] %= MOD

        # j + a[i]を選んだ場合
        if j + aa[i] <= s:
            dp[i + 1][j + aa[i]] += dp[i][j]
            dp[i + 1][j + aa[i]] %= MOD
print(dp[n][s])