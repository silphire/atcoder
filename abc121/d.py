a, b = map(int, input().split())

def f(x):
    return [x, 1, x ^ 1, 0][x % 4]

print(f(a - 1) ^ f(b))