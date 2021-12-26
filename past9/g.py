import sys
sys.setrecursionlimit(10000)

n, q = map(int, input().split())
gr = [set() for _ in range(n)]

visited = [False] * n
def check(x, y):
    if visited[x]:
        return False
    visited[x] = True
    for z in gr[x]:
        if z == y:
            return True
        if check(z, y):
            return True
    return False

for i in range(q):
    x, u, v = map(int, input().split())
    u -= 1
    v -= 1
    if x == 1:
        if v in gr[u]:
            gr[u].remove(v)
            gr[v].remove(u)
        else:
            gr[u].add(v)
            gr[v].add(u)
    else:
        visited = [False] * n
        if check(u, v):
            print('Yes')
        else:
            print('No')