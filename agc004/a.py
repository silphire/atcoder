a, b, c = map(int, input().split())
if min(a % 2, b % 2, c % 2) == 0:
    print(0)
else:
    print(min(a * b, b * c, c * a))
