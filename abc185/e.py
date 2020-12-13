n, m = map(int, input().split())
aa = tuple(map(int, input().split()))
bb = tuple(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(n + 1):
    dp[0][i] = i
for i in range(m + 1):
    dp[i][0] = i

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[j][i] = min(
            dp[j - 1][i] + 1,
            dp[j][i - 1] + 1,
            dp[j - 1][i - 1] + int(aa[i - 1] != bb[j - 1]),
        )
print(dp[m][n])