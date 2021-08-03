import math
aa = list(map(int, input().split()))
x = aa[1] + aa[1] - aa[0] - aa[2]
y = max(0, math.ceil(-x / 2))
print(x + 3 * y)