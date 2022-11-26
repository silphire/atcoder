h, w = map(int, input().split())
ss = [
    list(input().rstrip())
    for _ in range(h)
]
tt = [
    list(input().rstrip())
    for _ in range(h)
]

rs = tuple(sorted([tuple([ss[y][x] for y in range(h)]) for x in range(w)]))
rt = tuple(sorted([tuple([tt[y][x] for y in range(h)]) for x in range(w)]))
if rs == rt:
    print('Yes')
else:
    print('No')