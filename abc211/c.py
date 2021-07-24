from collections import defaultdict
MOD = 10 ** 9 + 7
s = input().rstrip()
n = len(s)
nc = len('chokudai')
cnt = defaultdict(int)

dp = [[0] * nc for _ in range(n)]
for i in range(n):
    cnt[s[i]] += 1
    for j in range(nc):
        if s[i] == 'chokudai'[j]:
            if j == 0:
                dp[i][j] = cnt[s[i]]
            elif i > 0:
                dp[i][j] += dp[i - 1][j] + dp[i - 1][j - 1]
        elif i > 0:
            dp[i][j] = dp[i - 1][j]
        dp[i][j] %= MOD
print(dp[-1][-1])