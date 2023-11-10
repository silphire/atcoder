h, w = map(int, input().split())
ss = [
    input()
    for _ in range(h)
]

inf = float('inf')
dp = [[inf] * w for _ in range(h)]
dp[0][0] = int(ss[0][0] == '#')

for y in range(h):
    for x in range(w):
        if y > 0:
            b = int(ss[y - 1][x] == '.' and ss[y][x] == '#')
            dp[y][x] = min(dp[y][x], dp[y - 1][x] + b)
        if x > 0:
            b = int(ss[y][x - 1] == '.' and ss[y][x] == '#')
            dp[y][x] = min(dp[y][x], dp[y][x - 1] + b)
print(dp[-1][-1])