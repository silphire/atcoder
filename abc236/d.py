import itertools
from multiprocessing.connection import answer_challenge

n = int(input())
aa = [
    ([None] * i) + list(map(int, input().split()))
    for i in range(1, 2 * n)
]

ans = 0
used = [False] * (2 * n)
def dfs(remain, p, a):
    global n, aa, used, ans
    if remain <= 0:
        ans = max(ans, a)
        return
    for i in range(2 * n - 1):
        if not used[i]:
            p = i
            break
    used[p] = True
    for i in range(p + 1, 2 * n):
        if not used[i]:
            na = a ^ aa[p][i]
            used[i] = True
            dfs(remain - 2, p + 1, na)
            used[i] = False
    used[p] = False

dfs(n * 2, 0, 0)
print(ans)