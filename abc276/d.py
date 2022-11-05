import heapq
from collections import defaultdict

n = int(input())
aa = list(map(int, input().split()))

if len(set(aa)) == 1:
    print(0)
    exit()

c2 = [0] * n
c3 = [0] * n

for i, a in enumerate(aa):
    x = 0
    while a % 2 == 0:
        a //= 2
        x += 1
    c2[i] = x

    x = 0
    while a % 3 == 0:
        a //= 3
        x += 1
    c3[i] = x

    aa[i] = a

if len(set(aa)) != 1:
    print(-1)
    exit()

x = sum(c2) + sum(c3) - (min(c2) + min(c3)) * n
print(x)