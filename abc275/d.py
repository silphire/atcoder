import functools

n = int(input())

@functools.lru_cache(maxsize=10**6)
def f(k):
    if k == 0:
        return 1
    return f(k // 2) + f(k // 3)

print(f(n))