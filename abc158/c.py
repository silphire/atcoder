import math

a, b = map(int, input().split())
for n in range(1, 10000):
    if math.floor(n * 0.08) == a and math.floor(n * 0.1) == b:
        print(n)
        exit(0)
print(-1)
