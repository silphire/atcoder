n = int(input())
ss = [
    tuple(input().rstrip())
    for _ in range(n)
]
for y in range(n):
    a = 0
    for x in range(n):
        if x >= 6 and ss[y][x - 6] == '#':
            a -= 1
        if ss[y][x] == '#':
            a += 1
        if a >= 4:
            print('Yes')
            exit()

for x in range(n):
    a = 0
    for y in range(n):
        if y >= 6 and ss[y - 6][x] == '#':
            a -= 1
        if ss[y][x] == '#':
            a += 1
        if a >= 4:
            print('Yes')
            exit()

for yy in range(n):
    if yy + 6 <= n:
        a = 0
        x = 0
        y = yy
        while x < n and y < n:
            if x - 6 >= 0 and y - 6 >= 0 and ss[y - 6][x - 6] == '#':
                a -= 1
            if ss[y][x] == '#':
                a += 1
            if a >= 4:
                print('Yes')
                exit()
            x += 1
            y += 1

    if yy - 5 >= 0:
        a = 0
        x = 0
        y = yy
        while x < n and y >= 0:
            if x - 6 >= 0 and y + 6 < n and ss[y + 6][x - 6] == '#':
                a -= 1
            if ss[y][x] == '#':
                a += 1
            if a >= 4:
                print('Yes')
                exit()
            x += 1
            y -= 1

for xx in range(n):
    if xx + 6 <= n:
        a = 0
        x = xx
        y = 0
        while x < n and y < n:
            if x - 6 >= 0 and y - 6 >= 0 and ss[y - 6][x - 6] == '#':
                a -= 1
            if ss[y][x] == '#':
                a += 1
            if a >= 4:
                print('Yes')
                exit()
            x += 1
            y += 1

    if xx - 5 >= 0:
        a = 0
        x = xx
        y = 0
        while x >= 0 and y < n:
            if x + 6 < n and y - 6 >= 0 and ss[y - 6][x + 6] == '#':
                a -= 1
            if ss[y][x] == '#':
                a += 1
            if a >= 4:
                print('Yes')
                exit()
            x -= 1
            y += 1

print('No')
