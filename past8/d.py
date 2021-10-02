import math
x, y = map(int, input().split())
xx = set()
for d in range(1, math.floor(x ** 0.5) + 1):
    if x % d == 0:
        xx.add(d)
        xx.add(x // d)
yy = set()
for d in range(1, math.floor(y ** 0.5) + 1):
    if y % d == 0:
        yy.add(d)
        yy.add(y // d)
if len(xx) < len(yy):
    print('Y')
elif len(xx) > len(yy):
    print('X')
else:
    print('Z')