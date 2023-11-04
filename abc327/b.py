b = int(input())
a = 1
while True:
    x = a ** a
    if x == b:
        print(a)
        exit()
    elif x > b:
        print(-1)
        exit()
    a += 1