from collections import deque

INF = 100000
n, xx, yy = map(int, input().split())
block = set()
for _ in range(n):
    block.add(tuple(map(int, input().split())))

traveled = set()
cand = deque([(xx, yy, 0)])

def travel(x, y, d):
    global xx, yy, block, traveled, cand

    if not (-202 <= x <= 202 and -202 <= y <= 202):
        return

    p = (x, y)
    if p == (0, 0):
        print(d)
        exit(0)
    if p in traveled or p in block:
        return
    traveled.add(p)
    cand.append((x, y, d))


while cand:
    x, y, d = cand.popleft()
    travel(x + 1, y - 1, d + 1)
    travel(x, y - 1, d + 1)
    travel(x - 1, y - 1, d + 1)
    travel(x + 1, y, d + 1)
    travel(x - 1, y, d + 1)
    travel(x, y + 1, d + 1)
print(-1)