import math

a, b, k = map(int, input().split())
n = a + b

def comb(a, b):
    return math.factorial(a + b) // math.factorial(a) // math.factorial(b)

total = comb(a, b)
ans = []
target = 0
for i in range(n):
    if a == 0 or b == 0:
        break

    nx = comb(a - 1, b)
    if target + nx >= k:
        ans.append('a')
        a -= 1
    else:
        ans.append('b')
        b -= 1
        target += nx

for i in range(a):
    ans.append('a')
for i in range(b):
    ans.append('b')
print(''.join(ans))