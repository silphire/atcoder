import math
import itertools

aa = tuple(map(int, input().split()))

def dfs(a, b, c):
    global aa
    if not (a >= b and b >= c):
        return 0
    if (a, b, c) == aa:
        return 1
    
    n = 0
    if a < aa[0]:
        n += dfs(a + 1, b, c)
    if b < aa[1]:
        n += dfs(a, b + 1, c)
    if c < aa[2]:
        n += dfs(a, b, c + 1)
    return n

print(dfs(0, 0, 0))