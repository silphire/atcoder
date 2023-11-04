aa = [
    list(map(int, input().split()))
    for _ in range(9)
]

def no(f):
    if f:
        print('No')
        exit()

for y in range(9):
    f = [False] * 9
    for x in range(9):
        f[aa[y][x] - 1] = True
    no(not all(f))

for x in range(9):
    f = [False] * 9
    for y in range(9):
        f[aa[y][x] - 1] = True
    no(not all(f))

for y in range(0, 9, 3):
    for x in range(0, 9, 3):
        f = [False] * 9
        for j in range(3):
            for i in range(3):
                f[aa[y + j][x + i] - 1] = True
        no(not all(f))

print('Yes')