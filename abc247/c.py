def dfs(n):
    if n == 1:
        return [1]
    else:
        x = dfs(n - 1)
        return x + [n] + x

n = int(input())
print(*dfs(n))