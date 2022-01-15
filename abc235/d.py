from collections import deque
a, n = map(int, input().split())
nn = len(str(n))
q = deque([(0, 1)])
found = set()
while q:
    c, x = q.popleft()
    if x == n:
        print(c)
        exit()
    
    sx = str(x)
    if len(sx) > nn:
        continue

    if x in found:
        continue
    found.add(x)

    c += 1
    q.append((c, x * a))
    if x >= 10 and x % 10 != 0:
        x = str(x)
        q.append((c, int(sx[-1] + sx[:-1])))
print(-1)