from collections import defaultdict

n, k = map(int, input().split())
aa = list(map(int, input().split()))
pos = defaultdict(set)
for i, a in enumerate(aa):
    pos[a].add(i)
aa.sort()
for i, a in enumerate(aa):
    f = True
    for p in pos[a]:
        if abs(i - p) % k == 0:
            f = False
            break
    if f:
        print('No')
        exit()
print('Yes')