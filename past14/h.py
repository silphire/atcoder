from collections import Counter
n = int(input())
aa = list(map(int, input().split()))
ctr = Counter(aa)
for x in sorted(ctr.keys()):
    d = min(ctr[x], ctr[x + 1], ctr[x + 2])
    ctr[x] -= d
    ctr[x + 1] -= d
    ctr[x + 2] -= d
print(sum(ctr.values()))