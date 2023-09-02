import itertools
import functools

n = int(input())
dd = [None] * (n - 1)
for i in range(n - 1):
    dd[i] = ([None] * (i + 1)) + list(map(int, input().split()))

@functools.lru_cache(maxsize=10 ** 5)
def dfs(bit):
    arr = set()
    for i in range(n):
        if bit & (1 << i) == 0:
            arr.add(i)
    a = 0
    for (x, y) in itertools.combinations(arr, 2):
        if x > y:
            x, y = y, x
        a = max(a, dd[x][y] + dfs(bit | (1 << x) | (1 << y)))
    return a

ans = dfs(0)
print(ans)