x = int(input())
if x == 0:
    print("1 1")
    exit(0)

i = 1
while True:
    for a in range(-i, i + 1):
        b = i
        if a ** 5 - b ** 5 == x:
            print("{} {}".format(a, b))
            exit(0)
    
        b = -i
        if a ** 5 - b ** 5 == x:
            print("{} {}".format(a, b))
            exit(0)
    
    for b in range(-i, i + 1):
        a = i
        if a ** 5 - b ** 5 == x:
            print("{} {}".format(a, b))
            exit(0)
    
        a = -i
        if a ** 5 - b ** 5 == x:
            print("{} {}".format(a, b))
            exit(0)
    
    i += 1
