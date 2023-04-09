a, b = map(int, input().split())

x = 0
while b != 0:
    ma = max(a, b)
    mi = min(a, b)
    d = ma // mi

    x += d
    a, b = mi, ma - d * mi
print(x - 1)