x, y, z = map(int, input().split())
s = input()
n = len(s)

dp = [[0] * (n + 1) for _ in range(2)]
dp[1][0] = z
for i, c in enumerate(s):
    if c == 'a':
        dp[0][i + 1] = min(dp[0][i] + x, dp[1][i] + z + x, dp[1][i] + z + y) # OFF a
        dp[1][i + 1] = min(dp[1][i] + y, dp[0][i] + z + x, dp[0][i] + z + y) # ON  a
    else:
        dp[0][i + 1] = min(dp[0][i] + y, dp[1][i] + z + x, dp[1][i] + z + y) # OFF A
        dp[1][i + 1] = min(dp[1][i] + x, dp[0][i] + z + x, dp[0][i] + z + y) # ON  A
print(min(dp[0][n], dp[1][n]))