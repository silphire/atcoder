from collections import Counter
from collections import defaultdict
s = input()
ctr = Counter(list(s))
d = defaultdict(int)
for _, v in ctr.items():
    d[v] += 1
for k, v in d.items():
    if v != 2:
        print('No')
        exit()
print('Yes')