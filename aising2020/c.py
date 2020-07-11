from typing import Collection

from collections import defaultdict
n = int(input())

f = defaultdict(int)
for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            d = x * x + y * y + z * z + x * y + y * z + z * x
            if 1 <= d <= 10 ** 4:
                f[d] += 1
for i in range(1, n + 1):
    print(f[i])