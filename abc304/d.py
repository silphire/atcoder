import bisect
from collections import defaultdict

w, h = map(int, input().split())
n = int(input())
pp = [None] * n
qq = [None] * n
for i in range(n):
    pp[i], qq[i] = map(int, input().split())
a = int(input())
aa = list(map(int, input().split()))
b = int(input())
bb = list(map(int, input().split()))

c = defaultdict(int)
for i in range(n):
    x = bisect.bisect_left(aa, pp[i])
    y = bisect.bisect_left(bb, qq[i])
    c[(x, y)] += 1

c = c.values()
maxc = max(c)
minc = min(c)
if len(c) < (a + 1) * (b + 1):
    minc = 0
print(minc, maxc)
