import math

n = int(input())

ans = 10 ** 10
for x in range(1, math.ceil(n ** 0.5) + 1):
    if n % x == 0:
        ans = min(ans, max(len(str(x)), len(str(n // x))))
print(ans)