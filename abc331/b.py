import functools

n, s, m, l = map(int, input().split())

@functools.lru_cache(maxsize=10000)
def dfs(n, c):
    global s, m, l

    if n <= 0:
        return c
    return min(
        dfs(n - 6,  c + s),
        dfs(n - 8,  c + m),
        dfs(n - 12, c + l),
    )

print(dfs(n, 0))