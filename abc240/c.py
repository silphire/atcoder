n, x = map(int, input().split())
cand = {0}
for _ in range(n):
    a, b = map(int, input().split())
    nc = set()
    for c in cand:
        nc.add(c + a)
        nc.add(c + b)
    cand = nc
if x in cand:
    print('Yes')
else:
    print('No')