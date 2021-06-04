from collections import deque

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
cc = [
    list(
        map(
            lambda x: {'#': -1, '.': 0}[x], 
            list(input().rstrip())
        )
    )
    for _ in range(r)
]
sy -= 1
sx -= 1
gy -= 1
gx -= 1

q = deque([(sx, sy, 0)])
while q:
    x, y, n = q.popleft()
    if x == gx and y == gy:
        print(n)
        exit()
    if not (0 <= x < c and 0 <= y < r) or cc[y][x] != 0:
        continue
    cc[y][x] = n
    q.append((x - 1, y, n + 1))
    q.append((x + 1, y, n + 1))
    q.append((x, y - 1, n + 1))
    q.append((x, y + 1, n + 1))
