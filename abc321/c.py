import sys
sys.setrecursionlimit(10 ** 9)

def dfs(x):
    arr = []
    d = x % 10
    for a in range(d - 1, -1, -1):
        arr.append(x * 10 + a)
        bb = dfs(x * 10 + a)
        arr.extend(bb)
    return arr

tb = list(range(1, 10))
for p in range(9, 0, -1):
    tb.extend(dfs(p))
tb.sort()

k = int(input())
print(tb[k - 1])