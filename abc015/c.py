n, k = map(int, input().split())
aa = set()
for _ in range(n):
    na = set()
    tt = list(map(int, input().split()))
    if aa:
        for t in tt:
            for a in aa:
                na.add(a ^ t)
        aa = na
    else:
        aa = tt
if 0 in aa:
    print('Found')
else:
    print('Nothing')