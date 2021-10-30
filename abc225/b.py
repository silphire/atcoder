from collections import defaultdict
g = defaultdict(set)
n = int(input())
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a].add(b)
    g[b].add(a)
if max([len(v) for k, v in g.items()]) == n - 1:
    print('Yes')
else:
    print('No')
