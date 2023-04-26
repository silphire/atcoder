import math
from collections import Counter

input()
ans = 0
for x in Counter(map(int, input().split())).values():
    ans += math.comb(x, 3)
print(ans)