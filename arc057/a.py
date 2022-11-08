a, k = map(int, input().split())

if k == 0:
    print(2 * 10 ** 12 - a)
else:
    x = 0
    while a < 2 * 10 ** 12:
        a += 1 + k * a
        x += 1
    print(x)