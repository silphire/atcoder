from collections import deque

n, s = map(int, input().split())
ab = [
    list(map(int, input().split()))
    for _ in range(n)
]

d = {ab[0][0]: 'H', ab[0][1]: 'T'}
for i in range(1, n):
    nd = {}
    for v, p in d.items():
        for j in range(2):
            nd[v + ab[i][j]] = p + 'HT'[j]
    d = nd
    
if s in d:
    print('Yes')
    print(d[s])
else:
    print('No')