import math
n, x = map(int, input().split())
xx = sorted(list(map(int, input().split())) + [x])
y = xx[0]
for i in range(n + 1):
    xx[i] -= y
y = xx[1]
for i in range(2, n + 1):
    y = math.gcd(y, xx[i])
print(y)
