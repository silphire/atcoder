L = int(input())
from math import factorial

n = L - 1
r = 11
x = factorial(n) // factorial(r) // factorial(n - r)
print(x)