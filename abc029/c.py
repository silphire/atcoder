import itertools
for s in sorted(itertools.product('abc', repeat=int(input()))):
    print(''.join(s))