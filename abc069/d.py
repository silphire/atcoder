h, w = map(int, input().split())
n = int(input())
aa = list(map(int, input().split()))

c = [[0] * w for _ in range(h)]
x = 0
y = 0
for ai, a in enumerate(aa):
    for i in range(a):
        if x == w:
            x = 0
            y += 1
        if y % 2 == 0:
            xx = x
        else:
            xx = w - 1 - x
        c[y][xx] = ai + 1
        x += 1
for y in range(h):
    print(' '.join(map(str, c[y])))
