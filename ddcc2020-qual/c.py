h, w, k = map(int, input().split())
ss = [
    input()
    for _ in range(h)
]

ans = [
    [0] * w
    for _ in range(h)
]

for y in range(h):
    for x in range(w):
        if ss[y][x] == '#':
            ans[y][x] = k
            k -= 1
        else:
            if x > 0:
                ans[y][x] = ans[y][x - 1]
    for x in range(w - 1, 0, -1):
        if ans[y][x - 1] == 0:
            ans[y][x - 1] = ans[y][x]
for y in range(1, h):
    if ans[y][x] != 0:
        continue
    for x in range(w):
        ans[y][x] = ans[y - 1][x]
for y in range(h - 2, -1, -1):
    if ans[y][x] != 0:
        continue
    for x in range(w):
        ans[y][x] = ans[y + 1][x]

for y in range(h):
    print(*ans[y])