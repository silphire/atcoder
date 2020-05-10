a, b, c, k = map(int, input().split())

n = 0
if k >= a:
    n += a
    k -= a
else:
    n = k
    k = 0

k -= b

if k >= 0:
    n -= max(k, 0)
print(n)
