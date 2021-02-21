from collections import defaultdict

n, m = map(int, input().split())
a = list(map(int, input().split()))
r = defaultdict(list)
for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    r[x].append(y)

dp = [float('inf')] * n

for i in range(n):
    for j in r[i]:
        dp[j] = min(a[i], dp[i], dp[j])
ans = -float('inf')
for i in range(n):
    ans = max(ans, a[i] - dp[i])
print(ans)