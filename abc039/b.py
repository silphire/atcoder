x = int(input())
for n in range(200):
    y = n ** 4
    if x == y:
        print(n)
        exit()