h, w, k = map(int, input().split())
cc = [
    list(input())
    for _ in range(h)
]

ans = 0
for y in range(2 ** h):
    ncc = [list(cc[i]) for i in range(h)]
    yl = set()

    a = 0
    i = 0
    while y > 0:
        if y & 1 == 1:
            yl.add(i)
            a += w
        i += 1
        y >>= 1

    if len(yl) > k:
        continue

    for cy in yl:
        for cx in range(w):
            ncc[cy][cx] = '#'
    
    wk = [0] * w
    for x in range(w):
        t = 0
        for i in range(h):
            if cc[i][x] == '.':
                t += 1
        wk[x] = t
    
    xl = sorted([(-w, i) for i, w in enumerate(wk)])[:k-len(yl)]
    for _, i in xl:
        for j in range(h):
            ncc[j][i] = '#'
    
    a = 0
    for j in range(h):
        for i in range(w):
            if ncc[j][i] == '#':
                a += 1

    ans = max(ans, a)
print(ans)