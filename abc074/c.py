a, b, c, d, e, f = map(int, input().split())

w = set()

ia = 0
while ia * 100 <= f:
    ib = 0
    while ia * 100 * a + ib * 100 * b <= f:
        w.add(ia * 100 * a + ib * 100 * b)
        ib += 1
    ia += 1

s = set()

ic = 0
while ic * 100 <= f:
    id = 0
    while ic * c + id * d <= f:
        s.add(ic * c + id * d)
        id += 1
    ic += 1

rmax = 0
rw = 0
rs = 0
for ww in w:
    for ss in s:
        if ww == 0 or ww + ss > f or ss / (ww + ss) > e / (100 + e):
            continue
        r = ss / (ww + ss)
        if r >= rmax:
            rmax = r
            rw = ww + ss
            rs = ss
print(f'{rw} {rs}')
