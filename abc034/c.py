MOD = 1000000007

w, h = map(int, input().split())
dp = [1] * w
for i in range(1, h):
    ndp = [0] * w
    ndp[0] = dp[0]
    for j in range(1, w):
        ndp[j] = (dp[j] + ndp[j - 1]) % MOD
    dp = ndp
    print(dp)
print(dp[-1])

