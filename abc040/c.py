n = int(input())
aa = list(map(int, input().split()))

dp = [0] * n
dp[1] = abs(aa[1] - aa[0])
for i in range(2, n):
    dp[i] = min(
        dp[i - 1] + abs(aa[i] - aa[i - 1]),
        dp[i - 2] + abs(aa[i] - aa[i - 2])
    )
print(dp[-1])