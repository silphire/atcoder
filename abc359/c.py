sx, sy = map(int, input().split())
tx, ty = map(int, input().split())

if sx < tx:
    if sy % 2 == 0:
        if sx % 2 == 0:
            sx += 1
    else:
        if sx % 2 == 1:
            sx += 1
elif sx > tx:
    if sy % 2 == 0:
        if sx % 2 == 1:
            sx -= 1
    else:
        if sx % 2 == 0:
            sx -= 1

if sx < tx:
    if ty % 2 == 0:
        if tx % 2 == 1:
            tx -= 1
    else:
        if tx % 2 == 0:
            tx -= 1
elif sx > tx:
    if ty % 2 == 0:
        if tx % 2 == 0:
            tx += 1
    else:
        if tx % 2 == 1:
            tx += 1

dx = abs(sx - tx)
dy = abs(sy - ty)
ans = dy + max((dx - dy) // 2 + (dx - dy) % 2, 0)
print(ans)