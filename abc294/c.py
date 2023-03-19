n, m = map(int, input().split())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))

cc  = [(a, 'a', i) for i, a in enumerate(aa)]
cc += [(b, 'b', i) for i, b in enumerate(bb)]
cc = sorted(cc)

pa = [0] * n
pb = [0] * m
for i, c in enumerate(cc):
    if c[1] == 'a':
        pa[c[2]] = i + 1
    else:
        pb[c[2]] = i + 1
print(*pa)
print(*pb)