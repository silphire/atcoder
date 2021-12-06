import math
a, b, x = map(int, input().split())
if x * 2 > a * a * b:
    a = math.atan((2 * b - (2 * x / a / a)) / a)
else:
    a = math.atan(a * b * b / 2 / x)
print(math.degrees(a))
