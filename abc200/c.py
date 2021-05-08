from math import factorial
from functools import lru_cache

@lru_cache(maxsize=1000)
def comb(n, r):
    if n < r:
        return 0
    return factorial(n) // factorial(r) // factorial(n - r)


n = int(input())
aa = list(map(int, input().split()))

ctr = [0] * 200
for a in aa:
    ctr[a % 200] += 1

ans = sum([comb(x, 2) for x in ctr])
print(ans)