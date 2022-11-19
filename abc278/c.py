from collections import defaultdict

n, q = map(int, input().split())

d = defaultdict(set)
for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        d[a].add(b)
    elif t == 2:
        d[a].discard(b)
    else:
        if b in d[a] and a in d[b]:
            print('Yes')
        else:
            print('No')