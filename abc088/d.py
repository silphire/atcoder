from collections import deque

h, w = map(int, input().split())
ss = [
    list(input().rstrip())
    for _ in range(h)
]

b = 0
for y in range(h):
    for x in range(w):
        if ss[y][x] == '#':
            b += 1

d = 0
q = deque([(0, 0, 1)])
while q:
    px, py, pd = q.popleft()
    if ss[py][px] != '.':
        continue
    ss[py][px] = 'v'
    for dx, dy in ((0, -1), (-1, 0), (1, 0), (0, 1)):
        yy = py + dy
        xx = px + dx
        if 0 <= yy < h and 0 <= xx < w:
            if ss[yy][xx] == '.':
                q.append((xx, yy, pd + 1))
    if px == w - 1 and py == h - 1:
        print(w * h - b - pd)
        exit()
print(-1)