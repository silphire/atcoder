n = int(input())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))

MOD = 998244353
N = 3001

dp = [[0] * N for _ in range(N)]
for i, (a, b) in enumerate(zip(aa, bb)):
    for x in range(a, b + 1):
        if i == 0:
            dp[i][x] = 1
        else:
            dp[i][x] += dp[i - 1][x]
            dp[i][x] %= MOD
    for x in range(1, N):
        dp[i][x] += dp[i][x - 1]
        dp[i][x] %= MOD

print(dp[n - 1][-1])