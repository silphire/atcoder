from collections import deque

n, m = map(int, input().split())
ss = [
    input()
    for _ in range(n)
]
ff = [
    [True] * m
    for _ in range(n)
]
dir = ((-1, 0), (1, 0), (0, -1), (0, 1))

visited = set()
ans = 0
q = deque([(1, 1)])
while q:
    p = q.popleft()
    if p in visited:
        continue
    visited.add(p)

    for d in dir:
        x = p[0]
        y = p[1]
        while ss[y][x] == '.':
            if ff[y][x]:
                ff[y][x] = False
                ans += 1
            x += d[0]
            y += d[1]
        
        x -= d[0]
        y -= d[1]
        if (x, y) not in visited:
            q.append((x, y))

print(ans)