n, W = map(int, input().split())
dp = [0] * (W + 1)
for _ in range(n):
    w, v = map(int, input().split())
    for x in range(W - w, -1, -1):
        if dp[x] > 0:
            dp[x + w] = max(dp[x + w], dp[x] + v)
    if dp[w] == 0:
        dp[w] = v
print(max(dp))