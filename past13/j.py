def is_orthogonal(a, b, c, d):
    s = (a[0] - b[0]) * (c[1] - a[1]) - (a[1] - b[1]) * (c[0] - a[0])
    t = (a[0] - b[0]) * (d[1] - a[1]) - (a[1] - b[1]) * (d[0] - a[0])
    if s * t > 0:
        return False
    
    s = (c[0] - d[0]) * (a[1] - c[1]) - (c[1] - d[1]) * (a[0] - c[0])
    t = (c[0] - d[0]) * (b[1] - c[1]) - (c[1] - d[1]) * (b[0] - c[0])
    if s * t > 0:
        return False
    
    return True

n, k = map(int, input().split())
xs, ys, xt, yt = map(int, input().split())
ww = [0] * n
for i in range(n):
    p, q, r, w = map(int, input().split())
    if q == 0:
        y0 = -1e9
        y1 = 1e9
        x0 = (r - q * y0) / p
        x1 = (r - q * y1) / p
    else:
        x0 = -1e9
        x1 = 1e9
        y0 = (r - p * x0) / q
        y1 = (r - p * x1) / q
    if is_orthogonal((xs, ys), (xt, yt), (x0, y0), (x1, y1)):
        ww[i] = w
print(sum(sorted(ww)[:k]))
