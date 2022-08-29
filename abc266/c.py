import numpy as np

vv = [
    np.array(list(map(int, input().split())))
    for _ in range(4)
]
s = set()
for i in range(4):
    v = np.cross(vv[i] - vv[(i + 1) % 4], vv[(i + 2) % 4] - vv[(i + 1) % 4])
    s.add(np.sign(v))
if len(s) == 1:
    print('Yes')
else:
    print('No')