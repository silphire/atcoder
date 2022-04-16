from collections import defaultdict
import bisect

d = defaultdict(list)
n = int(input())
aa = list(map(int, input().split()))
for i, a in enumerate(aa):
    d[a].append(i + 1)

q = int(input())
for _ in range(q):
    l, r, x = map(int, input().split())
    pl = bisect.bisect_left(d[x], l)
    pr = bisect.bisect_right(d[x], r)
    print(pr - pl)