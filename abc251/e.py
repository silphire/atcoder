n = int(input())
aa = list(map(int, input().split()))

ans = float('inf')
for i in range(2):
    dp = [[0] * n for _ in range(2)]
    if i == 0:
        dp[0][0] = 0
        dp[1][0] = float('inf')
    else:
        dp[0][0] = float('inf')
        dp[1][0] = aa[0]

    for j in range(1, n):
        dp[0][j] = dp[1][j - 1]
        dp[1][j] = min(dp[0][j - 1], dp[1][j - 1]) + aa[j]
    if i == 0:
        ans = min(ans, dp[1][-1])
    else:
        ans = min(ans, dp[0][-1], dp[1][-1])
print(ans)