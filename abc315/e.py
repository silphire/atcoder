from collections import deque
import sys
sys.setrecursionlimit(10 ** 7)

n = int(input())
bb = [None] * (n + 1)
for i in range(1, n + 1):
    c, *b = map(int, input().split())
    bb[i] = set(b)

ans = []
read = [False] * (n + 1)

def dfs(b):
    read[b] = True
    for c in bb[b]:
        if not read[c]:
            dfs(c)
    ans.append(b)
dfs(1)
if ans:
    ans.pop()
print(*ans)