h, w = map(int, input().split())
cc = [
    input()
    for _ in range(h)
]

n = min(h, w)
ss = [0] * n

for y in range(1, h - 1):
    for x in range(1, w - 1):
        s = cc[y][x] + cc[y - 1][x - 1] + cc[y - 1][x + 1] + cc[y + 1][x - 1] + cc[y + 1][x + 1]
        if s != '#####':
            continue
        a = 1
        while y + a < h and x + a < w and cc[y + a][x + a] == '#':
            a += 1
        ss[a - 2] += 1
print(*ss)