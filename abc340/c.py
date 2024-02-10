import functools
import sys

sys.setrecursionlimit(10 ** 8)

@functools.lru_cache(maxsize=10**7)
def dfs(x):
    if x < 2:
        return 0
    else:
        if x % 2 == 0:
            return x + 2 * dfs(x // 2)
        else:
            y = x // 2
            return x + dfs(y) + dfs(y + 1)

n = int(input())
print(dfs(n))