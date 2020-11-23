from collections import defaultdict
from collections import deque

n, m = map(int, input().split())

r = defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    r[a].append(b)
    r[b].append(a)

q = deque([(1, 0)])
while q:
    x, d = q.popleft()
    if x == n:
        print('POSSIBLE')
        exit()
    if d < 2:
        for a in r[x]:
            q.append((a, d + 1))
print('IMPOSSIBLE')