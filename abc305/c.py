h, w = map(int, input().split())
ss = [
    input()
    for _ in range(h)
]

minx = float('inf')
maxx = float('-inf')
miny = float('inf')
maxy = float('-inf')
for y in range(h):
    for x in range(w):
        if ss[y][x] == '#':
            minx = min(minx, x)
            maxx = max(maxx, x)
            miny = min(miny, y)
            maxy = max(maxy, y)
for y in range(miny, maxy + 1):
    for x in range(minx, maxx + 1):
        if ss[y][x] == '.':
            print(y + 1, x + 1)
            exit()