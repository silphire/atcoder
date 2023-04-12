h, w = map(int, input().split())
cc = [
    input()
    for _ in range(h)
]
dp = [[0] * w for _ in range(h)]
dp[0][0] = 1
for y in range(h):
    for x in range(w):
        if cc[y][x] == '#':
            continue
        if y > 0:
            dp[y][x] += dp[y - 1][x]
        if x > 0:
            dp[y][x] += dp[y][x - 1]
print(dp[-1][-1])