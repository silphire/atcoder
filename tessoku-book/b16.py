n = int(input())
hh = list(map(int, input().split()))

dp = [float('inf')] * n
dp[0] = 0
for i in range(n):
    if i + 1 < n:
        dp[i + 1] = min(dp[i + 1], abs(hh[i + 1] - hh[i]) + dp[i])
    if i + 2 < n:
        dp[i + 2] = min(dp[i + 2], abs(hh[i + 2] - hh[i]) + dp[i])
print(dp[n - 1])