import math

n = int(input())
k = math.floor(n ** 0.5)

ans = 0
for i in range(1, k + 1):
    ans += i * (n // i - n // (i + 1))
for i in range(1, n // (k + 1) + 1):
    ans += n // i
print(ans)
