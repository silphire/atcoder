import math

a, b, x = map(int, input().split())

n = min(10 ** 9, math.ceil((x - b) / a))

if n <= 0:
    print(0)
    exit()

while x < (a * n + b * sum(map(int, str(n)))):
    n -= 1
print(n)
