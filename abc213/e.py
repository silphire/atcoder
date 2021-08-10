from collections import deque

h, w = map(int, input().split())
s = [
    input().rstrip()
    for _ in range(h)
]
dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
visited = [
    [False] * w
    for _ in range(h)
]
q = deque([(0, 0, 0)])
while q:
    p, x, y = q.popleft()
    if visited[y][x]:
        continue
    visited[y][x] = True
    if x == w - 1 and y == h - 1:
        print(p)
        exit()
    for dx, dy in dir:
        xx = x + dx
        yy = y + dy
        if 0 <= xx < w and 0 <= yy < h:
            if visited[yy][xx]:
                continue
            if s[yy][xx] == '.':
                q.appendleft((p, xx, yy))
    for py in range(-2, 3):
        for px in range(-2, 3):
            if abs(px) + abs(py) == 4:
                continue
            if px == 0 and py == 0:
                continue
            xx = x + px
            yy = y + py
            if 0 <= xx < w and 0 <= yy < h and not visited[yy][xx]:
                q.append((p + 1, xx, yy))
print(-1)