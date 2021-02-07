import math
import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

from decimal import *
getcontext().prec = 64

xx, yy, r = map(Decimal, input().split())

ans = 0
for x in range(math.ceil(xx - r), math.floor(xx + r) + 1):
    # (x - xx) ** 2 + (y - yy) ** 2 <= r ** 2
    # (y - yy) ** 2 <= r ** 2 - (x - xx) ** 2
    # -sqrt(rn) <= y - yy <= +sqrt(rn) 
    # -sqrt(rn) + yy <= y <= +sqrt(rn) + yy 
    rn = r ** 2 - (x - xx) ** 2
    if rn < 0:
        continue
    rn = rn.sqrt()
    ans += math.floor(rn + yy) - math.ceil(-rn + yy) + 1
print(ans)