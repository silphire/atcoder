n, m = map(int, input().split())
aa = [
    list(map(int, input().split()))
    for _ in range(m)
]

f = [[False] * n for _ in range(n)]
for i in range(m):
    for j in range(1, n):
        x, y = aa[i][j - 1], aa[i][j]
        x -= 1
        y -= 1
        f[x][y] = f[y][x] = True

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if not f[i][j]:
            ans += 1
print(ans)
