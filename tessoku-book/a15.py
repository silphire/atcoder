n = int(input())
aa = list(map(int, input().split()))
bb = sorted([(a, i) for i, a in enumerate(aa)])
d = {}
i = 1
for (x, p) in bb:
    if x not in d:
        d[x] = i
        i += 1
print(*[d[a] for a in aa])