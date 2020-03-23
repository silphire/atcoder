from collections import Counter
import math

n = int(input())
aa = list(map(int, input().split()))

ctr = Counter(aa)

cmb2 = [0] * 200001
for n in range(2, 200001):
    r = 2
    num = 1
    for i in range(1, r + 1):
        num = num * (n - i + 1) // i
    cmb2[n] = num

x = 0
for k, v in ctr.items():
    x += cmb2[v]

for a in aa:
    k = ctr[a] - 1
    print(x - k)