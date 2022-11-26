import math

a, b = map(int, input().split())

def f(t):
    if t < 0:
        return float('inf')
    return a / ((1 + t) ** 0.5) + t * b

t = pow(2 * b / a, -2/3) - 1
f = min(f(math.floor(t)), f(math.ceil(t)))
print(f'{f:.10f}')