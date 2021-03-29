a, b, c, d = map(int, input().split())
if a * d == b * c:
    print("DRAW")
elif a / b > c / d:
    print("AOKI")
else:
    print("TAKAHASHI")
