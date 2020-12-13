x, y = map(int, input().split())
d = [-1, 0, 2, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
if d[x] == d[y]:
    print('Yes')
else:
    print('No')