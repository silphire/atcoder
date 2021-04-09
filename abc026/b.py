import math

n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())
a = sorted(a, reverse=True)
ans = 0
for i in range(n):
    x = a[i] * a[i]
    if i % 2 == 0:
        ans += x
    else:
        ans -= x
print(ans * math.pi)
