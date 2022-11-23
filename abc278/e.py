from collections import defaultdict

H, W, N, h, w = map(int, input().split())
aa = [
    list(map(int, input().split()))
    for _ in range(H)
]

ac = [
    [None] * W
    for _ in range(H)
]

for y in range(H):
    for x in range(W):
        if x == 0 and y == 0:
            c = defaultdict(int)
        elif y == 0:
            c = defaultdict(int, ac[y][x - 1])
        elif x == 0:
            c = defaultdict(int, ac[y - 1][x])
        else:
            c = defaultdict(int)
            for a, b in ac[y - 1][x].items():
                c[a] += b
            for a, b in ac[y][x - 1].items():
                c[a] += b
            for a, b in ac[y - 1][x - 1].items():
                c[a] -= b
        c[aa[y][x]] += 1
        ac[y][x] = c

ans = [
    [0] * (W - w + 1)
    for _ in range(H - h + 1)
]

for y in range(H - h + 1):
    for x in range(W - w + 1):
        c = defaultdict(int, ac[y + h - 1][x + w - 1])
        if y > 0:
            for a, b in ac[y - 1][x + w - 1].items():
                c[a] -= b
        if x > 0:
            for a, b in ac[y + h - 1][x - 1].items():
                c[a] -= b
        if x > 0 and y > 0:
            for a, b in ac[y - 1][x - 1].items():
                c[a] += b
        ans[y][x] = len([a for a, b in ac[-1][-1].items() if b - c[a] > 0])

for a in ans:
    print(*a)
