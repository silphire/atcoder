import math

x, k, d = map(int, input().split())

nk = abs(x) // d
if k <= nk:
    if x >= 0:
        x -= d * k
    else:
        x += d * k
    print(abs(x))
    exit(0)
    
if x >= 0:
    x -= d * nk
else:
    x += d * nk
k -= nk

if k > 0 and k % 2 == 1:
    if x >= 0:
        x -= d
    else:
        x += d
print(abs(x))
