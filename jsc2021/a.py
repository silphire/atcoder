import math
x, y, z = map(int, input().split())
if (y * z) % x == 0:
    print(y * z // x - 1)
else:
    print(math.floor(y * z / x))