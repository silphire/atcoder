n = int(input())
k = int(input())

def dfs(n, c):
    global k

    if n == 0:
        return c
    return min(
        dfs(n - 1, c * 2),
        dfs(n - 1, c + k)
    )

print(dfs(n, 1))
