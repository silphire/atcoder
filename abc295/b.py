r, c = map(int, input().split())
bb = [input() for _ in range(r)]
ans = [list(b) for b in bb]
for y in range(r):
    for x in range(c):
        if bb[y][x].isdigit():
            d = int(bb[y][x])
            for b in range(r):
                for a in range(c):
                    if abs(a - x) + abs(b - y) <= d:
                        ans[b][a] = '.'
for a in ans:
    print(''.join(a))