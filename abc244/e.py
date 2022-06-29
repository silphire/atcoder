MOD = 998244353
n, m, k, s, t, x = map(int, input().split())
s -= 1
t -= 1
x -= 1

edges = [
    tuple(map(lambda x: int(x) - 1, input().split()))
    for _ in range(m)
]

dp = [[[0] * 2 for _ in range(n)] for _ in range(k + 1)]
dp[0][s][0] = 1
for i in range(k):
    for u, v in edges:
        for j in range(2):
            dp[i + 1][v][j ^ int(v == x)] += dp[i][u][j]
            dp[i + 1][v][j ^ int(v == x)] %= MOD
            dp[i + 1][u][j ^ int(u == x)] += dp[i][v][j]
            dp[i + 1][u][j ^ int(u == x)] %= MOD
print(dp[k][t][0])