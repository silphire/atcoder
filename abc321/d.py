import bisect

n, m, p = map(int, input().split())
aa = list(sorted(map(int, input().split())))
bb = list(sorted(map(int, input().split())))

bc = [0] * (m + 1)
for i in range(m):
    bc[i + 1] = bc[i] + bb[i]

ans = 0
for i, a in enumerate(aa):
    if a >= p:
        ans += (n - i) * m * p
        break
    b = p - a
    j = bisect.bisect_left(bb, b)
    ans += j * a + bc[j] + (m - j) * p
print(ans)