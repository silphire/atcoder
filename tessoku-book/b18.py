import sys
sys.setrecursionlimit(10 ** 5)

n, s = map(int, input().split())
aa = list(map(int, input().split()))

def dfs(a, x):
    global ans, aa, s
    if a > s:
        return None
    if a == s:
        return []
    if x == n:
        return None
    r = dfs(a, x + 1)
    if r is not None:
        return r
    r = dfs(a + aa[x], x + 1)
    if r is not None:
        return [x + 1] + r

r = dfs(0, 0)
if r is None:
    print(-1)
else:
    print(len(r))
    print(*r)