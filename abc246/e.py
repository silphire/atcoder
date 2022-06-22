from collections import deque

n = int(input())
ay, ax = map(int, input().split())
by, bx = map(int, input().split())
ax -= 1
ay -= 1
bx -= 1
by -= 1
if (ax + ay) % 2 != (bx + by) % 2:
    print(-1)
    exit()

bd = [
    input().strip()
    for _ in range(n)
]

inf = float('inf')
dist = [[inf] * n for _ in range(n)]
f = [[0] * n for _ in range(n)]
dist[ay][ax] = 0
dir = ((-1, -1), (-1, 1), (1, -1), (1, 1))

q = deque([(ax, ay, 5)])
while q:
    x, y, d = q.popleft()
    if x == bx and y == by:
        print(dist[by][bx])
        exit()
    if f[y][x] & (1 << d) != 0:
        continue
    for j, (sx, sy) in enumerate(dir):
        i = 0
        while 0 <= x + sx * i < n and 0 <= y + sy * i < n and bd[y + sy * i][x + sx * i] == '.':
            nd = dist[y][x] + int(d != j)
            if dist[y + sy * i][x + sx * i] > nd:
                dist[y + sy * i][x + sx * i] = nd
                q.append((x + sx * i, y + sy * i, j))
                f[y + sy * i][x + sx * i] |= 1 << j
            i += 1

if dist[by][bx] == inf:
    print(-1)
else:
    print(dist[by][bx])
