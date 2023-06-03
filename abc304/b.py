import math
n = int(input())
if n <= 10 ** 3 - 1:
    print(n)
else:
    x = math.floor(math.log10(n)) - 2
    x = 10 ** x
    print(n // x * x)
