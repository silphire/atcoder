n, x = map(int, input().split())
aa = [0] * (n + 1)
bb = [0] * (n + 1)
cc = [0] * (n + 1)
for i in range(1, n + 1):
    aa[i], bb[i], cc[i] = map(int, input().split())

dp = [[(0, 0, 0)] * (x + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(x + 1):
        dp[i][j] = dp[i - 1][j]
        if j - bb[i] >= 0:
            g, s, b = dp[i - 1][j - bb[i]]
            g += cc[i]
            s -= aa[i]
            b -= bb[i]
            dp[i][j] = max(dp[i][j], (g, s, b))
g, s, b = dp[n][x]
print(g, s + 10 ** 9, b + x)