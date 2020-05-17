import math

a, b, h, m = map(int, input().split())

if (h * 60 + m) > 0:
    th = 2.0 * math.pi / (12 * 60) * (h * 60 + m)
else:
    th = 0.0
xh = a * math.cos(th)
yh = a * math.sin(th)

if m > 0:
    tm = 2.0 * math.pi / 60 * m
else:
    tm = 0.0
xm = b * math.cos(tm)
ym = b * math.sin(tm)

d = ((xh - xm) ** 2 + (yh - ym) ** 2) ** 0.5
print(d)
