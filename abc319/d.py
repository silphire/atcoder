n, m = map(int, input().split())
ll = list(map(int, input().split()))

lw = 0
rw = 10 ** 15
while rw - lw > 1:
    w = (lw + rw) // 2
    nl = 0
    cw = 0
    f = True
    for i, l in enumerate(ll):
        if i > 0:
            cw -= 1
        if l > w:
            f = False
            break
        while cw < l:
            cw = w
            nl += 1
        cw -= l
        if nl > m:
            f = False
            break
    if f:
        rw = w
    else:
        lw = w
print(rw)