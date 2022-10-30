n, ax, ay = map(int, input().split())
aa = list(map(int, input().split()))

xx = aa[2::2]
yy = aa[1::2]

xc = (aa[0], )
yc = (0, )
for x in xx:
    nxc = set()
    for c in xc:
        nxc.add(c + x)
        nxc.add(c - x)
    xc = nxc
for y in yy:
    nyc = set()
    for c in yc:
        nyc.add(c + y)
        nyc.add(c - y)
    yc = nyc

if ax in xc and ay in yc:
    print('Yes')
else:
    print('No')