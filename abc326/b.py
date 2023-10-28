n = int(input())

for x in range(n, 1000):
    if (x // 100) * (x // 10 % 10) == x % 10:
        print(x)
        exit()