import math

n, q = map(int, input().split())
aa = list(map(int, input().split()))
ss = list(map(int, input().split()))

gg = [0] * n
gg[0] = aa[0]
for i in range(1, n):
    gg[i] = math.gcd(gg[i - 1], aa[i])

for i in range(q):
    x = math.gcd(ss[i], gg[-1])
    if x > 1:
        print(x)
        continue

    x = ss[i]
    l = 0
    r = n - 1
    while l < r:
        c = (l + r) // 2
        if math.gcd(x, gg[c]) == 1:
            r = c
        else:
            l = c + 1
    print(l + 1)