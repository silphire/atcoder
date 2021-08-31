s = input().rstrip()
n = len(s)
dp = [[0] * n for _ in range(33)]

for i in range(n):
    if s[i] == 'L':
        dp[0][i] = i - 1
    else:
        dp[0][i] = i + 1

for p in range(32):
    for i in range(n):
        dp[p + 1][i] += dp[p][dp[p][i]]

ans = [0] * n
for i in range(n):
    ans[dp[32][i]] += 1
print(' '.join(map(str, ans)))