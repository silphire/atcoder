inf = float('inf')
n = int(input())
cc = [0] * n
zz = [0] * n
for i in range(n):
    x, y, zz[i] = map(int, input().split())
    cc[i] = max(0, (x + y) // 2 + 1 - x)
nw = sum(zz) // 2 + 1

dp = [[inf] * (nw + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    for j in range(nw + 1):
        dp[i + 1][min(nw, j + zz[i])] = min(
            dp[i + 1][min(nw, j + zz[i])],
            dp[i][j] + cc[i],
        )
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
print(dp[n][nw])