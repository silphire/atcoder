s = int(input())

M = 10 ** 9 + 7
dp = [0] * 2001

for x in range(3, s + 1):
    dp[x] = 1 + sum(dp[3:x-3+1])
    dp[x] %= M
print(dp[s])