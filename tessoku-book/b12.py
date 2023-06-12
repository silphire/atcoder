n = int(input())
lo = 0
hi = 10 ** 9
x = None
while hi - lo > 1e-6:
    x = (lo + hi) / 2
    y = x ** 3 + x - n
    if y < 0:
        lo = x
    else:
        hi = x
print(x)