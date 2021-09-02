n, w = map(int, input().split())
w1 = 0
v = [[] for _ in range(4)]
for i in range(n):
    ww, vv = map(int, input().split())
    if i == 0:
        w1 = ww
    v[ww - w1].append(vv)

nn = [0] * 4
for i in range(4):
    v[i].sort(reverse=True)
    nn[i] = len(v[i]) + 1

maxv = 0
for i0 in range(nn[0]):
    for i1 in range(nn[1]):
        for i2 in range(nn[2]):
            for i3 in range(nn[3]):
                if w1 * i0 + (w1 + 1) * i1 + (w1 + 2) * i2 + (w1 + 3) * i3 > w:
                    continue
                maxv = max(
                    maxv, 
                    sum(v[0][:i0]) + sum(v[1][:i1]) + sum(v[2][:i2]) + sum(v[3][:i3]))
print(maxv)