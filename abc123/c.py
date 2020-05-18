import math

n = int(input())
a = []
for i in range(5):
    a.append(int(input()))

ans = math.ceil(n / min(a)) + 4
print(ans)