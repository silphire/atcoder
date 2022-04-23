from collections import Counter
import math

n = int(input())
aa = list(map(int, input().split()))
ctr = Counter(aa)

ans = 0
for x in sorted(ctr):
    ds = []
    for y in range(1, math.floor(x ** 0.5) + 1):
        if x % y == 0:
            ds.append(y)
            if y != x // y:
                ds.append(x // y)
    for y in ds:
        ans += ctr[x] * ctr[y] * ctr[x // y]
print(ans)