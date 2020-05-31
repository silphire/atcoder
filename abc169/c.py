import decimal

a, b = input().rstrip().split()
a = decimal.Decimal(a)
b = decimal.Decimal(b)
print(int(a * b))