n = int(input())

aa = [[0] * n for _ in range(n)]
d = 1
for y in range (0, n, 2):
    for x in range(n):
        aa[y][x] = d
        d += 1
for y in range(1, n, 2):
    for x in range(n):
        aa[y][x] = d
        d += 1
for y in range(n):
    print(*aa[y])