import sys
sys.setrecursionlimit(10000)

a, b, x, y = map(int, input().split())

if a > b:
    a -= 1
if a == b:
    print(x)
    exit()

c = abs(a - b)
if x * 2 < y:
    print(x + c * x * 2)
else:
    print(x + y * c)