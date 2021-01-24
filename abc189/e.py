import numpy as np
from collections import defaultdict
import sys

input = sys.stdin.readline

n = int(input())
vv = [None] * n
for i in range(n):
    vv[i] = np.array(list(map(int, input().split())) + [1], dtype=np.int64).T

matrices = [
    np.array([
        [0, 1 ,0], 
        [-1, 0, 0], 
        [0, 0, 1]
    ], dtype=np.int64),
    np.array([
        [0, -1, 0],
        [1, 0, 0], 
        [0, 0, 1]
    ], dtype=np.int64),
    np.array([
        [-1, 0, 0], 
        [0, 1, 0], 
        [0, 0, 1]
    ], dtype=np.int64),
    np.array([
        [1, 0, 0], 
        [0, -1, 0], 
        [0, 0, 1]
    ], dtype=np.int64),
]

m = int(input())

r = [None] * (m + 1)
r[0] = np.identity(3, dtype=np.int64)

for i in range(m):
    op = list(map(int, input().split()))

    if op[0] == 1:
        r[i + 1] = matrices[0] @ r[i]
    elif op[0] == 2:
        r[i + 1] = matrices[1] @ r[i]
    elif op[0] == 3:
        matrices[2][0, 2] = op[1] * 2
        r[i + 1] = matrices[2] @ r[i]
    elif op[0] == 4:
        matrices[3][1, 2] = op[1] * 2
        r[i + 1] = matrices[3] @ r[i]

q = int(input())
for i in range(q):
    a, b = map(int, input().split())
    v = (r[a] @ vv[b - 1]).reshape([-1])
    print(f'{v[0]} {v[1]}')