import itertools

if True:
    n, m, q = map(int, input().split())
    aa = [0] * q
    bb = [0] * q
    cc = [0] * q
    dd = [0] * q
    for i in range(q):
        a, b, c, d = map(int, input().split())
        aa[i] = a - 1
        bb[i] = b - 1
        cc[i] = c
        dd[i] = d

ans = 0
ma = None
for a in itertools.combinations_with_replacement(list(range(1, m + 1)), n):
    x = 0
    for i in range(q):
        if a[bb[i]] - a[aa[i]] == cc[i]:
            x += dd[i]
    if x > ans:
        ma = a
    ans = max(ans, x)
print(ans)
