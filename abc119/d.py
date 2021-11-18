import bisect

a, b, q = map(int, input().split())
ss = sorted([0, float('inf')] + [
    int(input())
    for _ in range(a)
])
tt = sorted([0, float('inf')] + [
    int(input())
    for _ in range(b)
])
xx = [
    int(input())
    for _ in range(q)
]

for x in xx:
    slp = bisect.bisect_left(ss, x) - 1
    tlp = bisect.bisect_left(tt, x) - 1
    srp = bisect.bisect_right(ss, x)
    trp = bisect.bisect_right(tt, x)

    ans = [None] * 6
    if slp > 0 and tlp > 0:
        ans[0] = x - min(ss[slp], tt[tlp])

    if srp < len(ss) - 1 and trp < len(tt) - 1:
        ans[1] = max(ss[srp], tt[trp]) - x

    if slp > 0 and trp < len(tt) - 1:
        ans[2] = (x - ss[slp]) * 2 + tt[trp] - x
        ans[3] = (tt[trp] - x) * 2 + x - ss[slp]

    if tlp > 0 and srp < len(ss) - 1:
        ans[4] = (x - tt[tlp]) * 2 + ss[srp] - x
        ans[5] = (ss[srp] - x) * 2 + x - tt[tlp]

    print(min(filter(lambda x: x is not None, ans)))