a, b, k = map(int, input().split())
if a + b < k:
    print("0 0")
elif a < k:
    print("0 {}".format(b - (k - a)))
else:
    print("{} {}".format(a - k, b))