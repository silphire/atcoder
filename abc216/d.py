from collections import deque

n, m = map(int, input().split())
aa = [None] * m
stock = [None] * (n + 1)
pairs = deque()
for i in range(m):
    input()
    aa[i] = deque(map(int, input().split()))
    a = aa[i][0]
    if stock[a] is None:
        stock[a] = i
    else:
        pairs.append((stock[a], i))
        stock[a] = None
nn = n
while pairs:
    x, y = pairs.popleft()
    aa[x].popleft()
    aa[y].popleft()
    nn -= 1
    if len(aa[x]) > 0:
        c = aa[x][0]
        if stock[c] is None:
            stock[c] = x
        else:
            pairs.append((stock[c], x))
            stock[c] = None
    if len(aa[y]) > 0:
        c = aa[y][0]
        if stock[c] is None:
            stock[c] = y
        else:
            pairs.append((stock[c], y))
            stock[c] = None
if nn == 0:
    print('Yes')
else:
    print('No')