import sys
sys.setrecursionlimit(10 ** 6)

d = {}
def dfs(a):
    global d
    if a <= 3:
        return a
    elif a not in d:
        d[a] = dfs(a // 2) * dfs((a + 1) // 2) % 998244353
    return d[a]

x = int(input())
print(dfs(x))
