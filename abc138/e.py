from collections import defaultdict
import bisect

s = input().rstrip()
t = input().rstrip()
ns = len(s)

if set(t) - set(s):
    print(-1)
    exit()

d = defaultdict(list)
for i, c in enumerate(s):
    d[c].append(i)

a = []
x = -1
ans = 0
for c in t:
    y = bisect.bisect_left(d[c], x + 1)
    if y == len(d[c]):
        ans += ns
        x = d[c][0]
    else:
        x = d[c][y]
ans += x + 1
print(ans)