l = int(input())

def f(x):
    return x * x * (l - 2 * x)

print(max(f(l / 3), f(0)))
