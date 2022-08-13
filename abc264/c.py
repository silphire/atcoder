h1, w1 = map(int, input().split())
aa = [
    list(map(int, input().split()))
    for _ in range(h1)
]
h2, w2 = map(int, input().split())
bb = [
    list(map(int, input().split()))
    for _ in range(h2)
]

for j in range(1 << h1):
    for i in range(1 << w1):
        nb = 0
        for x in range(w1):
            if (i >> x) & 1 == 1:
                nb += 1
        if nb != w2:
            continue

        nb = 0
        for y in range(h1):
            if (j >> y) & 1 == 1:
                nb += 1
        if nb != h2:
            continue

        f = True
        xx = 0
        yy = 0
        for y in range(h1):
            if (j >> y) & 1 == 0:
                continue
            xx = 0
            for x in range(w1):
                if (i >> x) & 1 == 0:
                    continue

                if aa[y][x] != bb[yy][xx]:
                    f = False
                    break                
                xx += 1

            if not f:
                break
            yy += 1
            
        if f:
            print('Yes')
            exit()
print('No')