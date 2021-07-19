from collections import defaultdict

n = int(input())
r = defaultdict(list)
for _ in range(n):
    d, s, t = map(int, input().split())
    r[d].append((t, s))

for rr in r.values():
    rr.sort()
    m = len(rr)
    if m == 1:
        continue
    for i in range(1, m):
        if rr[i - 1][1] < rr[i][0] and rr[i][1] < rr[i - 1][0]:
            print('Yes')
            exit()
print('No')