from collections import deque
from collections import defaultdict

h, w = map(int, input().split())
aa = [
    input().rstrip()
    for _ in range(h)
]
gx = 0
gy = 0
sx = 0
sy = 0
warp = defaultdict(list)
for y in range(h):
    for x in range(w):
        if aa[y][x] == 'S':
            sx = x
            sy = y
        elif aa[y][x] == 'G':
            gx = x
            gy = y
        elif aa[y][x] not in '#.':
            warp[aa[y][x]].append((x, y))

MAX = 2000 * 2000 + 1
cc = [[MAX] * w for _ in range(h)]

def isvalid(x, y, c):
    global aa
    global cc

    if not (0 <= x < w and 0 <= y < h):
        return False
    if c >= cc[y][x]:
        return False
    if aa[y][x] == '#':
        return False
    return True

q = deque([(gx, gy, 0)])
while q:
    dx, dy, cost = q.popleft()
    if dx == sx and dy == sy:
        print(min(cost, cc[dy][dx]))
        exit()
    if cc[dy][dx] <= cost:
        continue

    cc[dy][dx] = cost
    m = aa[dy][dx]
    if m.isalpha() and m.islower():
        # warp
        for wx, wy in warp[m]:
            if wx == dx and wy == dy:
                continue
            if isvalid(wx, wy, cost + 1):
                q.append((wx, wy, cost + 1))
        warp[m] = []
    # road
    if isvalid(dx - 1, dy, cost + 1):
        q.append((dx - 1, dy, cost + 1))
    if isvalid(dx + 1, dy, cost + 1):
        q.append((dx + 1, dy, cost + 1))
    if isvalid(dx, dy - 1, cost + 1):
        q.append((dx, dy - 1, cost + 1))
    if isvalid(dx, dy + 1, cost + 1):
        q.append((dx, dy + 1, cost + 1))
print(-1)