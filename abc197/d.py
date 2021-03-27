import math

n = int(input())
x0, y0 = map(int, input().split())
x2, y2 = map(int, input().split())

cx = (x0 + x2) / 2
cy = (y0 + y2) / 2
r = ((x0 - x2) ** 2 + (y0 - y2) ** 2) ** 0.5 / 2
t = 2 * math.pi / n


x = x0 - cx
y = y0 - cy
p = math.atan2(y, x)

x = r * math.cos(t + p)
y = r * math.sin(t + p)
x += cx
y += cy
print(f'{x} {y}')