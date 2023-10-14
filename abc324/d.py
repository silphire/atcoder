from collections import Counter
from collections import defaultdict
import math

n = int(input())
s = input()
if s == '0':
    print(1)
    exit()
ctr = Counter(map(int, list(s)))

ans = 0
for x in range(math.floor(10 ** (13 / 2) + 1)):
    dctr = defaultdict(int)
    y = x * x
    while y > 0:
        dctr[y % 10] += 1
        y //= 10
    if ctr[0] < dctr[0]:
        continue
    f = True
    for i in range(1, 10):
        if ctr[i] != dctr[i]:
            f = False
            break
    if f:
        ans += 1
print(ans)