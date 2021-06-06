n = int(input())
tt = list(sorted(map(int, input().split()), reverse=True))
target = sum(tt) // 2

dp = [[False] * (10 ** 5) for _ in range(101)]
dp[1][0] = dp[1][tt[0]] = True
for i in range(2, n + 1):
    for j in range(10 ** 5):
        dp[i][j] = dp[i][j] or dp[i - 1][j]
        if j >= tt[i - 1]:
            dp[i][j] = dp[i][j] or dp[i - 1][j - tt[i - 1]]

while target >= 0 and not dp[n][target]:
    target -= 1
print(max(target, sum(tt) - target))