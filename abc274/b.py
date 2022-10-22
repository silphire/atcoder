h, w = map(int, input().split())
cc = [
    input().rstrip()
    for _ in range(h)
]
xx = [0] * w
for x in range(w):
    for y in range(h):
        if cc[y][x] == '#':
            xx[x] += 1
print(*xx)