from collections import deque

h, w = map(int, input().split())
ss = [
    input()
    for _ in range(h)
]

for y in range(h):
    for x in range(w):
        if ss[y][x] == 's':
            sx = x
            sy = y
        if ss[y][x] == 'g':
            gx = x
            gy = y
        if ss[y][x] == 'a':
            ax = x
            ay = y

d = [False] * (50 ** 4)
q = deque([(sx, sy, ax, ay, 0)])
while q:
    sx, sy, ax, ay, cnt = q.popleft()
    if ax == gx and ay == gy:
        print(cnt)
        exit()
    
    k = sx * (50 ** 3) + sy * (50 ** 2) + ax * 50 + ay
    if d[k]:
        continue
    d[k] = True

    if sy - 1 >= 0:
        if sx == ax and sy - 1 == ay:
            if ay - 1 >= 0 and ss[ay - 1][ax] != '#':
                q.append((sx, sy - 1, ax, ay - 1, cnt + 1))
        elif ss[sy - 1][sx] != '#':
            q.append((sx, sy - 1, ax, ay, cnt + 1))

    if sx - 1 >= 0:
        if sx - 1 == ax and sy == ay:
            if ax - 1 >= 0 and ss[ay][ax - 1] != '#':
                q.append((sx - 1, sy, ax - 1, ay, cnt + 1))
        elif ss[sy][sx - 1] != '#':
            q.append((sx - 1, sy, ax, ay, cnt + 1))
    
    if sy + 1 < h:
        if sx == ax and sy + 1 == ay:
            if ay + 1 < h and ss[ay + 1][ax] != '#':
                q.append((sx, sy + 1, ax, ay + 1, cnt + 1))
        elif ss[sy + 1][sx] != '#':
            q.append((sx, sy + 1, ax, ay, cnt + 1))

    if sx + 1 < w:
        if sx + 1 == ax and sy == ay:
            if ax + 1 < w and ss[ay][ax + 1] != '#':
                q.append((sx + 1, sy, ax + 1, ay, cnt + 1))
        elif ss[sy][sx + 1] != '#':
            q.append((sx + 1, sy, ax, ay, cnt + 1))

print(-1)