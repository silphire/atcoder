n, k = map(int, input().split())
aa = [
    list(map(int, input().split())),
    list(map(int, input().split())),
]
dp = [[True] * n for _ in range(2)]

for i in range(1, n):
    for j in range(2):
        dp[j][i] = (dp[0][i - 1] and abs(aa[0][i - 1] - aa[j][i]) <= k) or (dp[1][i - 1] and abs(aa[1][i - 1] - aa[j][i]) <= k)

if dp[0][n - 1] or dp[1][n - 1]:
    print('Yes')
else:
    print('No')