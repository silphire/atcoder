n, m = map(int, input().split())
s = [list(input().rstrip()) for _ in range(n)]

ns = 0
for y in range(n):
    for x in range(m):
        if s[y][x] == '.':
            ns += 1

def dfs(x, y, v):
    global s
    global n
    global m

    if not (0 <= x < m and 0 <= y < n):
        return 0
    if s[y][x] == '#':
        return 0
    if (x, y) in v:
        return 0

    v.add((x, y))
    a = 1
    a += dfs(x - 1, y, v)
    a += dfs(x + 1, y, v)
    a += dfs(x, y - 1, v)
    a += dfs(x, y + 1, v)
    return a

ans = 0
for y in range(n):
    for x in range(m):
        if s[y][x] == '.':
            continue
        s[y][x] = '.'
        a = dfs(x, y, set())
        if a == ns + 1:
            ans += 1
        s[y][x] = '#'
print(ans)
