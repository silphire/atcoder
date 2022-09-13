from collections import deque

h, w = map(int, input().split())
aa = [
    list(input().rstrip())
    for _ in range(h)
]
r = 0
for a in aa:
    for c in a:
        if c == '#':
            r += 1

def dfs(x, y, r):
    if x >= w or y >= h:
        return
    if aa[y][x] != '#':
        return
    r -= 1
    if r < 0:
        return
    if r == 0 and y == h - 1 and x == w - 1:
        print('Possible')
        exit()
    dfs(x + 1, y, r)
    dfs(x, y + 1, r)
    
dfs(0, 0, r)
print('Impossible')