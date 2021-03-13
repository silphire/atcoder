import bisect

n, m, q = map(int, input().split())
wv = [0] * n
x = [0] * m
for i in range(n):
    w, v = map(int, input().split())
    wv[i] = (w, v)
wv = sorted(wv, key=lambda x: (-x[1], x[0]))
x = list(map(int, input().split()))

for i in range(q):
    maxv = 0
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    b = sorted(x[:l] + x[r+1:])
    for w, v in wv:
        if not b:
            break
        p = bisect.bisect_left(b, w)
        if p < len(b):
            b.pop(p)
            maxv += v
    print(maxv)