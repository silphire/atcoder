from collections import defaultdict

n, q = map(int, input().split())
aa = list(map(int, input().split()))

d = {}
c = defaultdict(int)
for i, a in enumerate(aa):
    c[a] += 1
    d[(a, c[a])] = i + 1

for _ in range(q):
    x, k = map(int, input().split())
    print(d.get((x, k), -1))