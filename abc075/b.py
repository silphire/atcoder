h, w = map(int, input().split())
s = [
    input().rstrip()
    for _ in range(h)
]

for y in range(h):
    a = ''
    for x in range(w):
        if s[y][x] == '#':
            a += '#'
            continue
        n = 0
        for j in range(-1, 2):
            for i in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if 0 <= y + j < h and 0 <= x + i < w:
                    if s[y + j][x + i] == '#':
                        n += 1
        a += str(n)
    print(a)