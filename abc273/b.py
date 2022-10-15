from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

x, k = map(int, input().split())

t = 10
for i in range(k):
    x = Decimal(x).quantize(Decimal(f'1E{i + 1}'), rounding=ROUND_HALF_UP)
print(int(x))