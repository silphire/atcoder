a, b, x = map(int, input().split())

l = 1
r = 1000000000

if a + b > x:
    print(0)
    exit()

while l < r:
    n = (l + r) // 2
    d = len(str(n))
    y = a * n + b * d
    if y == x:
        print(n)
        exit()
    if r - l == 1:
        if a * r + b * len(str(r)) > x:
            print(l)
        else:
            print(r)
        exit()
    if y < x:
        l = n
    else:
        r = n - 1
print(l)
