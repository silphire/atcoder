n = int(input())

cands = set()

def dfs(n, c3, c5, c7):
    if c3 >= 1 and c5 >= 1 and c7 >= 1:
        cands.add(n)
    if n >= 10 ** 9:
        return
    dfs(n * 10 + 3, c3 + 1, c5, c7)
    dfs(n * 10 + 5, c3, c5 + 1, c7)
    dfs(n * 10 + 7, c3, c5, c7 + 1)

dfs(0, 0, 0, 0)
print(len([c for c in cands if c <= n]))