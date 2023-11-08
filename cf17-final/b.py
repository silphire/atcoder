from collections import Counter
ctr = Counter(list(input() + 'abc'))
vs = ctr.values()
if max(vs) - min(vs) <= 1:
    print('YES')
else:
    print('NO')