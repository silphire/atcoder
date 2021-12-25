import math
x, y = map(int, input().split())
print(max(0, math.ceil((y - x) / 10)))