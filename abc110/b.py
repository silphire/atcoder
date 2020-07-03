n, m, x, y = map(int, input().split())
xx = tuple(map(int, input().split())) + (x,)
yy = tuple(map(int, input().split())) + (y,)

maxx = max(xx)
miny = min(yy)

if maxx >= miny:
    print('War')
else:
    print('No War')
