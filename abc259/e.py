n = int(input())
ee = {}
ii = {}
for i in range(n):
    m = int(input())
    for _ in range(m):
        p, e = map(int, input().split())
        if p not in ee or ee[p] < e:
            ee[p], ii[p] = e, i
        elif ee[p] == e:
            if p in ii:
                del ii[p]
print(min(n, 1 + len(set(ii.values()))))