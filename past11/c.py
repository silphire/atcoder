import math

n, m = map(int, input().split())

lgn = math.log10(n)
s = ''
for i in range(m):
    if (i + 1) * lgn <= 9:
        s += 'o'
    else:
        s += 'x'
print(s)