import bisect
n, m = map(int, input().split())
aa = list(map(int, input().split()))
bb = list(sorted(map(int, input().split())))

ans = float('inf')
for a in aa:
    p = bisect.bisect_left(bb, a)
    for pp in range(p - 1, p + 2):
        if 0 <= pp < m:
            ans = min(ans, abs(a - bb[pp]))
print(ans)