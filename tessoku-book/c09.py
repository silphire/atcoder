n = int(input())
aa = list(map(int, input().split()))
dp = [0] * (n + 1)
dp[0] = aa[0]
dp[1] = aa[1]
for i in range(2, n):
    dp[i] = max(aa[i] + dp[i - 2], dp[i - 1])
print(max(dp[n - 1], dp[n - 2]))