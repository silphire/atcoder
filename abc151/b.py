n, k, m = map(int, input().split())
a = map(int, input().split())

x = m * n - sum(a)
if x < 0:
    print("0")
elif x > k:
    print("-1")
else:
    print(x)
