def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

txa, tya, txb, tyb, t, v = map(int, input().split())
d = v * t
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    if dist(x, y, txa, tya) + dist(x, y, txb, tyb) <= d:
        print('YES')
        exit()
print('NO')