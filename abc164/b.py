a, b, c, d = map(int, input().split())

while True:
    c -= b
    if c <= 0:
        print("Yes")
        exit(0)
    
    a -= d
    if a <= 0:
        print("No")
        exit(0)