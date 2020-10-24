from collections import defaultdict

n, m = map(int, input().split())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))

v = defaultdict(set)
for i in range(m):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    v[c].add(d)
    v[d].add(c)
for i in range(n):
    if i not in v and aa[i] != bb[i]:
        print('No')
        exit()

if sum(aa) == sum(bb):
    print('Yes')
else:
    print('No')
