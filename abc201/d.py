h, w = map(int, input().split())
tb = {'-': -1, '+': 1}
aa = [
    list(map(lambda x: tb[x], list(input().rstrip())))
    for _ in range(h)
]

dp = [[0] * w for _ in range(h)]

for y in range(h - 1, -1, -1):
    for x in range(w - 1, -1, -1):
        if x == w - 1 and y == h - 1:
            continue
        p = (x + y) % 2
        if p == 0:
            # Takahashi
            d = float('-inf')
            if x + 1 < w:
                d = max(d, dp[y][x + 1] + aa[y][x + 1])
            if y + 1 < h:
                d = max(d, dp[y + 1][x] + aa[y + 1][x])
            dp[y][x] = d
        else:
            # Aoki
            d = float('inf')
            if x + 1 < w:
                d = min(d, dp[y][x + 1] - aa[y][x + 1])
            if y + 1 < h:
                d = min(d, dp[y + 1][x] - aa[y + 1][x])
            dp[y][x] = d


if dp[0][0] == 0:
    print("Draw")
elif dp[0][0] > 0:
    print("Takahashi")
else:
    print("Aoki")