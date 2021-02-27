import math

n = int(input())
ans = n
found = set()
for a in range(2, math.ceil(n ** 0.5) + 1):
    aa = a * a
    for b in range(2, math.ceil(n ** 0.5) + 1):
        if aa > n:
            break
        if aa not in found:
            found.add(aa)
            aa *= a
            ans -= 1
print(ans)