n = int(input())
xx = [None] * n
yy = [None] * n
for i in range(n):
    xx[i], yy[i] = map(int, input().split())
dp = [[0] * (n + 1) for _ in range(2)]

for i in range(n):
    if xx[i] == 0:
        dp[0][i + 1] = max(dp[0][i], dp[0][i] + yy[i], dp[1][i] + yy[i])
        dp[1][i + 1] = dp[1][i]
    else:
        dp[0][i + 1] = dp[0][i]
        dp[1][i + 1] = max(dp[1][i], dp[0][i] + yy[i])
print(max(dp[0][n], dp[1][n]))