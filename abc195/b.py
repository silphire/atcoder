import math
a, b, w = map(int, input().split())
x = math.ceil(1000 * w / b)
y = math.floor(1000 * w / a)
if x > y:
    print("UNSATISFIABLE")
else:
    print(f'{x} {y}')