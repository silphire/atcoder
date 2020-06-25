n = int(input())
xx = [0] * n
yy = [0] * n
hh = [0] * n
for i in range(n):
    x, y, h = map(int, input().split())
    xx[i], yy[i], hh[i] = x, y, h
    if h > 0:
        x0, y0, h0 = x, y, h

for cx in range(101):
    for cy in range(101):
        f = True
        h = h0 + abs(x0 - cx) + abs(y0 - cy)
        for i in range(n):
            if hh[i] != max(h - abs(xx[i] - cx) - abs(yy[i] - cy), 0):
                f = False
                break
        if f:
            print("{} {} {}".format(cx, cy, h))
            exit(0)
