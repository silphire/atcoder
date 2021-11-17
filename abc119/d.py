import bisect

a, b, q = map(int, input().split())
ss = sorted([float('-inf'), float('inf')] + [
    int(input())
    for _ in range(a)
])
tt = sorted([float('-inf'), float('inf')] + [
    int(input())
    for _ in range(b)
])
xx = [
    int(input())
    for _ in range(q)
]
print(ss)
print(tt)

for x in xx:
    slp = bisect.bisect_left(ss, x)
    tlp = bisect.bisect_left(tt, x)
    srp = bisect.bisect_right(ss, x)
    trp = bisect.bisect_right(tt, x)

    ans = [None] * 6    
    ans[0] = x - min(ss[slp], tt[tlp])

    ans[1] = max(ss[srp], tt[trp]) - x

    ans[2] = (x - ss[slp]) * 2 + tt[trp] - ss[slp]
    ans[3] = (tt[trp] - x) * 2 + x - ss[slp]

    ans[4] = (x - tt[tlp]) * 2 + ss[srp] - tt[tlp]
    ans[5] = (ss[srp] - x) * 2 + x - tt[tlp]

    # print(ans)
    print(min(ans))