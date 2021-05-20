from functools import lru_cache

n = int(input())
ng = [int(input()) for _ in range(3)]

@lru_cache(maxsize=1000)
def dfs(x, c):
    if x == 0:
        return True
    if x < 0:
        return False
    if x in ng:
        return False
    if c == 100:
        return False
    return any([dfs(x - i, c + 1) for i in range(1, 4)])

if dfs(n, 0):
    print('YES')
else:
    print('NO')