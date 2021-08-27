import sys
sys.setrecursionlimit(100000)

n = int(input())

memo = {}
def dfs(x):
    global memo

    if x == 0:
        return 0

    memo[x] = float('inf')
    p = 9
    while x >= p:
        if (x - p) in memo:
            memo[x] = min(memo[x], memo[x - p] + 1)
        else:
            memo[x] = min(memo[x], dfs(x - p) + 1)
        p *= 9
    
    p = 6
    while x >= p:
        if (x - p) in memo:
            memo[x] = min(memo[x], memo[x - p] + 1)
        else:
            memo[x] = min(memo[x], dfs(x - p) + 1)
        p *= 6

    memo[x] = min(memo[x], x)
    return memo[x]

print(dfs(n))