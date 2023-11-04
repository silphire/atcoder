from collections import defaultdict
from collections import deque

n, m = map(int, input().split())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))

g = defaultdict(list)

for i in range(m):
    a = aa[i]
    b = bb[i]
    g[a].append(b)
    g[b].append(a)

color = [-1] * (n + 1)
avail = n

for c in range(1, n + 1):
    if avail == 0:
        break
    
    if color[c] != -1:
        continue
    q = deque([c])
    color[c] = 0
    avail -= 1
    while q:
        x = q.popleft()
        for y in g[x]:
            if color[y] == -1:
                color[y] = 1 - color[x]
                avail -= 1
                q.append(y)
            elif color[y] == color[x]:
                print('No')
                exit()
print('Yes')