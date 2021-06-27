import math

a, b, c, d = map(int, input().split())

if c * d == b:
    print(-1)
else:
    x = math.ceil(a / (c * d - b))
    if x < 0:
        print(-1)
    else:
        print(x)