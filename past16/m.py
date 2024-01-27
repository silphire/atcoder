xa, ya, xb, yb = map(int, input().split())
xc, yc, xd, yd = map(int, input().split())

if min(xa, xb) > max(xc, xd) or max(xa, xb) < min(xc, xd):
    print('No')
    exit()

if min(ya, yb) > max(yc, yd) or max(ya, yb) < min(yc, yd):
    print('No')
    exit()

s = (xa - xb) * (yc - ya) - (ya - yb) * (xc - xa)
t = (xa - xb) * (yd - ya) - (ya - yb) * (xd - xa)
if s * t > 0:
    print('No')
    exit()

s = (xc - xd) * (ya - yc) - (yc - yd) * (xa - xc)
t = (xc - xd) * (yb - yc) - (yc - yd) * (xb - xc)
if s * t > 0:
    print('No')
    exit()

print('Yes')