x = 0
n = int(input())
for _ in range(n):
    t, a = input().split()
    a = int(a)
    if t == '+':
        x += a
    elif t == '-':
        x -= a
    else:
        x *= a
    x %= 10000
    print(x)