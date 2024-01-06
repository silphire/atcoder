n = int(input())
ss = [[''] * n for _ in range(n)]

y = 0
x = 0
p = 1
d = 0
while p < n * n:
    ss[y][x] = str(p)
    p += 1
    if d == 0:
        x += 1
        if x >= n or ss[y][x]:
            x -= 1
            y += 1
            d = 1
    elif d == 1:
        y += 1
        if y >= n or ss[y][x]:
            y -= 1
            x -= 1
            d = 2
    elif d == 2:
        x -= 1
        if x < 0 or ss[y][x]:
            x += 1
            y -= 1
            d = 3
    elif d == 3:
        y -= 1
        if y < 0 or ss[y][x]:
            y += 1
            x += 1
            d = 0
ss[n // 2][n // 2] = 'T'
for s in ss:
    print(*s)
