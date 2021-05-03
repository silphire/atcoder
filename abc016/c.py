from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(set)
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    d[a].add(b)
    d[b].add(a)

for i in range(n):
    cands = set()
    for c in d[i]:
        cands |= d[c]
    cands -= {i}
    cands -= d[i]
    print(len(cands))