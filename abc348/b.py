import math

n = int(input())
pp = [None] * n
for i in range(n):
    pp[i] = tuple(map(float, input().split()))
for i in range(n):
    ans = -1
    md = 0
    for j in range(n):
        if i == j:
            continue
        d = math.dist(pp[i], pp[j])
        if d > md:
            ans = j
            md = d
    print(ans + 1)
