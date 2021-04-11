from collections import defaultdict

import sys
sys.setrecursionlimit(10 ** 9)

n = int(input())
c = list(map(int, input().split()))
g = defaultdict(list)
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

ans = [None] * n
visited = [False] * n
ctr = defaultdict(int)

def dfs(node):
    global ans, ctr, v, g, c
    if visited[node]:
        return
    
    ans[node] = ctr[c[node]] == 0

    visited[node] = True
    ctr[c[node]] += 1
    for x in g[node]:
        dfs(x)
    visited[node] = False
    ctr[c[node]] -= 1

dfs(0)

for i in range(n):
    if ans[i]:
        print(i + 1)