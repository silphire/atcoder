import bisect

n, m = map(int, input().split())
aa = list(sorted(map(int, input().split())))

ans = 0
for i, a in enumerate(aa):
    j = bisect.bisect_left(aa, a + m)
    ans = max(ans, j - i)
print(ans)