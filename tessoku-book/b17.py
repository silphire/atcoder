n = int(input())
hh = list(map(int, input().split()))

dp = [float('inf')] * n
prev = [None] * n
dp[0] = 0
for i in range(n):
    if i + 1 < n:
        nc = abs(hh[i + 1] - hh[i]) + dp[i]
        if dp[i + 1] > nc:
            dp[i + 1] = nc
            prev[i + 1] = i
    if i + 2 < n:
        nc = abs(hh[i + 2] - hh[i]) + dp[i]
        if dp[i + 2] > nc:
            dp[i + 2] = nc
            prev[i + 2] = i
ans = []
p = n - 1
while p is not None:
    ans.append(p + 1)
    p = prev[p]

ans = list(reversed(ans))
print(len(ans))
print(*ans)
