n, m = map(int, input().split())
d = [[False] * n for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    d[x][y] = d[y][x] = True

ans = 0
for x in range(2 ** n):
    y = x
    p = []
    for i in range(n):
        if y & 1 == 1:
            p.append(i)
        y >>= 1
    f = True
    for a in p:
        for b in p:
            if a == b:
                continue
            if not d[a][b]:
                f = False
                break
        if not f:
            break
    if f:
        ans = max(ans, len(p))
print(ans)