h, w, n = map(int, input().split())
t = input()
ss = [
    input()
    for _ in range(h)
]
ff = [[True] * w for _ in range(h)]

pos = set()
x = 0
y = 0
for c in t:
    if c == 'L':
        x -= 1
    elif c == 'R':
        x += 1
    elif c == 'U':
        y -= 1
    else:
        y += 1
    pos.add((x, y))

for y in range(h):
    for x in range(w):
        if ss[y][x] == '.':
            continue
        for p in pos:
            ax = x - p[0]
            ay = y - p[1]
            if 0 <= ax < w and 0 <= ay < h:
                ff[ay][ax] = False

ans = 0
for y in range(h):
    for x in range(w):
        if ff[y][x] and ss[y][x] == '.':
            ans += 1
print(ans)