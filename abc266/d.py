n = int(input())
d = {}

for i in range(n):
    t, x, a = map(int, input().split())
    d[(t, x)] = a
maxt = 10 ** 5
dp = [[0] * (5) for _ in range(maxt + 1)]

for t in range(1, maxt + 1):
    for x in range(5):
        if x > t:
            continue
        dp[t][x] = dp[t - 1][x]
        if x > 0:
            dp[t][x] = max(dp[t][x], dp[t - 1][x - 1])
        if x < 4:
            dp[t][x] = max(dp[t][x], dp[t - 1][x + 1])
        dp[t][x] += d.get((t, x), 0)
print(max(dp[maxt]))