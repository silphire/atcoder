n = int(input())
X = 2 * 10 ** 5
ans = 0
dp = [0] * (X + 1)

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a * b > X:
            break
        dp[a * b] += 1
for x in range(n + 1):
    ans += dp[x] * dp[n - x]
print(ans)