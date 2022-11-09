a, b, k, l = map(int, input().split())
if a * l > b:
    x = b * (k // l) + min(b, a * (k % l))
else:
    x = k * a
print(x)