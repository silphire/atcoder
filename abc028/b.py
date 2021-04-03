from collections import Counter
ctr = Counter(list(input().rstrip()))
print(' '.join([str(ctr[c]) for c in list('ABCDEF')]))