n = int(input())
miny = 1
maxy = n
while miny < maxy:
    ny = (miny + maxy) // 2
    print('?', 1, n, miny, ny)
    a = int(input())
    if a == -1:
        exit()
    if a == ny - miny + 1:
        miny = ny + 1
    else:
        maxy = ny
    # print('  *', miny, maxy)

minx = 1
maxx = n
while minx < maxx:
    nx = (minx + maxx) // 2
    print('?', minx, nx, 1, n)
    a = int(input())
    if a == -1:
        exit()
    if a == nx - minx + 1:
        minx = nx + 1
    else:
        maxx = nx
    # print('  *', minx, maxx)

print('!', minx, miny)
