import sys
from collections import defaultdict
sys.setrecursionlimit(10 + 2 * 10 ** 5)
 
n, m = map(int, input().split())
 
color = [None] * (n + 1)
for i in range(n + 1):
    color[i] = i
 
def root(x):
    global color
 
    if color[x] == x:
        return x
    color[x] = root(color[x])
    return color[x]
 
memo = [None] * (n + 1)
def memo_root(x):
    global memo
    global color
 
    if memo[x] is not None:
        return memo[x]
 
    if color[x] == x:
        memo[x] = x
        return memo[x]
 
    memo[x] = root(color[x])
    return memo[x]
 
def unite(x, y):
    rx = root(x)
    ry = root(y)
    if rx == ry:
        return
    color[rx] = ry
 
for i in range(m):
    a, b = map(int, input().split())
    unite(a, b)
 
cnt = defaultdict(int)
for i in range(n):
    cnt[root(i + 1)] += 1
print(max(cnt.values()))