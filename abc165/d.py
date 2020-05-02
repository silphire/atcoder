import math

def f(a, b, x):
    return math.floor(a * x / b) - a * math.floor(x / b)

a, b, n = map(int, input().split())

if n < b:
    print(math.floor(a * n / b))
    exit(0)
print(f(a, b, b - 1))
