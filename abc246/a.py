xx = [0] * 3
yy = [0] * 3
for i in range(3):
    xx[i], yy[i] = map(int, input().split())
xx.sort()
if xx[0] == xx[1]:
    x = xx[2]
else:
    x = xx[0]
yy.sort()
if yy[0] == yy[1]:
    y = yy[2]
else:
    y = yy[0]
print(*[x, y])