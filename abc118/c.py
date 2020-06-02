from fractions import gcd

n = int(input())
aa = tuple(map(int, input().split()))

a = aa[0]
for b in aa[1:]:
    a = gcd(a, b)
print(a)
