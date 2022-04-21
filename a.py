import math

l, r = map(int, input().split())
for i in range(r - l, 0, -1):
    for x in range(l, r - i + 1):
        for y in range(l + i, r + 1):
            if math.gcd(x, y) == 1:
                print(y - x)
                exit()