n, a, x, y = map(int, input().split())
if n > a:
    ans = a * x + (n - a) * y
    print(ans)
else:
    print(n * x)