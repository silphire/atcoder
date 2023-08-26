import sys
sys.setrecursionlimit(10 ** 9)
from collections import deque

h, w = map(int, input().split())
aa = [
    input()
    for _ in range(h)
]
visited = [
    [False] * w
    for _ in range(h)
]

for y in range(h):
    for x in range(w):
        if aa[y][x] == 'S':
            sx = x
            sy = y
        if aa[y][x] == 'G':
            gx = x
            gy = y
        if aa[y][x] == '#':
            visited[y][x] = True
        if aa[y][x] == '>':
            visited[y][x] = True
            for i in range(x + 1, w):
                if aa[y][i] in '#<>^v':
                    break
                visited[y][i] = True
        if aa[y][x] == '<':
            visited[y][x] = True
            for i in range(x - 1, -1, -1):
                if aa[y][i] in '#<>^v':
                    break
                visited[y][i] = True
        if aa[y][x] == 'v':
            visited[y][x] = True
            for i in range(y + 1, h):
                if aa[i][x] in '#<>^v':
                    break
                visited[i][x] = True
        if aa[y][x] == '^':
            visited[y][x] = True
            for i in range(y - 1, -1, -1):
                if aa[i][x] in '#<>^v':
                    break
                visited[i][x] = True

q = deque([(sx, sy, 0)])
while q:
    x, y, d = q.popleft()
    if not (0 <= x < w and 0 <= y < h):
        continue
    if visited[y][x]:
        continue
    visited[y][x] = True
    if aa[y][x] == 'G':
        print(d)
        exit()
    q.append((x - 1, y, d + 1))
    q.append((x + 1, y, d + 1))
    q.append((x, y - 1, d + 1))
    q.append((x, y + 1, d + 1))
print(-1)