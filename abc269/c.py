import itertools

n = int(input())
rr = []
i = 0
while n > 0:
    if n & 1 == 1:
        rr.append(i)
    n >>= 1
    i += 1
ans = [0]
for i in range(len(rr)):
    for p in itertools.combinations(rr, i + 1):
        a = 0
        for r in p:
            a += 1 << r
        ans.append(a)
for a in sorted(ans):
    print(a)