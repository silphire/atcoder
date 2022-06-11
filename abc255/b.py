n, k = map(int, input().split())
aa = set(map(lambda x: int(x) - 1, input().split()))
xx = [0] * n
yy = [0] * n
for i in range(n):
    xx[i], yy[i] = map(int, input().split())

rr = 0
for j in range(n):
    r = float('inf')
    if j in aa:
        continue
    for a in aa:
        r = min(r, (xx[a] - xx[j]) ** 2 + (yy[a] - yy[j]) ** 2)
    rr = max(rr, r)
print(rr ** 0.5)