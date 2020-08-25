from collections import defaultdict
from collections import deque

h, w = map(int, input().split())
ch, cw = map(int, input().split())
dh, dw = map(int, input().split())
ch -= 1
cw -= 1
dh -= 1
dw -= 1
d = {'#': -1, '.': 0}
ss = [
    list(map(lambda x: d[x], input().rstrip()))
    for i in range(h)
]

canmove = defaultdict(set)

def dfs(c, x, y):
    global ss
    if not (0 <= x < w and 0 <= y < h):
        return
    if ss[y][x] != 0:
        return
    ss[y][x] = c
    dfs(c, x - 1, y)
    dfs(c, x + 1, y)
    dfs(c, x, y - 1)
    dfs(c, x, y + 1)

c = 1
for y in range(h):
    for x in range(w):
        if ss[y][x] == 0:
            dfs(c, x, y)
            c += 1

for y in range(h):
    for x in range(w):
        if ss[y][x] <= 0:
            continue

        for j in range(y - 2, y + 3):
            if not (0 <= j < h):
                continue
            for i in range(x - 2, x + 3):
                if not (0 <= i < w):
                    continue
                if ss[j][i] <= 0:
                    continue
                c1 = ss[y][x]
                c2 = ss[j][i]
                if c1 != c2:
                    canmove[c1].add(c2)
                    canmove[c2].add(c1)

cs = ss[ch][cw]
cd = ss[dh][dw]
if cs == cd:
    print(0)
    exit(0)

q = [cs]
visited = [False] * c
visited[cs] = True
ans = 1
while q:
    nq = []

    for cc in q:
        for cm in canmove[cc]:
            if cm == cd:
                print(ans)
                exit(0)
            if not visited[cm]:
                visited[cm] = True
                nq.append(cm)
    q = nq
    ans += 1
print(-1)
