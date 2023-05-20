h, w = map(int, input().split())
ss = [
    input()
    for _ in range(h)
]
t = 'snuke'
nt = len(t)

for y in range(h):
    for x in range(w):
        if ss[y][x] != 's':
            continue
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                f = True
                for i in range(1, nt):
                    nx = x + dx * i
                    ny = y + dy * i
                    if not (0 <= nx < w and 0 <= ny < h and ss[ny][nx] == t[i]):
                        f = False
                        break
                if f:
                    for i in range(nt):
                        nx = x + dx * i
                        ny = y + dy * i
                        print(ny + 1, nx + 1)
