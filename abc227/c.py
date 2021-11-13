import math

n = int(input())
N = 10 ** 11
ans = 0
for a in range(1, 10 ** 4 + 1):
    y = n / a
    if y < 1 or y < a:
        break
    for b in range(a, 10 ** 6 + 1):
        x = n / (a * b)
        if x < 1 or x < b:
            break
        ans += math.floor(x) - b + 1
print(ans)