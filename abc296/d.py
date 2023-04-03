import math

n, m = map(int, input().split())

x = float('inf')
for a in range(1, min(n, math.ceil(m ** 0.5)) + 1):
    b = math.ceil(m / a)
    ab = a * b
    if b <= n and ab >= m:
        x = min(x, ab)
if x == float('inf'):
    print(-1)
else:
    print(x)