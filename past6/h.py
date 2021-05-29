import math

n, m, k, q = map(int, input().split())

c = [[0], [0]]
for i in range(n):
    p, t = map(int, input().split())
    c[t].append(p)
for i in range(2):
    c[i].sort()
    for j in range(1, len(c[i])):
        c[i][j] += c[i][j - 1]

ans = float('inf')
for x in range(len(c[1])):
    y = m - x
    if 0 <= y < len(c[0]):
        ans = min(ans, c[0][y] + c[1][x] + q * math.ceil(x / k))
print(ans)
