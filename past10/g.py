a, b, c = map(int, input().split())
l = 1
r = 2
while r - l > 1e-10:
    x = (l + r) / 2
    if a * x ** 5 + b * x + c < 0:
        l = x
    else:
        r = x
x = (l + r) / 2
print(x)