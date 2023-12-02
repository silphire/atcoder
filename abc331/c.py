import bisect
from collections import Counter
from collections import defaultdict

n = int(input())
aa = list(map(int, input().split()))

d = defaultdict(int)
c = 0
ctr = Counter(aa)
kk = sorted(ctr, reverse=True)
for a in kk:
    c += ctr[a] * a
    d[a] += c

ans = [0] * n
kk = sorted(kk)
for i in range(n):
    p = bisect.bisect_right(kk, aa[i])
    if p == len(kk):
        ans[i] = 0
    else:
        ans[i] = d[kk[p]]
print(*ans)