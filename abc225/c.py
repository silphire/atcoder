n, m = map(int, input().split())
bb = [
    list(map(int, input().split()))
    for _ in range(n)
]
f = True
for y in range(n):
    for x in range(m):
        if x > 0:
            f = f and (bb[y][x] == bb[y][x - 1] + 1)
            f = f and ((bb[y][x] - 1) % 7 > (bb[y][x - 1] - 1) % 7)
        if y > 0:
            f = f and (bb[y][x] == bb[y - 1][x] + 7)
if f:
    print('Yes')
else:
    print('No')