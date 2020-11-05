import math

n, m = map(int, input().split())

dv = []
for x in range(1, math.ceil(m ** 0.5) + 1):
    if m % x == 0:
        dv.append(x)
        dv.append(m // x)

ans = 0
for d in sorted(dv, reverse=True):
    if d <= m / n:
        ans = max(ans, d)
print(ans)