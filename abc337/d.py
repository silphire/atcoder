h, w, k = map(int, input().split())
ss = [
    input()
    for _ in range(h)
]

ans = float('inf')
for y in range(h):
    rd = 0
    ro = 0
    left = 0
    for x in range(w):
        if ss[y][x] == '.':
            rd += 1
        elif ss[y][x] == 'o':
            rd += 1
            ro += 1
        else:
            rd = 0
            ro = 0
            left = x
        if x >= left + k:
            if ss[y][x - k] == '.':
                rd -= 1
            elif ss[y][x - k] == 'o':
                rd -= 1
                ro -= 1
        if rd >= k:
            ans = min(ans, rd - ro)

for x in range(w):
    rd = 0
    ro = 0
    left = 0
    for y in range(h):
        if ss[y][x] == '.':
            rd += 1
        elif ss[y][x] == 'o':
            rd += 1
            ro += 1
        else:
            rd = 0
            ro = 0
            left = y
        if y >= left + k:
            if ss[y - k][x] == '.':
                rd -= 1
            elif ss[y - k][x] == 'o':
                rd -= 1
                ro -= 1
        if rd >= k:
            ans = min(ans, rd - ro)

if ans == float('inf'):
    print(-1)
else:
    print(ans)