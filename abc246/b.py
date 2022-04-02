import math
a, b = map(int, input().split())

t = math.atan2(b, a)
print(*[math.cos(t), math.sin(t)])