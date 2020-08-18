h, w = map(int, input().split())
s = [input().rstrip() for _ in range(h)]

for y in range(h):
    for x in range(w):
        if s[y][x] == '.':
            continue
        if y > 0 and s[y - 1][x] == '#':
            continue
        if y < h - 1 and s[y + 1][x] == '#':
            continue
        if x > 0 and s[y][x - 1] == '#':
            continue
        if x < w - 1 and s[y][x + 1] == '#':
            continue
        print('No')
        exit(0)
print('Yes')