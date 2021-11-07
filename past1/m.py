import math

n, m = map(int, input().split())
aa = [0] * n
bb = [0] * n
for i in range(n):
    aa[i], bb[i] = map(int, input().split())
cc = [0] * m
dd = [0] * m
for i in range(m):
    cc[i], dd[i] = map(int, input().split())

def judge(target):
    ab = [0] * n
    for i in range(n):
        ab[i] = bb[i] - aa[i] * target
    cd = float('-inf')
    for i in range(m):
        cd = max(cd, dd[i] - cc[i] * target)
    ab = sorted(ab, reverse=True)
    x = sum(ab[:5])
    if x >= 0:
        return True
    x = sum(ab[:4]) + cd
    return x >= 0

ok = 0
ng = 10 ** 7
while abs(ng - ok) > 1e-9:
    mid = (ok + ng) / 2
    if judge(mid):
        ok = mid
    else:
        ng = mid
print(ok)
