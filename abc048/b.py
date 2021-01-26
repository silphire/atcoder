a, b, x = map(int, input().split())

def f(n, x):
    if n < 0:
        return 0
    else:
        return n // x + 1

print(f(b, x) - f(a - 1, x))