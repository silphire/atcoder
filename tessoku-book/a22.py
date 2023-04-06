n = int(input())
aa = list(map(lambda x: int(x) - 1, input().split()))
bb = list(map(lambda x: int(x) - 1, input().split()))

dp = [0] * n
for i in range(n - 1):
    if i > 0 and dp[i] == 0:
        continue
    dp[aa[i]] = max(dp[aa[i]], dp[i] + 100)
    dp[bb[i]] = max(dp[bb[i]], dp[i] + 150)
print(dp[-1])