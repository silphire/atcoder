import bisect

n, m, d = map(int, input().split())
aa = list(sorted(set(map(int, input().split()))))
bb = list(sorted(set(map(int, input().split()))))
n = len(aa)
m = len(bb)

ans = -1
for a in aa:
    p = bisect.bisect_left(bb, a + d)
    if p < m and abs(bb[p] - a) <= d:
        ans = max(ans, a + bb[p])
    if p - 1 >= 0 and abs(bb[p - 1] - a) <= d:
        ans = max(ans, a + bb[p - 1])
print(ans)