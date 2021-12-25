import itertools

n, x = map(int, input().split())
ll = [0] * n
aa = [None] * n
for i in range(n):
    ls = list(map(int, input().split()))
    ll[i] = ls[0]
    aa[i] = ls[1:]

def dfs(prod, p):
    if p == n:
        return int(prod == x)
    return sum([dfs(prod * a, p + 1) for a in aa[p]])

print(dfs(1, 0))