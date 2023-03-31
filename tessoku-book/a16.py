n = int(input())
aa = [0] + list(map(int, input().split()))
bb = [0, 0] + list(map(int, input().split()))

dp = [0] * n
for i in range(1, n):
    dp[i] = dp[i - 1] + aa[i]
    if i >= 2:
        dp[i] = min(dp[i], dp[i - 2] + bb[i])
print(dp[-1])