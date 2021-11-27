ss = [
    list(input().rstrip())
    for _ in range(2)
]

n = 0
xx = 0
yy = 0
for y in range(2):
    for x in range(len(ss[0])):
        if ss[y][x] == '#':
            xx = x
            yy = y
            n += 1

def dfs(x, y):
    global ss

    if not (0 <= x < len(ss[0]) and 0 <= y < 2):
        return
    if ss[y][x] == '.':
        return
    ss[y][x] = '.'
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)

dfs(xx, yy)
for s in ss:
    for c in s:
        if c == '#':
            print('No')
            exit()
print('Yes')