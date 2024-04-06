import heapq

h, w = map(int, input().split())
aa = [
    list(input())
    for _ in range(h)
]

n = int(input())
ee = {}
for i in range(n):
    r, c, e = map(int, input().split())
    ee[(c - 1, r - 1)] = e

sx = sy = 0
tx = ty = 0
for y in range(h):
    for x in range(w):
        if aa[y][x] == 'S':
            sx = x
            sy = y
        elif aa[y][x] == 'T':
            tx = x
            ty = y

mine = [[0] * w for _ in range(h)]
q = [(0, sx, sy)]
while q:
    r, x, y = heapq.heappop(q)
    if x < 0 or x >= w or y < 0 or y >= h:
        continue
    if aa[y][x] == '#':
        continue
    if (x, y) in ee:
        if r > -ee[(x, y)]:
            r = -ee[(x, y)]
    if y == ty and x == tx:
        print('Yes')
        exit()
    if r >= mine[y][x]:
        continue
    mine[y][x] = r
    heapq.heappush(q, (r + 1, x - 1, y))
    heapq.heappush(q, (r + 1, x + 1, y))
    heapq.heappush(q, (r + 1, x, y - 1))
    heapq.heappush(q, (r + 1, x, y + 1))
print('No')