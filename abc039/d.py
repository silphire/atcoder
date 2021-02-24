h, w = map(int, input().split())
s = [
    input().rstrip()
    for _ in range(h)
]
b = [['.'] * w for _ in range(h)]

for y in range(h):
    for x in range(w):
        n = 0
        for j in range(-1, 2):
            for i in range(-1, 2):
                xx = x + i
                yy = y + j
                if 0 <= xx < w and 0 <= yy < h:
                    if s[yy][xx] == '#':
                        n += 1
                else:
                    n += 1
        if n == 9:
            b[y][x] = '#'

t = [['.'] * w for _ in range(h)]
for y in range(h):
    for x in range(w):
        for j in range(-1, 2):
            for i in range(-1, 2):
                xx = x + i
                yy = y + j
                if 0 <= xx < w and 0 <= yy < h and b[yy][xx] == '#':
                    t[y][x] = '#'
                    break
            if t[y][x] == '#':
                break
        if s[y][x] != t[y][x]:
            print('impossible')
            exit()

print('possible')
for y in range(h):
    print(''.join(b[y]))