import sys
import math
n = int(input())
if n == 1:
    print(1)
    exit()

num = math.ceil(n ** 0.5)
pos = n - (num - 1) ** 2
# print(f'num={num} pos={pos}', file=sys.stderr)

if pos < num:
    print(num - (pos - 1))
else:
    print(pos - num + 1)
