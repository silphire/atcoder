h, w, n = map(int, input().split())
xx = set()
yy = set()
aa = [None] * n
bb = [None] * n
for i in range(n):
    a, b = map(int, input().split())
    yy.add(a)
    xx.add(b)
    aa[i] = a
    bb[i] = b

xt = {}
yt = {}
for i, x in enumerate(sorted(xx)):
    xt[x] = i + 1
for i, y in enumerate(sorted(yy)):
    yt[y] = i + 1

for i in range(n):
    print(f'{yt[aa[i]]} {xt[bb[i]]}')