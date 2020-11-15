sx, sy, gx, gy = map(int, input().split())

sy = -sy
a = (sy - gy) / (sx - gx)
b = sy - a * sx
x = -b / a
print(x)