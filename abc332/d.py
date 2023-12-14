from collections import deque
import functools

h, w = map(int, input().split())
aa = [
    tuple(map(int, input().split()))
    for _ in range(h)
]
bb = [
    tuple(map(int, input().split()))
    for _ in range(h)
]
bb = functools.reduce(lambda x, y: x + y, bb)

cc = functools.reduce(lambda x, y: x + y, aa)
visited = set(cc)
q = deque([(cc, 0)])
while q:
    cc, cnt = q.popleft()
    if cc in visited:
        continue
    visited.add(cc)

    if bb == cc:
        print(cnt)
        exit()


    for a in range(h - 1):
        b = a + 1
        aa = [[0] * w for _ in range(h)]
        i = 0
        for y in range(h):
            for x in range(w):
                aa[y][x] = cc[i]
                i += 1
        for i in range(w):
            aa[a][i], aa[b][i] = aa[b][i], aa[a][i]

        dd = functools.reduce(lambda x, y: tuple(x) + tuple(y), aa)
        q.append((dd, cnt + 1))
    for a in range(w - 1):
        b = a + 1
        aa = [[0] * w for _ in range(h)]
        i = 0
        for y in range(h):
            for x in range(w):
                aa[y][x] = cc[i]
                i += 1
        for i in range(h):
            aa[i][a], aa[i][b] = aa[i][b], aa[i][a]

        dd = functools.reduce(lambda x, y: tuple(x) + tuple(y), aa)
        q.append((dd, cnt + 1))

print(-1)
