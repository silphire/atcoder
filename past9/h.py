s = input().rstrip()
t = input().rstrip()
ns = len(s)
nt = len(t)
dp = [[0] * 5001 for _ in range(5001)]
for i in range(ns):
    for j in range(nt):
        if s[i] == t[j]:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        else:
            dp[i + 1][j + 1] = dp[i][j] + 1
print(dp[ns][nt])
