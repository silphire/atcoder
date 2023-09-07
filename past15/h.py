from decimal import *
import math
n = int(input())
s = (Decimal(8) * n + Decimal(1)).sqrt() - Decimal(1)
print(math.floor(s / 2))
