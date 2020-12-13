n, m, t = map(int, input().split())
mn = n
pb = 0
for i in range(m):
    a, b = map(int, input().split())
    n -= a - pb
    if n <= 0:
        print('No')
        exit()
    n = min(mn, n + b - a)
    pb = b
n -= t - pb
if n <= 0:
    print('No')
else:
    print('Yes')