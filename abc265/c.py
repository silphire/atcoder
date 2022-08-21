h, w = map(int, input().split())
gg = [
    list(input().rstrip())
    for _ in range(h)
]
x = 0
y = 0
while True:
    d = gg[y][x]
    gg[y][x] = '.'
    if d == '.':
        print(-1)
        exit()
    elif d == 'U' and y > 0:
        y -= 1
    elif d == 'D' and y < h - 1:
        y += 1
    elif d == 'L' and x > 0:
        x -= 1
    elif d == 'R' and x < w - 1:
        x += 1
    else:
        break
print(*[y + 1, x + 1])