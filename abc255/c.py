x, a, d, n = map(int, input().split())
m = a + d * (n - 1)

if d > 0:
    if x <= a:
        print(a - x)
    elif x >= m:
        print(x - m)
    else:
        x -= a
        x %= d
        print(min(d - x, x))
else:
    if x >= a:
        print(x - a)
    elif x <= m:
        print(m - x)
    else:
        d = -d
        x -= a
        x %= d
        print(min(d - x, x))
    