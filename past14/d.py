import math

h, a, b, c, d = map(int, input().split())

ans = 0
while h > 0:
    nh = h - c
    if nh > 0:
        nh -= nh // 2
    nh = max(0, nh)
    n1 = math.ceil((h - nh) / a)
    if n1 * b < d:
        ans += n1 * b
        h -= n1 * a
    elif n1 * b == d:
        ans += d
        h = min(h - n1 * a, nh)
    else:
        ans += d
        h = nh
print(ans)