import math

p = int(input())

ans = 0
for i in range(10, 0, -1):
    x = math.factorial(i)
    for _ in range(100):
        if p >= x:
            p -= x
            ans += 1
        else:
            break
print(ans)