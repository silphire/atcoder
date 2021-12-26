import sys
sys.setrecursionlimit(10 ** 5)

a, b = map(int, input().split())
move = set()
for i in range(3):
    s = input().rstrip()
    for j in range(3):
        if s[j] == '#':
            move.add((i + 1 - 2, j + 1 - 2))
f = [[False] * 9 for _ in range(9)]
def dfs(x, y):
    if not (0 <= x < 9 and 0 <= y < 9):
        return
    if f[y][x]:
        return
    f[y][x] = True
    for dx, dy in move:
        dfs(x + dx, y + dy)
dfs(a - 1, b - 1)
ans = 0
for y in range(9):
    for x in range(9):
        if f[y][x]:
            ans += 1
print(ans)
