n, m = map(int, input().split())
aa = list(map(int, input().split()))

minf = float('-inf')
dp = [[0] * 2001 for _ in range(2001)]
dp[0][1] = minf
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i < j:
            dp[i][j] = minf
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + j * aa[i - 1])
print(dp[n][m])