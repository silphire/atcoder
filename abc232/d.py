h, w = map(int, input().split())
cc = [
    input().rstrip()
    for _ in range(h)
]

dp = [[0] * w for _ in range(h)]
dp[0][0] = 1
ans = 1
for y in range(h):
    for x in range(w):
        if cc[y][x] == '.':
            if y > 0 and cc[y - 1][x] == '.' and dp[y - 1][x] > 0:
                dp[y][x] = max(dp[y][x], dp[y - 1][x] + 1)
            if x > 0 and cc[y][x - 1] == '.' and dp[y][x - 1] > 0:
                dp[y][x] = max(dp[y][x], dp[y][x - 1] + 1)
            ans = max(ans, dp[y][x])
print(ans)