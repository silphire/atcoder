import math
n = int(input())
xs = list(map(int, input().split()))

p = sum(xs) / len(xs)
x1 = sum([(x - math.floor(p)) ** 2 for x in xs])
x2 = sum([(x - math.ceil(p)) ** 2  for x in xs])
print(min(x1, x2))