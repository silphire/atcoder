from collections import defaultdict

n, m = map(int, input().split())
xx = [0] + list(map(int, input().split())) + [0]
b = defaultdict(int)
for _ in range(m):
    c, y = map(int, input().split())
    b[c] = y

dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(min(i + 1, n)):
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + xx[i + 1] + b[j + 1])
        dp[i + 1][0] = max(dp[i + 1][0], dp[i][j])
print(max(dp[n]))
