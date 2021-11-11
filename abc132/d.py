n, k = map(int, input().split())

M = 10 ** 9 + 7
cb = [[0] * 2010 for _ in range(2010)]
cb[1][1] = 1
for a in range(2, 2010):
    for b in range(1, a + 1):
        cb[a][b] = cb[a - 1][b] + cb[a - 1][b - 1]
        cb[a][b] %= M

for i in range(1, k + 1):
    print(cb[n - k + 2][i + 1] * cb[k][i] % M)