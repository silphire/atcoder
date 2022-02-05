n = int(input())
aa = list(map(int, input().split()))

rs = {0}
r = 0
for a in aa:
    r += a
    r %= 360
    rs.add(r)
rs = sorted(rs)
ans = 360 - rs[-1]
for i in range(1, len(rs)):
    ans = max(ans, rs[i] - rs[i - 1])
print(ans)