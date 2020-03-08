a, b, m = map(int, input().split())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))
xx = [0] * m
yy = [0] * m
cc = [0] * m
for i in range(m):
    xx[i], yy[i], cc[i] = map(int, input().split())

ans = min(aa) + min(bb)
for i in range(m):
    ans = min(ans, aa[xx[i] - 1]+ bb[yy[i] - 1] - cc[i])
print(ans)
