import math

n = int(input())
aa = list(map(int, input().split()))
d = 0
for a in [abs(aa[i] - aa[i - 1]) for i in range(1, n)]:
    d = math.gcd(d, a)
print(1 + int(d == 1))