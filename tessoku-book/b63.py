from collections import deque

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
cc = [
    input()
    for _ in range(r)
]
visited = [[True] * c for _ in range(r)]

sy -= 1
sx -= 1
gy -= 1
gx -= 1

q = deque([(sx, sy, 0)])
while q:
    x, y, d = q.popleft()
    if x == gx and y == gy:
        print(d)
        exit()
    if x - 1 >= 0 and visited[y][x - 1] and cc[y][x - 1] == '.':
        visited[y][x - 1] = False
        q.append((x - 1, y, d + 1))
    if x + 1 < c and visited[y][x + 1] and cc[y][x + 1] == '.':
        visited[y][x + 1] = False
        q.append((x + 1, y, d + 1))
    if y - 1 >= 0 and visited[y - 1][x] and cc[y - 1][x] == '.':
        visited[y - 1][x] = False
        q.append((x, y - 1, d + 1))
    if y + 1 < r and visited[y + 1][x] and cc[y + 1][x] == '.':
        visited[y + 1][x] = False
        q.append((x, y + 1, d + 1))