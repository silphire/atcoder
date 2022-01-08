import bisect
import math

x = input().rstrip()
n = len(x)
if n == 1:
    print(x)
    exit()

a = []
for s in range(math.floor(10 / (n - 1)) + 1):
    for d in range(10):
        st = ''
        f = True
        for i in range(n):
            dg = d + i * s
            if dg < 0 or dg >= 10:
                f = False
                break
            st += str(dg)
        if f and int(st) >= int(x):
            a.append(int(st))

        st = ''
        f = True
        for i in range(n):
            dg = d - i * s
            st += str(dg)
            if dg < 0 or dg >= 10:
                f = False
                break
        if f and int(st) >= int(x):
            a.append(int(st))
a.append(int('1' * (n + 1)))
a.sort()
p = bisect.bisect_left(a, int(x))
print(a[p])