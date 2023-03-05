import math
from fractions import *

n = int(input())
a, b, c, d = map(int, input().split())
x = Fraction(input())
t = a + 2 * b + 3 * c + 4 * d
p = (t - n * x) / (x - 1)
print(math.ceil(max(0, p)))