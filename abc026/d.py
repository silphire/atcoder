import math

a, b, c = map(int, input().split())

def f(t):
    global a, b, c
    return a * t + b * math.sin(c * t * math.pi)

l = 0
r = 1e10
t = (l + r) / 2
while abs(f(t) - 100) > 1e-6:
    if f(t) < 100:
        l = t
    else:
        r = t
    t = (l + r) / 2

print(t)