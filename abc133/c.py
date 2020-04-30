l, r = map(int, input().split())
z = 2020
for x in range(l, r + 1):
    for y in range(x + 1, r + 1):
        z = min(z, (x * y) % 2019)
        if z == 0:
            print(0)
            exit(0)
print(z)