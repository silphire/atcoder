s = list(map(int, list(input().rstrip())))
n = len(s)

dp = [0] * 3000
dp[0] = 1
ans = 0
p = 1
x = 0
for i in range(n - 1, -1, -1):
    x = (x + s[i] * p) % 2019
    ans += dp[x]
    p = (p * 10) % 2019
    dp[x] += 1
print(ans)