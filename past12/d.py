n, m = map(int, input().split())
f = True
ss = set()
for i in range(m):
    u, v = map(int, input().split())
    f = f and 1 <= u <= n and 1 <= v <= n
    if u == v:
        f = False
    elif u > v:
        u, v = v, u
    ss.add((u, v))
if f and len(ss) == m:
    print('Yes')
else:
    print('No')