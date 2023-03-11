h, w = map(int, input().split())
aa = [
    list(map(int, input().split()))
    for _ in range(h)
]

s = set()
def dfs(x, y):
    global w, h, aa, s
    if x >= w or y >= h:
        return 0
    if aa[y][x] in s:
        return 0
    if x == w - 1 and y == h - 1:
        return 1
    s.add(aa[y][x])
    r = dfs(x + 1, y) + dfs(x, y + 1)
    s.discard(aa[y][x])
    return r
print(dfs(0, 0))