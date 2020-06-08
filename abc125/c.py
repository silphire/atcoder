from fractions import gcd

n = int(input())
aa = tuple(map(int, input().split()))

gcdl = [0] * n
gcdr = [0] * n

gcdl[0] = aa[0]
for i in range(1, n):
    gcdl[i] = gcd(gcdl[i - 1], aa[i])
gcdr[-1] = aa[-1]
for i in range(n - 2, -1, -1):
    gcdr[i] = gcd(gcdr[i + 1], aa[i])

ans = 1
for i in range(n):
    if i == 0:
        x = gcdr[1]
    elif i == n - 1:
        x = gcdl[n - 2]
    else:
        x = gcd(gcdl[i - 1], gcdr[i + 1])
    ans = max(ans, x)

print(ans)
