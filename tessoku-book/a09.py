h, w, n = map(int, input().split())
ss = [
    [0] * (w + 1)
    for _ in range(h + 1)
]
for _ in range(n):
    a, b, c, d = map(lambda x: int(x) - 1, input().split())
    ss[a][b] += 1
    ss[c + 1][b] -= 1
    ss[a][d + 1] -= 1
    ss[c + 1][d + 1] += 1

for y in range(h):
    for x in range(w):
        ss[y][x + 1] += ss[y][x]
for x in range(w):
    for y in range(h):
        ss[y + 1][x] += ss[y][x]

for y, s in enumerate(ss):
    if y == h:
        break
    print(*s[:w])