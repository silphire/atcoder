n, m = map(int, input().split())
a = set()
for i in range(m):
    a.add(int(input()))

MOD = 1000000007
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1 if 1 not in a else 0
for i in range(2, n + 1):
    if i in a:
        dp[i] = 0
        continue
    dp[i] = dp[i - 1] + dp[i - 2]
    dp[i] = dp[i] % MOD
print(dp[n])
