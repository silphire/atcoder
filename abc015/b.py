import math
n = int(input())
aa = list(map(int, input().split()))
x = 0
y = 0
for a in aa:
    if a > 0:
        x += 1
        y += a
if x == 0:
    print(0)
else:
    print(math.ceil(y / x))