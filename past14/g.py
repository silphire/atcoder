h, w = map(int, input().split())
aa = [
    list(map(int, input().split()))
    for _ in range(h)
]
pos = [None] * (h * w + 1)
for y in range(h):
    for x in range(w):
        pos[aa[y][x]] = (x, y)

for i in range(1, h * w + 1):
    ans = []
    x, y = pos[i]
    if x - 1 >= 0:
        j = aa[y][x - 1]
        if i < j:
            ans.append(j)
    if x + 1 < w:
        j = aa[y][x + 1]
        if i < j:
            ans.append(j)
    if y - 1 >= 0:
        j = aa[y - 1][x]
        if i < j:
            ans.append(j)
    if y + 1 < h:
        j = aa[y + 1][x]
        if i < j:
            ans.append(j)
    for a in sorted(ans):
        print(i, a)
