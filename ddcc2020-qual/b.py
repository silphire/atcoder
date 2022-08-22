n = int(input())
aa = list(map(int, input().split()))
l = 0
r = sum(aa)
ans = r
for a in aa:
    l += a
    r -= a
    ans = min(ans, abs(r - l))
print(ans)