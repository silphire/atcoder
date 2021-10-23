h, w = map(int, input().split())
aa = [
    list(map(int, input().split()))
    for _ in range(h)
]
f = True
for i1 in range(h):
    for j1 in range(w):
        for i2 in range(i1 + 1, h):
            for j2 in range(j1 + 1, w):
                f = f and aa[i1][j1] + aa[i2][j2] <= aa[i2][j1] + aa[i1][j2]
if f:
    print('Yes')
else:
    print('No')