import math

n = int(input())
aa = list(map(int, input().split()))

x = aa[0]
for i in range(1, n):
    x = math.gcd(x, aa[i])
print(x)