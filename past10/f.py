h, w, n = map(int, input().split())
aa = [
    list(map(int, input().split()))
    for _ in range(h)
]
cc = list(map(int, input().split()))

for y in range(h):
    for x in range(w):
        for xx, yy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if 0 <= x + xx < w and 0 <= y + yy < h:
                if aa[y][x] != aa[y + yy][x + xx] and cc[aa[y][x] - 1] == cc[aa[y + yy][x + xx] - 1]:
                    print('No')
                    exit()
print('Yes')