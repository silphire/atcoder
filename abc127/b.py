r, d, xn = map(int, input().split())
for n in range(10):
    xn = r * xn - d
    print(xn)