import math

n = int(input())
if n % 2 == 1:
    print(0)
    exit()

ans = 0
x = 10
while n >= x:
    ans += math.floor(n // x)
    x *= 5
print(ans)