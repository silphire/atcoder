N = 1500
dp = [[0] * N for _ in range(N)]

n = int(input())
for _ in range(n):
    x, y = map(lambda a: int(a) - 1, input().split())
    dp[y][x] += 1

for y in range(N):
    for x in range(1, N):
        dp[y][x] += dp[y][x - 1]
    if y == 0:
        continue
    for x in range(N):
        dp[y][x] += dp[y - 1][x]

q = int(input())
for _ in range(q):
    a, b, c, d = map(lambda x: int(x) - 1, input().split())
    ans = dp[d][c]
    if a > 0:
        ans -= dp[d][a - 1]
    if b > 0:
        ans -= dp[b - 1][c]
    if a > 0 and b > 0:
        ans += dp[b - 1][a - 1]
    print(ans)