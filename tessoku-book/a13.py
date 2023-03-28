import bisect

n, k = map(int, input().split())
aa = list(sorted(map(int, input().split())))

ans = 0
for i, a in enumerate(aa):
    p = bisect.bisect_left(aa, a + k)
    ans += p - i
    if p == n or aa[p] != a + k:
        ans -= 1
print(ans)