import itertools
import math

n = int(input())
x = []
y = []
for i in range(n):
    xx, yy = map(int, input().split())
    x.append(xx)
    y.append(yy)

dd = 0
patterns = list(itertools.permutations(list(range(n))))
for p in patterns:
    xd = 0
    for i in range(len(p) - 1):
        d = math.sqrt((x[p[i]] - x[p[i + 1]]) * (x[p[i]] - x[p[i + 1]]) + (y[p[i]] - y[p[i + 1]]) * (y[p[i]] - y[p[i + 1]]))
        xd += d
    dd += xd
print(dd / len(patterns))
