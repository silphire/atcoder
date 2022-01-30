from collections import deque
import sys
sys.setrecursionlimit(10 ** 7)

n = int(input())
s = input().rstrip()

def dfs(x):
    global n, s

    if x == n:
        return deque([x])
    if s[x] == 'L':
        q = dfs(x + 1)
        q.append(x)
        return q
    else:
        q = dfs(x + 1)
        q.appendleft(x)
        return q

ans = dfs(0)
print(' '.join(map(str, ans)))