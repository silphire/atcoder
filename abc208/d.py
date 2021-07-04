n, m = map(int, input().split())

r = [
    [float('inf')] * n
    for _ in range(n)
]
for i in range(m):
    a, b, c = map(int, input().split())
    r[a - 1][b - 1] = c

ans = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            r[i][j] = min(r[i][j], r[i][k] + r[k][j])
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if r[i][j] < 1e15:
                ans += r[i][j]
print(ans)