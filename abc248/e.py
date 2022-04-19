n, k = map(int, input().split())
xx = [0] * n
yy = [0] * n
for i in range(n):
    xx[i], yy[i] = map(int, input().split())

if k == 1:
    print('Infinity')
    exit()

vis = set()
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if (i, j) in vis:
            continue
        c = 2
        s = {i, j}
        for z in range(j + 1, n):
            if (xx[j] - xx[i]) * (yy[z] - xx[i]) == (xx[z] - xx[i]) * (yy[j] - yy[i]):
                c += 1
                s.add(z)
        for a in s:
            for b in s:
                if a != b:
                    vis.add((a, b))
                    vis.add((b, a))
        if c >= k:
            ans += 1
print(ans)