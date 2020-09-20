x = int(''.join(input().split()))
a = 1
while True:
    aa = a * a
    if aa == x:
        print("Yes")
        exit()
    elif aa > x:
        print("No")
        exit(0)
    a += 1