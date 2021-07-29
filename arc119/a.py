import math
n = int(input())
ans = float('inf')
for b in range(61):
    a = math.floor(n / (1 << b))
    c = n - a * (1 << b)
    if a >= 0 and c >= 0:
        ans = min(ans, a + b + c)
print(ans)