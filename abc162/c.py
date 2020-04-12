import math

k = int(input())

tb = [
    [math.gcd(a, b) for a in range(0, 201)]
    for b in range(0, 201)
]

x = 0
for a in range(1, k + 1):
    for b in range(1, k + 1):
        t = tb[a][b]
        for c in range(1, k + 1):
            x += tb[t][c]
print(x)
