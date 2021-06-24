a, b = map(int, input().split())
r = b - a
while r > 0:
    c = a // r + int(a % r > 0)
    d = c + 1
    if a <= c * r <= b and a <= d * r <= b:
        print(r)
        exit()
    r -= 1