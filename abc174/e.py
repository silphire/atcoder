import math

n, k = map(int, input().split())
aa = tuple(map(int, input().split()))

amax = max(aa)
al = 1
ar = amax

def f(x):
    global aa

    y = 0
    for a in aa:
        y += math.ceil(a / x) - 1
    return y

while ar - al > 1:
    a = (al + ar) // 2
    b = f(a)
    if b <= k:
        ar = a
    else:
        al = a

f = True
for a in aa:
    if a % al != 0:
        f = False
        break
if f:
    print(al)
else:
    print(al + 1)