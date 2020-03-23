a, b = map(int, input().split())
if a == b:
    print(a + b)
else:
    c = max(a, b)
    print(c + c - 1)