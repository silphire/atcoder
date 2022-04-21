import math

l, r = map(int, input().split())
for i in range(r - l, 0, -1):
    for x in range(l, r - i + 1):
        if math.gcd(x, x + i) == 1:
            print(i)
            exit()