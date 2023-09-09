import itertools

cc = [
    list(map(int, input().split()))
    for _ in range(3)
]

n = 0
c = 0
for order in itertools.permutations([a for a in range(1, 10)], 9):
    n += 1
    f = False
    for y in range(3):
        a = [0, 0, 0]
        for x in range(3):
            a[x] = (order[y * 3 + x], cc[y][x])
        a.sort()
        if a[0][1] == a[1][1] and a[0][1] != a[2][1]:
            c += 1
            f = True
            break
    if f:
        continue

    f = False
    for x in range(3):
        a = [0, 0, 0]
        for y in range(3):
            a[y] = (order[y * 3 + x], cc[y][x])
        a.sort()
        if a[0][1] == a[1][1] and a[0][1] != a[2][1]:
            c += 1
            f = True
            break
    if f:
        continue
        
    a = [0, 0, 0]
    for x in range(3):
        y = x
        a[x] = (order[y * 3 + x], cc[y][x])
    a.sort()
    if a[0][1] == a[1][1] and a[0][1] != a[2][1]:
        c += 1
        continue
        
    a = [0, 0, 0]
    for x in range(3):
        y = 2 - x
        a[x] = (order[y * 3 + x], cc[y][x])
    a.sort()
    if a[0][1] == a[1][1] and a[0][1] != a[2][1]:
        c += 1
        continue

print(1 - c / n)