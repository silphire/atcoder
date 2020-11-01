from collections import Counter

sd = input().rstrip()
s = Counter(sd)
es = []
nn = []
for x in range(0, 1000, 2):
    if (((x % 1000) // 2) % 100) % 4 == 0:
        e = Counter(list(str(x)))
        es.append(e.items())
        nn.append(sum(e.values()))

for i in range(len(es)):
    e = es[i]
    if nn[i] < 3:
        if len(sd) != nn[i]:
            continue
    f = True
    for k, v in e:
        if k not in s or s[k] < v:
            f = False
            break
    if f:
        print('Yes')
        exit()
print('No')