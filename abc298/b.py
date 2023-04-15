n = int(input())
aa = [
    list(map(int, input().split()))
    for _ in range(n)
]
bb = [
    list(map(int, input().split()))
    for _ in range(n)
]

for _ in range(4):
    f = True
    for y in range(n):
        for x in range(n):
            if aa[y][x] == 1 and bb[y][x] == 0:
                f = False
                break
        if not f:
            break
    if f:
        print('Yes')
        exit()

    cc = [[0] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            cc[n - 1 - x][y] = aa[y][x]
    aa = cc
print('No')