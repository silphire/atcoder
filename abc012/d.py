n, m = map(int, input().split())

d = [[float('inf')] * n for _ in range(n)]
for i in range(n):
    d[i][i] = 0

for _ in range(m):
    a, b, t = map(int, input().split())
    a -= 1
    b -= 1
    d[a][b] = d[b][a] = t

for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

ans = float('inf')
for i in range(n):
    ans = min(ans, max(d[i]))
print(ans)