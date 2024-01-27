from decimal import *
n = int(input())
aa = list(map(int, input().split()))
ma = Decimal(max(aa))
print(*[(Decimal(10 ** 9) * Decimal(a) / ma).quantize(Decimal(1), ROUND_HALF_UP) for a in aa])