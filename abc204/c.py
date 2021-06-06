from collections import defaultdict
from collections import deque

n, m = map(int, input().split())
d = defaultdict(set)
for _ in range(m):
    a, b = map(int, input().split())
    d[a].add(b)

ans = 0
for i in range(n):
    q = deque([i + 1])
    dest = set()
    while q:
        x = q.popleft()
        if x in dest:
            continue
        dest.add(x)
        q.extend(d[x] - dest)
    ans += len(dest)
print(ans)