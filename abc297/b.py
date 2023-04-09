from collections import defaultdict

s = input()
d = defaultdict(list)
for i, c in enumerate(s):
    d[c].append(i)
if (d['B'][1] - d['B'][0]) % 2 == 1 and d['R'][0] < d['K'][0] < d['R'][1]:
    print('Yes')
else:
    print('No')