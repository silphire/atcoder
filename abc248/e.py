n, k = map(int, input().split())
xx = [0] * n
yy = [0] * n
for i in range(n):
    xx[i], yy[i] = map(int, input().split())

if k == 1:
    print('Infinity')
    exit()

f = [[False] * n for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if f[i][j]:
            continue
        s = {i, j}
        for z in range(j + 1, n):
            if (xx[j] - xx[i]) * (yy[z] - yy[i]) == (xx[z] - xx[i]) * (yy[j] - yy[i]):
                s.add(z)
        for a in s:
            for b in s:
                f[a][b] = f[b][a] = True
        if len(s) >= k:
            ans += 1
print(ans)