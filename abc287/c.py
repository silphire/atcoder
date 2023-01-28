from collections import defaultdict

n, m = map(int, input().split())
if n - 1 != m:
    print('No')
    exit()
g = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

st = None
for x, y in g.items():
    if len(y) == 1:
        st = x
        break
if st is None:
    print('No')
    exit()

c = 0
x = st
prev = None
while True:
    if len(g[x]) == 2:
        if g[x][0] == prev:
            prev = x
            x = g[x][1]
            c += 1
        elif g[x][1] == prev:
            prev = x
            x = g[x][0]
            c += 1
        else:
            print('No')
            exit()
    elif len(g[x]) == 1:
        if prev is None:
            prev = x
            x = g[x][0]
            c += 1
        elif prev == g[x][0]:
            c += 1
            break
        else:
            print('No')
            exit()
    else:
        print('No')
        exit()
        
if c == n:
    print('Yes')
else:
    print('No')