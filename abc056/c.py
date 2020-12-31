x = int(input())

a = 0
for i in range(1, 50000):
    a += i
    if a >= x:
        print(i)
        exit(0)