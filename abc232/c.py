import itertools

n, m = map(int, input().split())
ab = tuple(sorted([tuple(sorted(map(lambda x: int(x) - 1, input().split()))) for _ in range(m)]))
cd = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

ns = [i for i in range(n)]
for p in itertools.permutations(ns, n):
    ncd = tuple(sorted([tuple(sorted((p[c], p[d]))) for c, d in cd]))
    if ab == ncd:
        print('Yes')
        exit()
print('No')