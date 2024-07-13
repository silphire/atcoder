xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())

def check(x1, y1, x2, y2):
    if x1 * x2 + y1 * y2 == 0:
        print('Yes')
        exit()

check(xb - xa, yb - ya, xc - xa, yc - ya)
check(xa - xb, ya - yb, xc - xb, yc - yb)
check(xa - xc, ya - yc, xb - xc, yb - yc)
print('No')