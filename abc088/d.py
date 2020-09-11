from collections import deque


h, w = map(int, input().split())
tb = {'#': -1, '.': 0}
ss = [
    list(map(lambda x: tb[x], list(input().rstrip())))
    for _ in range(h)
]

b = 0
for y in range(h):
    for x in range(w):
        if ss[y][x] == -1:
            b += 1

ss[0][0] = 1
q = deque([(0, 0)])
while q:
    pos = q.pop()
    d = ss[pos[1]][pos[0]]
    for x, y in ((0, -1), (-1, 0), (1, 0), (0, 1)):
        yy = pos[1] + y
        xx = pos[0] + x
        if 0 <= yy < h and 0 <= xx < w:
            if ss[yy][xx] == 0:
                ss[yy][xx] = d + 1
                q.append((xx, yy))
    if pos == (w - 1, h - 1):
        break
d = ss[h - 1][w - 1]
if d == 0:
    print(-1)
else:
    print(w * h - b - d)