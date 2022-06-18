n = int(input())
aa = list(map(int, input().split()))

dd = []
p = 0
for a in aa:
    nd = []
    dd.append(0)
    for i, d in enumerate(dd):
        if d + a >= 4:
            p += 1
        else:
            nd.append(d + a)
    dd = nd
print(p)