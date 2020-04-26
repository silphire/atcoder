n, d = map(int, input().split())
x = n // (2 * d + 1)
if n % (2 * d + 1) > 0:
    x += 1
print(x)