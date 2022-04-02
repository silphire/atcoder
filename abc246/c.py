import math

n, k, x = map(int, input().split())
aa = list(map(int, input().split()))

for i in range(n):
    r = min(k, math.floor(aa[i] / x))
    aa[i] -= r * x
    k -= r
    if k <= 0:
        print(sum(aa))
        exit()
aa.sort()
print(sum(aa[:-k]))