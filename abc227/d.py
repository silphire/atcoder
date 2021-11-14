n, k = map(int, input().split())
aa = list(map(int, input().split()))
mina = min(aa)

ok = 0
ng = 10 ** 18
while ng - ok > 1:
    mid = (ok + ng) // 2
    s = 0
    for a in aa:
        s += min(a, mid)
    if mid * k <= s:
        ok = mid
    else:
        ng = mid
print(ok)
