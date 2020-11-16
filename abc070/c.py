import math

def lcm(x, y):
    return x // math.gcd(x, y) * y

n = int(input())
t = [None] * n
ans = int(input())
for i in range(1, n):
    ans = lcm(ans, int(input()))
print(ans)