import math

n, k = map(int, input().split())
aa = tuple(map(int, input().split()))

p = 0
for i in range(n):
    if aa[i] == 1:
        p = i
        break

n -= 1
k -= 1
x = math.ceil(n / k)
print(x)
