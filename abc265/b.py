n, m, t = map(int, input().split())
aa = list(map(int, input().split()))
d = {}
for i in range(m):
    x, y = map(int, input().split())
    d[x] = y
for i in range(1, n):
    t += d.get(i, 0)
    t -= aa[i - 1]
    if t <= 0:
        print('No')
        exit()
print('Yes')