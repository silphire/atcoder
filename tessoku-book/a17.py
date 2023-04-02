n = int(input())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))

dp = [0] * n
for i in range(1, n):
    dp[i] = dp[i - 1] + aa[i - 1]
    if i >= 2:
        dp[i] = min(dp[i], dp[i - 2] + bb[i - 2])

ans = []
i = n - 1
while i > 0:
    ans.append(i + 1)
    if dp[i] == dp[i - 1] + aa[i - 1]:
        i -= 1
    else:
        i -= 2

ans.append(1)
print(len(ans))
print(*reversed(ans))