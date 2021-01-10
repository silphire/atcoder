import math
from collections import Counter

n = int(input())
aa = list(map(int, input().split()))

ctr = Counter(aa)
ans = 0
for k, v in ctr.items():
    ans += v - 1
if ans % 2 == 1:
    ans += 1
print(n - ans)
