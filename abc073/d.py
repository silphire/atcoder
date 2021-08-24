import itertools

n, m, r = map(int, input().split())
rr = list(map(int, input().split()))
for i in range(r):
    rr[i] -= 1

d = [[float('inf')] * n for _ in range(n)]
for i in range(n):
    d[i][i] = 0
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    d[a][b] = c
    d[b][a] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

ans = float('inf')
for x in itertools.permutations(rr, r):
    a = 0
    for i in range(1, r):
        a += d[x[i - 1]][x[i]]
    ans = min(ans, a)
print(ans)