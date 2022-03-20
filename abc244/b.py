n = int(input())
t = input().rstrip()

xx = [1, 0, -1, 0]
yy = [0, -1, 0, 1]
x = 0
y = 0
r = 0
for c in t:
    if c == 'S':
        x += xx[r]
        y += yy[r]
    else:
        r = (r + 1) % 4
print(*[x, y])