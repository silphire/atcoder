from collections import defaultdict

n = int(input())
mm = [0] * n
pp = [None] * n
ee = [None] * n
aa = defaultdict(list)
for i in range(n):
    mm[i] = int(input())
    pp[i] = [0] * mm[i]
    ee[i] = [0] * mm[i]
    for j in range(mm[i]):
        p, e = map(int, input().split())
        if p not in aa:
            aa[p] = [0, 0]
        if aa[p][0] < e:
            aa[p][1] = aa[p][0]
            aa[p][0] = e
        elif aa[p][1] < e:
            aa[p][1] = e
        pp[i][j] = p
        ee[i][j] = e
        aa[p].append(e)

ak = sorted(aa.keys())
s = set()
for i in range(n):
    def gen():
        j = 0
        for k in ak:
            if j < mm[i] and pp[i][j] == k:
                p = pp[i][j]
                e = ee[i][j]
                if aa[p][0] == e:
                    v = aa[p][1]
                else:
                    v = aa[p][0]
                yield (p, v)
                j += 1
            else:
                yield (k, aa[k][0])
    s.add(tuple((x for x in gen())))
print(len(s))