import math

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r = abs(r1 - r2)
c = abs(c1 - c2)

if r == 0 and c == 0:
    print(0)
    exit()
if r == c:
    print(1)
    exit()
if abs(r + c) <= 3:
    print(1)
    exit()

rr = r
cc = c

x = min(r, c)
r -= x
c -= x
if abs(r + c) <= 3:
    print(2)
    exit()

if abs(rr - cc) % 2 == 1:
    print(3)
else:
    print(2)
