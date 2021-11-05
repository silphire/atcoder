from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 8)

g = defaultdict(list)
n = int(input())
for i in range(n):
    p = int(input())
    g[p].append(i + 1)

l = [-1] * (n + 1)
r = [-1] * (n + 1)

index = 0
def dfs(x, parent):
    global g, index
    
    l[x] = index
    index += 1
    for y in g[x]:
        if y != parent:
            dfs(y, x)
    r[x] = index    
dfs(g[-1][0], -1)

q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    if l[b] <= l[a] and r[a] <= r[b]:
        print('Yes')
    else:
        print('No')