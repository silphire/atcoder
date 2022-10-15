from collections import defaultdict
import bisect

h, w, rs, cs = map(int, input().split())

n = int(input())
wr = defaultdict(list)
wc = defaultdict(list)
for i in range(n):
    r, c = map(int, input().split())
    wr[r].append(c)
    wc[c].append(r)
for r in wr:
    wr[r].sort()
for c in wc:
    wc[c].sort()

q = int(input())
for i in range(q):
    d, l = input().split()
    l = int(l)

    if d == 'L':
        p = bisect.bisect_left(wr[rs], cs)
        if p == 0:
            cs = max(1, cs - l)
        elif cs - l > wr[rs][p - 1]:
            cs -= l
        else:
            cs = wr[rs][p - 1] + 1
    elif d == 'R':
        p = bisect.bisect_left(wr[rs], cs)
        if p == len(wr[rs]):
            cs = min(w, cs + l)
        elif cs + l < wr[rs][p]:
            cs += l
        else:
            cs = wr[rs][p] - 1
    elif d == 'U':
        p = bisect.bisect_left(wc[cs], rs)
        if p == 0:
            rs = max(1, rs - l)
        elif rs - l > wc[cs][p - 1]:
            rs -= l
        else:
            rs = wc[cs][p - 1] + 1
    else:
        p = bisect.bisect_left(wc[cs], rs)
        if p == len(wc[cs]):
            rs = min(h, rs + l)
        elif rs + l < wc[cs][p]:
            rs += l
        else:
            rs = wc[cs][p] - 1
    print(rs, cs)