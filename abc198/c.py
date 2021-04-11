import math

r, x, y = map(int, input().split())

d = (x * x + y * y) ** 0.5
if d / r < 1:
    print(2)
else:
    print(math.ceil(d / r))