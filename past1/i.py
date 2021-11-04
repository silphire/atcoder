n, m = map(int, input().split())
ss = [0] * m
cc = [0] * m
for i in range(m):
    s, cc[i] = input().split()
    cc[i] = int(cc[i])
    for x in range(n):
        ss[i] |= int(s[x] == 'Y') << x

dp = [float('inf')] * (1 << n)
dp[0] = 0
for i in range(1 << n):
    for j in range(m):
        dp[i | ss[j]] = min(dp[i | ss[j]], dp[i] + cc[j])
if dp[-1] == float('inf'):
    print(-1)
else:
    print(dp[-1])