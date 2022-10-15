import bisect
from collections import Counter

n = int(input())
aa = list(map(int, input().split()))
bb = list(sorted(set(aa)))
nb = len(bb)
cc = []
for a in aa:
    p = bisect.bisect_left(bb, a)
    cc.append(nb - 1 - p)
ctr = Counter(cc)
for i in range(n):
    print(ctr[i])